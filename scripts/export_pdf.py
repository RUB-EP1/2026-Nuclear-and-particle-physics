"""Export rendered Reveal decks as 16:9 slide snapshots with clickable links."""

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from io import BytesIO
from pathlib import Path
from threading import Thread

from playwright.sync_api import sync_playwright
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen.canvas import Canvas

WIDTH, HEIGHT = 1920, 1080


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def export(browser, url, output):
    page = browser.new_page(viewport={"width": WIDTH, "height": HEIGHT})
    temporary = output.with_suffix(".tmp.pdf")
    try:
        page.goto(url, wait_until="domcontentloaded")
        page.wait_for_function("window.Reveal && Reveal.isReady()")
        page.evaluate("""() => {
            document.documentElement.classList.add('export-pdf');
            Reveal.configure({transition: 'none', backgroundTransition: 'none',
                autoSlide: 0, controls: false, progress: false,
                width: 1920, height: 1080, minScale: 1, maxScale: 1});
            Reveal.layout();
        }""")
        page.evaluate("document.fonts.ready")
        slides = page.evaluate("""() => Reveal.getSlides().map(slide => {
            const {h, v} = Reveal.getIndices(slide);
            return {h, v};
        })""")
        if not slides:
            raise RuntimeError(f"No slides found at {url}")
        output.parent.mkdir(parents=True, exist_ok=True)
        pdf = Canvas(str(temporary), pagesize=(WIDTH, HEIGHT))
        pdf.setTitle(output.stem)
        for slide in slides:
            page.evaluate("""({h, v}) => {
                Reveal.slide(h, v);
                Reveal.getCurrentSlide().querySelectorAll('.fragment')
                    .forEach(el => el.classList.add('visible'));
            }""", slide)
            page.wait_for_timeout(500)
            page.evaluate("""async () => {
                await Promise.all([...Reveal.getCurrentSlide().querySelectorAll('img')]
                    .map(img => Promise.race([
                        img.decode().catch(() => {}),
                        new Promise(resolve => setTimeout(resolve, 5000))
                    ])));
                document.querySelectorAll('video, audio').forEach(el => el.pause());
            }""")
            pdf.drawImage(ImageReader(BytesIO(page.screenshot())),
                          0, 0, width=WIDTH, height=HEIGHT)
            links = page.evaluate("""() =>
                [...Reveal.getCurrentSlide().querySelectorAll('a[href]')]
                .filter(a => ['https://', 'http://', 'mailto:']
                    .some(prefix => a.getAttribute('href').startsWith(prefix)))
                .map(a => {
                    const r = a.getBoundingClientRect();
                    return {url: a.href, x: r.x, y: r.y, w: r.width, h: r.height};
                })""")
            for link in links:
                if link["url"].startswith(("https://", "http://", "mailto:")) and link["w"] > 0 and link["h"] > 0:
                    pdf.linkURL(link["url"], (link["x"], HEIGHT - link["y"] - link["h"],
                                             link["x"] + link["w"], HEIGHT - link["y"]),
                                relative=0, thickness=0)
            pdf.showPage()
        pdf.save()
        temporary.replace(output)
        print(f"Wrote {output} ({len(slides)} slides)", flush=True)
    finally:
        page.close()
        temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--html-root", type=Path, default=Path("."))
    parser.add_argument("--pdf-root", type=Path, default=Path("."))
    parser.add_argument("lectures", nargs="+")
    args = parser.parse_args()
    paths = [Path("slides/lectures") / name / f"{name}.html" for name in args.lectures]
    for path in paths:
        if not (args.html_root / path).is_file():
            parser.error(f"Missing {args.html_root / path}; render the HTML first.")
    server = ThreadingHTTPServer(("127.0.0.1", 0),
                                partial(QuietHandler, directory=str(args.html_root.resolve())))
    Thread(target=server.serve_forever, daemon=True).start()
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            try:
                for path in paths:
                    export(browser, f"http://127.0.0.1:{server.server_port}/{path.as_posix()}?export=1",
                           args.pdf_root / path.with_suffix(".pdf"))
            finally:
                browser.close()
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    main()

"""Check that the files a lecture refers to are in the built website.

Quarto copies files that Markdown links to, but not widgets that Reveal loads
at run time (data-src, data-poster) nor their scripts and styles. Those must be
listed under `resources` in the CI `_quarto.yml`, otherwise the deployed deck
shows an empty widget slide.

    python scripts/check_site.py --site _site           # files exist in the site
    python scripts/check_site.py --site _site --browser # and each widget runs

The file check needs only the standard library. --browser needs Playwright (the
PDF export installs it) and fails on 404s, script errors and an empty page.
Set CHECK_SITE_CHANNEL=chrome to use an installed Google Chrome instead of
Playwright's Chromium.
"""

import argparse
import os
import re
import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread

LECTURE_ATTRS = re.compile(r'(?:data-src|data-poster)="([^"]+)"|\]\(([^)\s]+)\)|\bsrc="([^"]+)"')
WIDGET_ATTRS = re.compile(r'(?:src|href)="([^"]+)"')
EXTERNAL = ("http:", "https:", "data:", "mailto:", "#", "//")


def local(ref):
    ref = ref.split("#")[0].split("?")[0]
    return ref if ref and not ref.startswith(EXTERNAL) else None


def lecture_refs(qmd):
    """Relative files referenced by a lecture, as paths from the lecture folder."""
    text = qmd.read_text(encoding="utf-8")
    refs = {local(m) for groups in LECTURE_ATTRS.findall(text) for m in groups if m}
    return sorted(r for r in refs if r and "/" in r and not r.startswith("<"))


def widget_refs(widget):
    """Relative files a widget page loads, as paths from the lecture folder."""
    base = widget.parent
    found = set()
    for ref in WIDGET_ATTRS.findall(widget.read_text(encoding="utf-8")):
        ref = local(ref)
        if ref:
            found.add((base / ref).resolve())
    return found


def check_files(root, site):
    errors, widgets = [], []
    for qmd in sorted(root.glob("slides/lectures/Lecture_*/Lecture_*.qmd")):
        folder = qmd.parent
        out = site / folder.relative_to(root)
        wanted = {(folder / r).resolve(): r for r in lecture_refs(qmd)}
        for page in [folder / r for r in wanted.values() if r.endswith(".html") and r.startswith("widgets/")]:
            if page.exists():
                widgets.append((folder, page))
                wanted.update({p: str(p.relative_to(folder.resolve())) for p in widget_refs(page)})
        for path, ref in wanted.items():
            rel = path.relative_to(folder.resolve())
            if not path.exists():
                errors.append(f"{qmd.name}: {ref} does not exist in the source")
            elif not (out / rel).exists():
                errors.append(f"{qmd.name}: {rel} is missing from the built site ({out / rel})")
    return errors, widgets


class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def check_browser(root, site, widgets):
    from playwright.sync_api import sync_playwright

    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(Quiet, directory=str(site)))
    Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{server.server_address[1]}"
    errors = []
    with sync_playwright() as p:
        browser = p.chromium.launch(channel=os.environ.get("CHECK_SITE_CHANNEL") or None)
        for folder, page_file in widgets:
            rel = page_file.resolve().relative_to(root.resolve()).as_posix()
            problems = []
            page = browser.new_page(viewport={"width": 1600, "height": 880})
            page.route("**/favicon.ico", lambda r: r.fulfill(status=204))  # browsers ask for it unprompted
            page.on("pageerror", lambda e: problems.append(f"script error: {e}"))
            page.on("console", lambda m: problems.append(f"console: {m.text}") if m.type == "error" else None)
            page.on("response", lambda r: problems.append(f"HTTP {r.status}: {r.url}") if r.status >= 400 else None)
            page.goto(f"{base}/{rel}", wait_until="load")
            page.wait_for_timeout(500)
            drawn = page.evaluate("""() => [...document.querySelectorAll('canvas, svg')]
                .some(e => e.getBoundingClientRect().width > 50 && e.getBoundingClientRect().height > 50)""")
            if not drawn:
                problems.append("no canvas or svg of a usable size")
            errors += [f"{rel}: {m}" for m in problems]
            page.close()
        browser.close()
    server.shutdown()
    return errors


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--site", default="_site", help="rendered website (default: _site)")
    ap.add_argument("--root", default=".", help="repository root (default: .)")
    ap.add_argument("--browser", action="store_true", help="also load every widget in headless Chromium")
    args = ap.parse_args()
    root, site = Path(args.root), Path(args.site)
    if not site.is_dir():
        sys.exit(f"{site} does not exist: render the website first")
    errors, widgets = check_files(root, site)
    if args.browser:
        errors += check_browser(root, site, widgets)
    for e in errors:
        print("FAIL", e)
    print(f"{len(widgets)} widgets checked, {len(errors)} problems")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()

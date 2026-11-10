"""Local draft QA for Lecture 8: offline widget, controls, poster, slide geometry and screenshots."""
from pathlib import Path
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from functools import partial
from threading import Thread
import json
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[4]
DECK = ROOT / 'slides/lectures/Lecture_8'
OUT = DECK / 'tmp/qa'; OUT.mkdir(parents=True, exist_ok=True)


class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


server = ThreadingHTTPServer(('127.0.0.1', 0), partial(Quiet, directory=str(ROOT)))
Thread(target=server.serve_forever, daemon=True).start()
base = f'http://127.0.0.1:{server.server_address[1]}'
errors, report = [], []
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1920, 'height': 1080}, device_scale_factor=1)
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.on('response', lambda r: errors.append(f'HTTP {r.status}: {r.url}') if r.status >= 400 else None)
    page.route('**/favicon.ico', lambda r: r.fulfill(status=204))
    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith(base) else r.abort())
    # Widget: poster, layout fits, physics checks through the real controls.
    page.goto(f'{base}/slides/lectures/Lecture_8/widgets/designer.html', wait_until='networkidle')
    page.screenshot(path=str(DECK / 'widgets/designer-poster.png'))
    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
    assert page.evaluate('document.documentElement.scrollHeight <= innerHeight')
    s = page.evaluate('ringState'); assert abs(s['circumference'] / 26690 - 1) < .01 and s['storable']
    page.select_option('#particle', 'electron'); assert not page.evaluate('ringState.storable')
    page.locator('#energy').fill('2.019'); page.locator('#field').fill('0.11'); assert 1 < page.evaluate('ringState.lossPerTurn') < 10
    page.select_option('#particle', 'muon'); assert 'turns before decay' in page.locator('#decay').inner_text()
    page.click('#reset'); assert page.evaluate('ringState.particle') == 'proton'
    # Deck in export mode: every slide.
    page.goto(f'{base}/slides/lectures/Lecture_8/Lecture_8.html?export=1', wait_until='domcontentloaded')
    page.wait_for_function('window.Reveal && Reveal.isReady()')
    page.evaluate("Reveal.configure({transition:'none'});Reveal.layout()")
    count = page.evaluate('Reveal.getTotalSlides()')
    for i in range(count):
        page.evaluate('(i)=>Reveal.slide(i)', i); page.wait_for_timeout(100)
        page.evaluate("async()=>{await document.fonts.ready;await Promise.all([...Reveal.getCurrentSlide().querySelectorAll('img')].map(i=>i.decode().catch(()=>{})));}")
        page.screenshot(path=str(OUT / f'slide-{i+1:02}.png'))
        report.append(page.evaluate('''() => {const s=Reveal.getCurrentSlide(),r=s.getBoundingClientRect();return {title:s.querySelector('h2')?.innerText,images:[...s.querySelectorAll('img')].map(i=>({src:i.getAttribute('src'),ok:i.complete&&i.naturalWidth>0})),overflow:[...s.querySelectorAll('.slide-body p,.slide-body table,.slide-body img,h2')].filter(e=>!e.closest('.notes')).filter(e=>{const b=e.getBoundingClientRect();return b.bottom>r.bottom+2||b.right>r.right+2||b.left<r.left-2}).map(e=>e.tagName+':'+e.textContent.slice(0,60)),mathErrors:s.querySelectorAll('merror').length,rawMarkup:s.innerText.includes('$$')||s.innerText.includes(':::')};}'''))
    # Live demo loads in an iframe and detaches on navigation.
    page.goto(f'{base}/slides/lectures/Lecture_8/Lecture_8.html', wait_until='domcontentloaded'); page.wait_for_function('window.Reveal && Reveal.isReady()')
    slide = page.evaluate('Reveal.getSlides().findIndex(s=>s.querySelector("h2")?.textContent==="Ring designer demo")'); assert slide >= 0
    page.evaluate('(i)=>Reveal.slide(i)', slide); frame = page.frame_locator('section.present iframe'); frame.locator('h1').wait_for()
    assert frame.locator('h1').inner_text() == 'Design a circular collider'
    page.evaluate('Reveal.slide(0)'); page.wait_for_timeout(100); assert page.locator('section iframe').count() == 0
    browser.close()
server.shutdown()
(OUT / 'report.json').write_text(json.dumps({'slides': report, 'errors': errors}, indent=2))
assert not errors, errors
bad = [(i + 1, x) for i, x in enumerate(report) if x['overflow'] or x['mathErrors'] or x['rawMarkup'] or any(not a['ok'] for a in x['images'])]
assert not bad, json.dumps(bad, indent=2)
print(f'{len(report)} slides: images, math, bounds, offline widget controls and iframe lifecycle passed.')

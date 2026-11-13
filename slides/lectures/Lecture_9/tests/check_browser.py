"""Local draft QA: offline requests, controls, posters, slide geometry and screenshots."""
from pathlib import Path
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from functools import partial
from threading import Thread
import json
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[4]
DECK=ROOT/'slides/lectures/Lecture_9'
OUT=DECK/'tmp/qa';OUT.mkdir(parents=True,exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(ROOT)))
Thread(target=server.serve_forever,daemon=True).start()
base=f'http://127.0.0.1:{server.server_address[1]}'
errors=[];report=[]
with sync_playwright() as p:
 browser=p.chromium.launch()
 page=browser.new_page(viewport={'width':1920,'height':1080},device_scale_factor=1)
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.on('response',lambda r:errors.append(f'HTTP {r.status}: {r.url}') if r.status>=400 else None)
 page.route('**/favicon.ico',lambda r:r.fulfill(status=204))
 # Enforce offline widget operation: local assets only.
 page.route('**/*',lambda r:r.continue_() if r.request.url.startswith(base) else r.abort())
 for name in ['queue','threshold']:
  page.goto(f'{base}/slides/lectures/Lecture_9/widgets/{name}.html',wait_until='networkidle')
  page.screenshot(path=str(DECK/f'widgets/{name}-poster.png'))
  assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
  assert page.evaluate('document.documentElement.scrollHeight <= innerHeight')
  if name=='queue':
   page.select_option('#mode','dead');assert page.locator('#capacity').is_disabled()
   page.locator('#rate').fill('0');assert page.evaluate('queueState.arrived')==0
   page.click('#reset');assert page.evaluate('queueState.arrived')>0
   page.click('#play');page.wait_for_timeout(200);assert 0<page.evaluate('queueState.clock')<200
   page.click('#play');page.locator('#time').fill('0');assert page.evaluate('queueState.arrived')==0
   page.select_option('#burst','burst');assert page.evaluate('queueState.arrived')>0
  else:
   page.locator('#cut').fill('0');assert page.evaluate('thresholdState.effS')==1
   page.locator('#signal').fill('0');page.locator('#background').fill('0');assert page.locator('#purity').inner_text()=='undefined'
   page.click('#reset');before=page.evaluate('thresholdState')
   page.locator('#size').fill('400');after=page.evaluate('thresholdState');assert after['bandwidth']==2*before['bandwidth'];assert after['effS']==before['effS']
  page.click('#reset')
 # Inspect template reference and every new slide, with export posters.
 page.goto(f'{base}/slides/lectures/Lecture_6/Lecture_6.html?export=1',wait_until='domcontentloaded')
 page.wait_for_function('window.Reveal && Reveal.isReady()');page.screenshot(path=str(OUT/'reference-lecture6.png'));errors.clear()
 page.goto(f'{base}/slides/lectures/Lecture_9/Lecture_9.html?export=1',wait_until='domcontentloaded')
 page.wait_for_function('window.Reveal && Reveal.isReady()')
 page.evaluate("Reveal.configure({transition:'none'});Reveal.layout()")
 assert page.evaluate('Reveal.getTotalSlides()')==51  # numbering stops at the thank-you slide
 count=page.evaluate('document.querySelectorAll(".reveal .slides > section").length');assert count==78,count
 for i in range(count):
  page.evaluate('(i)=>Reveal.slide(i)',i);page.wait_for_timeout(100)
  page.evaluate("async()=>{await document.fonts.ready;await Promise.all([...Reveal.getCurrentSlide().querySelectorAll('img')].map(i=>i.decode().catch(()=>{})));}")
  page.screenshot(path=str(OUT/f'slide-{i+1:02}.png'))
  item=page.evaluate('''() => {const s=Reveal.getCurrentSlide(),r=s.getBoundingClientRect();return {title:s.querySelector('h2')?.innerText,images:[...s.querySelectorAll('img')].map(i=>({src:i.getAttribute('src'),ok:i.complete&&i.naturalWidth>0})),overflow:[...s.querySelectorAll('.slide-body p,.slide-body table,.slide-body img,h2')].filter(e=>!e.closest('.notes')).filter(e=>{const b=e.getBoundingClientRect();return b.bottom>r.bottom+2||b.right>r.right+2||b.left<r.left-2}).map(e=>e.tagName+':'+e.textContent.slice(0,60)),mathErrors:s.querySelectorAll('merror').length,rawMarkup:s.innerText.includes('$$')||s.innerText.includes(':::')};}''')
  report.append(item)
 # Live embedded demos must load and detach on navigation.
 page.goto(f'{base}/slides/lectures/Lecture_9/Lecture_9.html',wait_until='domcontentloaded');page.wait_for_function('window.Reveal && Reveal.isReady()')
 for heading,title in [('Event queue demo','Dead time and event buffers'),('Trigger threshold demo','A trigger selects a physics sample')]:
  slide=page.evaluate('(heading)=>Reveal.getSlides().findIndex(s=>s.querySelector("h2")?.textContent===heading)',heading);assert slide>=0
  page.evaluate('(i)=>Reveal.slide(i)',slide);frame=page.frame_locator('section.present iframe');frame.locator('h1').wait_for();assert frame.locator('h1').inner_text()==title
  page.evaluate('Reveal.slide(0)');page.wait_for_timeout(100);assert page.locator('section iframe').count()==0
 browser.close()
server.shutdown()
(OUT/'report.json').write_text(json.dumps({'slides':report,'errors':errors},indent=2))
assert not errors,errors
assert not any(x['overflow'] or x['mathErrors'] or x['rawMarkup'] or any(not a['ok'] for a in x['images']) for x in report),json.dumps(report,indent=2)
print(f'{len(report)} slides: images, math, bounds, offline demo controls and iframe lifecycle passed.')

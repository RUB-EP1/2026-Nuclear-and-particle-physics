'use strict';
const $ = id => document.getElementById(id);
const C = 26659, V = { cyclist: 50 / 3.6, runner: 20 / 3.6, proton: 299792458 };
let t = 0, playing = false, last = null;
function setup(canvas) {
  const r = canvas.getBoundingClientRect(), d = devicePixelRatio || 1;
  canvas.width = r.width * d; canvas.height = r.height * d;
  const c = canvas.getContext('2d'); c.scale(d, d); c.font = (r.width > 700 ? '20' : '16') + 'px Helvetica,Arial,sans-serif';
  return { c, w: r.width, h: r.height };
}
const fmtT = s => s < 60 ? s.toFixed(1) + ' s' : s < 3600 ? Math.floor(s / 60) + ' min ' + Math.floor(s % 60) + ' s' : Math.floor(s / 3600) + ' h ' + Math.floor((s % 3600) / 60) + ' min';
const fmtN = n => n >= 1e6 ? (n / 1e6).toFixed(1) + ' million' : n >= 1e4 ? Math.round(n).toLocaleString('en') : n.toFixed(2);
function draw() {
  const k = 10 ** +$('k').value;
  $('kValue').textContent = '× ' + Math.round(k); $('clock').textContent = fmtT(t);
  const laps = { cyclist: t * V.cyclist / C, runner: t * V.runner / C, proton: t * V.proton / C };
  $('cyc').textContent = laps.cyclist.toFixed(2); $('run').textContent = laps.runner.toFixed(2); $('pro').textContent = fmtN(laps.proton);
  $('play').textContent = playing ? 'Pause' : 'Start race';
  const { c, w, h } = setup($('ring')), cx = w / 2, cy = h / 2, R = Math.min(w, h) / 2 - 60;
  c.strokeStyle = '#2c6ea3'; c.lineWidth = 14; c.beginPath(); c.arc(cx, cy, R, 0, 2 * Math.PI); c.stroke();
  c.strokeStyle = '#cfe2f1'; c.lineWidth = 4; c.beginPath(); c.arc(cx, cy, R, 0, 2 * Math.PI); c.stroke();
  const pts = [['ATLAS', 0], ['ALICE', 0.125], ['CMS', 0.5], ['LHCb', 0.875]]; // interaction points at octants 1, 2, 5, 8
  for (const [name, f] of pts) { const a = -Math.PI / 2 + 2 * Math.PI * (f % 1); c.fillStyle = '#f2b705'; c.beginPath(); c.arc(cx + R * Math.cos(a), cy + R * Math.sin(a), 12, 0, 2 * Math.PI); c.fill(); c.fillStyle = '#526675'; c.textAlign = 'center'; c.fillText(name, cx + (R + 38) * Math.cos(a), cy + (R + 38) * Math.sin(a) + 6); }
  const pos = f => { const a = -Math.PI / 2 + 2 * Math.PI * (f % 1); return [cx + R * Math.cos(a), cy + R * Math.sin(a)]; };
  // Proton: draw as a blur ring if it laps faster than the frame rate.
  const lapsPerFrame = V.proton / C * k / 60;
  if (lapsPerFrame > 0.3 && playing) { c.strokeStyle = 'rgba(189,50,73,.55)'; c.lineWidth = 8; c.beginPath(); c.arc(cx, cy, R - 22, 0, 2 * Math.PI); c.stroke(); }
  else { const [x, y] = pos(laps.proton); c.fillStyle = '#bd3249'; c.beginPath(); c.arc(x + (cx - x) * 0.06, y + (cy - y) * 0.06, 9, 0, 2 * Math.PI); c.fill(); }
  const mark = (f, col, label, inset) => { const [x, y] = pos(f); const X = x + (cx - x) * inset, Y = y + (cy - y) * inset; c.fillStyle = col; c.beginPath(); c.arc(X, Y, 13, 0, 2 * Math.PI); c.fill(); c.fillStyle = '#fff'; c.textAlign = 'center'; c.font = 'bold 15px Helvetica,Arial,sans-serif'; c.fillText(label, X, Y + 5); };
  mark(laps.cyclist, '#007dc5', 'C', 0.14); mark(laps.runner, '#268565', 'R', 0.22);
  c.font = '20px Helvetica,Arial,sans-serif'; c.fillStyle = '#152d40'; c.textAlign = 'center';
  c.fillText('C cyclist · R runner · red: proton', cx, cy - 8); c.fillStyle = '#526675'; c.fillText(lapsPerFrame > 0.3 && playing ? 'proton: a blur, ' + fmtN(V.proton / C * k) + ' laps per real second' : 'proton', cx, cy + 22);
  window.raceState = { t, laps };
}
function loop(now) { if (!playing) return; if (last !== null) t += (now - last) / 1000 * 10 ** +$('k').value; last = now; draw(); requestAnimationFrame(loop); }
$('play').onclick = () => { playing = !playing; last = null; draw(); if (playing) requestAnimationFrame(loop); };
$('reset').onclick = () => { playing = false; t = 0; $('k').value = 2.3; draw(); };
$('k').addEventListener('input', draw);
window.addEventListener('resize', draw);
t = 960; draw();

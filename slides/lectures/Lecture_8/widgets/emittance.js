'use strict';
const $ = id => document.getElementById(id);
let pts, from = null, to = null, anim = 0, raf = null, p = 1, steps = [];
const FOCAL = 1.25;
function setup(canvas) {
  const r = canvas.getBoundingClientRect(), d = devicePixelRatio || 1;
  canvas.width = r.width * d; canvas.height = r.height * d;
  const c = canvas.getContext('2d'); c.scale(d, d); c.font = (r.width > 800 ? '19' : '16') + 'px Helvetica,Arial,sans-serif';
  return { c, w: r.width, h: r.height };
}
function reset() { pts = Phys.emitBeam(600, 7, 1, 1.6); p = 1; steps = []; from = to = null; draw(); }
function apply(map, label) {
  if (raf) { cancelAnimationFrame(raf); raf = null; if (to) pts = to; }
  from = pts; to = pts.map(map); steps.push(label); anim = 0;
  const tick = () => { anim = Math.min(1, anim + 0.06); pts = from.map((a, i) => [a[0] + (to[i][0] - a[0]) * anim, a[1] + (to[i][1] - a[1]) * anim]); draw(); if (anim < 1) raf = requestAnimationFrame(tick); else { pts = to; raf = null; draw(); } };
  tick();
}
function draw() {
  const s = Phys.rmsEmittance(pts);
  $('sx').textContent = s.sx.toFixed(2) + ' mm'; $('sp').textContent = s.sp.toFixed(2) + ' mrad';
  $('eps').textContent = s.eps.toFixed(2) + ' mm·mrad'; $('mom').textContent = '× ' + p;
  $('log').textContent = steps.length ? 'Applied: ' + steps.slice(-6).join(' → ') : 'Start: a round-ish beam. Try a few drifts and lenses.';
  let { c, w, h } = setup($('phase'));
  const cx = w / 2, cy = h / 2, sc = Math.min(w, h) / 2 / 4.2;
  c.strokeStyle = '#dce5eb'; c.lineWidth = 1;
  for (let k = -4; k <= 4; k++) { c.beginPath(); c.moveTo(cx + k * sc, 10); c.lineTo(cx + k * sc, h - 10); c.stroke(); c.beginPath(); c.moveTo(10, cy - k * sc); c.lineTo(w - 10, cy - k * sc); c.stroke(); }
  c.strokeStyle = '#9aabb6'; c.beginPath(); c.moveTo(10, cy); c.lineTo(w - 10, cy); c.moveTo(cx, 10); c.lineTo(cx, h - 10); c.stroke();
  c.fillStyle = '#007dc5';
  for (const [x, xp] of pts) { const X = cx + x * sc, Y = cy - xp * sc; if (X > 0 && X < w && Y > 0 && Y < h) c.fillRect(X - 2, Y - 2, 4, 4); }
  // rms ellipse (2 sigma) from the covariance matrix.
  const n = pts.length; let xx = 0, pp = 0, xpp = 0; for (const [x, xp] of pts) { xx += x * x; pp += xp * xp; xpp += x * xp; } xx /= n; pp /= n; xpp /= n;
  const tr = xx + pp, det = xx * pp - xpp * xpp, l1 = tr / 2 + Math.sqrt(tr * tr / 4 - det), l2 = tr / 2 - Math.sqrt(Math.max(tr * tr / 4 - det, 0)), ang = 0.5 * Math.atan2(2 * xpp, xx - pp);
  c.save(); c.translate(cx, cy); c.rotate(-ang); c.strokeStyle = '#bd3249'; c.lineWidth = 3; c.beginPath(); c.ellipse(0, 0, 2 * Math.sqrt(l1) * sc, 2 * Math.sqrt(Math.max(l2, 0)) * sc, 0, 0, 2 * Math.PI); c.stroke(); c.restore();
  c.fillStyle = '#526675'; c.textAlign = 'right'; c.fillText('position x [mm] →', w - 14, cy - 10); c.textAlign = 'left'; c.fillText('↑ angle x′ [mrad]', cx + 10, 28);
  // Profile histogram.
  ({ c, w, h } = setup($('profile')));
  const bins = 41, lo = -4.2, hi = 4.2, hist = new Array(bins).fill(0);
  for (const [x] of pts) { const b = Math.floor((x - lo) / (hi - lo) * bins); if (b >= 0 && b < bins) hist[b]++; }
  const m = Math.max(40, ...hist), bw = (w - 40) / bins;
  c.fillStyle = '#007dc5'; hist.forEach((v, i) => c.fillRect(20 + i * bw, h - 30 - (h - 60) * v / m, bw - 1, (h - 60) * v / m));
  c.fillStyle = '#526675'; c.textAlign = 'center'; c.fillText('beam profile: what a screen would show', w / 2, 22); c.fillText('x', w - 12, h - 10);
  window.emitState = { eps: s.eps, sx: s.sx, sp: s.sp, p, steps: steps.length };
}
$('drift').onclick = () => apply(Phys.drift(1), 'drift');
$('focus').onclick = () => apply(Phys.lens(FOCAL), 'focusing lens');
$('defocus').onclick = () => apply(Phys.lens(-FOCAL), 'defocusing lens');
$('squeeze').onclick = () => {
  // Strong lens, then drift to the waist (where the x–x' correlation vanishes).
  const f = 0.6, a = pts.map(Phys.lens(f)); const n = a.length; let xx = 0, xpp = 0, pp = 0; for (const [x, xp] of a) { xx += x * x; xpp += x * xp; pp += xp * xp; }
  const L = Math.max(0, -xpp / pp); apply(q => Phys.drift(L)(Phys.lens(f)(q)), 'strong lens + drift to focus');
};
$('accel').onclick = () => { p *= 2; apply(Phys.boost(2), 'accelerate ×2'); };
$('reset').onclick = reset;
window.addEventListener('resize', draw);
reset();

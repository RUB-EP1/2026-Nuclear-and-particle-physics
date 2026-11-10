'use strict';
const $ = id => document.getElementById(id);
let tau = 0, playing = false, gainSoFar = 0, raf = null;
const cells = () => +$('cells').value, phi = () => +$('phi').value * Math.PI / 180;
function setup(canvas) {
  const r = canvas.getBoundingClientRect(), d = devicePixelRatio || 1;
  canvas.width = r.width * d; canvas.height = r.height * d;
  const c = canvas.getContext('2d'); c.scale(d, d); c.font = (r.width > 900 ? '19' : '16') + 'px Helvetica,Arial,sans-serif';
  return { c, w: r.width, h: r.height };
}
// tau in RF periods; particle position z = 2 tau in cell units (lambda/2 per cell at v = c).
const field = (k, t) => ((k % 2) ? -1 : 1) * Math.cos(2 * Math.PI * t - Math.PI / 2 + phi());
const bfield = (k, t) => ((k % 2) ? -1 : 1) * Math.sin(2 * Math.PI * t - Math.PI / 2 + phi());
function finalState() { tau = cells() / 2 + 0.25; gainSoFar = Phys.rfGain(+$('phi').value, cells()); }
function draw() {
  const n = cells(), T = 2 / Math.PI;
  $('phiValue').textContent = (+$('phi').value) + '°';
  $('gain').textContent = (100 * gainSoFar / (n * T)).toFixed(0) + '%';
  $('len').textContent = (n * 11.5).toFixed(n > 1 ? 0 : 1) + ' cm';
  $('play').textContent = playing ? 'Pause' : 'Send a bunch';
  let { c, w, h } = setup($('cavity'));
  const L = 50, R = w - 50, cw = (R - L) / n, cy = h / 2, rad = Math.min(h * 0.36, cw * 0.9);
  // Cavity walls: cells with irises.
  c.fillStyle = '#e9eef2'; c.strokeStyle = '#9aabb6'; c.lineWidth = 2;
  for (let k = 0; k < n; k++) {
    const x0 = L + k * cw; c.beginPath(); c.ellipse(x0 + cw / 2, cy, cw / 2, rad, 0, 0, 2 * Math.PI); c.fill(); c.stroke();
  }
  c.fillStyle = '#fff'; c.fillRect(L - 50, cy - 14, R - L + 100, 28);
  c.strokeStyle = '#b8c7d2'; c.beginPath(); c.moveTo(L - 50, cy - 14); c.lineTo(R + 50, cy - 14); c.moveTo(L - 50, cy + 14); c.lineTo(R + 50, cy + 14); c.stroke();
  // Field arrows (E along the axis, several rows), B as circles near the wall.
  for (let k = 0; k < n; k++) {
    const e = field(k, tau), b = bfield(k, tau), xc = L + (k + 0.5) * cw;
    for (const dy of [-0.55, -0.3, 0.3, 0.55]) {
      const y = cy + dy * rad, len = cw * 0.38 * e, col = e >= 0 ? '#007dc5' : '#bd3249';
      c.strokeStyle = col; c.fillStyle = col; c.lineWidth = 3; c.beginPath(); c.moveTo(xc - len, y); c.lineTo(xc + len, y); c.stroke();
      if (Math.abs(len) > 6) { const s = Math.sign(len); c.beginPath(); c.moveTo(xc + len, y); c.lineTo(xc + len - s * 10, y - 7); c.lineTo(xc + len - s * 10, y + 7); c.closePath(); c.fill(); }
    }
    for (const dy of [-0.85, 0.85]) {
      const y = cy + dy * rad, r0 = 4 + 7 * Math.abs(b);
      c.strokeStyle = '#268565'; c.lineWidth = 2; c.beginPath(); c.arc(xc, y, r0, 0, 2 * Math.PI); c.stroke();
      c.fillStyle = '#268565'; if ((b >= 0) === (dy < 0)) { c.beginPath(); c.arc(xc, y, 2.5, 0, 2 * Math.PI); c.fill(); } else { c.fillText('×', xc - 5, y + 6); }
    }
  }
  // Particle bunch.
  const z = 2 * tau;
  if (z >= -0.3 && z <= n + 0.3) { const x = L + z * cw; c.fillStyle = '#152d40'; c.beginPath(); c.ellipse(x, cy, 10, 7, 0, 0, 2 * Math.PI); c.fill(); }
  // Input coupler on the downstream beam pipe: RF power from the klystron.
  c.fillStyle = '#fbe9d8'; c.strokeStyle = '#cf741b'; c.lineWidth = 2; c.fillRect(R + 12, cy + 14, 24, h - cy - 44); c.strokeRect(R + 12, cy + 14, 24, h - cy - 44);
  c.fillStyle = '#cf741b'; c.textAlign = 'right'; c.fillText('RF power in from klystron (coupler) →', R + 4, h - 12);
  c.fillStyle = '#526675'; c.textAlign = 'left'; c.fillText('beam →', 8, cy - 22);
  c.textAlign = 'left'; let lx = 8; for (const [txt, col] of [['E forward', '#007dc5'], ['E backward', '#bd3249'], ['B circling the axis (⊙ / ×)', '#268565']]) { c.fillStyle = col; c.fillText(txt, lx, 20); lx += c.measureText(txt).width + 28; }
  // Gain versus phase.
  ({ c, w, h } = setup($('curve')));
  const l = 60, r = w - 16, t = 20, bt = h - 44, X = p => l + (r - l) * (p + 180) / 360, Y = g => (t + bt) / 2 - (bt - t) / 2 * g / (n * T * 1.1);
  c.strokeStyle = '#dce5eb'; c.lineWidth = 1; for (const p of [-180, -90, 0, 90, 180]) { c.beginPath(); c.moveTo(X(p), t); c.lineTo(X(p), bt); c.stroke(); c.fillStyle = '#526675'; c.textAlign = 'center'; c.fillText(p + '°', X(p), bt + 22); }
  c.beginPath(); c.moveTo(l, Y(0)); c.lineTo(r, Y(0)); c.stroke();
  c.strokeStyle = '#007dc5'; c.lineWidth = 2.5; c.beginPath(); for (let p = -180; p <= 180; p += 3) { const g = n * T * Math.cos(p * Math.PI / 180); p === -180 ? c.moveTo(X(p), Y(g)) : c.lineTo(X(p), Y(g)); } c.stroke();
  const gp = Phys.rfGain(+$('phi').value, n); c.fillStyle = '#bd3249'; c.beginPath(); c.arc(X(+$('phi').value), Y(gp), 7, 0, 2 * Math.PI); c.fill();
  c.fillStyle = '#526675'; c.textAlign = 'left'; c.fillText('energy gain vs arrival phase (∝ cos φ)', l, bt + 40);
  window.rfState = { cells: n, phi: +$('phi').value, gain: gp, tau, playing };
}
function loop() {
  if (!playing) return;
  const n = cells(), prevZ = 2 * tau; tau += 0.004 * +$('speed').value;
  const z = 2 * tau;
  if (z > 0 && prevZ < n) { // integrate the kick along the step
    const a = Math.max(prevZ, 0), b = Math.min(z, n), m = 8;
    for (let i = 0; i < m; i++) { const zz = a + (b - a) * (i + 0.5) / m, k = Math.min(n - 1, Math.floor(zz)); gainSoFar += field(k, zz / 2) * (b - a) / m; }
  }
  if (z > n + 0.6) { playing = false; }
  draw(); if (playing) raf = requestAnimationFrame(loop);
}
$('play').onclick = () => {
  if (playing) { playing = false; draw(); return; }
  if (2 * tau > cells() + 0.5) { tau = -0.25; gainSoFar = 0; }
  playing = true; loop();
};
$('reset').onclick = () => { playing = false; $('cells').value = '9'; $('phi').value = 0; $('speed').value = '0.6'; finalState(); draw(); };
for (const id of ['cells', 'phi']) $(id).addEventListener('input', () => { playing = false; finalState(); draw(); });
window.addEventListener('resize', draw);
finalState(); draw();

'use strict';
const $ = id => document.getElementById(id);
const DT = 1e-3, START_CYCLES = 6;
let st, trace, playing = false, lastDiodes = [], raf = null;
const opts = () => ({ load: +$('load').value });
function setup(canvas) {
  const r = canvas.getBoundingClientRect(), d = devicePixelRatio || 1;
  canvas.width = r.width * d; canvas.height = r.height * d;
  const c = canvas.getContext('2d'); c.scale(d, d); c.font = (r.width > 800 ? '19' : '16') + 'px Helvetica,Arial,sans-serif';
  return { c, w: r.width, h: r.height };
}
function advance(cycles) {
  const steps = Math.round(cycles / DT);
  for (let i = 0; i < steps; i++) {
    lastDiodes = Phys.cwStep(st, DT, opts()).diodes;
    if (Math.round(st.t / DT) % 25 === 0) trace.push([st.t, Phys.cwNodes(st).B[st.n]]);
  }
}
function rebuild(cycles = START_CYCLES) {
  st = Phys.cwCreate(+$('n').value); trace = [[0, 0]]; lastDiodes = [];
  advance(cycles); draw();
}
function kv(v) { return (v * +$('v0').value).toFixed(0) + ' kV'; }
function draw() {
  const n = st.n, v0 = +$('v0').value, nodes = Phys.cwNodes(st);
  $('nValue').textContent = n; $('v0Value').textContent = v0 + ' kV';
  $('vout').textContent = kv(nodes.B[n]); $('ideal').textContent = (2 * n * v0) + ' kV';
  $('cyc').textContent = st.t.toFixed(1); $('srcv').textContent = kv(nodes.src);
  $('play').textContent = playing ? 'Pause' : 'Play';
  // Ladder: A_k at level 2k-1 (left), B_k at level 2k (right).
  let { c, w, h } = setup($('ladder'));
  const xa = w * 0.36, xb = w * 0.7, top = 34, bottom = h - 78, gnd = h - 18, lv = l => bottom - (bottom - top) * (l + 1) / (2 * n + 1);
  const A = k => [xa, lv(2 * k - 1)], B = k => [xb, lv(2 * k)];
  // Stage bands: stage k = caps A(k-1)–A(k), B(k-1)–B(k) and diodes B(k-1)→A(k)→B(k).
  for (let k = 1; k <= n; k++) {
    const y0 = lv(2 * k + 0.5), y1 = lv(2 * k - 1.5);
    c.fillStyle = k % 2 ? '#f3f7fa' : '#e8eff4'; c.fillRect(0, y0, w, y1 - y0);
    c.fillStyle = '#7d8f9c'; c.textAlign = 'left'; c.fillText('stage ' + k, 6, (y0 + y1) / 2 + 6);
  }
  const line = (p, q, col, wdt = 2) => { c.strokeStyle = col; c.lineWidth = wdt; c.beginPath(); c.moveTo(...p); c.lineTo(...q); c.stroke(); };
  const cap = (p, q) => { const my = (p[1] + q[1]) / 2, x = p[0]; line(p, [x, my - 6], '#526675'); line([x, my + 6], q, '#526675'); line([x - 16, my - 6], [x + 16, my - 6], '#152d40', 3); line([x - 16, my + 6], [x + 16, my + 6], '#152d40', 3); };
  const diode = (p, q, on) => {
    const col = on ? '#e07b16' : '#9aabb6'; line(p, q, col, on ? 4 : 2);
    if (on) { c.fillStyle = '#e07b16'; for (let j = 0; j < 3; j++) { const f = ((st.t * 6 + j / 3) % 1 + 1) % 1; if (f < 0.4 || f > 0.6) { c.beginPath(); c.arc(p[0] + (q[0] - p[0]) * f, p[1] + (q[1] - p[1]) * f, 4.5, 0, 2 * Math.PI); c.fill(); } } }
    const mx = (p[0] + q[0]) / 2, my = (p[1] + q[1]) / 2, ang = Math.atan2(q[1] - p[1], q[0] - p[0]);
    c.save(); c.translate(mx, my); c.rotate(ang); c.fillStyle = col; c.beginPath(); c.moveTo(9, 0); c.lineTo(-7, -9); c.lineTo(-7, 9); c.closePath(); c.fill(); c.fillRect(9, -10, 3, 20); c.restore();
  };
  // Ground rail and source: A0 is the source terminal, B0 is ground.
  line([xa - 40, gnd], [xb + 40, gnd], '#b8c7d2', 2);
  c.fillStyle = '#526675'; c.textAlign = 'left'; c.fillText('ground', xb + 46, gnd + 6);
  const s0 = A(0), sy = (s0[1] + gnd) / 2; line([xa, s0[1]], [xa, gnd], '#526675');
  c.fillStyle = '#fff'; c.strokeStyle = '#526675'; c.lineWidth = 2; c.beginPath(); c.arc(xa, sy, 14, 0, 2 * Math.PI); c.fill(); c.stroke();
  c.beginPath(); for (let i = 0; i <= 16; i++) { const xx = xa - 8 + i, yy = sy - 6 * Math.sin(i / 16 * 2 * Math.PI); i ? c.lineTo(xx, yy) : c.moveTo(xx, yy); } c.stroke();
  c.fillStyle = '#526675'; c.textAlign = 'left'; c.fillText('AC ±V₀', xa + 22, sy + 6);
  line(B(0), [xb, gnd], '#526675');
  for (let k = 1; k <= n; k++) { cap(A(k - 1), A(k)); cap(B(k - 1), B(k)); }
  const thr = 0.5;
  for (let k = 0; k < n; k++) { diode(B(k), A(k + 1), (lastDiodes[k] || [0, 0])[0] > thr); diode(A(k + 1), B(k + 1), (lastDiodes[k] || [0, 0])[1] > thr); }
  if (+$('load').value > 0) { const t = B(n); line(t, [xb + 90, t[1]], '#526675'); for (let i = 0; i < 6; i++) line([xb + 90 + (i % 2 ? 8 : -8), t[1] + 10 + i * 8], [xb + 90 + (i % 2 ? -8 : 8), t[1] + 18 + i * 8], '#bd3249', 2); c.fillStyle = '#bd3249'; c.textAlign = 'left'; c.fillText('beam load', xb + 104, t[1] + 34); }
  const node = (p, v, col) => { c.fillStyle = col; c.beginPath(); c.arc(p[0], p[1], 9, 0, 2 * Math.PI); c.fill(); };
  for (let k = 0; k <= n; k++) {
    node(A(k), nodes.A[k], '#cf741b'); node(B(k), nodes.B[k], '#007dc5');
    c.textAlign = 'right'; c.fillStyle = '#cf741b'; c.fillText(kv(nodes.A[k]), A(k)[0] - 24, A(k)[1] + 6);
    c.textAlign = 'left'; c.fillStyle = '#007dc5'; c.fillText(kv(nodes.B[k]), B(k)[0] + 24, B(k)[1] + 6);
  }
  c.textAlign = 'center'; c.fillStyle = '#152d40'; c.fillText('output (HV terminal)', xb, top - 14);
  c.fillStyle = '#7d8f9c'; c.fillText('AC coupling', xa, h - 2); c.fillText('DC stack', xb, h - 2);
  // Output trace.
  ({ c, w, h } = setup($('trace')));
  const L = 56, R = w - 16, T = 18, Bt = h - 36, tmax = Math.max(10, st.t), vmax = 2 * n * 1.1;
  const X = t => L + (R - L) * t / tmax, Y = v => Bt - (Bt - T) * v / vmax;
  c.strokeStyle = '#dce5eb'; c.lineWidth = 1; for (let k = 0; k <= n; k++) { c.beginPath(); c.moveTo(L, Y(2 * k)); c.lineTo(R, Y(2 * k)); c.stroke(); c.fillStyle = '#526675'; c.textAlign = 'right'; c.fillText(String(2 * k * v0), L - 6, Y(2 * k) + 5); }
  c.strokeStyle = '#bd3249'; c.setLineDash([6, 5]); c.beginPath(); c.moveTo(L, Y(2 * n)); c.lineTo(R, Y(2 * n)); c.stroke(); c.setLineDash([]);
  c.strokeStyle = '#007dc5'; c.lineWidth = 2.5; c.beginPath(); trace.forEach(([t, v], i) => i ? c.lineTo(X(t), Y(v)) : c.moveTo(X(t), Y(v))); c.stroke();
  c.fillStyle = '#526675'; c.textAlign = 'left'; c.fillText('output [kV] vs AC cycles · dashed: 2N·V₀', L, Bt + 28);
  window.cwState = { n, vout: nodes.B[n] * v0, ideal: 2 * n * v0, cycles: st.t, playing };
}
function loop() { if (!playing) return; advance(0.02 * +$('speed').value * 2); draw(); raf = requestAnimationFrame(loop); }
$('play').onclick = () => { playing = !playing; draw(); if (playing) loop(); };
$('half').onclick = () => { playing = false; advance(0.5); draw(); };
$('reset').onclick = () => { playing = false; for (const [id, v] of Object.entries({ n: 3, v0: 100, load: '0', speed: '0.5' })) $(id).value = v; rebuild(0); };
$('n').addEventListener('input', () => { playing = false; rebuild(0); });
for (const id of ['v0', 'load']) $(id).addEventListener('input', draw);
window.addEventListener('resize', draw);
rebuild();

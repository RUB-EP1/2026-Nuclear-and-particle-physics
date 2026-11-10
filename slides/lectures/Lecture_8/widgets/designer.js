'use strict';
const $ = id => document.getElementById(id);
const DEFAULTS = { particle: 'proton', energy: 3.845, field: 8.33 };
function fmtLength(m) { return m >= 1000 ? (m / 1000).toPrecision(3) + ' km' : m.toPrecision(3) + ' m'; }
function fmtEnergy(g) {
  const a = Math.abs(g);
  if (a >= 1e3) return (g / 1e3).toPrecision(3) + ' TeV';
  if (a >= 1) return g.toPrecision(3) + ' GeV';
  if (a >= 1e-3) return (g * 1e3).toPrecision(3) + ' MeV';
  if (a >= 1e-6) return (g * 1e6).toPrecision(3) + ' keV';
  return (g * 1e9).toPrecision(3) + ' eV';
}
function fmtCount(n) { return !Number.isFinite(n) ? 'stable' : n >= 1e4 ? n.toExponential(1).replace('e+', '×10^') : n.toFixed(0); }
function setup(canvas) {
  const r = canvas.getBoundingClientRect(), d = devicePixelRatio || 1;
  canvas.width = r.width * d; canvas.height = r.height * d;
  const c = canvas.getContext('2d'); c.scale(d, d); c.font = (r.width > 900 ? '20' : '16') + 'px Helvetica,Arial,sans-serif';
  return { c, w: r.width, h: r.height };
}
function text(c, s, x, y, color = '#526675', align = 'left') { c.fillStyle = color; c.textAlign = align; c.fillText(s, x, y); }
function draw() {
  const particle = $('particle').value, energy = 10 ** +$('energy').value, field = +$('field').value;
  const v = Accel.ring({ particle, energy, field });
  $('energyValue').textContent = fmtEnergy(energy); $('fieldValue').textContent = field.toFixed(2) + ' T';
  $('rho').textContent = fmtLength(v.rho); $('circ').textContent = fmtLength(v.circumference);
  $('loss').textContent = fmtEnergy(v.lossPerTurn);
  $('sqrts').textContent = fmtEnergy(v.sqrtsCollider);
  $('fixed').textContent = `Same beam on a fixed proton target: √s = ${fmtEnergy(v.sqrtsFixed)}`;
  const frac = v.lossFraction;
  $('status').innerHTML = !v.storable ? 'Impossible: each turn would radiate more than the whole beam energy.'
    : frac > 1e-2 ? `Each turn radiates ${(100 * frac).toPrecision(2)}% of the beam energy: RF must replace it every turn.`
    : `Each turn radiates a fraction ${frac.toExponential(1).replace(/e([+-]\d+)/, (m, e) => ' × 10<sup>' + (+e) + '</sup>')} of the beam energy.`;
  $('status').className = 'budget ' + (!v.storable || frac > 1e-2 ? 'over' : 'under');
  $('decay').textContent = particle === 'muon'
    ? `Muon lab lifetime γτ = ${(v.labLifetime * 1e3).toPrecision(3)} ms → about ${fmtCount(v.turnsBeforeDecay)} turns before decay.`
    : `${Accel.PARTICLES[particle].label} are stable; revolution frequency ${(v.frev / 1e3).toPrecision(3)} kHz.`;

  // Ring sizes to scale, with LHC and FCC references.
  let { c, w, h } = setup($('rings'));
  const refs = [{ C: 26659, label: 'LHC 26.7 km', color: '#9aabb6' }, { C: 90700, label: 'FCC 91 km', color: '#c3ced6' }];
  const maxC = Math.max(v.circumference, 90700) * 1.05, cx = w / 2, cy = h / 2 + 8, R = Math.min(w, h) / 2 - 26;
  const r = C => R * C / maxC;
  for (const ref of refs) {
    c.setLineDash([7, 6]); c.strokeStyle = ref.color; c.lineWidth = 2; c.beginPath(); c.arc(cx, cy, r(ref.C), 0, 2 * Math.PI); c.stroke();
    c.setLineDash([]); text(c, ref.label, cx + r(ref.C) * 0.72 + 6, cy - r(ref.C) * 0.72, '#7c8c97');
  }
  c.strokeStyle = '#007dc5'; c.lineWidth = 5; c.beginPath(); c.arc(cx, cy, Math.max(r(v.circumference), 1.5), 0, 2 * Math.PI); c.stroke();
  text(c, 'Your ring ' + fmtLength(v.circumference), 14, 24, '#007dc5');
  if (v.circumference < 2000) text(c, '(drawn at its true scale: a dot)', 14, 48, '#526675');

  // Energy lost per turn on a log axis, with landmarks.
  ({ c, w, h } = setup($('lossbar')));
  const lo = -9, hi = 6, left = 20, right = w - 20, y0 = 52;
  const x = g => left + (right - left) * (Math.log10(Math.max(g, 1e-12)) - lo) / (hi - lo);
  c.fillStyle = '#edf3f7'; c.fillRect(left, y0, right - left, 22);
  c.fillStyle = '#fbe3e7'; c.fillRect(Math.min(right, Math.max(left, x(energy))), y0, right - Math.min(right, Math.max(left, x(energy))), 22);
  const ticks = ['1 eV', '1 keV', '1 MeV', '1 GeV', '1 TeV', '1 PeV'];
  ticks.forEach((t, i) => { const k = lo + 3 * i; c.fillStyle = '#b8c7d2'; c.fillRect(x(10 ** k), y0 + 22, 1, 7); text(c, t, x(10 ** k), y0 + 48, '#526675', i === 0 ? 'left' : i === ticks.length - 1 ? 'right' : 'center'); });
  const marks = [[6.7e-6, 'LHC p'], [3.4, 'LEP2 e']];
  for (const [g, label] of marks) { c.fillStyle = '#526675'; c.fillRect(x(g) - 1, y0 - 6, 2, 34); text(c, label, x(g), y0 - 12, '#526675', 'center'); }
  const xv = Math.min(right, Math.max(left, x(v.lossPerTurn)));
  c.fillStyle = v.storable ? '#007dc5' : '#bd3249'; c.beginPath(); c.arc(xv, y0 + 11, 10, 0, 2 * Math.PI); c.fill();
  text(c, 'energy lost per turn · red: more than the beam energy', left, 18, '#526675');
  window.ringState = v;
}
for (const id of ['particle', 'energy', 'field']) $(id).addEventListener('input', draw);
$('reset').onclick = () => { for (const [id, val] of Object.entries(DEFAULTS)) $(id).value = val; draw(); };
window.addEventListener('resize', draw);
draw();

// Shared kinematics and drawing helpers for the Lecture 2 widgets.
// Natural units, GeV. Particle order for Λb → p K⁻ J/ψ: 1 = p, 2 = K⁻, 3 = J/ψ.
// Pair invariants: s12 = m²(pK), s13 = m²(J/ψ p), s23 = m²(J/ψ K).
(function (root) {
  const LB = { M: 5.6196, m: [0.938272, 0.493677, 3.0969], names: ['p', 'K⁻', 'J/ψ'] };
  // B⁺ → D⁺D⁻K⁺ with the same labelling pattern: 1 = D⁻, 2 = K⁺, 3 = D⁺, so s12 = m²(D⁻K⁺), s13 = m²(D⁻D⁺).
  const DDK = { M: 5.27934, m: [1.86966, 0.493677, 1.86966], names: ['D⁻', 'K⁺', 'D⁺'] };
  // The system used when a function is called without one (W.use(DDK) switches it).
  let CUR = LB;
  const use = (sys) => { CUR = sys; };
  const COLORS = { ink: '#152b41', muted: '#526677', grid: '#dfe7ee', blue: '#087bb9', red: '#d1495b', green: '#2a9d74', purple: '#8c58ad', orange: '#e08a1e', fill: '#f1f6fa' };

  const kallen = (a, b, c) => a * a + b * b + c * c - 2 * a * b - 2 * a * c - 2 * b * c;
  const breakup = (s, ma, mb) => Math.sqrt(Math.max(kallen(s, ma * ma, mb * mb), 0)) / (2 * Math.sqrt(s));

  // Kinematic limits of s12 and, at fixed s12, of s13.
  function s12Range(k = CUR) { return [(k.m[0] + k.m[1]) ** 2, (k.M - k.m[2]) ** 2]; }
  function s13Range(s12, k = CUR) {
    const [m1, m2, m3] = k.m, rs = Math.sqrt(s12);
    const E1 = (s12 + m1 * m1 - m2 * m2) / (2 * rs), E3 = (k.M * k.M - s12 - m3 * m3) / (2 * rs);
    const p1 = Math.sqrt(Math.max(E1 * E1 - m1 * m1, 0)), p3 = Math.sqrt(Math.max(E3 * E3 - m3 * m3, 0));
    const c = m1 * m1 + m3 * m3 + 2 * E1 * E3;
    return [c - 2 * p1 * p3, c + 2 * p1 * p3];
  }
  function s13Range_of_cos(s12, cos, k = CUR) { const [a, b] = s13Range(s12, k); return a + (b - a) * (1 + cos) / 2; }
  function inside(s12, s13, k = CUR) {
    const [lo, hi] = s12Range(k); if (s12 <= lo || s12 >= hi) return false;
    const [a, b] = s13Range(s12, k); return s13 > a && s13 < b;
  }
  // Helicity angle of particle 1 in the (12) rest frame, measured from the direction opposite particle 3.
  function cos12(s12, s13, k = CUR) { const [a, b] = s13Range(s12, k); return (2 * s13 - a - b) / (b - a); }
  // Helicity angle of particle 1 in the (13) rest frame, measured from the direction opposite particle 2.
  function cos13(s12, s13, k = CUR) {
    const swapped = { M: k.M, m: [k.m[0], k.m[2], k.m[1]] };
    return cos12(s13, s12, swapped);
  }
  const s23Of = (s12, s13, k = CUR) => k.M * k.M + k.m[0] ** 2 + k.m[1] ** 2 + k.m[2] ** 2 - s12 - s13;

  // Four-vectors [px, py, pz, E] in the parent rest frame, all momenta in the xz plane.
  function fourVectors(s12, s13, k = CUR) {
    const [m1, m2, m3] = k.m, M = k.M, s23 = s23Of(s12, s13, k);
    const E = [(M * M + m1 * m1 - s23) / (2 * M), (M * M + m2 * m2 - s13) / (2 * M), (M * M + m3 * m3 - s12) / (2 * M)];
    const P = E.map((e, i) => Math.sqrt(Math.max(e * e - k.m[i] ** 2, 0)));
    // p3 along −z; p1 at angle t13 to p3 from (p1+p3)² = s13.
    const c13 = (m1 * m1 + m3 * m3 + 2 * E[0] * E[2] - s13) / (2 * P[0] * P[2]);
    const t = Math.acos(Math.max(-1, Math.min(1, c13)));
    const v3 = [0, 0, -P[2], E[2]];
    const v1 = [P[0] * Math.sin(t), 0, -P[0] * Math.cos(t), E[0]];
    const v2 = [-v1[0] - v3[0], 0, -v1[2] - v3[2], E[1]];
    return [v1, v2, v3];
  }
  function boostToRest(v, p) { // boost four-vector v into the rest frame of p
    const m = Math.sqrt(Math.max(p[3] ** 2 - p[0] ** 2 - p[1] ** 2 - p[2] ** 2, 1e-12));
    const b = [p[0] / p[3], p[1] / p[3], p[2] / p[3]], b2 = b[0] ** 2 + b[1] ** 2 + b[2] ** 2;
    if (b2 < 1e-14) return v.slice();
    const g = p[3] / m, bp = b[0] * v[0] + b[1] * v[1] + b[2] * v[2], f = (g - 1) * bp / b2 - g * v[3];
    return [v[0] + f * b[0], v[1] + f * b[1], v[2] + f * b[2], g * (v[3] - bp)];
  }
  const add = (a, b) => a.map((x, i) => x + b[i]);
  function angleBetween(a, b) {
    const d = a[0] * b[0] + a[1] * b[1] + a[2] * b[2], na = Math.hypot(a[0], a[1], a[2]), nb = Math.hypot(b[0], b[1], b[2]);
    return Math.acos(Math.max(-1, Math.min(1, d / (na * nb))));
  }
  // Wigner angle between the proton helicity frames of the (pK) chain and the (J/ψ p) chain.
  // In the proton rest frame, the two chains quantise the spin along the directions of the two
  // pairs; the rotation that aligns them is a rotation about the decay-plane normal by this angle.
  function protonWigner(s12, s13, k = CUR) {
    const [v1, v2, v3] = fourVectors(s12, s13, k);
    return angleBetween(boostToRest(add(v1, v2), v1), boostToRest(add(v1, v3), v1));
  }

  // Line shapes and angular functions.
  function bw(s, m, w) { // 1/(m² − s − i m Γ) as [re, im], scaled by mΓ so |A| ≤ 1
    const a = m * m - s, b = m * w, d = a * a + b * b; return [a * b / d, b * b / d];
  }
  function legendre(J, x) {
    if (J === 0) return 1; if (J === 1) return x;
    let p0 = 1, p1 = x; for (let n = 2; n <= J; n++) { const p2 = ((2 * n - 1) * x * p1 - (n - 1) * p0) / n; p0 = p1; p1 = p2; } return p1;
  }
  const cmul = (a, b) => [a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]];
  const cadd = (a, b) => [a[0] + b[0], a[1] + b[1]];
  const cabs2 = (a) => a[0] * a[0] + a[1] * a[1];
  const cexp = (phi) => [Math.cos(phi), Math.sin(phi)];

  // Seeded random numbers, so print fallbacks are reproducible.
  function rng(seed = 7) { let s = seed >>> 0; return () => ((s = (s * 1664525 + 1013904223) >>> 0) / 4294967296); }
  // Uniform phase-space events: uniform in (s12, s13) inside the boundary.
  function phaseSpaceEvents(n, seed = 7, k = CUR) {
    const r = rng(seed), [x0, x1] = s12Range(k), y0 = (k.m[0] + k.m[2]) ** 2, y1 = (k.M - k.m[1]) ** 2, out = [];
    while (out.length < n) { const x = x0 + (x1 - x0) * r(), y = y0 + (y1 - y0) * r(); if (inside(x, y, k)) out.push([x, y]); }
    return out;
  }
  // Events following an intensity f(s12, s13) by accept–reject.
  function sampleEvents(n, f, fmax, seed = 11, k = CUR) {
    const r = rng(seed), [x0, x1] = s12Range(k), y0 = (k.m[0] + k.m[2]) ** 2, y1 = (k.M - k.m[1]) ** 2, out = [];
    let guard = 0;
    while (out.length < n && guard++ < 4e6) {
      const x = x0 + (x1 - x0) * r(), y = y0 + (y1 - y0) * r();
      if (inside(x, y, k) && r() * fmax < f(x, y)) out.push([x, y]);
    }
    return out;
  }

  // ── Canvas ───────────────────────────────────────────────────────────────
  function setupCanvas(canvas) {
    const z = parseFloat(getComputedStyle(document.documentElement).zoom) || 1; // keep the canvas sharp under CSS zoom
    const r = (window.devicePixelRatio || 1) * z, w = canvas.clientWidth, h = canvas.clientHeight;
    canvas.width = Math.round(w * r); canvas.height = Math.round(h * r);
    const ctx = canvas.getContext('2d'); ctx.setTransform(r, 0, 0, r, 0, 0); ctx.clearRect(0, 0, w, h);
    return { ctx, w, h };
  }
  // A rectangular plot area with linear axes.
  function frame(ctx, box, xr, yr, opt = {}) {
    const { x, y, w, h } = box;
    const X = (v) => x + (v - xr[0]) / (xr[1] - xr[0]) * w, Y = (v) => y + h - (v - yr[0]) / (yr[1] - yr[0]) * h;
    ctx.save();
    ctx.strokeStyle = COLORS.muted; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x, y + h); ctx.lineTo(x + w, y + h); ctx.stroke();
    ctx.fillStyle = COLORS.muted; ctx.font = '17px Helvetica, Arial, sans-serif';
    (opt.xticks || []).forEach((t) => { ctx.textAlign = 'center'; ctx.fillText(opt.xfmt ? opt.xfmt(t) : t, X(t), y + h + 22); ctx.beginPath(); ctx.moveTo(X(t), y + h); ctx.lineTo(X(t), y + h + 6); ctx.stroke(); });
    (opt.yticks || []).forEach((t) => { ctx.textAlign = 'right'; ctx.fillText(opt.yfmt ? opt.yfmt(t) : t, x - 9, Y(t) + 6); ctx.beginPath(); ctx.moveTo(x - 6, Y(t)); ctx.lineTo(x, Y(t)); ctx.stroke(); });
    ctx.fillStyle = COLORS.ink; ctx.font = '19px Helvetica, Arial, sans-serif';
    if (opt.xlabel) { ctx.textAlign = 'center'; ctx.fillText(opt.xlabel, x + w / 2, y + h + 50); }
    if (opt.ylabel) { ctx.textAlign = 'left'; ctx.fillText(opt.ylabel, x - 4, y - 14); }
    ctx.restore();
    return { X, Y };
  }
  function ticks(a, b, step) { const out = []; for (let t = Math.ceil(a / step) * step; t <= b + 1e-9; t += step) out.push(+t.toFixed(6)); return out; }
  function boundaryPath(ctx, X, Y, k = CUR, n = 240) {
    const [x0, x1] = s12Range(k), lo = [], hi = [];
    for (let i = 0; i <= n; i++) { const s = x0 + (x1 - x0) * (0.5 - 0.5 * Math.cos(Math.PI * i / n)); const [a, b] = s13Range(s, k); lo.push([s, a]); hi.push([s, b]); }
    ctx.beginPath(); lo.forEach(([s, v], i) => (i ? ctx.lineTo(X(s), Y(v)) : ctx.moveTo(X(s), Y(v)))); hi.reverse().forEach(([s, v]) => ctx.lineTo(X(s), Y(v))); ctx.closePath();
  }
  function curve(ctx, pts, X, Y, color, width = 3, dash) {
    ctx.save(); ctx.strokeStyle = color; ctx.lineWidth = width; if (dash) ctx.setLineDash(dash);
    ctx.beginPath(); pts.forEach(([a, b], i) => (i ? ctx.lineTo(X(a), Y(b)) : ctx.moveTo(X(a), Y(b)))); ctx.stroke(); ctx.restore();
  }
  function text(ctx, s, x, y, opt = {}) {
    ctx.save(); ctx.fillStyle = opt.color || COLORS.ink; ctx.font = `${opt.weight || ''} ${opt.size || 20}px Helvetica, Arial, sans-serif`;
    ctx.textAlign = opt.align || 'left'; ctx.fillText(s, x, y); ctx.restore();
  }
  // Colour map for densities: white → deep blue.
  function blues(t) { t = Math.max(0, Math.min(1, t)); const a = [255, 255, 255], b = [8, 123, 185], c = [12, 45, 90];
    const [p, q, u] = t < 0.6 ? [a, b, t / 0.6] : [b, c, (t - 0.6) / 0.4]; return p.map((v, i) => Math.round(v + (q[i] - v) * u)); }
  // Density map drawn into an offscreen image; f returns a non-negative value.
  function densityImage(ctx, box, xr, yr, f, fmax, k = CUR, res = 3) {
    const { x, y, w, h } = box, img = ctx.createImageData(Math.ceil(w / res), Math.ceil(h / res));
    for (let j = 0; j < img.height; j++) for (let i = 0; i < img.width; i++) {
      const sx = xr[0] + (i + 0.5) / img.width * (xr[1] - xr[0]), sy = yr[1] - (j + 0.5) / img.height * (yr[1] - yr[0]);
      const o = 4 * (j * img.width + i);
      if (!inside(sx, sy, k)) { img.data[o + 3] = 0; continue; }
      const c = blues(Math.sqrt(f(sx, sy) / fmax)); img.data[o] = c[0]; img.data[o + 1] = c[1]; img.data[o + 2] = c[2]; img.data[o + 3] = 255;
    }
    const off = document.createElement('canvas'); off.width = img.width; off.height = img.height; off.getContext('2d').putImageData(img, 0, 0);
    ctx.save(); ctx.imageSmoothingEnabled = true; ctx.drawImage(off, x, y, w, h); ctx.restore();
  }

  // ── Controls ─────────────────────────────────────────────────────────────
  function slider(host, label, min, max, step, value, onInput, fmt = (v) => v) {
    const l = document.createElement('label'), i = document.createElement('input'), o = document.createElement('output');
    l.innerHTML = `<span>${label}</span>`; Object.assign(i, { type: 'range', min, max, step, value });
    o.textContent = fmt(+value); i.addEventListener('input', () => { o.textContent = fmt(+i.value); onInput(+i.value); });
    l.append(i, o); host.append(l); return i;
  }
  function choice(host, label, options, value, onChange) {
    const l = document.createElement('label'), s = document.createElement('select');
    l.innerHTML = `<span>${label}</span>`;
    options.forEach(([v, t]) => { const o = document.createElement('option'); o.value = v; o.textContent = t; s.append(o); });
    s.value = value; s.addEventListener('change', () => onChange(s.value)); l.append(s); host.append(l); return s;
  }
  function toggle(host, label, value, onChange) {
    const l = document.createElement('label'), i = document.createElement('input');
    i.type = 'checkbox'; i.checked = value; i.addEventListener('change', () => onChange(i.checked));
    l.append(i, document.createTextNode(label)); host.append(l); return i;
  }
  const params = () => new URLSearchParams(location.search);
  // Redraw on resize and once fonts are ready; skip while the frame is hidden (zero size).
  function live(draw) {
    const safe = () => { const c = document.querySelector('canvas'); if (c && c.clientWidth > 50 && c.clientHeight > 50) draw(); };
    safe(); window.addEventListener('resize', safe); if (document.fonts) document.fonts.ready.then(safe);
  }

  root.W = { LB, DDK, use, COLORS, kallen, breakup, s12Range, s13Range, s13Range_of_cos, inside, cos12, cos13, s23Of, fourVectors, boostToRest, add, angleBetween, protonWigner,
    bw, legendre, cmul, cadd, cabs2, cexp, rng, phaseSpaceEvents, sampleEvents,
    setupCanvas, frame, ticks, boundaryPath, curve, text, blues, densityImage, slider, choice, toggle, params, live };
})(typeof window !== 'undefined' ? window : globalThis);

'use strict';
// Deterministic teaching models shared by the Lecture 8 widgets and tests.
(function (root) {
  // ---- Cockcroft–Walton ladder --------------------------------------------------------------
  // Nodes: A0 = AC source (amplitude 1), A1..AN oscillating column, B0 = ground, B1..BN DC column.
  // Capacitors (all C = 1): push column A_{k-1}–A_k, stack column B_{k-1}–B_k.
  // Ideal diodes with small series resistance r: B_{k-1} -> A_k and A_k -> B_k. Optional load R_L from B_N to ground.
  function cwCreate(stages) {
    return { n: stages, t: 0, p: new Array(stages).fill(0), s: new Array(stages).fill(0) };
  }
  function cwNodes(st) {
    const src = Math.sin(2 * Math.PI * st.t), A = [src], B = [0];
    for (let k = 0; k < st.n; k++) { A.push(A[k] + st.p[k]); B.push(B[k] + st.s[k]); }
    return { A, B, src };
  }
  function cwStep(st, dt, { r = 0.02, load = 0 } = {}) {
    const { A, B } = cwNodes(st), n = st.n;
    const dUp = [], dOut = [];          // dUp[k]: B_{k} -> A_{k+1}; dOut[k]: A_{k+1} -> B_{k+1}
    for (let k = 0; k < n; k++) {
      dUp.push(Math.max(0, B[k] - A[k + 1]) / r);
      dOut.push(Math.max(0, A[k + 1] - B[k + 1]) / r);
    }
    const injA = [], injB = [];
    for (let k = 0; k < n; k++) {
      injA.push(dUp[k] - dOut[k]);
      injB.push(dOut[k] - (k + 1 < n ? dUp[k + 1] : 0) - (k + 1 === n && load > 0 ? B[n] / load : 0));
    }
    // Current injected at node k flows to the source/ground through capacitors 1..k.
    for (let k = 0; k < n; k++) for (let j = 0; j <= k; j++) { st.p[j] += injA[k] * dt; st.s[j] += injB[k] * dt; }
    st.t += dt;
    return { diodes: dUp.map((u, k) => [u, dOut[k]]) };
  }
  function cwRun(stages, cycles, opts = {}) {
    const st = cwCreate(stages), dt = opts.dt || 1e-3;
    const steps = Math.round(cycles / dt); const trace = [];
    for (let i = 0; i < steps; i++) { cwStep(st, dt, opts); if (i % Math.round(0.05 / dt) === 0) trace.push([st.t, cwNodes(st).B[stages]]); }
    return { state: st, trace, vout: cwNodes(st).B[stages] };
  }

  // ---- RF cavity: chain of pi-mode cells, each lambda/2 long, particle at v = c -------------
  // Field in cell k: E_z = E0 (-1)^k cos(omega t + phi). Returns energy gain in units of E0*lambda/2 per cell.
  function rfGain(phiDeg, cells = 1, steps = 400) {
    const phi = phiDeg * Math.PI / 180; let gain = 0;
    for (let k = 0; k < cells; k++) for (let i = 0; i < steps; i++) {
      const z = k + (i + 0.5) / steps;            // position in units of lambda/2
      const omegaT = Math.PI * (z - 0.5);         // omega t = pi z; phase origin: crest at the centre of cell 0
      gain += ((k % 2) ? -1 : 1) * Math.cos(omegaT + phi) / steps;
    }
    return gain; // per unit E0*(lambda/2); maximum per cell is 2/pi (transit-time factor)
  }

  // ---- Emittance: particles in (x, x') through drifts and thin lenses -------------------------
  function emitBeam(n = 400, seed = 11, eps = 1, beta = 1) {
    let a = seed >>> 0; const rnd = () => ((a = (a * 1664525 + 1013904223) >>> 0) / 4294967296);
    const pts = [];
    for (let i = 0; i < n; i++) {
      const u = Math.sqrt(-2 * Math.log(rnd() + 1e-12)), th = 2 * Math.PI * rnd();
      const r = u * Math.sqrt(eps);
      pts.push([r * Math.cos(th) * Math.sqrt(beta), r * Math.sin(th) / Math.sqrt(beta)]);
    }
    return pts;
  }
  const drift = L => ([x, xp]) => [x + L * xp, xp];
  const lens = f => ([x, xp]) => [x, xp - x / f];
  const boost = g => ([x, xp]) => [x, xp / g];   // acceleration by factor g in momentum: x' = p_x / p shrinks
  function rmsEmittance(pts) {
    const n = pts.length; let mx = 0, mp = 0; for (const [x, p] of pts) { mx += x; mp += p; } mx /= n; mp /= n;
    let xx = 0, pp = 0, xp = 0; for (const [x, p] of pts) { xx += (x - mx) ** 2; pp += (p - mp) ** 2; xp += (x - mx) * (p - mp); }
    xx /= n; pp /= n; xp /= n; return { eps: Math.sqrt(Math.max(xx * pp - xp * xp, 0)), sx: Math.sqrt(xx), sp: Math.sqrt(pp) };
  }

  const api = { cwCreate, cwNodes, cwStep, cwRun, rfGain, emitBeam, drift, lens, boost, rmsEmittance };
  if (typeof module !== 'undefined') module.exports = api; else root.Phys = api;
})(this);

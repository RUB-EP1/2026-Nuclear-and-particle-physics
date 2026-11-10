'use strict';
const assert = require('assert');
const P = require('../widgets/physics.js');
const close = (a, b, tol, msg) => assert(Math.abs(a - b) <= tol, `${msg}: ${a} vs ${b}`);
// Cockcroft–Walton: unloaded ladder approaches 2N times the peak input; a load lowers it.
for (const n of [1, 2, 3]) {
  const run = P.cwRun(n, 40 * n * n);
  close(run.vout, 2 * n, 0.12 * n, `CW ${n} stages unloaded`);
}
const loaded = P.cwRun(3, 200, { load: 200 }).vout, free = P.cwRun(3, 200).vout;
assert(loaded < free - 0.1, `load must lower the output (${loaded} vs ${free})`);
// RF: one pi-mode cell at crest gives the transit-time factor 2/pi; gain is odd about 90 degrees; cells add.
close(P.rfGain(0, 1), 2 / Math.PI, 1e-3, 'single-cell transit factor');
close(P.rfGain(90, 1), 0, 1e-6, 'zero-crossing gain');
close(P.rfGain(180, 1), -2 / Math.PI, 1e-3, 'decelerating phase');
close(P.rfGain(0, 9), 9 * 2 / Math.PI, 5e-3, 'nine cells add');
close(P.rfGain(30, 1), (2 / Math.PI) * Math.cos(Math.PI / 6), 1e-3, 'cos(phi) dependence');
// Emittance: drifts and lenses conserve rms emittance; acceleration divides it by the momentum ratio.
let b = P.emitBeam(2000, 3); const e0 = P.rmsEmittance(b).eps;
for (let i = 0; i < 5; i++) b = b.map(P.drift(1.3)).map(P.lens(0.9));
close(P.rmsEmittance(b).eps, e0, 1e-9 + 1e-9 * e0, 'Liouville under linear optics');
close(P.rmsEmittance(b.map(P.boost(4))).eps, e0 / 4, 1e-9, 'adiabatic damping');
console.log('Cockcroft–Walton ladder, RF transit factor and emittance checks passed.');

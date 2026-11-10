'use strict';
const assert = require('assert');
const { ring } = require('../widgets/ring.js');
const close = (a, b, rel, msg) => assert(Math.abs(a / b - 1) < rel, `${msg}: ${a} vs ${b}`);
// LHC: 7 TeV protons, 8.33 T -> rho ~ 2.80 km, circumference ~ 26.7 km, ~6.7 keV per turn.
const lhc = ring({ particle: 'proton', energy: 7000, field: 8.33 });
close(lhc.rho, 2803, 0.01, 'LHC bending radius');
close(lhc.circumference, 26690, 0.01, 'LHC circumference');
close(lhc.lossPerTurn, 6.7e-6, 0.03, 'LHC synchrotron loss');
close(lhc.frev, 11232, 0.01, 'LHC revolution frequency');
close(lhc.sqrtsFixed, 114.6, 0.01, 'fixed-target sqrt(s)');
// LEP2 check: 104.5 GeV electrons at rho = 3096 m lose ~3.4 GeV per turn (field chosen to give that rho).
const lep = ring({ particle: 'electron', energy: 104.5, field: 104.5 / (0.299792458 * 3096) });
close(lep.lossPerTurn, 3.41, 0.02, 'LEP2 synchrotron loss');
// A 7 TeV electron ring in the LHC tunnel cannot store the beam.
assert(!ring({ particle: 'electron', energy: 7000, field: 8.33 }).storable, 'electron LHC must be impossible');
// Muon lifetime: gamma * 2.197 us; finite number of turns; mass scaling of losses (m_e/m_mu)^4.
const mu = ring({ particle: 'muon', energy: 1500, field: 10 });
close(mu.labLifetime, 1500 / 0.105658 * 2.197e-6, 1e-6, 'muon lab lifetime');
assert(Number.isFinite(mu.turnsBeforeDecay) && mu.turnsBeforeDecay > 100, 'muon turns');
const e = ring({ particle: 'electron', energy: 1500, field: 10 });
close(e.lossPerTurn / mu.lossPerTurn, (0.105658 / 0.000510999) ** 4, 1e-6, 'mass^4 scaling');
console.log('Ring model: LHC, LEP2, fixed-target, electron-LHC impossibility and muon checks passed.');

'use strict';
// Analytic ring model shared by the widget and tests. Units: GeV, T, m, s.
(function (root) {
  const C_GAMMA = 8.85e-5;            // m GeV^-3, electrons: dE/turn = C_GAMMA E^4 / rho
  const FILL = 0.66;                  // fraction of the circumference filled with dipoles (LHC ~ 17.6/26.7 km)
  const C = 299792458;                // m/s
  const PARTICLES = {
    electron: { label: 'Electrons', mass: 0.000510999, tau: Infinity },
    muon: { label: 'Muons', mass: 0.105658, tau: 2.1970e-6 },
    proton: { label: 'Protons', mass: 0.938272, tau: Infinity }
  };
  function ring({ particle = 'proton', energy = 7000, field = 8.33 }) {
    const p = PARTICLES[particle];
    const momentum = Math.sqrt(Math.max(energy * energy - p.mass * p.mass, 0));
    const rho = momentum / (0.299792458 * field);                     // m
    const circumference = 2 * Math.PI * rho / FILL;                   // m
    const gamma = energy / p.mass;
    const lossPerTurn = C_GAMMA * Math.pow(energy, 4) / rho * Math.pow(PARTICLES.electron.mass / p.mass, 4); // GeV
    const frev = C / circumference;                                    // Hz (beta ~ 1)
    const labLifetime = gamma * p.tau;                                 // s
    const turnsBeforeDecay = Number.isFinite(labLifetime) ? labLifetime * frev : Infinity;
    const sqrtsCollider = 2 * energy;
    const sqrtsFixed = Math.sqrt(2 * energy * 0.938272 + p.mass * p.mass + 0.938272 * 0.938272);
    return { particle, energy, field, rho, circumference, gamma, lossPerTurn, lossFraction: lossPerTurn / energy,
             frev, labLifetime, turnsBeforeDecay, sqrtsCollider, sqrtsFixed, storable: lossPerTurn < energy };
  }
  const api = { ring, PARTICLES, FILL, C_GAMMA };
  if (typeof module !== 'undefined') module.exports = api; else root.Accel = api;
})(this);

"""Lecture 8 (accelerators): analytic teaching figures. No measured data; all inputs are stated below."""
from pathlib import Path
import os
ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault('MPLCONFIGDIR', str(ROOT / 'tmp/matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

B = '#007dc5'; O = '#cf741b'; R = '#bd3249'; G = '#268565'; GR = '#607382'; LG = '#9aabb6'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 17, 'axes.labelsize': 18, 'axes.titlesize': 20,
                     'axes.spines.top': False, 'axes.spines.right': False, 'axes.edgecolor': '#b8c7d2',
                     'grid.color': '#e0e8ed', 'svg.fonttype': 'none', 'lines.linewidth': 3,
                     'legend.frameon': False, 'figure.facecolor': 'white'})
OUT = ROOT / 'figures'
MP, ME, MMU = 0.938272, 0.000510999, 0.105658  # GeV


def plot(title=None):
    f, a = plt.subplots(figsize=(10.6, 6.5), layout='constrained')
    a.grid(alpha=.75); a.set_axisbelow(True)
    if title:
        a.set_title(title, loc='left', pad=16)
    return f, a


def save(f, name):
    f.savefig(OUT / (name + '.svg')); plt.close(f)


# 1. Fixed target versus symmetric collider: sqrt(s) for a proton beam.
f, a = plot('Collision energy available to make new particles')
E = np.geomspace(1, 1e5, 300)
a.loglog(E, 2 * E, color=B, label='Collider: two beams of energy E')
a.loglog(E, np.sqrt(2 * MP * E + 2 * MP**2), color=O, label='Fixed target: beam E on a proton at rest')
for x, y, c, t, dx, dy in [(7000, 14000, B, '14 TeV', .25, 1.6), (7000, np.sqrt(2 * MP * 7000 + 2 * MP**2), O, '115 GeV', .25, .45)]:
    a.scatter(x, y, color=c, s=80, zorder=3); a.annotate(t, (x, y), xytext=(x * dx, y * dy), color=c, fontsize=17)
a.axvline(7000, color=LG, ls=':', lw=2); a.text(7600, 2.2, 'LHC beam\n7 TeV', color=GR, fontsize=15)
a.set(xlabel='Beam energy E [GeV]', ylabel='√s [GeV]', ylim=(1, 4e5)); a.legend(loc='upper left'); save(f, 'fixed-target-collider')

# 2. RF phase stability (below transition): later particles see a larger voltage and catch up.
f, a = plot('A bunch forms around the synchronous phase')
ph = np.linspace(-30, 210, 500)
a.plot(ph, np.sin(np.radians(ph)), color=LG, lw=2.5, label='Cavity voltage seen on arrival')
for p, c, lab in [(10, O, 'early: smaller kick'), (35, B, 'synchronous'), (60, G, 'late: larger kick')]:
    v = np.sin(np.radians(p)); a.vlines(p, 0, v, color=c, lw=2, ls='--'); a.scatter(p, v, color=c, s=110, zorder=3)
    a.annotate(lab, (p, v), xytext=(p + 8, v - .32 if p != 60 else v + .12), color=c, fontsize=16)
a.axhline(0, color='#b8c7d2', lw=1)
a.set(xlabel='Arrival phase [degrees]', ylabel='Energy gain [arb. units]', ylim=(-.6, 1.25), xlim=(-30, 210))
a.legend(loc='upper right'); save(f, 'rf-phase-stability')

# 3. Bending radius rho = p / (0.3 B) for three dipole technologies.
f, a = plot('Stronger magnets make smaller rings')
E = np.geomspace(10, 1e5, 300)
for Bf, c, lab in [(1.8, LG, '1.8 T · iron, normal conducting'), (8.33, B, '8.33 T · Nb–Ti at 1.9 K (LHC)'), (16, O, '16 T · Nb₃Sn goal (FCC-hh)')]:
    a.loglog(E, E / (.3 * Bf) / 1000, color=c, label=lab)
for x, Bf, c, lab, dx, dy in [(450, 2.0, GR, 'SPS 450 GeV', .2, 1.6), (7000, 8.33, B, 'LHC 7 TeV', .18, 1.7), (50000, 16, O, 'FCC-hh 50 TeV', .13, 1.9)]:
    rho = x / (.3 * Bf) / 1000; a.scatter(x, rho, color=c, s=80, zorder=3)
    a.annotate(f'{lab}: ρ = {rho:.2g} km', (x, rho), xytext=(x * dx, rho * dy), color=c, fontsize=15)
a.set(xlabel='Beam momentum [GeV/c]', ylabel='Bending radius ρ [km]', ylim=(5e-3, 300)); a.legend(loc='upper left', fontsize=15)
save(f, 'bending-radius')

# 4. FODO channel: thin lenses of focal length +-f, spacing L, both transverse planes.
f, axes = plt.subplots(2, 1, figsize=(10.6, 6.5), layout='constrained', sharex=True)
fl, L, cells = 1.2, 1.0, 6
starts = [(1.0, 0.0), (0.0, 0.8), (-0.6, 0.5)]
for a, plane in zip(axes, ['x', 'y']):
    sign = 1 if plane == 'x' else -1
    for k in range(2 * cells + 1):
        foc = (k % 2 == 0) == (sign == 1)
        a.axvline(k * L, color=B if foc else O, lw=5 if foc else 2.5, alpha=.35)
    for (x0, xp0), c in zip(starts, [B, G, R]):
        zs, xs = [0], [x0]; x, xp = x0, xp0
        for k in range(2 * cells):
            kick = (1 if k % 2 == 0 else -1) * sign / fl
            xp -= kick * x
            for z in np.linspace(0, L, 20)[1:]:
                zs.append(k * L + z); xs.append(x + xp * z)
            x = x + xp * L
        a.plot(zs, xs, color=c, lw=2.2)
    a.set_ylabel(f'{plane} [arb.]'); a.grid(alpha=.6); a.set_ylim(-3, 3)
    a.set_title(f'{plane} plane (thick: focusing, thin: defocusing)', loc='left', fontsize=16, color=GR)
axes[1].set_xlabel('Position along the beam line [cell lengths]'); save(f, 'fodo-trajectories')

# 5. Synchrotron radiation: Delta E per turn = C_gamma E^4 / rho, C_gamma = 8.85e-5 m GeV^-3 for electrons.
f, a = plot('Energy radiated per turn in a 27 km ring')
E = np.geomspace(1, 1e4, 300); r4 = (ME / MP)**4
lossE = lambda e: 8.85e-5 * e**4 / 3096
lossP = lambda e: 8.85e-5 * e**4 / 2804 * r4
a.loglog(E, lossE(E), color=R, label='Electrons (ρ = 3.1 km)')
a.loglog(E, lossP(E), color=B, label='Protons (ρ = 2.8 km)')
a.loglog(E, E, color=LG, ls=':', label='Entire beam energy')
a.scatter([104.5, 7000], [lossE(104.5), lossP(7000)], color=[R, B], s=90, zorder=3)
a.annotate(f'LEP2, 104.5 GeV: {lossE(104.5):.1f} GeV/turn', (104.5, lossE(104.5)), xytext=(110, 1e-2), color=R, fontsize=16)
a.annotate(f'LHC, 7 TeV: {lossP(7000)*1e6:.1f} keV/turn', (7000, lossP(7000)), xytext=(150, 3e-7), color=B, fontsize=16)
a.set(xlabel='Beam energy [GeV]', ylabel='Energy lost per turn [GeV]', ylim=(1e-12, 1e5)); a.legend(loc='upper left')
save(f, 'synchrotron-loss')

# 6. Livingston-style plot for colliders: maximum sqrt(s) [GeV], plotted at the first year that energy was reached.
f, a = plot('Collision energy of colliders')
ee = [('ADONE', 1969, 3), ('SPEAR', 1972, 8), ('PETRA', 1978, 46.8), ('TRISTAN', 1986, 64), ('LEP', 1989, 91), ('LEP2', 2000, 209)]
hh = [('ISR', 1971, 63), ('SppS', 1981, 630), ('Tevatron', 1987, 1800), ('RHIC pp', 2009, 500), ('LHC', 2010, 7000), ('LHC', 2015, 13000), ('LHC', 2022, 13600)]
ep = [('HERA', 1992, 300)]
for data, c, mk, lab in [(ee, R, 'o', 'e⁺e⁻'), (hh, B, 's', 'Hadron (pp, pp̄)'), (ep, G, 'D', 'ep')]:
    a.semilogy([d[1] for d in data], [d[2] for d in data], mk, color=c, ms=11, label=lab)
    for name, yr, e in data:
        if name == 'LHC' and yr != 2010: continue
        a.annotate(name, (yr, e), xytext=(6, -16 if name in ('ADONE', 'TRISTAN', 'RHIC pp') else 7), textcoords='offset points', color=c, fontsize=14)
yr = np.array([1965, 1992]); a.semilogy(yr, 3 * 10 ** ((yr - 1969) / 15), color=LG, ls='--', lw=2)
a.text(1966, 900, '×10 every 15 years', color=GR, fontsize=15)
a.set(xlabel='Year', ylabel='√s [GeV]', xlim=(1965, 2030), ylim=(1, 5e4)); a.legend(loc='lower right')
save(f, 'collider-history')

print('6 reproducible plots generated.')

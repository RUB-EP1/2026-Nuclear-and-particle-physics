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
ep = [('HERA', 1992, 318)]
for data, c, mk, lab in [(ee, R, 'o', 'e⁺e⁻'), (hh, B, 's', 'Hadron (pp, pp̄)'), (ep, G, 'D', 'ep')]:
    a.semilogy([d[1] for d in data], [d[2] for d in data], mk, color=c, ms=11, label=lab)
    for name, yr, e in data:
        if name == 'LHC' and yr != 2010: continue
        a.annotate(name, (yr, e), xytext=(6, -16 if name in ('ADONE', 'TRISTAN', 'RHIC pp') else 7), textcoords='offset points', color=c, fontsize=14)
yr = np.array([1965, 1992]); a.semilogy(yr, 3 * 10 ** ((yr - 1969) / 15), color=LG, ls='--', lw=2)
a.text(1966, 900, '×10 every 15 years', color=GR, fontsize=15)
a.set(xlabel='Year', ylabel='√s [GeV]', xlim=(1965, 2030), ylim=(1, 5e4)); a.legend(loc='lower right')
save(f, 'collider-history')

# 7. Dipole and quadrupole: field lines B and force on a positive particle moving into the page (v along -z).
f, axes = plt.subplots(1, 2, figsize=(12.4, 6.4), layout='constrained')
f.get_layout_engine().set(h_pad=0.25)
gg = np.linspace(-1.05, 1.05, 200); XX, YY = np.meshgrid(gg, gg)
g = np.linspace(-.8, .8, 5); X, Y = np.meshgrid(g, g); inside = X**2 + Y**2 <= .8
for a, kind in zip(axes, ['dipole', 'quadrupole']):
    BXX, BYY = (np.zeros_like(XX), np.ones_like(XX)) if kind == 'dipole' else (YY, XX)
    a.streamplot(gg, gg, BXX, BYY, color='#7fb8de', density=1.0, linewidth=1.6, arrowsize=1.3)
    Bx, By = (np.zeros_like(X), np.ones_like(X)) if kind == 'dipole' else (Y, X)
    Fx, Fy = By, -Bx      # (-z) x B
    a.quiver(X[inside], Y[inside], Fx[inside], Fy[inside], color=O, scale=10, width=.007, zorder=3)
    a.add_patch(plt.Circle((0, 0), 1.05, fill=False, color='#9aabb6', lw=2))
    if kind == 'dipole':
        for yy, lab in ((1.3, 'S'), (-1.3, 'N')):  # field points up: leaves N (bottom), enters S (top)
            a.add_patch(plt.Rectangle((-1.1, yy - .12), 2.2, .24, color='#c87533' if lab == 'N' else '#7c8c97')); a.text(1.25, yy - .06, lab, fontsize=17)
        a.set_title('Dipole: same force everywhere → bends', loc='left', fontsize=18)
    else:
        for ang, lab in zip([45, 135, 225, 315], ['S', 'N', 'S', 'N']):  # B = (y, x) leaves the 135° and 315° poles
            r = np.radians(ang); a.add_patch(plt.Circle((1.3 * np.cos(r), 1.3 * np.sin(r)), .16, color='#c87533' if lab == 'N' else '#7c8c97')); a.text(1.55 * np.cos(r) - .05, 1.55 * np.sin(r) - .07, lab, fontsize=16)
        a.set_title('Quadrupole: force ∝ distance → a lens', loc='left', fontsize=18)
        a.text(0, -1.72, 'here: pushes out in x, in towards the axis in y', ha='center', fontsize=15, color=GR)
    a.set_aspect('equal'); a.set_xlim(-1.8, 1.8); a.set_ylim(-1.85, 1.75); a.axis('off')
axes[0].plot([], [], color='#7fb8de', lw=3, label='field lines B'); axes[0].plot([], [], color=O, lw=6, label='force on a proton entering the page')
axes[0].legend(loc='lower left', bbox_to_anchor=(-.02, -.08), fontsize=15)
save(f, 'magnet-fields')

# 8. Radiation pattern for acceleration perpendicular to velocity (orbit plane), Jackson 14.44:
# dP/dOmega ∝ [(1 - b cos t)^2 - (1 - b^2) sin^2 t cos^2 phi] / (1 - b cos t)^5, phi = 0 (plane of the orbit).
f, axes = plt.subplots(1, 2, figsize=(10.6, 5.6), layout='constrained', subplot_kw={'projection': 'polar'})
th = np.linspace(0, 2 * np.pi, 1440)
for a, b, lab in zip(axes, [0.0, 0.9], ['v ≪ c: dipole pattern', 'v = 0.9 c: forward cone ~1/γ']):
    num = (1 - b * np.cos(th))**2 - (1 - b**2) * np.sin(th)**2
    P = np.clip(num, 0, None) / (1 - b * np.cos(th))**5; P /= P.max()
    a.plot(th, P, color=R, lw=2.5); a.fill(th, P, color=R, alpha=.15)
    a.annotate('', xy=(0, 1.15), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=B, lw=2.5))
    a.annotate('', xy=(np.pi / 2, .7), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=G, lw=2.5))
    a.set_rticks([]); a.set_thetagrids([]); a.set_ylim(0, 1.2); a.set_title(lab, fontsize=17, pad=10)
axes[0].text(0.05, 1.25, 'v', color=B, fontsize=16); axes[0].text(np.pi / 2 + .25, .8, 'a', color=G, fontsize=16)
save(f, 'radiation-pattern')

print('8 reproducible plots generated.')

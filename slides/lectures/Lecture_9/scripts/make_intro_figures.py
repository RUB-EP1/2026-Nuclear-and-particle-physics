"""Original schematics for the introductory part of Lecture 9 (undergraduate rework).

Hand-written SVG for apparatus drawings; Matplotlib for qualitative curves.
No measured data. Run from the repository root:
    .venv-pdf/bin/python slides/lectures/Lecture_9/scripts/make_intro_figures.py
"""
from pathlib import Path
import os, re
ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault('MPLCONFIGDIR', str(ROOT / 'tmp/matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

OUT = ROOT / 'figures'
B = '#007dc5'; O = '#cf741b'; R = '#bd3249'; G = '#268565'; GR = '#607382'; INK = '#1d2733'
FONT = 'Helvetica Neue, Helvetica, Arial, sans-serif'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 17, 'axes.labelsize': 18,
                     'axes.titlesize': 20, 'axes.spines.top': False, 'axes.spines.right': False,
                     'axes.edgecolor': '#b8c7d2', 'grid.color': '#e0e8ed', 'svg.fonttype': 'none',
                     'lines.linewidth': 3, 'legend.frameon': False, 'figure.facecolor': 'white'})

def _sans(path):
    p=Path(path);p.write_text(p.read_text().replace("font-family: 'DejaVu Sans'","font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif"))


def svg(name, w, h, body):
    head = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" font-family="{FONT}">\n'
            '<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker>'
            '<marker id="arb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" '
            f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{B}"/></marker></defs>\n')
    (OUT / f'{name}.svg').write_text(head + body + '\n</svg>\n')


def text(x, y, s, size=28, fill=INK, anchor='start', weight=400, italic=False):
    st = ' font-style="italic"' if italic else ''
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" '
            f'font-weight="{weight}"{st}>{s}</text>')


def track(x1, y1, x2, y2, col=B, w=5):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}" '
            f'stroke-linecap="round" marker-end="url(#arb)"/>')


def gm_tube():
    """Side view of a Geiger–Müller tube with the external circuit."""
    p = []
    x0, x1, yc, r = 150, 1050, 330, 120
    # gas volume and cathode wall
    p.append(f'<rect x="{x0}" y="{yc-r}" width="{x1-x0}" height="{2*r}" rx="18" fill="#eef5fa" stroke="#7f8f9c" stroke-width="10"/>')
    # thin entrance window (left end)
    p.append(f'<line x1="{x0}" y1="{yc-r+14}" x2="{x0}" y2="{yc+r-14}" stroke="{O}" stroke-width="10"/>')
    # avalanche glow along the whole wire
    p.append(f'<rect x="{x0+30}" y="{yc-26}" width="{x1-x0-60}" height="52" rx="26" fill="{R}" opacity="0.18"/>')
    rng = np.random.default_rng(5)
    for x in range(x0 + 50, x1 - 30, 9):
        p.append(f'<circle cx="{x + rng.uniform(-4, 4):.0f}" cy="{yc + rng.normal(0, 11):.0f}" r="2.6" fill="{R}" opacity="0.7"/>')
    # anode wire
    p.append(f'<line x1="{x0+20}" y1="{yc}" x2="{x1+150}" y2="{yc}" stroke="{INK}" stroke-width="3.5"/>')
    # particle track with primary ionization
    tx1, ty1, tx2, ty2 = 420, 140, 520, 466
    p.append(track(tx1, ty1, tx2, ty2))
    for k in range(1, 9):
        t = 0.24 + 0.065 * k
        x = tx1 + t * (tx2 - tx1); y = ty1 + t * (ty2 - ty1)
        if yc - r + 12 < y < yc + r - 12:
            p.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="6" fill="none" stroke="{INK}" stroke-width="2.5"/>')
    # discharge arrows: spreads in both directions
    p.append(f'<line x1="{560}" y1="{yc+70}" x2="{x0+60}" y2="{yc+70}" stroke="{R}" stroke-width="4" marker-end="url(#ar)"/>')
    p.append(f'<line x1="{600}" y1="{yc+70}" x2="{x1-40}" y2="{yc+70}" stroke="{R}" stroke-width="4" marker-end="url(#ar)"/>')
    # external circuit: resistor to HV, capacitor to output
    xw = x1 + 150
    p.append(f'<path d="M{xw},{yc} v-40 l-14,-8 l28,-16 l-28,-16 l28,-16 l-28,-16 l14,-8 v-40" fill="none" stroke="{INK}" stroke-width="3.5"/>')
    p.append(f'<circle cx="{xw}" cy="{yc-190}" r="7" fill="{INK}"/>')
    p.append(text(xw + 22, yc - 182, '+500 V', 30, INK, weight=600))
    p.append(text(xw + 22, yc - 110, 'R', 28, GR, italic=True))
    p.append(f'<line x1="{xw}" y1="{yc}" x2="{xw}" y2="{yc+70}" stroke="{INK}" stroke-width="3.5"/>')
    p.append(f'<line x1="{xw-26}" y1="{yc+70}" x2="{xw+26}" y2="{yc+70}" stroke="{INK}" stroke-width="5"/>')
    p.append(f'<line x1="{xw-26}" y1="{yc+84}" x2="{xw+26}" y2="{yc+84}" stroke="{INK}" stroke-width="5"/>')
    p.append(f'<line x1="{xw}" y1="{yc+84}" x2="{xw}" y2="{yc+150}" stroke="{INK}" stroke-width="3.5"/>')
    p.append(f'<circle cx="{xw}" cy="{yc+150}" r="7" fill="{INK}"/>')
    # output pulse sketch
    px, py = xw - 60, yc + 250
    p.append(f'<path d="M{px},{py} h30 l6,-70 q10,0 30,40 q20,28 60,30 h20" fill="none" stroke="{R}" stroke-width="4"/>')
    p.append(text(xw, yc + 290, 'output: ≈ 1 V, same', 26, R, 'middle', 600))
    p.append(text(xw, yc + 322, 'for every particle', 26, R, 'middle', 600))
    # labels
    p.append(text(x0, 60, 'cathode: metal tube wall (ground)', 28, GR))
    p.append(f'<line x1="{x0+120}" y1="72" x2="{x0+160}" y2="{yc-r-8}" stroke="{GR}" stroke-width="2"/>')
    p.append(text(860, 60, 'anode: thin wire', 28, GR))
    p.append(f'<line x1="950" y1="72" x2="1000" y2="{yc-6}" stroke="{GR}" stroke-width="2"/>')
    p.append(text(x0 - 10, yc + r + 95, 'thin window (lets weak radiation in)', 26, O, weight=600))
    p.append(text(640, yc - 70, 'gas: noble gas + quencher', 26, GR))
    p.append(text(x0, yc + r + 50, '1 electron → avalanche → discharge along the whole wire', 27, R, weight=600))
    p.append(text(tx1 + 25, ty1 + 10, 'charged particle', 27, B, weight=600))
    svg('gm-tube', 1400, 700, '\n'.join(p))


def gas_regions():
    """Qualitative pulse size versus voltage for gas-filled counters."""
    V = np.linspace(0, 1, 600)

    def curve(n0):
        lg = np.log10(n0)
        rise = lg * (1 - np.exp(-V / 0.035))                      # recombination → full collection
        gain = np.clip((V - 0.33) / 0.27, 0, None) ** 1.6 * 4.6       # proportional growth
        y = rise + gain
        sat = 9.6                                                    # Geiger: independent of n0
        w = 1 / (1 + np.exp(-(V - 0.72) / 0.03))
        y = (1 - w) * np.minimum(y, sat + 0.2) + w * sat
        disc = np.clip((V - 0.9) / 0.1, 0, None) ** 2 * 2
        return y + disc

    f, a = plt.subplots(figsize=(11.5, 6.6), layout='constrained')
    bands = [(0, .07, 'recom-\nbination'), (.07, .33, 'ionization\nchamber'), (.33, .6, 'proportional\ncounter'),
             (.6, .72, 'limited\nprop.'), (.72, .9, 'Geiger–Müller'), (.9, 1, 'dis-\ncharge')]
    shades = ['#f4f6f8', '#eaf2f8', '#fff5e6', '#f6f0e8', '#fbeaec', '#eeeeee']
    for (lo, hi, lab), sh in zip(bands, shades):
        a.axvspan(lo, hi, color=sh, zorder=0)
        a.text((lo + hi) / 2, 11.45, lab, ha='center', va='top', fontsize=14.5, color=GR)
    a.plot(V, curve(1e4), color=O, label='large primary ionization (α)')
    a.plot(V, curve(1e2), color=B, label='small primary ionization (β)')
    a.annotate('Lecture 7:\ndrift tubes, MWPC', (0.47, 5.3), xytext=(0.36, 7.4), fontsize=15, color=INK,
               arrowprops=dict(arrowstyle='->', color=INK))
    a.annotate('every particle gives\nthe same big pulse', (0.8, 9.5), xytext=(0.73, 6.6), fontsize=15, color=R,
               arrowprops=dict(arrowstyle='->', color=R))
    a.set(xlabel='Voltage between wire and wall  →', ylabel='Charge collected per particle (log₁₀ electrons)',
          xlim=(0, 1), ylim=(0, 11.6), xticks=[], yticks=range(0, 12, 2))
    a.legend(loc='lower right', bbox_to_anchor=(1, 0.12), fontsize=15)
    f.savefig(OUT / 'gas-regions.svg'); plt.close(f); _sans(OUT / 'gas-regions.svg')


def counter_side(x, y, w=360, h=70, label=None):
    s = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="35" fill="#eef5fa" stroke="#7f8f9c" stroke-width="6"/>',
         f'<line x1="{x+20}" y1="{y+h/2}" x2="{x+w-20}" y2="{y+h/2}" stroke="{INK}" stroke-width="2.5"/>']
    if label:
        s.append(text(x - 20, y + h / 2 + 10, label, 30, INK, 'end', 600))
    return s


def coincidence():
    """Two counters with an absorber; timing diagram with AND output."""
    p = []
    # apparatus (left)
    p += counter_side(150, 120, label='1')
    p.append(f'<rect x="150" y="250" width="360" height="90" fill="#9aa5b1"/>')
    p.append(text(160, 306, 'absorber', 26, 'white', 'start', 600))
    p += counter_side(150, 400, label='2')
    p.append(track(300, 30, 360, 540))
    p.append(text(372, 545, 'cosmic ray', 26, B, weight=600))
    # an uncorrelated hit in counter 1 only (e.g. radioactivity)
    p.append(f'<path d="M560,90 L430,150" stroke="{O}" stroke-width="4" stroke-dasharray="10 7" marker-end="url(#ar)" fill="none"/>')
    p.append(text(570, 92, 'background γ', 26, O, weight=600))
    p.append(text(570, 124, '(only counter 1)', 24, O))
    # timing diagram (right)
    x0, x1 = 820, 1640
    rows = [(150, 'counter 1', [1.0, 3.4], INK), (290, 'counter 2', [1.05], INK), (470, '1 AND 2', [1.0], R)]
    T = lambda t: x0 + (t / 5) * (x1 - x0)
    for y, lab, times, col in rows:
        p.append(text(x0 - 25, y + 8, lab, 28, col, 'end', 600))
        d = f'M{x0},{y}'
        for t in times:
            d += f' H{T(t):.0f} v-60 h{0.22/5*(x1-x0):.0f} v60'
        d += f' H{x1}'
        p.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="4"/>')
    p.append(f'<rect x="{T(0.92):.0f}" y="40" width="{T(1.35)-T(0.92):.0f}" height="470" fill="{R}" opacity="0.08"/>')
    p.append(text(T(1.13), 30, 'same time', 24, R, 'middle', 600))
    p.append(f'<line x1="{x0}" y1="540" x2="{x1}" y2="540" stroke="{INK}" stroke-width="2.5" marker-end="url(#ar)"/>')
    p.append(text(x1, 580, 'time', 26, GR, 'end'))
    p.append(f'<rect x="{x0+160}" y="350" width="170" height="64" rx="10" fill="white" stroke="{R}" stroke-width="3"/>')
    p.append(text(x0 + 245, 392, 'AND gate', 26, R, 'middle', 600))
    svg('coincidence', 1700, 600, '\n'.join(p))


def cloud_trigger():
    """Counter-controlled cloud chamber, after Blackett & Occhialini (1933)."""
    p = []
    p += counter_side(200, 60, 420, 64, label='counter A')
    # cloud chamber
    p.append(f'<rect x="170" y="190" width="480" height="270" rx="12" fill="#f7f9fb" stroke="#7f8f9c" stroke-width="6"/>')
    p.append(text(410, 230, 'cloud chamber', 26, GR, 'middle', 600))
    p.append(f'<rect x="190" y="460" width="440" height="34" fill="#c3ced6"/>')
    p.append(text(410, 486, 'piston', 22, INK, 'middle'))
    p += counter_side(200, 540, 420, 64, label='counter B')
    # track: straight through counters, droplets in the chamber
    p.append(track(380, 10, 450, 650))
    for k in range(18):
        y = 255 + k * 11
        x = 380 + (y - 10) * 70 / 640
        p.append(f'<circle cx="{x + (k%3-1)*3:.0f}" cy="{y}" r="3.4" fill="{INK}" opacity="0.7"/>')
    p.append(text(470, 660, 'cosmic ray', 26, B, weight=600))
    # logic
    p.append(f'<path d="M620,92 H860 V300" fill="none" stroke="{INK}" stroke-width="3.5"/>')
    p.append(f'<path d="M620,572 H860 V380" fill="none" stroke="{INK}" stroke-width="3.5"/>')
    p.append(f'<rect x="780" y="300" width="160" height="80" rx="12" fill="white" stroke="{R}" stroke-width="4"/>')
    p.append(text(860, 350, 'A AND B', 28, R, 'middle', 700))
    p.append(f'<line x1="940" y1="340" x2="1050" y2="340" stroke="{R}" stroke-width="4" marker-end="url(#ar)"/>')
    p.append(f'<rect x="1060" y="270" width="380" height="140" rx="12" fill="#fbeaec" stroke="{R}" stroke-width="3"/>')
    p.append(text(1250, 322, 'expand the chamber', 27, INK, 'middle', 600))
    p.append(text(1250, 358, 'flash the lamp', 27, INK, 'middle', 600))
    p.append(text(1250, 394, 'take the photograph', 27, INK, 'middle', 600))
    p.append(f'<path d="M1060,380 C900,470 760,470 640,478" fill="none" stroke="{R}" stroke-width="3" stroke-dasharray="9 7" marker-end="url(#ar)"/>')
    p.append(text(1060, 140, 'fast, simple detectors:', 27, B, weight=700))
    p.append(text(1060, 176, 'decide whether to record', 27, B))
    p.append(text(1060, 500, 'slow, detailed detector:', 27, O, weight=700))
    p.append(text(1060, 536, 'records the picture', 27, O))
    svg('cloud-trigger', 1480, 690, '\n'.join(p))


def discriminator():
    """Analogue pulses, a threshold and the logic output."""
    t = np.linspace(0, 600, 3000)
    def pulse(t0, A):
        u = np.clip((t - t0) / 18, 0, None)
        return A * u ** 2 * np.exp(2 - 2 * u)
    rng = np.random.default_rng(3)
    v = pulse(60, 420) + pulse(250, 120) + pulse(420, 700) + rng.normal(0, 8, t.size)
    thr = 200
    logic = (v > thr).astype(float)
    f, (a, b) = plt.subplots(2, 1, figsize=(11, 6.6), layout='constrained', sharex=True,
                             gridspec_kw=dict(height_ratios=[2.2, 1]))
    a.plot(t, v, color=B, lw=2.2)
    a.axhline(thr, color=R, ls='--', lw=2.5)
    a.text(598, thr + 18, 'threshold', color=R, ha='right', fontsize=17)
    a.text(305, 95, '← too small: ignored', color=GR, ha='left', fontsize=15)
    a.set(ylabel='Analogue signal [mV]', ylim=(-40, 760)); a.grid(alpha=.7)
    a.set_title('Discriminator: analogue pulse in, yes/no out', loc='left', pad=12)
    b.step(t, logic, where='post', color=R, lw=3)
    b.set(ylim=(-.25, 1.35), yticks=[0, 1], yticklabels=['0', '1'], ylabel='Logic', xlabel='Time [ns]')
    b.grid(alpha=.7)
    f.savefig(OUT / 'discriminator.svg'); plt.close(f); _sans(OUT / 'discriminator.svg')


def rate_funnel():
    """From collisions to storage at the LHC (round numbers)."""
    stages = [('pp collisions', 1e9, '#9aa5b1', ''),
              ('bunch crossings', 4e7, '#9aa5b1', 'every 25 ns'),
              ('after Level-1', 1e5, B, 'hardware, decides in ≈ 2.5 µs'),
              ('after High-Level Trigger', 1e3, B, 'computer farm, ≈ 0.1–1 s per event'),
              ]
    f, a = plt.subplots(figsize=(12, 6.2), layout='constrained')
    y = np.arange(len(stages))[::-1]
    for yi, (lab, r, col, note) in zip(y, stages):
        a.barh(yi, np.log10(r) + 1, left=-1, color=col, height=.62)
        a.text(-0.85, yi, lab, va='center', color='white', fontsize=17, weight='bold')
        val = {1e9: '10⁹ /s', 4e7: '4×10⁷ /s', 1e5: '10⁵ /s', 1e3: '10³ /s'}[r]
        a.text(np.log10(r) + .15, yi + .08, val, va='center', fontsize=19, color=INK, weight='bold')
        if note:
            a.text(np.log10(r) + .15, yi - .24, note, va='center', fontsize=14.5, color=GR)
    a.axvline(np.log10(0.5), color=R, ls='--', lw=2.5)
    a.text(np.log10(0.5) + .1, -0.62, 'Higgs bosons produced: ≈ 1 every 2 s', color=R, fontsize=15)
    a.set(xlim=(-1, 11.3), ylim=(-0.85, len(stages) - .5), yticks=[],
          xticks=range(-1, 11), xticklabels=[f'10$^{{{k}}}$' for k in range(-1, 11)],
          xlabel='Rate [per second], logarithmic')
    a.spines['left'].set_visible(False); a.grid(axis='x', alpha=.6); a.set_axisbelow(True)
    f.savefig(OUT / 'rate-funnel.svg'); plt.close(f); _sans(OUT / 'rate-funnel.svg')


def detector_layers():
    """Lecture 7 signpost without the lecture brackets."""
    src = (ROOT.parent / 'Lecture_7/figures/detector-layers-signpost.svg').read_text()
    src = re.sub(r'<g fill="none" stroke-width="3" stroke-linecap="round">\s*<path d="M336,722.*?</g>\n', '', src, flags=re.S)
    src = re.sub(r'<text[^>]*>Lecture [78]</text>\n', '', src)
    (OUT / 'detector-layers.svg').write_text(src)


if __name__ == '__main__':
    gm_tube(); gas_regions(); coincidence(); cloud_trigger(); discriminator(); rate_funnel(); detector_layers()

"""Original schematics for the DAQ and LHC-trigger sections of Lecture 9.

The DAQ build-up (daq-step-a/b/c) is redrawn after N. Neufeld, ESI 2009, pp. 16-20.
Run from the repository root:
    .venv-pdf/bin/python slides/lectures/Lecture_9/scripts/make_daq_figures.py
"""
import math, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_intro_figures import OUT, B, O, R, G, GR, INK, svg, text, _sans, plt, np  # noqa: E402

NEW = O          # colour for the element added in each step
LINE = INK


def box(x, y, w, h, label, fill='#eef5fa', stroke='#7f8f9c', col=INK, size=28, weight=600, rx=10, sw=4):
    s = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>']
    lines = label.split('\n')
    y0 = y + h / 2 - (len(lines) - 1) * size * 0.6 + size * 0.35
    for i, ln in enumerate(lines):
        s.append(text(x + w / 2, y0 + i * size * 1.2, ln, size, col, 'middle', weight))
    return s


def wire(d, col=LINE, w=3.5, arrow=True, dash=None):
    a = ' marker-end="url(#ar)"' if arrow else ''
    ds = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{w}"{a}{ds}/>'


def daq_step(step):
    """Neufeld's 'trivial DAQ with a real trigger', built up in three steps."""
    p = []
    cx = 230                                   # left column: the data path
    p += box(130, 30, 200, 70, 'Sensor', '#ffffff', INK)
    p.append(wire(f'M{cx},100 V175'))
    p.append(f'<circle cx="{cx}" cy="140" r="7" fill="{INK}"/>')
    p.append(wire(f'M{cx},140 H600'))                                 # copy to the trigger
    p += box(130, 180, 200, 70, 'Delay', '#f4f6f8')
    p.append(wire(f'M{cx},250 V295'))
    p += box(130, 300, 200, 70, 'ADC')
    if step == 'c':
        p.append(wire(f'M{cx},370 V415', NEW))
        p += box(130, 420, 200, 70, 'FIFO', '#fff1e3', NEW, NEW)
        p.append(wire(f'M{cx},490 V535', NEW))
    else:
        p.append(wire(f'M{cx},370 V535'))
    p.append(f'<ellipse cx="{cx}" cy="580" rx="115" ry="44" fill="#fffbe6" stroke="#7f8f9c" stroke-width="4"/>')
    p.append(text(cx, 590, 'Processing', 28, INK, 'middle', 600))
    p.append(wire(f'M{cx},624 V665'))
    p.append(f'<path d="M150,680 v50 a80,16 0 0 0 160,0 v-50" fill="#e6e9f7" stroke="#7f8f9c" stroke-width="4"/>')
    p.append(f'<ellipse cx="{cx}" cy="680" rx="80" ry="16" fill="#e6e9f7" stroke="#7f8f9c" stroke-width="4"/>')
    p.append(text(cx, 728, 'Storage', 26, INK, 'middle', 600))
    # trigger column
    p += box(600, 105, 280, 70, 'Discriminator', '#fbeaec', R, R)
    p.append(text(740, 85, 'TRIGGER', 24, R, 'middle', 700))
    if step == 'a':
        p.append(wire('M740,175 V335 H335'))
    else:
        gate = 'AND NOT busy' if step == 'b' else 'AND NOT full'
        p.append(wire('M740,175 V240'))
        p += box(600, 245, 280, 70, gate, '#fff1e3', NEW, NEW, 27)
        p.append(wire('M600,280 H500 V335 H335'))
    p.append(text(420, 325, 'Start', 25, GR, 'middle', 600))
    if step == 'b':
        p += box(600, 420, 280, 70, 'Busy flag', '#fff1e3', NEW, NEW)
        p.append(wire('M740,420 V320', NEW))
        p.append(text(752, 385, 'busy', 24, NEW, 'start', 600))
        p.append(wire('M500,335 V455 H595', NEW))
        p.append(text(510, 445, 'set', 24, NEW, 'start', 600))
        p.append(wire('M345,580 H800 V495', NEW))
        p.append(text(560, 570, 'clear when done ("ready")', 24, NEW, 'middle', 600))
    if step == 'c':
        p.append(wire('M335,455 H740 V320', NEW))
        p.append(text(560, 445, 'full?', 24, NEW, 'middle', 600))
    svg(f'daq-step-{step}', 940, 760, '\n'.join(p))


def crossings_in_flight():
    """At 25 ns spacing, particles from several crossings are inside the detector at once."""
    s = 38                     # px per metre
    x0, y0 = 90, 590           # interaction point (bottom left)
    L, H = 23, 12.5            # ATLAS-sized half detector, schematic
    p = [f'<clipPath id="det"><rect x="{x0}" y="{y0 - H*s}" width="{L*s}" height="{H*s}"/></clipPath>']
    for (z, r, col, lab) in [(23, 12.5, '#e9f4ef', ''), (6.5, 4.25, '#f6eef3', 'calorimeters'),
                             (3.5, 1.1, '#e6f1f8', '')]:
        p.append(f'<rect x="{x0}" y="{y0 - r*s}" width="{z*s}" height="{r*s}" fill="{col}" stroke="#b8c7d2" stroke-width="2"/>')
        if lab:
            p.append(text(x0 + z * s - 12, y0 - r * s + 32, lab, 24, GR, 'end', 600))
    p.append(text(x0 + 3.5 * s / 2, y0 - 12, 'tracker', 20, GR, 'middle', 600))
    p.append(text(x0 + L * s, y0 - H * s - 12, 'muon system', 24, GR, 'end', 600))
    cols = [R, O, G, B]
    for k, col in enumerate(cols):
        r = (k + 0.0) * 7.5 * s
        ago = 25 * k
        if k == 0:
            p.append(f'<circle cx="{x0}" cy="{y0}" r="12" fill="{B}"/>')
            continue
        p.append(f'<path d="M{x0 + r},{y0} A{r},{r} 0 0 0 {x0},{y0 - r}" fill="none" stroke="{cols[k-1]}" '
                 f'stroke-width="7" clip-path="url(#det)"/>')
        lx = x0 + 260 + 200 * (k - 1)
        p.append(f'<line x1="{lx}" y1="{y0+150}" x2="{lx+50}" y2="{y0+150}" stroke="{cols[k-1]}" stroke-width="7"/>')
        p.append(text(lx + 62, y0 + 159, f'{ago} ns ago', 24, cols[k-1], 'start', 700))
    p.append(text(x0 + 22, y0 + 40, 'collision point: a new crossing now', 24, B, 'start', 700))
    p.append(text(x0, y0 + 159, 'particles produced', 24, INK, 'start', 700))
    p.append(f'<line x1="{x0}" y1="{y0+70}" x2="{x0 + 7.5*s}" y2="{y0+70}" stroke="{INK}" stroke-width="2.5" marker-end="url(#ar)" marker-start="url(#ar)"/>')
    p.append(text(x0 + 7.5 * s / 2, y0 + 105, 'c × 25 ns = 7.5 m', 26, INK, 'middle', 700))
    p.append(text(x0 + L * s, y0 + 105, 'half of an ATLAS-sized detector, to scale (schematic)', 22, GR, 'end'))
    svg('crossings-in-flight', x0 + L * s + 40, y0 + 180, '\n'.join(p))


def pipeline_belt():
    """The pipeline as a conveyor belt of memory cells."""
    p = []
    n, w, h, x0, y0 = 14, 82, 90, 120, 180
    for i in range(n):
        x = x0 + i * w
        if i == 7:
            p.append(text(x + w / 2, y0 + h / 2 + 12, '…', 40, GR, 'middle', 700))
            continue
        num = 1100 - i if i < 7 else 1100 - (i + 86)
        col = '#eef5fa' if i < n - 1 else '#fff1e3'
        st = '#7f8f9c' if i < n - 1 else O
        p.append(f'<rect x="{x}" y="{y0}" width="{w-8}" height="{h}" rx="8" fill="{col}" stroke="{st}" stroke-width="3"/>')
        p.append(text(x + (w - 8) / 2, y0 + h / 2 + 10, f'#{num}', 22, INK, 'middle', 600))
    p.append(wire(f'M30,{y0 + h/2} H{x0 - 8}', B, 4))
    p.append(text(20, y0 - 58, 'new crossing in', 26, B, 'start', 700))
    p.append(text(20, y0 - 28, 'every 25 ns', 24, B))
    p.append(wire(f'M{x0 + 40},{y0 + h + 40} H{x0 + (n - 1) * w}', GR, 3))
    p.append(text(x0 + (n - 1) * w / 2, y0 + h + 80, 'every cell moves one step to the right every 25 ns', 26, GR, 'middle'))
    xe = x0 + (n - 1) * w + w
    p.append(text(x0 + n * w / 2, y0 - 50, '100 cells = 2.5 µs / 25 ns', 30, INK, 'middle', 700))
    # decision
    p.append(wire(f'M{xe - 40},{y0 - 70} V{y0 - 8}', R, 4))
    p.append(text(xe - 40, y0 - 85, 'Level-1 decision for #1001', 26, R, 'middle', 700))
    p.append(wire(f'M{xe},{y0 + 25} H{xe + 120}', G, 4))
    p.append(text(xe + 130, y0 + 33, 'yes → read out', 28, G, 'start', 700))
    p.append(wire(f'M{xe},{y0 + 65} H{xe + 120}', GR, 4, dash='8 7'))
    p.append(text(xe + 130, y0 + 73, 'no → overwrite', 28, GR, 'start', 700))
    svg('pipeline-belt', xe + 360, 400, '\n'.join(p))


def lhc_chain():
    """Two-level trigger and DAQ chain after Neufeld p52, with round Run-2 numbers."""
    p = []
    X, W = 300, 520
    rows = [(30, 'Detector: ~10⁸ channels', '#ffffff', INK),
            (150, 'Front-end pipelines', '#eef5fa', '#7f8f9c'),
            (300, 'Readout buffers', '#eef5fa', '#7f8f9c'),
            (420, 'Event building network', '#eef5fa', '#7f8f9c'),
            (540, 'Computer farm', '#eef5fa', '#7f8f9c'),
            (680, 'Storage', '#e6e9f7', '#7f8f9c')]
    for y, lab, f, st in rows:
        p += box(X, y, W, 80, lab, f, st, INK, 30)
    for (y1, y2, rate) in [(110, 150, '40 MHz'), (230, 300, '100 kHz'), (380, 420, ''), (500, 540, ''), (620, 680, '~1 kHz')]:
        p.append(wire(f'M{X + W/2},{y1} V{y2 - 4}'))
        if rate:
            p.append(text(X + W / 2 + 20, (y1 + y2) / 2 + 10, rate, 30, B, 'start', 700))
    # Level-1 and HLT
    p += box(20, 150, 230, 140, 'Level-1\nhardware\n≈ 2.5 µs', '#fbeaec', R, R, 28)
    p.append(wire(f'M250,200 H{X - 6}', R))
    p += box(20, 520, 230, 120, 'High-Level\nTrigger\n(software)', '#fbeaec', R, R, 28)
    p.append(text(135, 670, '≈ 0.1–1 s per event', 22, R, 'middle', 600))
    p.append(wire(f'M250,580 H{X - 6}', R, arrow=False))
    svg('lhc-chain', X + W + 30, 780, '\n'.join(p))


def daq_history():
    """Recording bandwidth from Tycho Brahe to the LHC (orders of magnitude)."""
    rows = [('Tycho Brahe, logbook (1580s)', 100 / 3600, '#9aa5b1', '≈ 100 bytes per hour'),
            ('Thermometer read once per second', 4, '#9aa5b1', 'one number per second'),
            ('LHC experiment → disk', 1e9, B, '≈ 1 GB/s'),
            ('LHCb Run 3: full readout, no hardware trigger', 5e12, B, '≈ 5 TB/s'),
            ('Every LHC crossing × 1 MB', 4e13, R, '40 TB/s: impossible to keep')]
    f, a = plt.subplots(figsize=(12, 6.6), layout='constrained')
    y = np.arange(len(rows))[::-1]
    for yi, (lab, v, col, note) in zip(y, rows):
        a.barh(yi, np.log10(v) + 2, left=-2, color=col, height=.6)
        a.text(np.log10(v) + .25, yi, note, va='center', fontsize=20, color=INK, weight='bold')
        a.text(-1.85, yi + .45, lab, va='center', fontsize=19, color=GR)
    a.set(xlim=(-2, 18.5), ylim=(-.6, len(rows) - .25), yticks=[],
          xticks=range(-2, 15, 2), xticklabels=[f'10$^{{{k}}}$' for k in range(-2, 15, 2)],
          xlabel='Bytes per second, logarithmic')
    a.spines['left'].set_visible(False); a.grid(axis='x', alpha=.6); a.set_axisbelow(True)
    f.savefig(OUT / 'daq-history.svg'); plt.close(f); _sans(OUT / 'daq-history.svg')


def turn_on():
    """Toy trigger turn-on: a sharp cut on a smeared measurement."""
    pt = np.linspace(0, 60, 600)
    thr = 25
    f, a = plt.subplots(figsize=(10.6, 6.2), layout='constrained')
    a.plot(pt, (pt >= thr).astype(float), color='#9aa5b1', ls='--', lw=2.5, label='perfect measurement')
    for res, col in [(.08, B), (.2, O)]:
        eff = .5 * (1 + np.vectorize(math.erf)((pt - thr) / (np.sqrt(2) * res * np.maximum(pt, 1e-3))))
        a.plot(pt, .95 * eff, color=col, label=f'trigger resolution {int(res*100)}%')
    a.axvline(thr, color=R, ls=':', lw=2)
    a.text(thr + .6, .08, 'threshold\n25 GeV', color=R, fontsize=15)
    a.annotate('plateau < 100%:\ngaps, dead channels', (50, .95), xytext=(36, .62), fontsize=15, color=GR,
               arrowprops=dict(arrowstyle='->', color=GR))
    a.annotate('turn-on', (thr, .47), xytext=(6, .62), fontsize=16, color=INK,
               arrowprops=dict(arrowstyle='->', color=INK))
    a.set(xlabel='True transverse momentum $p_T$ [GeV]', ylabel='Fraction of events that fire the trigger',
          ylim=(-.03, 1.1), xlim=(0, 60))
    a.grid(alpha=.7); a.legend(loc='lower right')
    a.set_title('Toy model: the trigger cuts on a fast, less precise $p_T$', loc='left', pad=12)
    f.savefig(OUT / 'turn-on-toy.svg'); plt.close(f); _sans(OUT / 'turn-on-toy.svg')


def _pol(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy - r * math.sin(a)


def _shower(x, y, deg, length, col, seed):
    """A small branching shower starting at (x, y) along direction deg."""
    rng = np.random.default_rng(seed)
    s = []
    def branch(x, y, d, L, depth):
        if depth == 0 or L < 6:
            return
        x2, y2 = x + L * math.cos(math.radians(d)), y - L * math.sin(math.radians(d))
        s.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{1 + depth*0.5:.1f}" stroke-linecap="round"/>')
        for dd in (-1, 1):
            branch(x2, y2, d + dd * rng.uniform(10, 26), L * rng.uniform(.55, .75), depth - 1)
    branch(x, y, deg, length * 0.38, 5)
    return s


def detector_slice():
    """Quarter r-phi slice: which systems feed the fast trigger (after Neufeld p54)."""
    p = []
    cx, cy = 70, 690
    layers = [(0, 150, '#e6f1f8', 'tracker'), (165, 235, '#fbeaec', 'EM calorimeter'),
              (240, 345, '#f1ebf6', 'hadron calorimeter'), (360, 600, '#e9f4ef', 'muon system')]
    for r1, r2, col, lab in layers:          # annular sectors
        x2, y2 = _pol(cx, cy, r2, 90)
        p.append(f'<path d="M{cx},{cy} L{cx + r2},{cy} A{r2},{r2} 0 0 0 {x2:.0f},{y2:.0f} L{cx},{cy - r1} A{r1},{r1} 0 0 1 {cx + r1},{cy} Z" fill="{col}" stroke="#b8c7d2" stroke-width="2"/>')
    # muon stations
    for r in (395, 480, 565):
        x2, y2 = _pol(cx, cy, r, 90)
        p.append(f'<path d="M{cx + r},{cy} A{r},{r} 0 0 0 {x2:.0f},{y2:.0f}" fill="none" stroke="#7fb79c" stroke-width="16"/>')
    for r, lab, dy in [(75, 'tracker', 30), (200, 'EM calo', 58), (292, 'hadron calo', 30), (480, 'muon chambers', 30)]:
        p.append(text(cx + r, cy + dy, lab, 22, GR, 'middle', 600))
    # particles
    def ray(r1, r2, deg, col, dash=None, w=3.5):
        x1, y1 = _pol(cx, cy, r1, deg); x2, y2 = _pol(cx, cy, r2, deg)
        ds = f' stroke-dasharray="{dash}"' if dash else ''
        return f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{col}" stroke-width="{w}"{ds}/>'
    def curved(deg, bend, r_end, col):
        xm, ym = _pol(cx, cy, 80, deg + bend)
        x1, y1 = _pol(cx, cy, 150, deg)
        x2, y2 = _pol(cx, cy, r_end, deg - bend * 0.6)
        return f'<path d="M{cx},{cy} Q{xm:.0f},{ym:.0f} {x1:.0f},{y1:.0f} L{x2:.0f},{y2:.0f}" fill="none" stroke="{col}" stroke-width="3.5"/>'
    p.append(ray(0, 165, 76, B, '6 6', 2.5)); p += _shower(*_pol(cx, cy, 168, 76), 76, 60, R, 1)
    p.append(curved(64, 5, 165, B)); p += _shower(*_pol(cx, cy, 168, 64), 64, 60, R, 2)
    p.append(curved(45, -6, 600, B))
    ax_, ay_ = _pol(cx, cy, 150, 45); bx_, by_ = _pol(cx, cy, 600, 48.6)
    hits = []
    for r in (395, 480, 565):
        t = (r - 150) / 450
        x, y = ax_ + t * (bx_ - ax_), ay_ + t * (by_ - ay_)
        hits.append((x, y))
        p.append(f'<rect x="{x-7:.0f}" y="{y-7:.0f}" width="14" height="14" fill="{O}" stroke="{INK}" stroke-width="1.5"/>')
    p.append(curved(26, 4, 245, B)); p += _shower(*_pol(cx, cy, 247, 25), 25, 85, '#8660a5', 3)
    p.append(ray(0, 245, 12, B, '6 6', 2.5)); p += _shower(*_pol(cx, cy, 247, 12), 12, 85, '#8660a5', 4)
    p.append(ray(0, 610, 86, GR, '2 7', 2.5))
    for deg, lab, r in [(78, 'γ', 120), (66, 'e', 130), (47, 'μ', 640), (28, 'π±', 210), (14, 'n', 210), (87, 'ν', 640)]:
        x, y = _pol(cx, cy, r, deg)
        p.append(text(x, y, lab, 28, INK, 'middle', 700))
    # trigger paths
    xp = 820
    p += box(xp, 40, 560, 150, '', '#fbeaec', R, R)
    p.append(text(xp + 20, 80, 'Calorimeter trigger', 30, R, 'start', 700))
    p.append(text(xp + 20, 118, 'sum energy in groups of cells,', 26, INK))
    p.append(text(xp + 20, 152, 'find large E_T: e, γ, jets, missing E_T', 26, INK))
    ex_, ey_ = _pol(cx, cy, 215, 70)
    p.append(wire(f'M{ex_:.0f},{ey_:.0f} C200,120 500,40 {xp - 6},115', R))
    p += box(xp, 250, 560, 150, '', '#fbeaec', R, R)
    p.append(text(xp + 20, 290, 'Muon trigger', 30, R, 'start', 700))
    p.append(text(xp + 20, 328, 'hits in several stations →', 26, INK))
    p.append(text(xp + 20, 362, 'bending → p_T of the muon', 26, INK))
    mx, my = hits[2]
    p.append(wire(f'M{mx + 12:.0f},{my:.0f} C620,260 700,325 {xp - 6},325', R))
    p += box(xp, 460, 560, 110, '', '#eef5fa', '#7f8f9c')
    p.append(text(xp + 20, 500, 'Tracker: too many channels', 28, INK, 'start', 700))
    p.append(text(xp + 20, 540, 'data wait in the pipeline', 26, INK))
    p.append(wire(f'M{_pol(cx, cy, 120, 35)[0]:.0f},{_pol(cx, cy, 120, 35)[1]:.0f} C500,640 650,560 {xp - 6},520', '#7f8f9c', dash='8 7'))
    p += box(xp, 610, 560, 80, 'new data every 25 ns · decision in ~µs', '#fff6d6', O, INK, 26)
    svg('detector-slice', 1400, 760, '\n'.join(p))


CALO = np.array([[0.1, 0.2, 0.0, 0.3, 0.1, 0.2, 0.1, 0.0],
                 [0.2, 0.6, 0.4, 0.1, 0.0, 0.1, 0.3, 0.1],
                 [0.0, 0.5, 0.3, 0.2, 0.1, 0.0, 0.2, 0.2],
                 [0.1, 0.0, 0.2, 0.1, 0.2, 0.1, 0.0, 0.1],
                 [0.3, 0.1, 0.0, 0.2, 2.9, 1.6, 0.2, 0.0],
                 [0.0, 0.2, 0.1, 0.1, 1.2, 0.7, 0.1, 0.3],
                 [0.2, 0.0, 0.3, 0.0, 0.1, 0.2, 0.0, 0.1],
                 [0.1, 0.1, 0.0, 0.2, 0.0, 0.1, 0.2, 0.0]])


def calo_trigger():
    """Toy L0 calorimeter trigger: cells → overlapping 2x2 sums → compare with threshold."""
    sums = CALO[:-1, :-1] + CALO[1:, :-1] + CALO[:-1, 1:] + CALO[1:, 1:]
    i, j = np.unravel_index(np.argmax(sums), sums.shape)
    thr = 4.0
    f, axes = plt.subplots(1, 2, figsize=(14, 6.6), layout='constrained')
    for a, M, title, vmax in [(axes[0], CALO, '① Energy in each cell [GeV]', 3.2), (axes[1], sums, '② Sum of every 2×2 group [GeV]', 6.5)]:
        a.imshow(M, cmap='Oranges', vmin=0, vmax=vmax)
        for (r, c), v in np.ndenumerate(M):
            a.text(c, r, f'{v:.1f}', ha='center', va='center', fontsize=14 if M is CALO else 13,
                   color='white' if v > vmax * .55 else INK)
        a.set_xticks([]); a.set_yticks([]); a.set_title(title, loc='left', fontsize=19, pad=10)
        for sp in a.spines.values(): sp.set_visible(False)
    axes[0].add_patch(plt.Rectangle((j - .5, i - .5), 2, 2, fill=False, ec=B, lw=4))
    axes[0].text(7.4, 8.15, f'hottest cell {CALO.max():.1f} GeV < {thr:.0f} GeV', ha='right', fontsize=15, color=GR)
    axes[1].add_patch(plt.Rectangle((j - .5, i - .5), 1, 1, fill=False, ec=B, lw=4))
    axes[1].text(6.4, 7.15, f'③ largest sum {sums.max():.1f} GeV > {thr:.0f} GeV → ACCEPT', ha='right', fontsize=16, color=B, weight='bold')
    f.savefig(OUT / 'calo-trigger-toy.svg'); plt.close(f); _sans(OUT / 'calo-trigger-toy.svg')


if __name__ == '__main__':
    for st in 'abc':
        daq_step(st)
    crossings_in_flight(); pipeline_belt(); lhc_chain(); daq_history(); turn_on()
    detector_slice(); calo_trigger()

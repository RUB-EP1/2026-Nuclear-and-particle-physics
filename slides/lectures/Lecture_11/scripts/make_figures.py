"""Original teaching figures for Lecture 11 (Feynman rules, traces, QED cross sections), plain SVG.

Run from the repository root:
    python3 slides/lectures/Lecture_11/scripts/make_figures.py
No dependencies. Time runs from left to right in all Feynman diagrams.
"""
from math import atan2, cos, hypot, log10, pi, sin
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "figures"
BLUE, ORANGE, RED, GREEN, MUTED, INK, LINE = (
    "#007dc5", "#c86418", "#bd3249", "#23734e", "#627383", "#12202d", "#dfe3e7")
FONT = "font-family=\"Helvetica Neue,Helvetica,Arial,sans-serif\""


def svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
            f'<rect width="{w}" height="{h}" fill="#fff"/>{body}</svg>\n')


def text(x, y, s, size=26, fill=INK, anchor="start", weight=400, style=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" {FONT} font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}" {style}>{s}</text>')


def line(x1, y1, x2, y2, stroke=INK, w=3, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{stroke}" stroke-width="{w}" stroke-linecap="round"{d}/>')


def arrowhead(x, y, ang, color, size=18):
    """Filled triangle with its tip at (x, y), pointing along angle ang (radians)."""
    p = [(x, y)]
    for s in (+1, -1):
        p.append((x - size * cos(ang) + s * 0.5 * size * sin(ang),
                  y - size * sin(ang) - s * 0.5 * size * cos(ang)))
    pts = " ".join(f"{a:.1f},{b:.1f}" for a, b in p)
    return f'<polygon points="{pts}" fill="{color}"/>'


def arrow(x1, y1, x2, y2, color=INK, w=3, size=18):
    ang = atan2(y2 - y1, x2 - x1)
    return line(x1, y1, x2 - 0.8 * size * cos(ang), y2 - 0.8 * size * sin(ang), color, w) + arrowhead(x2, y2, ang, color, size)


def fermion(x1, y1, x2, y2, color=INK, w=4, backward=False):
    """Fermion line from (x1,y1) to (x2,y2) with the charge-flow arrow in the middle.
    backward=True draws the arrow against the direction of motion (antiparticle)."""
    ang = atan2(y2 - y1, x2 - x1)
    if backward:
        ang += pi
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    return line(x1, y1, x2, y2, color, w) + arrowhead(mx + 12 * cos(ang), my + 12 * sin(ang), ang, color, 24)


def wavy(x1, y1, x2, y2, color=ORANGE, amp=10, waves=None, w=4):
    L = hypot(x2 - x1, y2 - y1)
    waves = waves or max(3, round(L / 34))
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    pts = []
    for i in range(301):
        s = i / 300
        o = amp * sin(2 * pi * waves * s)
        pts.append((x1 + ux * L * s - uy * o, y1 + uy * L * s + ux * o))
    d = "M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in pts)
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}"/>'


def dot(x, y, r=9, color=INK):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}"/>'


def spin(x, y, ang, color, length=70):
    """Hollow double-shafted spin arrow centred on (x, y)."""
    dx, dy = 0.5 * length * cos(ang), 0.5 * length * sin(ang)
    nx, ny = -sin(ang) * 5, cos(ang) * 5
    x1, y1, x2, y2 = x - dx, y - dy, x + dx, y + dy
    b = line(x1 + nx, y1 + ny, x2 + nx - 14 * cos(ang), y2 + ny - 14 * sin(ang), color, 3)
    b += line(x1 - nx, y1 - ny, x2 - nx - 14 * cos(ang), y2 - ny - 14 * sin(ang), color, 3)
    return b + arrowhead(x2, y2, ang, color, 26)


# ---------------------------------------------------------------- diagrams

def vertex_crossings():
    W, H = 1720, 560
    b = []
    titles = (("e⁻ scatters", "e⁻ → e⁻ γ"), ("e⁺ scatters", "e⁺ → e⁺ γ"),
              ("pair creation", "γ → e⁻ e⁺"), ("annihilation", "e⁻ e⁺ → γ"))
    for k, (title, reac) in enumerate(titles):
        ox = 30 + k * 425
        cx, cy = ox + 190, 290
        b.append(f'<rect x="{ox}" y="40" width="395" height="480" rx="8" fill="#f7f9fb" stroke="{LINE}" stroke-width="2"/>')
        b.append(text(ox + 197, 92, title, 32, INK, "middle", 600))
        b.append(text(ox + 197, 490, reac, 28, MUTED, "middle"))
        if k == 0:
            b.append(fermion(cx - 150, cy + 110, cx, cy, BLUE))
            b.append(fermion(cx, cy, cx + 150, cy + 110, BLUE))
            b.append(wavy(cx, cy, cx + 150, cy - 130))
        elif k == 1:
            b.append(fermion(cx - 150, cy + 110, cx, cy, RED, backward=True))
            b.append(fermion(cx, cy, cx + 150, cy + 110, RED, backward=True))
            b.append(wavy(cx, cy, cx + 150, cy - 130))
        elif k == 2:
            b.append(wavy(cx - 160, cy, cx, cy))
            b.append(fermion(cx, cy, cx + 150, cy - 110, BLUE))
            b.append(fermion(cx, cy, cx + 150, cy + 110, RED, backward=True))
        else:
            b.append(fermion(cx - 150, cy - 110, cx, cy, BLUE))
            b.append(fermion(cx - 150, cy + 110, cx, cy, RED, backward=True))
            b.append(wavy(cx, cy, cx + 160, cy))
        b.append(dot(cx, cy, 11))
    b.append(arrow(60, 545, 420, 545, MUTED, 2, 14))
    b.append(text(440, 553, "time", 22, MUTED))
    return svg(W, H, "".join(b))


def emu_t(annotated=True):
    W, H = 1000, 760
    b = []
    A, B = (500, 230), (500, 530)
    b.append(fermion(150, 90, *A, BLUE))
    b.append(fermion(*A, 850, 90, BLUE))
    b.append(fermion(150, 670, *B, GREEN))
    b.append(fermion(*B, 850, 670, GREEN))
    b.append(wavy(*A, *B))
    b.append(dot(*A, 12) + dot(*B, 12))
    b.append(text(130, 80, "e⁻", 36, BLUE, "end", 600))
    b.append(text(870, 80, "e⁻", 36, BLUE, "start", 600))
    b.append(text(130, 700, "μ⁻", 36, GREEN, "end", 600))
    b.append(text(870, 700, "μ⁻", 36, GREEN, "start", 600))
    if annotated:
        b.append(text(270, 205, "p₁ : u(p₁)", 30, BLUE, "middle"))
        b.append(text(730, 205, "p₃ : ū(p₃)", 30, BLUE, "middle"))
        b.append(text(270, 580, "p₂ : u(p₂)", 30, GREEN, "middle"))
        b.append(text(730, 580, "p₄ : ū(p₄)", 30, GREEN, "middle"))
        b.append(text(535, 265, "vertex: −ieQ γ<tspan baseline-shift='super' font-size='70%'>μ</tspan>", 28, INK))
        b.append(text(535, 520, "vertex: −ieQ γ<tspan baseline-shift='super' font-size='70%'>ν</tspan>", 28, INK))
        b.append(text(535, 390, "photon: −i g<tspan baseline-shift='sub' font-size='70%'>μν</tspan> / q²", 28, ORANGE, "start", 600))
        b.append(text(535, 428, "q = p₁ − p₃", 26, MUTED))
    else:
        b.append(text(470, 385, "γ", 34, ORANGE, "end", 600))
    return svg(W, H, "".join(b))


def ee_s(annotated=True):
    W, H = 1000, 760
    b = []
    A, B = (330, 380), (670, 380)
    b.append(fermion(80, 120, *A, BLUE))
    b.append(fermion(80, 640, *A, RED, backward=True))
    b.append(fermion(*B, 920, 120, GREEN))
    b.append(fermion(*B, 920, 640, ORANGE, backward=True))
    b.append(wavy(*A, *B))
    b.append(dot(*A, 12) + dot(*B, 12))
    b.append(text(70, 105, "e⁻", 36, BLUE, "end", 600))
    b.append(text(70, 680, "e⁺", 36, RED, "end", 600))
    b.append(text(930, 105, "μ⁻", 36, GREEN, "start", 600))
    b.append(text(930, 680, "μ⁺", 36, ORANGE, "start", 600))
    if annotated:
        b.append(text(230, 225, "p₁ : u(p₁)", 30, BLUE))
        b.append(text(230, 570, "p₂ : v̄(p₂)", 30, RED))
        b.append(text(770, 225, "p₃ : ū(p₃)", 30, GREEN, "end"))
        b.append(text(770, 570, "p₄ : v(p₄)", 30, ORANGE, "end"))
        b.append(text(500, 330, "q = p₁ + p₂", 28, INK, "middle"))
        b.append(text(500, 450, "q² = s", 28, MUTED, "middle"))
    return svg(W, H, "".join(b))


def crossing():
    W, H = 1700, 640
    b = []
    # left: t-channel e mu -> e mu
    A, B = (380, 200), (380, 440)
    b.append(text(380, 50, "e⁻μ⁻ → e⁻μ⁻   (photon in t)", 32, INK, "middle", 600))
    b.append(fermion(120, 100, *A, BLUE) + fermion(*A, 640, 100, BLUE))
    b.append(fermion(120, 540, *B, GREEN) + fermion(*B, 640, 540, GREEN))
    b.append(wavy(*A, *B) + dot(*A, 11) + dot(*B, 11))
    b.append(text(100, 95, "e⁻", 32, BLUE, "end", 600) + text(660, 95, "e⁻", 32, BLUE, "start", 600))
    b.append(text(100, 560, "μ⁻", 32, GREEN, "end", 600) + text(660, 560, "μ⁻", 32, GREEN, "start", 600))
    b.append(text(380, 610, "q² = t = (p₁ − p₃)² &lt; 0", 28, MUTED, "middle"))
    # middle arrow
    b.append(arrow(760, 320, 940, 320, INK, 4, 26))
    b.append(text(850, 290, "rotate by 90°", 26, INK, "middle"))
    b.append(text(850, 370, "s ↔ t", 34, RED, "middle", 700))
    # right: s-channel ee -> mu mu
    A, B = (1180, 320), (1440, 320)
    b.append(text(1310, 50, "e⁺e⁻ → μ⁺μ⁻   (photon in s)", 32, INK, "middle", 600))
    b.append(fermion(1010, 130, *A, BLUE) + fermion(1010, 510, *A, BLUE, backward=True))
    b.append(fermion(*B, 1610, 130, GREEN) + fermion(*B, 1610, 510, GREEN, backward=True))
    b.append(wavy(*A, *B) + dot(*A, 11) + dot(*B, 11))
    b.append(text(990, 125, "e⁻", 32, BLUE, "end", 600) + text(990, 535, "e⁺", 32, BLUE, "end", 600))
    b.append(text(1630, 125, "μ⁻", 32, GREEN, "start", 600) + text(1630, 535, "μ⁺", 32, GREEN, "start", 600))
    b.append(text(1310, 610, "q² = s = (p₁ + p₂)² &gt; 0", 28, MUTED, "middle"))
    return svg(W, H, "".join(b))


def ep_blob():
    W, H = 1600, 700
    b = []
    for k, (ox, target, col) in enumerate(((60, "μ⁻", GREEN), (860, "p", RED))):
        A, B = (ox + 340, 200), (ox + 340, 470)
        b.append(text(ox + 340, 50, "point-like muon" if k == 0 else "proton: 3 quarks + gluons", 32, INK, "middle", 600))
        b.append(fermion(ox + 80, 90, *A, BLUE) + fermion(*A, ox + 600, 90, BLUE))
        b.append(text(ox + 60, 85, "e⁻", 32, BLUE, "end", 600) + text(ox + 620, 85, "e⁻", 32, BLUE, "start", 600))
        if k == 0:
            b.append(wavy(*A, *B))
            b.append(fermion(ox + 80, 600, *B, col) + fermion(*B, ox + 600, 600, col))
            b.append(dot(*A, 11) + dot(*B, 11))
            b.append(text(ox + 380, 345, "γ", 32, ORANGE, "start", 600))
            b.append(text(ox + 340, 670, "known current ū γ<tspan baseline-shift='super' font-size='70%'>μ</tspan> u  →  tensor L<tspan baseline-shift='super' font-size='70%'>μν</tspan>", 28, MUTED, "middle"))
        else:
            b.append(wavy(A[0], A[1], B[0], B[1] - 62))
            for dy in (-14, 0, 14):
                b.append(line(ox + 80, 600 + dy, B[0] - 50, B[1] + 20 + dy * 0.6, col, 3))
                b.append(line(B[0] + 50, B[1] + 20 + dy * 0.6, ox + 600, 600 + dy, col, 3))
            b.append(f'<ellipse cx="{B[0]}" cy="{B[1] + 10}" rx="78" ry="70" fill="#fbe9ec" stroke="{RED}" stroke-width="4"/>')
            b.append(text(B[0], B[1] + 24, "?", 52, RED, "middle", 700))
            b.append(dot(*A, 11))
            b.append(text(ox + 380, 330, "γ", 32, ORANGE, "start", 600))
            b.append(text(ox + 60, 620, "p", 32, RED, "end", 600) + text(ox + 620, 620, "p", 32, RED, "start", 600))
            b.append(text(ox + 340, 670, "unknown structure  →  form factors (Lecture 12)", 28, MUTED, "middle"))
    return svg(W, H, "".join(b))


# ---------------------------------------------------------------- helicity pictures

def helicity_vertex():
    """Allowed and forbidden helicity combinations at a QED vertex for E >> m."""
    W, H = 1700, 600
    b = []
    panels = (("scattering", True, ("R", "R")), ("scattering", False, ("R", "L")),
              ("annihilation", True, ("R", "L")), ("annihilation", False, ("R", "R")))
    for k, (kind, ok, (h1, h2)) in enumerate(panels):
        ox = 30 + k * 420
        cx, cy = ox + 200, 300
        col = GREEN if ok else RED
        b.append(f'<rect x="{ox}" y="30" width="390" height="540" rx="8" fill="#f7f9fb" stroke="{col}" stroke-width="3"/>')
        b.append(text(ox + 195, 80, kind, 30, INK, "middle", 600))
        if kind == "scattering":
            b.append(fermion(cx - 160, cy + 120, cx, cy, BLUE))
            b.append(fermion(cx, cy, cx + 160, cy + 120, BLUE))
            b.append(wavy(cx, cy, cx, cy - 150))
            # momentum along line; spin along (R) or against (L) momentum
            a1 = atan2(-120, 160)
            a2 = atan2(120, 160)
            b.append(spin(cx - 100, cy + 40, a1 if h1 == "R" else a1 + pi, INK, 64))
            b.append(spin(cx + 100, cy + 40, a2 if h2 == "R" else a2 + pi, INK, 64))
            b.append(text(cx - 100, cy + 150, f"e⁻ {h1}", 28, BLUE, "middle", 600))
            b.append(text(cx + 100, cy + 150, f"e⁻ {h2}", 28, BLUE, "middle", 600))
        else:
            b.append(fermion(cx - 160, cy - 110, cx, cy, BLUE))
            b.append(fermion(cx - 160, cy + 110, cx, cy, RED, backward=True))
            b.append(wavy(cx, cy, cx + 160, cy))
            a1 = atan2(110, 160)
            a2 = atan2(-110, 160)
            b.append(spin(cx - 105, cy - 125, a1 if h1 == "R" else a1 + pi, INK, 64))
            b.append(spin(cx - 105, cy + 125, a2 if h2 == "R" else a2 + pi, INK, 64))
            b.append(text(cx - 150, cy - 160, f"e⁻ {h1}", 28, BLUE, "start", 600))
            b.append(text(cx - 150, cy + 190, f"e⁺ {h2}", 28, RED, "start", 600))
        b.append(dot(cx, cy, 10))
        b.append(text(ox + 195, 545, "allowed" if ok else "forbidden", 32, col, "middle", 700))
    return svg(W, H, "".join(b))


def helicity_ee():
    """e+e- -> mu+mu- in the CM frame: J_z = +1 along the beam, J = ±1 along the mu- direction."""
    W, H = 1700, 700
    b = []
    # initial state
    ox, cy = 60, 330
    b.append(text(ox + 260, 60, "initial: e⁻<tspan baseline-shift='sub' font-size='70%'>R</tspan> e⁺<tspan baseline-shift='sub' font-size='70%'>L</tspan>", 32, INK, "middle", 600))
    b.append(arrow(ox + 30, cy, ox + 200, cy, BLUE, 5, 26))
    b.append(arrow(ox + 490, cy, ox + 320, cy, RED, 5, 26))
    b.append(text(ox + 30, cy - 30, "e⁻", 30, BLUE, "start", 600))
    b.append(text(ox + 490, cy - 30, "e⁺", 30, RED, "end", 600))
    b.append(spin(ox + 115, cy + 80, 0, INK, 80))
    b.append(spin(ox + 405, cy + 80, 0, INK, 80))
    b.append(text(ox + 260, cy + 180, "spins add: J<tspan baseline-shift='sub' font-size='70%'>z</tspan> = +1", 30, INK, "middle", 600))
    b.append(text(ox + 260, cy + 220, "along the e⁻ beam", 26, MUTED, "middle"))
    b.append(line(ox + 560, 110, ox + 560, 620, LINE, 3))
    # two final states
    for k, (lam, lab, formula) in enumerate(((+1, "μ⁻<tspan baseline-shift='sub' font-size='70%'>R</tspan> μ⁺<tspan baseline-shift='sub' font-size='70%'>L</tspan>", "(1 + cos θ)²"), (-1, "μ⁻<tspan baseline-shift='sub' font-size='70%'>L</tspan> μ⁺<tspan baseline-shift='sub' font-size='70%'>R</tspan>", "(1 − cos θ)²"))):
        fx = 700 + k * 500
        cx = fx + 200
        th = 50 * pi / 180
        b.append(text(cx, 60, f"final: {lab}", 32, INK, "middle", 600))
        b.append(line(cx - 190, cy, cx + 190, cy, MUTED, 2, "8 8"))
        ux, uy = cos(th), -sin(th)
        b.append(arrow(cx, cy, cx + 170 * ux, cy + 170 * uy, GREEN, 5, 26))
        b.append(arrow(cx, cy, cx - 170 * ux, cy - 170 * uy, ORANGE, 5, 26))
        b.append(text(cx + 185 * ux + 10, cy + 185 * uy, "μ⁻", 30, GREEN, "start", 600))
        b.append(text(cx - 185 * ux - 10, cy - 185 * uy + 20, "μ⁺", 30, ORANGE, "end", 600))
        ang = atan2(uy, ux) if lam > 0 else atan2(uy, ux) + pi
        nx, ny = -uy, ux  # perpendicular offset
        b.append(spin(cx + 95 * ux - 60 * nx, cy + 95 * uy - 60 * ny, ang, INK, 70))
        b.append(spin(cx - 95 * ux - 60 * nx, cy - 95 * uy - 60 * ny, ang, INK, 70))
        b.append(f'<path d="M{cx + 110:.1f},{cy:.1f} A110,110 0 0 0 {cx + 110 * ux:.1f},{cy + 110 * uy:.1f}" fill="none" stroke="{INK}" stroke-width="2"/>')
        b.append(text(cx + 125, cy - 35, "θ", 30, INK, "start", 600, 'font-style="italic"'))
        b.append(text(cx, cy + 180, f"J = {'+1' if lam > 0 else '−1'} along μ⁻", 30, INK, "middle", 600))
        b.append(text(cx, cy + 225, f"|M|² = e⁴ {formula}", 32, BLUE if lam > 0 else RED, "middle", 700))
    b.append(text(W / 2, 670, "Amplitude = overlap of J<tspan baseline-shift='sub' font-size='70%'>z</tspan> = +1 with J = ±1 along θ:  d¹(θ) = (1 ± cos θ)/2", 28, MUTED, "middle"))
    return svg(W, H, "".join(b))


# ---------------------------------------------------------------- plots

class Plot:
    def __init__(self, W, H, xr, yr, left=130, right=40, top=40, bottom=110, logy=False):
        self.W, self.H, self.xr, self.yr, self.logy = W, H, xr, yr, logy
        self.l, self.r, self.t, self.b = left, W - right, top, H - bottom

    def X(self, x):
        return self.l + (x - self.xr[0]) / (self.xr[1] - self.xr[0]) * (self.r - self.l)

    def Y(self, y):
        if self.logy:
            y = log10(max(y, 1e-12))
            lo, hi = log10(self.yr[0]), log10(self.yr[1])
        else:
            lo, hi = self.yr
        y = min(max(y, lo), hi)
        return self.b - (y - lo) / (hi - lo) * (self.b - self.t)

    def frame(self, xticks, yticks, xlabel, ylabel):
        b = [f'<rect x="{self.l}" y="{self.t}" width="{self.r - self.l}" height="{self.b - self.t}" fill="none" stroke="{INK}" stroke-width="2"/>']
        for x, lab in xticks:
            b.append(line(self.X(x), self.b, self.X(x), self.b - 10, INK, 2))
            b.append(line(self.X(x), self.t, self.X(x), self.b, LINE, 1))
            b.append(text(self.X(x), self.b + 36, lab, 26, INK, "middle"))
        for y, lab in yticks:
            b.append(line(self.l, self.Y(y), self.l + 10, self.Y(y), INK, 2))
            b.append(line(self.l, self.Y(y), self.r, self.Y(y), LINE, 1))
            b.append(text(self.l - 14, self.Y(y) + 9, lab, 26, INK, "end"))
        b.append(text((self.l + self.r) / 2, self.H - 30, xlabel, 30, INK, "middle"))
        b.append(f'<text transform="translate(40,{(self.t + self.b) / 2}) rotate(-90)" {FONT} font-size="30" fill="{INK}" text-anchor="middle">{ylabel}</text>')
        return "".join(b)

    def curve(self, f, color, w=5, dash=None, n=400):
        pts = []
        for i in range(n + 1):
            x = self.xr[0] + (self.xr[1] - self.xr[0]) * i / n
            pts.append((self.X(x), self.Y(f(x))))
        d = "M" + " L".join(f"{a:.1f},{c:.1f}" for a, c in pts)
        da = f' stroke-dasharray="{dash}"' if dash else ""
        return (f'<clipPath id="c{id(self)}"><rect x="{self.l}" y="{self.t}" width="{self.r - self.l}" height="{self.b - self.t}"/></clipPath>'
                f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}"{da} clip-path="url(#c{id(self)})"/>')


def ee_angular():
    W, H = 1100, 760
    P = Plot(W, H, (-1, 1), (0, 4.2))
    b = [P.frame([(c, f"{c:g}".replace("-", "−")) for c in (-1, -0.5, 0, 0.5, 1)],
                 [(y, f"{y:g}") for y in range(0, 5)], "cos θ", "⟨|M|²⟩ / e⁴   and channels")]
    b.append(P.curve(lambda c: (1 + c) ** 2, BLUE, 4, "12 8"))
    b.append(P.curve(lambda c: (1 - c) ** 2, RED, 4, "12 8"))
    b.append(P.curve(lambda c: 1 + c * c, INK, 7))
    b.append(text(P.X(0.62), P.Y(3.25), "RL→RL, LR→LR", 26, BLUE, "end", 600))
    b.append(text(P.X(0.62), P.Y(3.25) + 32, "(1 + cos θ)²", 26, BLUE, "end"))
    b.append(text(P.X(-0.62), P.Y(3.25), "RL→LR, LR→RL", 26, RED, "start", 600))
    b.append(text(P.X(-0.62), P.Y(3.25) + 32, "(1 − cos θ)²", 26, RED, "start"))
    b.append(text(P.X(-0.96), P.Y(2.15), "average: 1 + cos²θ", 28, INK, "start", 700))
    return svg(W, H, "".join(b))


def emu_angular():
    W, H = 1100, 760
    P = Plot(W, H, (-1, 0.9), (0.1, 3000), logy=True)
    yt = [(0.1, "0.1"), (1, "1"), (10, "10"), (100, "10²"), (1000, "10³")]
    b = [P.frame([(c, f"{c:g}".replace("-", "−")) for c in (-1, -0.5, 0, 0.5)],
                 yt, "cos θ", "⟨|M|²⟩ / e⁴   and channels")]
    RR = lambda c: 16 / (1 - c) ** 2            # 4 s²/t²
    RL = lambda c: 4 * (1 + c) ** 2 / (1 - c) ** 2  # 4 u²/t²
    avg = lambda c: 0.5 * (RR(c) + RL(c))
    b.append(P.curve(RR, BLUE, 4, "12 8"))
    b.append(P.curve(RL, RED, 4, "12 8"))
    b.append(P.curve(avg, INK, 7))
    b.append(text(P.X(-0.95), P.Y(RR(-0.95)) - 26, "RR, LL:  4s²/t²", 26, BLUE, "start", 600))
    b.append(text(P.X(-0.55), P.Y(RL(-0.55)) + 44, "RL, LR:  4u²/t²  → 0 at θ = π", 26, RED, "start", 600))
    b.append(text(P.X(0.1), P.Y(avg(0.1)) + 48, "average: 2(s² + u²)/t²", 28, INK, "start", 700))
    b.append(text(P.X(0.86), P.Y(0.2), "forward peak ∝ 1/θ⁴", 26, MUTED, "end"))
    return svg(W, H, "".join(b))


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    figs = (("vertex-crossings", vertex_crossings), ("emu-tchannel", emu_t), ("ee-schannel", ee_s),
            ("crossing", crossing), ("ep-blob", ep_blob), ("helicity-vertex", helicity_vertex),
            ("helicity-ee", helicity_ee), ("ee-angular", ee_angular), ("emu-angular", emu_angular))
    for name, fn in figs:
        (OUT / f"{name}.svg").write_text(fn(), encoding="utf-8")
        print("wrote", OUT / f"{name}.svg")

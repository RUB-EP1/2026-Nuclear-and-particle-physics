"""Original teaching figures for Lecture 10 (Dirac equation), written as plain SVG.

Run from the repository root:
    python3 slides/lectures/Lecture_10/scripts/make_figures.py
No dependencies. All quantities in units of the mass m.
"""
from math import atan2, cos, degrees, hypot, pi, sin, sqrt
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
            f'stroke="{stroke}" stroke-width="{w}"{d}/>')


def arrowhead(x, y, ang, color, size=18):
    """Filled triangle with its tip at (x, y), pointing along angle ang (radians)."""
    p = [(x, y)]
    for s in (+1, -1):
        p.append((x - size * cos(ang) + s * 0.5 * size * sin(ang),
                  y - size * sin(ang) - s * 0.5 * size * cos(ang)))
    pts = " ".join(f"{a:.1f},{b:.1f}" for a, b in p)
    return f'<polygon points="{pts}" fill="{color}"/>'


def arrow(x1, y1, x2, y2, color=INK, w=3):
    ang = atan2(y2 - y1, x2 - x1)
    return line(x1, y1, x2 - 14 * cos(ang), y2 - 14 * sin(ang), color, w) + arrowhead(x2, y2, ang, color)


def wavy(x1, y1, x2, y2, color=ORANGE, amp=9, waves=6, w=3):
    L = hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    pts = []
    for i in range(201):
        s = i / 200
        o = amp * sin(2 * pi * waves * s)
        pts.append((x1 + ux * L * s - uy * o, y1 + uy * L * s + ux * o))
    d = "M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in pts)
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}"/>'


def dispersion():
    W, H = 1000, 760
    x0, y0, sx, sy = 140, 390, 250, 95
    X = lambda p: x0 + p * sx
    Y = lambda E: y0 - E * sy
    b = []
    b.append(f'<rect x="{x0}" y="{Y(1)}" width="{X(3.3) - x0}" height="{Y(-1) - Y(1)}" fill="#f1f4f7"/>')
    b.append(text(X(2.4), Y(0.45), "no states: gap 2m", 26, MUTED, "middle"))
    b.append(arrow(x0, Y(-3.6), x0, Y(3.7)))
    b.append(arrow(x0, y0, X(3.4), y0))
    b.append(text(x0 - 20, Y(3.6), "E", 32, INK, "end", 600, 'font-style="italic"'))
    b.append(text(X(3.4), y0 + 40, "|p|", 30, INK, "end", 400, 'font-style="italic"'))
    for E, lab in ((1, "+m"), (-1, "−m")):
        b.append(line(x0 - 10, Y(E), x0 + 10, Y(E), INK, 2))
        b.append(text(x0 - 18, Y(E) + 9, lab, 26, INK, "end"))
    for sgn, col in ((1, BLUE), (-1, RED)):
        pts = [(X(p), Y(sgn * sqrt(1 + p * p))) for p in [i * 3.3 / 200 for i in range(201)]]
        d = "M" + " L".join(f"{a:.1f},{c:.1f}" for a, c in pts)
        b.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="5"/>')
    b.append(line(X(1.3), Y(1.3), X(3.3), Y(3.3), MUTED, 2, "8 8"))
    b.append(line(X(1.3), Y(-1.3), X(3.3), Y(-3.3), MUTED, 2, "8 8"))
    b.append(text(X(3.0), Y(3.32) - 4, "E = |p|", 22, MUTED, "end"))
    b.append(text(X(1.0), Y(2.75), "E = +√(p² + m²)", 30, BLUE, "start", 600))
    b.append(text(X(1.0), Y(2.75) + 38, "u₁, u₂  (spin ↑, ↓)", 28, BLUE))
    b.append(text(X(1.0), Y(-2.75) + 10, "E = −√(p² + m²)", 30, RED, "start", 600))
    b.append(text(X(1.0), Y(-2.75) + 48, "u₃, u₄  (spin ↑, ↓)", 28, RED))
    b.append(f'<circle cx="{X(0)}" cy="{Y(1)}" r="10" fill="{BLUE}"/><circle cx="{X(0)}" cy="{Y(-1)}" r="10" fill="{RED}"/>')
    b.append(text(X(0.1), Y(0.62), "at rest: E = +m", 24, BLUE))
    b.append(text(X(0.1), Y(-0.62) + 10, "at rest: E = −m", 24, RED))
    return svg(W, H, "".join(b))


def dirac_sea():
    W, H = 1300, 760
    b = []
    for k, (ox, title) in enumerate(((60, "Vacuum: every E &lt; 0 state filled"),
                                     (700, "Photon lifts an electron: pair"))):
        axis_x = ox + 40
        Y = lambda E: 380 - E * 105
        b.append(text(ox + 280, 50, title, 30, INK, "middle", 600))
        b.append(arrow(axis_x, 715, axis_x, 80))
        b.append(text(axis_x - 14, 100, "E", 30, INK, "end", 600, 'font-style="italic"'))
        b.append(f'<rect x="{axis_x + 20}" y="{Y(1)}" width="480" height="{Y(-1) - Y(1)}" fill="#f1f4f7"/>')
        for E, lab in ((1, "+m"), (-1, "−m")):
            b.append(text(axis_x - 14, Y(E) + 9, lab, 24, INK, "end"))
        b.append(text(axis_x + 90, Y(0) + 9, "gap 2m", 24, MUTED, "middle"))
        levels = [1 + 0.32 * i for i in range(6)]
        for E in levels:
            b.append(line(axis_x + 60, Y(E), axis_x + 460, Y(E), BLUE, 2))
            b.append(line(axis_x + 60, Y(-E), axis_x + 460, Y(-E), RED, 2))
            for j in range(5):
                cx = axis_x + 100 + 80 * j
                hole = k == 1 and abs(E - levels[1]) < 1e-9 and j == 1
                if hole:
                    b.append(f'<circle cx="{cx}" cy="{Y(-E) - 11}" r="11" fill="#fff" stroke="{RED}" stroke-width="3"/>')
                else:
                    b.append(f'<circle cx="{cx}" cy="{Y(-E) - 11}" r="10" fill="{RED}"/>')
        b.append(text(axis_x + 260, 712, "… infinitely many, all occupied (Pauli)", 22, MUTED, "middle"))
        if k == 1:
            hx, hy = axis_x + 180, Y(-levels[1]) - 11
            ex, ey = axis_x + 180, Y(levels[3]) - 11
            b.append(f'<circle cx="{ex}" cy="{ey}" r="11" fill="{BLUE}"/>')
            b.append(arrow(hx, hy - 16, ex, ey + 18, INK, 3))
            b.append(wavy(axis_x + 500, Y(0), ex + 12, Y(0), ORANGE, 8, 7))
            b.append(text(axis_x + 500, Y(0) - 18, "γ with E &gt; 2m", 24, ORANGE, "end", 600))
            b.append(text(ex + 22, Y(0.72), "e⁻: charge −e, E &gt; 0", 24, BLUE, "start", 600))
            b.append(text(ex + 22, Y(-0.42) + 16, "hole ≙ e⁺: charge +e, E &gt; 0", 24, RED, "start", 600))
    return svg(W, H, "".join(b))


def zigzag():
    W, H = 1300, 760
    b = []
    b.append(arrow(70, 720, 70, 60))
    b.append(text(58, 80, "t", 32, INK, "end", 600, 'font-style="italic"'))
    b.append(arrow(70, 720, 860, 720))
    b.append(text(860, 708, "x", 30, INK, "end", 600, 'font-style="italic"'))
    P0, A, B, P3 = (170, 690), (360, 220), (590, 520), (800, 90)
    for (x1, y1), (x2, y2), col in ((P0, A, BLUE), (A, B, RED), (B, P3, BLUE)):
        b.append(line(x1, y1, x2, y2, col, 6))
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        b.append(arrowhead(mx + 0.03 * (x2 - x1), my + 0.03 * (y2 - y1), atan2(y2 - y1, x2 - x1), col, 28))
    b.append(wavy(B[0], B[1], 760, 690, ORANGE))
    b.append(wavy(A[0], A[1], 160, 110, ORANGE))
    b.append(text(770, 700, "γ", 30, ORANGE, "start", 600))
    b.append(text(150, 100, "γ", 30, ORANGE, "end", 600))
    for y, lab in ((630, "one e⁻"), (380, "e⁻ + e⁺ + e⁻"), (150, "one e⁻")):
        b.append(line(80, y, 850, y, MUTED, 2, "10 8"))
        b.append(text(855, y + 8, lab, 24, MUTED))
    b.append(f'<circle cx="{A[0]}" cy="{A[1]}" r="9" fill="{INK}"/><circle cx="{B[0]}" cy="{B[1]}" r="9" fill="{INK}"/>')
    b.append(text(B[0] + 22, B[1] + 34, "pair creation", 24, INK))
    b.append(text(A[0] - 20, A[1] - 22, "annihilation", 24, INK, "end"))
    b.append(text(1040, 260, "red segment:", 26, RED, "middle", 600))
    b.append(text(1040, 296, "e⁻ with E &lt; 0", 26, RED, "middle"))
    b.append(text(1040, 332, "backwards in time", 26, RED, "middle"))
    b.append(text(1040, 380, "≡", 34, INK, "middle"))
    b.append(text(1040, 428, "e⁺ with E &gt; 0", 26, RED, "middle"))
    b.append(text(1040, 464, "forwards in time", 26, RED, "middle"))
    return svg(W, H, "".join(b))


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for name, fn in (("dispersion", dispersion), ("dirac-sea", dirac_sea), ("zigzag", zigzag)):
        (OUT / f"{name}.svg").write_text(fn(), encoding="utf-8")
        print("wrote", OUT / f"{name}.svg")

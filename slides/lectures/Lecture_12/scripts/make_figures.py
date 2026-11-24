"""Original teaching figures for Lecture 12 (elastic e⁻p scattering, form factors, proton radius), plain SVG.

Run from the repository root:
    python3 slides/lectures/Lecture_12/scripts/make_figures.py
No dependencies. Drawing helpers are reused from Lecture 11; the helicity, Rutherford and
e⁻p-blob figures are generated there and copied into figures/ here.
"""
import sys
from math import cos, exp, log10, pi, radians, sin, sqrt
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "Lecture_11" / "scripts"))
from make_figures import (BLUE, GREEN, INK, LINE, MUTED, ORANGE, RED, Plot, arrow, dot,  # noqa: E402
                          line, svg, text, wavy)

OUT = Path(__file__).resolve().parent.parent / "figures"
HBARC = 0.1973  # GeV fm
MP = 0.938      # GeV


def sup(s):
    return f"<tspan baseline-shift='super' font-size='70%'>{s}</tspan>"


def sub(s):
    return f"<tspan baseline-shift='sub' font-size='70%'>{s}</tspan>"


# ---------------------------------------------------------------- kinematics

def ep_kinematics():
    """Lab frame: electron E hits a proton at rest, leaves with E' at angle theta; the proton recoils."""
    W, H = 1100, 800
    O = (470, 400)
    b = []
    b.append(arrow(60, O[1], O[0] - 16, O[1], BLUE, 5, 26))
    b.append(text(150, O[1] - 26, "e⁻:  p" + sub("1") + " = (E, 0, 0, E)", 30, BLUE, "start", 600))
    th = radians(38)
    L = 520
    e3 = (O[0] + L * cos(th), O[1] - L * sin(th))
    b.append(arrow(O[0] + 14 * cos(th), O[1] - 14 * sin(th), *e3, BLUE, 5, 26))
    b.append(text(e3[0] - 30, e3[1] - 22, "e⁻:  p" + sub("3") + ",  energy E′", 30, BLUE, "end", 600))
    ph = radians(-47)
    Lp = 300
    p4 = (O[0] + Lp * cos(ph), O[1] - Lp * sin(ph))
    b.append(arrow(O[0] + 30 * cos(ph), O[1] - 30 * sin(ph), *p4, RED, 6, 28))
    b.append(text(p4[0] + 18, p4[1] + 12, "p:  p" + sub("4") + "  (recoil)", 30, RED, "start", 600))
    b.append(line(O[0], O[1], O[0] + 560, O[1], MUTED, 2, "10 8"))
    # angle arc
    r = 150
    pts = " L".join(f"{O[0] + r * cos(a):.1f},{O[1] - r * sin(a):.1f}" for a in [th * i / 40 for i in range(41)])
    b.append(f'<path d="M{pts}" fill="none" stroke="{INK}" stroke-width="3"/>')
    b.append(text(O[0] + r + 20, O[1] - 36, "θ", 38, INK, "start", 700, 'font-style="italic"'))
    b.append(f'<circle cx="{O[0]}" cy="{O[1]}" r="26" fill="#fbe9ec" stroke="{RED}" stroke-width="4"/>')
    b.append(text(O[0] - 40, O[1] + 70, "p at rest:  p" + sub("2") + " = (M, 0, 0, 0)", 30, RED, "end", 600))
    b.append(text(60, 720, "q = p" + sub("1") + " − p" + sub("3") + " = p" + sub("4") + " − p" + sub("2")
                  + ",    Q" + sup("2") + " ≡ −q" + sup("2") + " > 0  (spacelike)", 30, ORANGE, "start", 600))
    b.append(text(60, 770, "elastic: the proton stays a proton,  p" + sub("4") + sup("2") + " = M" + sup("2"),
                  28, MUTED))
    return svg(W, H, "".join(b))


def eprime_theta():
    W, H = 1100, 760
    P = Plot(W, H, (0, 180), (0, 1.05), left=140)
    b = [P.frame([(x, f"{x}°") for x in range(0, 181, 30)],
                 [(y, f"{y:.2f}".rstrip("0").rstrip(".")) for y in (0, 0.25, 0.5, 0.75, 1)],
                 "scattering angle θ", "E′ / E")]
    for E, col, dash, lab, at in ((0.05, MUTED, None, "E = 50 MeV", 150), (0.5, GREEN, None, "0.5 GeV", 150),
                                  (2.0, BLUE, None, "2 GeV", 120), (10.0, RED, None, "10 GeV", 62)):
        f = lambda t, E=E: 1 / (1 + 2 * E / MP * sin(radians(t) / 2) ** 2)
        b.append(P.curve(f, col, 6, dash))
        y = f(at)
        b.append(text(P.X(at) + 8, P.Y(y) - 16, lab, 28, col, "start", 700))
    b.append(text(P.X(4), P.Y(0.06), "proton at rest, M = 0.938 GeV", 26, MUTED))
    return svg(W, H, "".join(b))


# ---------------------------------------------------------------- form factors

R_RMS = 0.84  # fm


def shapes():
    """Three charge distributions with the same rms radius: (label, colour, rho(r) normalised, F(q) with q in fm^-1)."""
    a = R_RMS / sqrt(12)              # exponential
    R = R_RMS * sqrt(5 / 3)           # uniform sphere
    s = R_RMS / sqrt(3)               # Gaussian: <r^2> = 3 s^2

    def F_sphere(q):
        x = q * R
        return 1 - x * x / 10 if x < 1e-3 else 3 * (sin(x) - x * cos(x)) / x ** 3
    return (
        ("exponential  →  dipole", BLUE, lambda r: exp(-r / a) / (8 * pi * a ** 3), lambda q: (1 + (q * a) ** 2) ** -2),
        ("Gaussian  →  Gaussian", GREEN, lambda r: exp(-r * r / (2 * s * s)) / (2 * pi * s * s) ** 1.5,
         lambda q: exp(-(q * s) ** 2 / 2)),
        ("uniform sphere", RED, lambda r: 3 / (4 * pi * R ** 3) if r < R else 0.0, F_sphere),
    )


def form_factors():
    W, H = 1760, 760
    left = Plot(860, H, (0, 2.0), (0, 3.0), left=130, right=30)
    # r^2 rho(r) * 4 pi: probability per unit radius, peaks show where the charge is
    b = [left.frame([(x, f"{x:g}") for x in (0, 0.5, 1, 1.5, 2)], [(y, f"{y:g}") for y in (0, 1, 2, 3)],
                    "r (fm)", "4πr² ρ(r)  (fm⁻¹)")]
    for lab, col, rho, F in shapes():
        b.append(left.curve(lambda r, rho=rho: 4 * pi * r * r * rho(r), col, 6, n=800))
    b.append(text(left.X(1.15), left.Y(2.1), "same rms radius", 28, INK, "start", 700))
    b.append(text(left.X(1.15), left.Y(2.1) + 36, "0.84 fm", 28, INK, "start", 700))
    right = Plot(900, H, (0, 25), (1e-4, 1.3), left=150, right=30, logy=True)
    yt = [(1, "1"), (0.1, "0.1"), (0.01, "10⁻²"), (1e-3, "10⁻³"), (1e-4, "10⁻⁴")]
    g = [right.frame([(x, f"{x:g}") for x in (0, 5, 10, 15, 20, 25)], yt, "q² (fm⁻²)     [1 fm⁻² ≈ 0.039 GeV²]", "|F(q²)|²")]
    for i, (lab, col, rho, F) in enumerate(shapes()):
        g.append(right.curve(lambda q2, F=F: F(sqrt(q2)) ** 2, col, 6, n=900))
        g.append(text(right.X(24.5), right.Y(1) + 40 + 40 * i, lab, 28, col, "end", 700))
    g.append(text(right.X(0.6), right.Y(2.2e-4), "low q²: identical, slope = −⟨r²⟩/6", 26, MUTED))
    body = "".join(b) + f'<g transform="translate(860,0)">{"".join(g)}</g>'
    return svg(W, H, body)


def rosenbluth():
    """Schematic Rosenbluth separation: sigma_R linear in epsilon at fixed Q^2."""
    W, H = 1000, 720
    P = Plot(W, H, (0, 1), (0, 1.0), left=120, right=40, bottom=120)
    b = [P.frame([(x, f"{x:g}") for x in (0, 0.25, 0.5, 0.75, 1)], [], "virtual-photon polarisation ε", "σ" + sub("R") + " = ε G" + sub("E") + sup("2") + " + τ G" + sub("M") + sup("2"))]
    a0, sl = 0.32, 0.42
    b.append(P.curve(lambda e: a0 + sl * e, BLUE, 6))
    for e in (0.22, 0.55, 0.88):
        b.append(dot(P.X(e), P.Y(a0 + sl * e), 12, INK))
    b.append(dot(P.X(0), P.Y(a0), 12, RED))
    b.append(text(P.X(0.03), P.Y(a0) + 46, "intercept  τ G" + sub("M") + sup("2"), 30, RED, "start", 700))
    x1, x2 = 0.55, 0.88
    b.append(line(P.X(x1), P.Y(a0 + sl * x1), P.X(x2), P.Y(a0 + sl * x1), ORANGE, 3, "8 6"))
    b.append(line(P.X(x2), P.Y(a0 + sl * x1), P.X(x2), P.Y(a0 + sl * x2), ORANGE, 3, "8 6"))
    b.append(text(P.X(x2) + 14, P.Y(a0 + sl * (x1 + x2) / 2) + 10, "slope  G" + sub("E") + sup("2"), 30, ORANGE, "start", 700))
    b.append(text(P.X(0.03), P.Y(0.93), "fixed Q²: vary beam energy E and angle θ together", 26, MUTED))
    b.append(text(P.X(0.5), P.Y(0.06), "← backward (θ → 180°)              forward (θ → 0) →", 24, MUTED, "middle"))
    return svg(W, H, "".join(b))


# ---------------------------------------------------------------- proton radius puzzle

RADII = (
    # label, year, value, error, kind
    ("CODATA 2006", 2007, 0.8768, 0.0069, "codata"),
    ("Mainz A1, e⁻p scattering", 2010, 0.879, 0.008, "e"),
    ("muonic hydrogen (PSI)", 2010.5, 0.84184, 0.00067, "mu"),
    ("CODATA 2010", 2012, 0.8775, 0.0051, "codata"),
    ("muonic hydrogen (PSI)", 2013, 0.84087, 0.00039, "mu"),
    ("H 2S–4P (Garching)", 2017, 0.8335, 0.0095, "h"),
    ("H 1S–3S (Paris)", 2018, 0.877, 0.013, "h"),
    ("PRad, e⁻p at JLab", 2019, 0.831, 0.014, "e"),
    ("H Lamb shift (Toronto)", 2019.5, 0.833, 0.010, "h"),
    ("CODATA 2018", 2020.4, 0.8414, 0.0019, "codata"),
    ("H 1S–3S (Garching)", 2020.9, 0.8482, 0.0038, "h"),
    ("CODATA 2022", 2024.6, 0.84075, 0.00064, "codata"),
)
KIND = {"e": (BLUE, "electron scattering"), "mu": (RED, "muonic hydrogen"),
        "h": (GREEN, "hydrogen spectroscopy"), "codata": (INK, "CODATA value")}


def radius_puzzle():
    W, H = 1500, 800
    P = Plot(W, H, (2005.5, 2026), (0.81, 0.90), left=140, right=40, top=90)
    b = [P.frame([(y, str(y)) for y in range(2006, 2027, 2)],
                 [(v, f"{v:.2f}") for v in (0.82, 0.84, 0.86, 0.88, 0.90)], "year of publication", "r" + sub("p") + "  (fm)")]
    for lab, yr, v, e, k in RADII:
        col = KIND[k][0]
        x = P.X(yr)
        b.append(line(x, P.Y(v - e), x, P.Y(v + e), col, 4))
        if k == "codata":
            b.append(f'<rect x="{x - 11:.1f}" y="{P.Y(v) - 11:.1f}" width="22" height="22" fill="#fff" stroke="{INK}" stroke-width="4"/>')
        else:
            b.append(dot(x, P.Y(v), 11, col))
    for i, k in enumerate(("e", "mu", "h", "codata")):
        col, lab = KIND[k]
        x0 = (160, 480, 790, 1150)[i]
        if k == "codata":
            b.append(f'<rect x="{x0 - 10}" y="36" width="20" height="20" fill="#fff" stroke="{INK}" stroke-width="4"/>')
        else:
            b.append(dot(x0, 46, 10, col))
        b.append(text(x0 + 22, 56, lab, 26, col, "start", 700))
    b.append(text(P.X(2010.9), P.Y(0.8418) + 52, "2010: 4 % smaller", 26, RED, "start", 700))
    return svg(W, H, "".join(b))


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    figs = (("ep-kinematics", ep_kinematics), ("eprime-theta", eprime_theta), ("form-factors", form_factors),
            ("rosenbluth", rosenbluth), ("radius-puzzle", radius_puzzle))
    for name, fn in figs:
        (OUT / f"{name}.svg").write_text(fn(), encoding="utf-8")
        print("wrote", OUT / f"{name}.svg")

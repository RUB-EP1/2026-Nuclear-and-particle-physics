# Lecture 13: Form factors and inelastic scattering

KT1 2026/27, Tuesday 1 December 2026. Thomson, *Modern Particle Physics*, Chapters 7–8.

**Status: draft.** Lecture 12 stopped at slide 29 ("A charge cloud: the form factor") on 24 November. This deck restarts there, adds a diffraction picture for form factors, and carries over the rest of Lecture 12 unchanged. The inelastic part is still to be written. Plan in `slides/lectures.yml`.

## Structure

- 3 · Elastic scattering, where we stopped: the form factor (copied from Lecture 12), diffraction explorer (widget), what the wall tells us.
- Copied from Lecture 12: radius from the slope (board), same radius with different shapes, proton-radius explorer (widget), why small Q², G_E and G_M, the Rosenbluth formula.
- 4 · How big is the proton? Scattering versus spectroscopy, the day the proton shrank (copied from Lecture 12).
- Next: inelastic scattering (placeholder). Backup: references.

## Notes

- `layout.html`, `lecture.css`, `figures/*.svg`, `widgets/proton-radius.html` and its poster are copied from Lecture 12.
- `widgets/diffraction.html` is self-contained, no external requests. Fraunhofer diffraction off a black disk (2J₁(x)/x), hard sphere (3j₁(x)/x), soft-edge sphere (× e^(−q²s²/2), s = R/4), Gaussian and exponential (same rms as the hard sphere). Shows the wall in perspective and face-on, and |F|² (optionally × Mott) versus θ, |t| or qR, with the unreachable region q > 2k shaded. Poster: `widgets/diffraction-poster.png` (headless Chrome screenshot at 1920×1080).
- Presets: ¹²C at 420 MeV modelled as a soft-edge sphere of R = 2.5 fm (first minimum near 50°); pp at 6.5 TeV per beam as a black disk of R = 1.10 fm (dip at |t| ≈ 0.47 GeV², TOTEM 13 TeV).

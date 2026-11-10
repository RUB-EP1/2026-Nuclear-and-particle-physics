# Lecture 8: Accelerators

This is a local draft for the KT1 2026/27 course. It follows Lecture 7 (tracking, light and charge) and comes before Lecture 9 (DAQ and trigger), so the course follows an experiment in order: accelerate → collide → detect → select → measure.

The deck has 46 slides: 39 main slides (five section dividers, a photo opener, a roadmap and six interactive demos), then a backup divider and six backup slides. Luminosity and pile-up (covered in Lecture 4) are in the backup. Speaker notes give timings, worked arithmetic and photo credits.

## Preview

```sh
quarto render slides/lectures/Lecture_8/Lecture_8.qmd
python3 -m http.server 8000
```

Open `http://localhost:8000/slides/lectures/Lecture_8/Lecture_8.html` and press `S` for speaker notes. Each widget also opens on its own (see Widgets below).

## Teaching sequence (90 min)

1. **Why accelerate?** (0–12 min): resolution and thresholds, fixed target vs collider, history of colliders.
2. **Electric fields** (12–35 min): electrostatic machines and the **Cockcroft–Walton demo**; cyclotron; synchrotron principle; RF cavities and the **RF cavity demo**; bunches (the 25 ns clock); the CERN injector chain.
3. **Magnetic fields** (35–62 min): p = 0.3 Bρ; dipoles and quadrupoles; the LHC tunnel; inside the magnets and the **magnet explorer**; FODO focusing; emittance and the **emittance demo**; beam size at the collision point.
4. **Synchrotron radiation** (62–80 min): why a bent beam radiates (the same physics as bremsstrahlung, a different force); energy lost per turn; three ways around the limit; **ring designer demo**; pause question.
5. **From collisions to experiments** (80–90 min): cross-section hierarchy, which leads into Lecture 9; applications; summary; exit questions.

With six demos the time is tight: keep each demo to 3–4 minutes, and drop the magnet explorer if needed.

## Widgets

Each widget opens on its own from `widgets/`. They are offline and deterministic; the shared models are in `widgets/physics.js` and `widgets/ring.js`.

- **`cw.html`, Cockcroft–Walton ladder:** a numerical circuit integration (equal capacitors, ideal diodes with a small series resistance, an optional load). Conducting diodes are highlighted, and the output approaches 2N·V₀.
- **`rf.html`, RF cavity:** a chain of π-mode cells with an oscillating on-axis field and a particle at the speed of light. The energy gain varies as cos φ, and a single cell gives the 2/π transit-time factor.
- **`race.html`, a lap of the LHC:** a time-trial cyclist (50 km/h), a runner (20 km/h) and a proton (c). Not in the deck any more (replaced by the backup LHC video); kept for reuse.
- **`magnet.html`, magnet explorer:** a clickable schematic of the LHC dipole cross-section with 13 parts.
- **`emittance.html`, emittance:** particles in (x, x′) passing through drifts and thin lenses (the area is conserved), a squeeze to a focus, and acceleration (the area shrinks as 1/p).
- **`designer.html`, ring designer:** bending radius, circumference, synchrotron loss per turn, √s, and muon decay.

## Publication

Lecture 8 is published on the course website. CERN photographs and figures without a confirmed open licence (LHC tunnel, CERN complex, LEAR dipole, CMS pile-up plot) are loaded from the git-ignored `figures/local/` folder: they show in the lecture room and as a credited placeholder online, following the Lecture 7 rule in `THIRD_PARTY.md`. Keep a local copy of that folder to present the full deck.

## Assets and validation

Photographs come from Wikimedia Commons with stated licences; [SOURCES.md](SOURCES.md) lists each file, author and licence. The eight plots are reproducible:

```sh
.venv-pdf/bin/python slides/lectures/Lecture_8/scripts/make_plots.py
```

To run the checks:

```sh
node slides/lectures/Lecture_8/tests/ring.test.cjs
node slides/lectures/Lecture_8/tests/physics.test.cjs
.venv-pdf/bin/python slides/lectures/Lecture_8/tests/check_browser.py
```

The browser check renders all six widget posters and exercises each widget through its controls with physics assertions (the ring designer, the Cockcroft–Walton output, the RF phase dependence, emittance conservation, the magnet facts and the race counters). It checks every slide for missing images, overflow and maths errors, confirms that the live iframe mounts and unmounts, and saves screenshots to the ignored `tmp/qa/` folder.

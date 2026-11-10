# Lecture 8: Accelerators

This is a local draft for the KT1 2026/27 course. It follows Lecture 7 (tracking, light and charge) and comes before Lecture 9 (DAQ and trigger), so the course follows an experiment in order: accelerate → collide → detect → select → measure.

The deck has 38 slides: 32 main slides (including six section dividers, a photo opener, a roadmap and one interactive demo), then a backup divider and three backup slides. Speaker notes give timings for a 90-minute lecture, worked arithmetic and photo credits.

## Preview

```sh
quarto render slides/lectures/Lecture_8/Lecture_8.qmd
python3 -m http.server 8000
```

Open `http://localhost:8000/slides/lectures/Lecture_8/Lecture_8.html` and press `S` for speaker notes. The widget also opens on its own at `widgets/designer.html`.

## Teaching sequence (90 min)

1. **Why accelerate?** (0–15 min): resolution and thresholds, fixed target vs collider, history of colliders.
2. **Electric fields** (15–35 min): electrostatic machines, cyclotron, RF cavities, bunches (the 25 ns clock), the CERN injector chain.
3. **Magnetic fields** (35–52 min): p = 0.3 Bρ, the LHC tunnel, a look inside the magnets, FODO focusing, beam size at the collision point.
4. **Synchrotron radiation** (52–67 min): E⁴/m⁴ scaling, LEP2 vs LHC, three ways around the limit, ring designer demo, pause question.
5. **Luminosity** (67–80 min): luminosity from beam parameters, rates and integrated luminosity, pile-up.
6. **From collisions to experiments** (80–90 min): cross-section hierarchy, which leads into Lecture 9; applications; summary; exit questions.

If time is short, shorten the "inside the magnets" and beam-size slides, and set the backup derivations as reading.

## Draft publication guard

Lectures 8 and 9 are excluded from the website `render` and `resources` lists in `.github/workflows/pages.yml`, from the site checker and from the PDF export. Remove those exclusions only when you want to publish.

## Assets and validation

Photographs come from Wikimedia Commons with stated licences; [SOURCES.md](SOURCES.md) lists each file, author and licence. The six plots are reproducible:

```sh
.venv-pdf/bin/python slides/lectures/Lecture_8/scripts/make_plots.py
```

To run the checks:

```sh
node slides/lectures/Lecture_8/tests/ring.test.cjs
.venv-pdf/bin/python slides/lectures/Lecture_8/tests/check_browser.py
```

The browser check renders the widget poster, exercises the widget controls with physics assertions (LHC, LEP2, an impossible electron LHC, muons), and checks every slide for missing images, overflow and maths errors. It also confirms that the live iframe mounts and unmounts, and saves screenshots to the ignored `tmp/qa/` folder.

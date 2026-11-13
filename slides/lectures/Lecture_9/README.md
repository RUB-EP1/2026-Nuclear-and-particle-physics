# Lecture 9: Basics of Trigger and DAQ

KT1 2026/27 course, reworked and published on 13 November 2026 for undergraduates who meet trigger and data acquisition for the first time. Follows Lecture 7 (detectors) and Lecture 8 (accelerators). 78 slides: 51 numbered main slides (four section dividers, six accelerator recap slides, two interactive demos, ending with a thank-you slide), then a backup divider and 26 unnumbered backup slides (`visibility="uncounted"`, so the counter stops at 51/51) holding the advanced material of the earlier draft (real CMS turn-on, ATLAS diagram, prescales, tag and probe, menus, bandwidth, CPU budget, persistence, time of flight). The history and DAQ parts follow the storyline of N. Neufeld's ESI 2009 lecture (Tycho Brahe; a trivial DAQ built up step by step). Speaker notes give a 90-minute pace and answers.

## Preview

```sh
quarto render slides/lectures/Lecture_9/Lecture_9.qmd
python3 -m http.server 8000
```

Open `http://localhost:8000/slides/lectures/Lecture_9/Lecture_9.html`.
The generated HTML is local and untracked. Press `S` for Reveal speaker notes. The widgets also open independently:

- `widgets/queue.html`: ADC, FIFO and processor; one-stage dead-time alternative; replay/scrubber and reset.
- `widgets/threshold.html`: fixed signal/background samples, selection efficiencies, purity and bandwidth.

No external widget libraries, fonts, data services or network calls. `?export=1` on the deck uses the checked PNG posters, following the existing export convention. Widgets initially show a completed deterministic result rather than starting an animation automatically.

## Publication

Lecture 9 is included in the website render, resource checks and PDF export, and linked from the course index. GitHub Actions publishes it on pushes to `main`.

## Teaching sequence

Recommended 90-minute route:

- Accelerator recap: 0–12 min. Six slides, each with one check question.
- The complete experiment: 12–25 min. Events and pile-up, pulse, ADC/TDC, event size, 40 TB/s.
- History: 25–45 min. Tycho Brahe's systematic measurements and Kepler's 8 arcminutes; Geiger–Müller counter, gas-counter regimes, coincidences, accidentals, counter-controlled cloud chamber; trigger and DAQ defined.
- Building a DAQ step by step: 45–65 min. (1) one sensor on a clock, (2) many sensors: crates and networks, (3) trigger + delay, discriminator, (4) busy logic and dead time, (5) FIFO; queue demo; pause and check.
- Scaling up to the LHC: 65–85 min. Crossings in flight, the full detector at work (which systems feed Level-1), a calorimeter trigger worked example (2×2 sums), a class exercise, the LHCb Level-0 calorimeter trigger, signatures, threshold and demo, toy turn-on, the pipeline as the grown-up delay, two trigger levels, rates, LHCb software trigger.
- Summary and exit questions: 85–90 min. No homework slide; the next lecture is on the Dirac equation.

The LHC section is now full: if time is short, drop the threshold demo or the rates slide rather than the calorimeter example.

## Visual teaching material

The first half now pairs short explanations with pulse, digitization, event-fragment, gain, bandwidth, pipeline, dead-time and buffer plots. The trigger section adds spectra, efficiency/purity and selection-bias plots. There are 18 reproducible SVG teaching plots plus an attributed source readout diagram. Section 2 adds a pipeline-buffer plot; section 4 adds tag-and-probe pseudo-data; section 5 adds a threshold-versus-prescale plot. Two simple analytic plots were replaced by tables (rate × size, storage choices) and one by a click-to-reveal calculation (pause and check), alongside the existing experiment figures and both interactive demos.

Regenerate plots from the repository root:

```sh
.venv-pdf/bin/python slides/lectures/Lecture_9/scripts/make_plots.py
.venv-pdf/bin/python slides/lectures/Lecture_9/scripts/make_intro_figures.py
.venv-pdf/bin/python slides/lectures/Lecture_9/scripts/make_daq_figures.py
```

Requires NumPy, Matplotlib, Pillow and Node. See `SOURCES.md` for parameters and source transformations.

## Validation

```sh
node slides/lectures/Lecture_9/tests/models.test.cjs
.venv-pdf/bin/python slides/lectures/Lecture_9/tests/check_browser.py
```

The first checks event accounting, busy/completion boundaries, finite-buffer overload, the long-run non-paralyzable formula, deterministic samples, threshold limits and bandwidth units. The browser check renders both posters, exercises the actual controls, blocks external requests, checks live iframe mount/unmount, and captures all slides for visual review. Local screenshots and reports go to ignored `tmp/qa/`.

See [SOURCES.md](SOURCES.md) for image credits and the precise toy models. Original source PDFs remain in the internal reference archive; the deck does not link to that archive.

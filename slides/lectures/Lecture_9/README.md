# Lecture 9: Basics of Trigger and DAQ

Local draft for the KT1 2026/27 course, reworked on 13 November 2026 for undergraduates who meet trigger and data acquisition for the first time. Follows Lecture 7 (detectors) and Lecture 8 (accelerators). 64 slides: 42 main slides (four section dividers, six accelerator recap slides, two interactive demos), then a backup divider and 21 backup slides holding the advanced material of the earlier draft (tag and probe, menus, bandwidth, CPU budget, persistence, time of flight). Speaker notes give a 90-minute pace and answers.

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

## Draft publication guard

Lecture 9 is explicitly excluded from both the generated website's `render` and `resources` lists in `.github/workflows/pages.yml`. It has not been added to the course index. The website checker and PDF exporter also skip this draft; a build assertion rejects any Lecture 9 output. Remove the Lecture 9 exclusions and assertion together only when publication is requested. No publishing commands or pushes were performed for this draft.

## Teaching sequence

Recommended 90-minute route:

- Accelerator recap: 0–12 min. Six slides, each with one check question: RF cavities, magnets, colliders, synchrotron radiation, bunches (40 MHz), luminosity and rates.
- The complete experiment: 12–27 min. Detector layers, what an event is (pile-up), pulse, ADC/TDC, event size, 40 TB/s.
- The first trigger: 27–45 min. Geiger–Müller counter, gas-counter regimes, Bothe–Kolhörster coincidences, accidental rate, Blackett–Occhialini counter-controlled cloud chamber, definitions of trigger and DAQ.
- DAQ: 45–63 min. Discriminator, readout chain, dead time, buffers, queue demo, pause and check.
- Triggering at the LHC: 63–85 min. Rate funnel, signatures, threshold and demo, turn-on curve, pipeline, ATLAS two levels, prescale, LHCb software trigger.
- Summary, exit questions, homework: 85–90 min.

If time is short, shorten the demos and skip the prescale slide.

## Visual teaching material

The first half now pairs short explanations with pulse, digitization, event-fragment, gain, bandwidth, pipeline, dead-time and buffer plots. The trigger section adds spectra, efficiency/purity and selection-bias plots. There are 18 reproducible SVG teaching plots plus an attributed source readout diagram. Section 2 adds a pipeline-buffer plot; section 4 adds tag-and-probe pseudo-data; section 5 adds a threshold-versus-prescale plot. Two simple analytic plots were replaced by tables (rate × size, storage choices) and one by a click-to-reveal calculation (pause and check), alongside the existing experiment figures and both interactive demos.

Regenerate plots from the repository root:

```sh
.venv-pdf/bin/python slides/lectures/Lecture_9/scripts/make_plots.py
.venv-pdf/bin/python slides/lectures/Lecture_9/scripts/make_intro_figures.py
```

Requires NumPy, Matplotlib, Pillow and Node. See `SOURCES.md` for parameters and source transformations.

## Validation

```sh
node slides/lectures/Lecture_9/tests/models.test.cjs
.venv-pdf/bin/python slides/lectures/Lecture_9/tests/check_browser.py
```

The first checks event accounting, busy/completion boundaries, finite-buffer overload, the long-run non-paralyzable formula, deterministic samples, threshold limits and bandwidth units. The browser check renders both posters, exercises the actual controls, blocks external requests, checks live iframe mount/unmount, and captures all slides for visual review. Local screenshots and reports go to ignored `tmp/qa/`.

See [SOURCES.md](SOURCES.md) for image credits and the precise toy models. Original source PDFs remain in the internal reference archive; the deck does not link to that archive.

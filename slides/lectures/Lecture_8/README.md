# Lecture 8: DAQ and Trigger

Local draft for the KT1 2026/27 course. Built from the internal lecture plan; assumes Lecture 7 calorimetry/PID is already covered. 50 slides: 44 main slides (including six section dividers, a roadmap and two interactive demos), followed by a backup divider and five backup slides. Synchrotron radiation (section 1) and time of flight (section 2) were added because they were not covered in earlier lectures. Speaker notes give a 90-minute pace, questions and answers, model assumptions, and references.

## Preview

```sh
quarto render slides/lectures/Lecture_8/Lecture_8.qmd
python3 -m http.server 8000
```

Open `http://localhost:8000/slides/lectures/Lecture_8/Lecture_8.html`.
The generated HTML is local and untracked. Press `S` for Reveal speaker notes. The widgets also open independently:

- `widgets/queue.html`: ADC, FIFO and processor; one-stage dead-time alternative; replay/scrubber and reset.
- `widgets/threshold.html`: fixed signal/background samples, selection efficiencies, purity and bandwidth.

No external widget libraries, fonts, data services or network calls. `?export=1` on the deck uses the checked PNG posters, following the existing export convention. Widgets initially show a completed deterministic result rather than starting an animation automatically.

## Draft publication guard

Lecture 8 is explicitly excluded from both the generated website's `render` and `resources` lists in `.github/workflows/pages.yml`. It has not been added to the course index. The website checker and PDF exporter also skip this draft; a build assertion rejects any Lecture 8 output. Remove the Lecture 8 exclusions and assertion together only when publication is requested. No publishing commands or pushes were performed for this draft.

## Teaching sequence

The six sections are visible as dividers and in the footer throughout. Recommended 90-minute route (timings include transitions and discussion):

- Orientation and physics rates: 0–21 min. Stirling hierarchy, luminosity, synchrotron radiation (why protons), pile-up.
- Acquiring an event: 21–38 min. Digitization, time of flight, assembly, bandwidth, latency, pipeline storage, then the ATLAS Run-2 architecture as a worked example.
- Dead time and buffering: 38–50 min. Dead-time formula, FIFO, overload and queue demo.
- Trigger performance: 50–68 min. Real CMS turn-on, tag-and-probe, threshold demo and bias.
- Operating a menu: 68–80 min. Overlaps, prescales, CPU, ATLAS rates versus bandwidth.
- Real-time analysis and synthesis: 80–90 min. LHCb, ATLAS/LHCb comparison, persistence, provenance, exit questions; the ACTS tracking slide is a next-lecture preview.

The expanded deck is also a reference for students. Individual speaker-note times are discussion allowances; use this section budget for a single 90-minute lecture. The deck is over-full for 90 minutes. To make room, defer CPU composition and tag-and-probe details, shorten the demos, show the ACTS preview without discussion, and assign the backup exercises. Keep all five landmark figures and their interpretation.

## Visual teaching material

The first half now pairs short explanations with pulse, digitization, event-fragment, gain, bandwidth, pipeline, dead-time and buffer plots. The trigger section adds spectra, efficiency/purity and selection-bias plots. There are 18 reproducible SVG teaching plots plus an attributed source readout diagram. Section 2 adds a pipeline-buffer plot; section 4 adds tag-and-probe pseudo-data; section 5 adds a threshold-versus-prescale plot. Two simple analytic plots were replaced by tables (rate × size, storage choices) and one by a click-to-reveal calculation (pause and check), alongside the existing experiment figures and both interactive demos.

Regenerate plots from the repository root:

```sh
.venv-pdf/bin/python slides/lectures/Lecture_8/scripts/make_plots.py
```

Requires NumPy, Matplotlib, Pillow and Node. See `SOURCES.md` for parameters and source transformations.

## Validation

```sh
node slides/lectures/Lecture_8/tests/models.test.cjs
.venv-pdf/bin/python slides/lectures/Lecture_8/tests/check_browser.py
```

The first checks event accounting, busy/completion boundaries, finite-buffer overload, the long-run non-paralyzable formula, deterministic samples, threshold limits and bandwidth units. The browser check renders both posters, exercises the actual controls, blocks external requests, checks live iframe mount/unmount, and captures all slides for visual review. Local screenshots and reports go to ignored `tmp/qa/`.

See [SOURCES.md](SOURCES.md) for image credits and the precise toy models. Original source PDFs remain in the internal reference archive; the deck does not link to that archive.

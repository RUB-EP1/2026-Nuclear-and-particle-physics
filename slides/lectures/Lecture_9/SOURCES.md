# Lecture 9: sources, assets and models

Prepared 7 November 2026. Core teaching source: Marian Stahl, *DAQ – Trigger – Reconstruction and Data Analysis*, WS 2025/26, supplied Lecture-08.pdf, especially pages 4, 7–13 and 15–16. The internal reconstruction and next-lecture plan are in `reference/lecture-notes/`. No source-archive links are embedded in the student deck.

Style follows Lecture 6: 1920×1080 Reveal canvas, Helvetica/Arial, large black headings, blue emphasis, quiet source links, bottom course footer and full-slide widgets. `layout.html` is copied from Lecture 6; lecture CSS contains the relevant matching rules rather than importing the whole Lecture 6 stylesheet.

## External figures

| Local asset | Original source | Transformation / terms |
|---|---|---|
| `figures/atlas-run2-tdaq.png` | ATLAS Collaboration, *Operation of the ATLAS trigger system in Run 2*, JINST 15 P10004 (2020), [arXiv:2007.12539](https://arxiv.org/abs/2007.12539), Fig. 1, PDF p6 | Cropped from the 2200-pixel source-page rendering in the internal archive, preserving the complete figure; the printed paper caption is cropped off (bottom rows from y=862) and given in speaker notes. CC BY 4.0. Period is Run 2, not current operation; the drawn FTK system was under commissioning and not used for HLT trigger decisions in Run 2. |
| `figures/lhcb-run3-dataflow.png` | [LHCb Starterkit Run-3 data flow](https://lhcb.github.io/starterkit-lessons/first-analysis-steps/dataflow-run3.html), [original PNG](https://lhcb.github.io/starterkit-lessons/_images/hidef_RTA_dataflow_widescreen.png) | Unmodified educational design diagram; numbers are reference design allocations, not a live operational snapshot. No independent image reuse license verified. Credit LHCb; not MIT-relicensed. |
| `figures/acts-tracking.svg` | [ACTS, Tracking in a nutshell](https://acts.readthedocs.io/en/latest/tracking.html), [original SVG](https://acts.readthedocs.io/en/latest/_images/tracking.svg) | Unmodified SVG from the internal archive, retrieved 7 November 2026. Per-asset reuse license not independently verified; retain ACTS credit. |

## Added readout diagram

`figures/neufeld-readout-chain.png` reproduces the physical and logical panels from N. Neufeld, *Trigger and DAQ* (2009), PDF p16, linked below. Cropped from the archived 1600×1237 page rendering at fractional bounds (0.13, 0.43, 0.88, 0.845). Historical hardware illustration; no independent reuse license verified. Retain Neufeld attribution; not MIT-relicensed.

## Reproducible teaching plots

All 18 new SVGs are original illustrative calculations, not measured detector data. Regenerate with `python scripts/make_plots.py` from this lecture directory (NumPy, Matplotlib, Pillow, and Node required). SVG labels remain editable text. Model assumptions also appear in speaker notes.

| Assets | Calculation / assumptions |
|---|---|
| `signal-pulse.svg`, `adc-sampling.svg` | Shaped pulse 600 u² exp(2−2u) mV, u=(t−30 ns)/22 ns for t>30 ns. Pulse illustration adds Gaussian noise σ=9 mV, seed 8. ADC illustration samples the noiseless pulse every 10 ns and rounds to 100 mV codes 0–7. |
| `event-fragments.svg` | Three invented event IDs across three subsystems; arrival times in arbitrary units. Colour identifies an event, not its arrival rank. |
| `gain-drift.svg` | Constant 100 GeV input, gain 1+0.025t with t in hours; correction divides by the known gain. No experimental stability claim. |
| `data-per-day.svg` | V=Bt, decimal units; continuous recording. |
| `pipeline-buffer.svg` | Crossings every 25 ns, each stored for a fixed 2.5 µs latency; 161 crossings; four accepted crossings chosen by hand (accept fraction exaggerated for visibility). |
| `pipeline-timing.svg` | Three stages, one time unit each; four events. Small gaps only separate bars visually. |
| `deadtime-timeline.svg`, `deadtime-rate.svg` | Fixed non-paralyzable busy interval: deterministic timeline τ=2 arbitrary units; Poisson mean rate R/(1+Rτ), τ=0.12 ms. |
| `buffer-bursts.svg`, `buffer-capacity.svg` | Direct outputs of `widgets/models.js`, seed 821; ADC time zero, processor 0.1 ms. Burst traces: 8 kHz mean, 60 ms, 0/8 waiting slots. Capacity sweep: steady 8/15 kHz input over 2000 ms. These settings isolate buffering; they differ from the widget's default nonzero ADC time. |
| `efficiency-purity.svg`, `threshold-spectra.svg`, `selection-bias.svg` | Analytic versions of the trigger model below: nonnegative normal signal and exponential background. Signal 100 Hz, background 100 kHz; cut 7 GeV/c where drawn. Kept density is not renormalized. |
| `tag-and-probe.svg` | Seed 91. Gaussian Z peak, mean 91.19 GeV, σ 2.6 GeV; exponential background (slope 25 GeV) on 70–110 GeV; 18,400/1,600 signal and 600/900 background pairs in pass/fail samples; Poisson pseudo-data in 1 GeV bins. |
| `prescale-threshold.svg` | Path rate 20 kHz×(threshold/10 GeV)⁻⁴; prescale 40; 100 Hz allocation. |
| `synchrotron-loss.svg` | ΔE = 8.85×10⁻⁵ E⁴/ρ GeV (E in GeV, ρ in m) for electrons at ρ = 3096 m; protons at ρ = 2804 m scaled by (m_e/m_p)⁴. LEP2 104.5 GeV → 3.4 GeV/turn; LHC 7 TeV → 6.7 keV/turn. |
| `tof-separation.svg` | t = (L/c)√(1+(m/p)²), L = 5 m, Gaussian σ_t = 100 ps; PDG masses for π, K, p; exact momentum and path length. |

## Explanatory sources

- [N. Neufeld, trigger and DAQ lecture, 2009](https://indico.cern.ch/event/43007/contributions/1065030/attachments/927884/1313738/trigger-daq-analysis-esi09-neufeld1.pdf), pp16–20: trivial DAQ, trigger, dead time, buffers.
- [ATLAS Run-2 trigger paper](https://arxiv.org/abs/2007.12539): hardware/software staging and readout.
- [LHCb Starterkit](https://lhcb.github.io/starterkit-lessons/first-analysis-steps/dataflow-run3.html): GPU HLT1, buffering/calibration, CPU HLT2 and selective persistence. Some wording is from pre-Run-3 planning; no present-day quantitative claims are inferred from it.
- [LHCb CHEP 2024 trigger-performance presentation](https://indico.cern.ch/event/1338689/contributions/6015396/attachments/2951324/5187948/CHEP24_LHCb_Run3_trigger_performance.pdf): confirms the software-trigger architecture in Run-3 operation.

The rate×size arithmetic, sample fragment table, generic selection equations, questions and explanations are original teaching material. “Event” is an acquisition unit; it is explicitly distinguished from an interaction and a bunch crossing.

## Queue model

Implemented in `widgets/models.js`; all times in milliseconds, input rate in kHz = events/ms. Seed 821. One ADC and one serial processor, each with fixed service time. A finite FIFO holds converted events; capacity excludes an event in the processor and an event in the ADC. An arrival while ADC-busy is lost. At ADC completion, an idle processor starts immediately; otherwise enqueue or drop if full. CPU completion precedes ADC completion and then arrivals at equal timestamps.

Arrivals are Poisson at constant rate, or an inhomogeneous Poisson burst process: each 20 ms period has 4 ms at 4R and 16 ms at R/4, preserving mean R. Thinning generates the latter. A simulation spans 200 ms; it does not drain pending events beyond the observation window. The displayed identity is `arrived = completed + ADC-busy losses + FIFO-full losses + pending`, including both active stages. Busy fractions integrate actual busy time; output rate is completed count / elapsed time.

The alternative non-paralyzable mode combines ADC and processing times into one fixed busy period τ and ignores the FIFO. Lost arrivals do not extend τ. For steady Poisson input, long-run accepted rate is R/(1+Rτ). This is not an exact prediction for burst mode or for the buffered two-stage mode. At finite times accepted count and completed count differ by events still in service.

Replay advances 200 ms over approximately 10 seconds. It animates a precomputed deterministic event history, not a live real-time process. Parameter changes rebuild the same-seed run; Reset restores defaults. The code is O(number of arrivals), not an artificial per-frame Bernoulli approximation.

## Trigger model

Seed 809; fixed banks of 30,000 signal and 30,000 background candidates. Signal follows N(8, 2²) conditioned on nonnegative momentum, background an exponential distribution with mean 1.5 GeV/c. Exactly one candidate per event; measured momentum is exact. A hard threshold accepts x≥cut. There is no detector smearing, trigger turn-on, pileup or correlation between candidates.

Efficiencies are surviving fractions within each bank. Banks are reweighted by user-selected input rates (signal Hz, background kHz), not interpreted as equal physical priors. Selected signal fraction is S/(S+B) and shown as undefined if S+B=0. Bandwidth in decimal MB/s is total accepted Hz × event kB / 1000. Event size changes do not change selection efficiencies. Threshold changes never resample candidates. Histograms have 0.5 GeV/c bins plus a 20+ overflow bin, showing weighted rates on a log axis with a 0.1 Hz floor. Zero surviving samples are not a physical tail-probability bound.

## Posters and checks

`queue-poster.png` and `threshold-poster.png` are browser screenshots of default widget states at 1920×1080. They are derivatives of our own executable models. `tests/models.test.cjs` exercises model invariants and limiting cases; `tests/check_browser.py` exercises the UI and captures the deck. No experimental event-level dataset or digitized measurement was used.


## Landmark figures added for the broader lecture

Retrieved 7 November 2026. Original collaboration labels, axes and legends are retained. These are historical examples with explicit periods, not current operating specifications.

| Asset | Primary source and transformation | What students must read |
|---|---|---|
| `stirling-cross-sections.png` | W. J. Stirling, [2010 LHC lecture](https://indico.cern.ch/event/94815/contributions/1282690/attachments/1106827/1579062/LBLMIT_Stirling_v2.pdf), slide 22, WJS2009 plot. Crop (965,205,1735,1250) of 1800×1350 rendering; preserves full plot. Source archived as `stirling-lhc-2010.pdf`. | Log cross-section hierarchy, fixed-energy comparison, luminosity-dependent right axis. Historical Higgs mass assumptions 120/200/500 GeV. |
| `cms-run2-pileup.png` | [CMS luminosity public results](https://twiki.cern.ch/twiki/bin/view/CMSPublic/LumiPublicResults), [original PDF](https://cern.ch/cmslumi/publicplots/pileup_allYears_run2.pdf), rendered uncropped at 1800 px. Archived as `cms-run2-pileup.pdf`. | Recorded luminosity distribution versus mean interactions per crossing; not single-event vertex counts. |
| `cms-muon-turnon.png` | CMS, *Performance of the CMS high-level trigger during LHC Run 2*, JINST 19 P11021 (2024), [Fig.7a](https://cms-results.web.cern.ch/cms-results/public-results/publications/TRG-19-001/CMS-TRG-19-001_Figure_007-a.png), original PNG. | Offline momentum, full L1+HLT efficiency, non-unit plateau, data/MC ratio. |
| `cms-menu-rates.png` | Same CMS paper, [Fig.2](https://cms-results.web.cern.ch/cms-results/public-results/publications/TRG-19-001/CMS-TRG-19-001_Figure_002.png), original PNG. | Inclusive versus pure group rates and accounting for shared paths. |
| `cms-cpu-budget.png` | Same CMS paper, [Fig.1](https://cms-results.web.cern.ch/cms-results/public-results/publications/TRG-19-001/CMS-TRG-19-001_Figure_001.png), original PNG. | Reconstruction cost by category. The adjacent 20,000-core estimate is a separate illustrative calculation. |
| `atlas-stream-rate-bandwidth.png` | ATLAS, *Operation of the ATLAS trigger system in Run 2*, [arXiv:2007.12539](https://arxiv.org/abs/2007.12539), Fig.7, PDF p17; both plot panels cropped together from a 2200 px rendering at fractional bounds (0.24,0.18,0.78,0.625). | Different dominance of trigger-level analysis in event rate and byte rate; changing fill strategy. |

ATLAS paper is CC BY 4.0. Retain all collaboration/author attributions for other figures; separate per-asset licenses have not been verified and these figures are not MIT-relicensed. Source PDFs stay in the internal archive. No experimental figures were redrawn from approximate values.

Additional teaching connections: pipeline storage versus event FIFO; tag-and-probe avoids requiring the tested trigger in its own denominator; menu OR overlaps invalidate naive rate addition; prescales differ from thresholds; retained conditions and selection provenance are needed for reproducible analysis. Introductory numerical rate and CPU examples are explicitly illustrative.

## Undergraduate rework (13 November 2026)

The deck was restructured for students meeting trigger and DAQ for the first time: six accelerator recap slides, the complete experiment, the first trigger (Geiger–Müller counters and coincidences), DAQ and dead time, triggering at the LHC. Advanced slides of the 7 November draft moved to the backup.

### New original schematics

Generated by `scripts/make_intro_figures.py` (run from the repository root with `.venv-pdf/bin/python`). Qualitative drawings, no measured data.

| Asset | Content / assumptions |
|---|---|
| `gm-tube.svg` | Side view of a Geiger–Müller tube: cathode wall, anode wire, end window, discharge along the whole wire, HV through a resistor, capacitive output. Voltage (+500 V) and output (≈1 V) are typical orders of magnitude. |
| `gas-regions.svg` | Textbook diagram of collected charge versus voltage (recombination, ionization chamber, proportional, limited proportional, Geiger–Müller, discharge), redrawn qualitatively after e.g. Knoll and Leo. Two curves differ by a factor 100 in primary ionization; numbers on the axis are schematic. |
| `coincidence.svg` | Two counters with an absorber (after Bothe and Kolhörster 1929) and a timing diagram of an AND gate. |
| `cloud-trigger.svg` | Counter-controlled cloud chamber after Blackett and Occhialini (1933): counters above and below, coincidence fires the expansion, lamp and camera. |
| `discriminator.svg` | Three pulses of the same shape (amplitudes 420, 120, 700 mV; Gaussian noise σ=8 mV, seed 3), a 200 mV threshold and the logic output. |
| `rate-funnel.svg` | Round numbers: 10⁹ pp collisions/s at 10³⁴ cm⁻²s⁻¹, 4×10⁷ crossings/s, 10⁵/s after Level-1 (≈2.5 µs latency), 10³/s after the HLT, Higgs production ≈ 0.5/s. ATLAS/CMS Run-2 orders of magnitude. |

### Figures copied from Lecture 8

`srf-cavity.jpg` (Z22, CC BY-SA 4.0, Wikimedia Commons), `magnet-fields.svg`, `fixed-target-collider.svg`, `rf-phase-stability.svg` (original Lecture 8 models). See `../Lecture_8/SOURCES.md` for their provenance.

### Historical sources (not linked in the deck)

H. Geiger, W. Müller, Naturwiss. 16 (1928) 617; W. Bothe, W. Kolhörster, Z. Phys. 56 (1929) 751; B. Rossi, Nature 125 (1930) 636; P. M. S. Blackett, G. P. S. Occhialini, Proc. R. Soc. A 139 (1933) 699.

All Matplotlib SVGs now name Helvetica/Arial instead of DejaVu Sans, so browsers no longer fall back to a serif font.

## DAQ storyline after Neufeld (13 November 2026)

Sections 2–4 follow the storyline of N. Neufeld, *Introduction to Trigger / Data Acquisition / Data Analysis*, ESI 2009 (local copy `reference/lecture-notes/originals/neufeld-daq-2009.pdf`): Tycho Brahe as the first systematic DAQ (pp. 6–11), the trivial DAQ with trigger, busy logic and FIFO (pp. 16–20), one to many sensors (pp. 23–29), LHC challenges and the two-level trigger (pp. 49–55). Text is paraphrased; diagrams are redrawn.

| Asset | Source / assumptions |
|---|---|
| `tycho-portrait.jpg` | Embedded image on Neufeld p. 6 (240×339 px), extracted with `pdfimages`. 16th-century portrait of Tycho Brahe, public domain as an artwork; the photograph's source is not stated by Neufeld. |
| `vme-crate.jpg` | Embedded photo on Neufeld p. 29, extracted with `pdfimages`. Original photographer not stated; no reuse license verified. Retain Neufeld attribution; not MIT-relicensed. |
| `daq-step-a/b/c.svg` | Redrawn after Neufeld pp. 17–19: sensor, delay, ADC, (FIFO), processing, storage; discriminator; busy flag / FIFO-full gate. Generated by `scripts/make_daq_figures.py`. |
| `crossings-in-flight.svg` | Quarter view of an ATLAS-sized detector (half length 23 m, half height 12.5 m; calorimeters to 4.25 m × 6.5 m, tracker 1.1 m × 3.5 m, approximate), arcs at c × 25, 50, 75 ns. Idea after Neufeld p. 51. |
| `pipeline-belt.svg` | 100 memory cells = 2.5 µs / 25 ns; schematic. |
| `lhc-chain.svg` | Two-level chain after Neufeld p. 52, round ATLAS/CMS Run-2 numbers (40 MHz, 100 kHz, ~1 kHz, ~500 event fragments). |
| `daq-history.svg` | Orders of magnitude: Tycho ~100 B/h (Neufeld p. 8), 4 B/s thermometer, ~1 GB/s to disk, ~5 TB/s LHCb Run-3 readout (Starterkit diagram), 40 MHz × 1 MB. |
| `turn-on-toy.svg` | 25 GeV cut on p_T smeared by a Gaussian of 8% or 20% of p_T; plateau 0.95. |

Historical facts for the Tycho slides (Hven/Uraniborg 1576–1597, 1563 conjunction, ~2′ precision, Kepler's 8′ discrepancy, Astronomia Nova 1609) are standard history-of-astronomy statements, not taken from a single source; check before publication.

## Full detector and calorimeter trigger (13 November 2026)

| Asset | Source / assumptions |
|---|---|
| `detector-slice.svg` | Original quarter r-φ slice redrawn after Neufeld p. 54 (a CMS illustration there): tracker, EM and hadron calorimeters, three muon stations; γ, e, μ, π±, n, ν; arrows to calorimeter and muon triggers, tracker to pipeline. Schematic radii. |
| `calo-trigger-toy.svg` | Toy 8×8 cell energies (fixed array in `make_daq_figures.py`, 0–0.6 GeV noise plus a shower 2.9/1.6/1.2/0.7 GeV); all overlapping 2×2 sums; 4 GeV threshold. |

The exercise grid on "Your turn: be the trigger" is hand-made: largest 2×2 sum 6.0 GeV (rows 2–3, columns 2–3); sums around the 3.6 GeV cell are 4.7, 4.7, 4.6, 4.3 GeV. LHCb Level-0 numbers (≈6000 ECAL / 1500 HCAL cells, 2×2 clusters, ≤1 MHz, 4 µs) are rounded from memory of the LHCb trigger papers, e.g. JINST 8 P04022 (2013); check before publication.

`xsec-ladder.svg` (Recap 6, `make_intro_figures.py`): rounded 13 TeV cross sections — inelastic 80 mb, bb̄ 0.5 mb, W→ℓν 20 nb and Z→ℓℓ 2 nb per lepton flavour, tt̄ 830 pb, Higgs 55 pb — times 10³⁴ cm⁻²s⁻¹. Replaces the busier Lecture 4 figure.

## Publication (13 November 2026)

Licences were checked before publication; see `THIRD_PARTY.md` (Lecture 9). ATLAS (arXiv:2007.12539) and CMS (arXiv:2410.17038) papers are CC BY 4.0, the LHCb Starterkit is CC BY 4.0, ACTS is MPL 2.0, and the Tycho portrait is a public-domain artwork. `cms-run2-pileup.png`, `stirling-cross-sections.png`, `vme-crate.jpg` and the unused `neufeld-readout-chain.png` have no confirmed open licence: they live in the git-ignored `figures/local/` folder and the public deck shows a placeholder (`.local-photo`, as in Lecture 8).

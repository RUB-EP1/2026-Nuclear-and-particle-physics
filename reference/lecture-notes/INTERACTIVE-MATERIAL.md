# Interactive material: implementation briefs

Status: specifications only; no widgets have been built in this task. All proposed stochastic examples use synthetic data unless explicitly replaced by a documented public dataset. Source assets and their provenance are in [SOURCES.md](SOURCES.md) and [FIGURES.md](FIGURES.md).

| Priority | Model and controls | Observable / learning check | Sources and limits |
|---|---|---|---|
| Next lecture 1 | Dead time / queue: arrival rate, fixed service time, capacity, burst mode, reproducible random seed | Occupancy timeline, accepted/lost counts, output rate; a buffer smooths bursts but cannot cure sustained overload | L08 p10; Neufeld pp16–20. Separate non-paralyzable dead-time model from queue model. State whether capacity includes event in service. |
| Next lecture 2 | Threshold selection: signal/background rates, threshold, event size, bandwidth ceiling | Efficiency, background acceptance, purity, output bandwidth, selected spectra | L08 pp9–13. Use labelled analytic toy distributions. Keep samples fixed when adjusting cuts. |
| Following lecture | Track fitting: hit precision, field strength, momentum, material/scattering, outliers | Hit association, fitted curvature and uncertainty; compare a measurement error with a scattering kick | L08 pp16–18, ACTS originals. Start in 2D; label projection and toy material model. |
| Following lecture | PID comparison: momentum, flight length, time resolution, refractive index, angular resolution | TOF separation and Cherenkov thresholds; compare hypotheses | L07 pp13–16 and L09 pp9–12. Independent Gaussian responses are a toy approximation; no claimed experimental efficiency. |
| Analysis lecture | Mass peak: sample size, resolution, background level, fitted peak position | Histogram, likelihood curve and interval; repeat synthetic experiments to inspect coverage | L09 pp20–23; PDG statistics and LHCb mass paper. Separate detector resolution from uncertainty on the mean. |
| Optional recap | Calorimeter resolution: stochastic, constant and noise coefficients | Terms versus energy; crossover and relative vs absolute resolution | L07 p9. Dimensionless energy convention stated in note. |

## Minimal numerical checks when implemented

- Queue: conservation of arrived = dropped + completed + queued/in-service. Zero arrivals produces zero output. In non-paralyzable mode compare the long-run rate with $R/(1+R\tau)$. In buffered mode verify deterministic arrival/service cases separately.
- Trigger: thresholds outside the sample range accept all/none. Compute purity from selected signal / all selected, not from signal efficiency. Display undefined purity when no event survives.
- TOF/RICH: no real Cherenkov angle below threshold; $t\to L/c$ at high momentum; increasing flight length increases time separation.
- Track: turn off measurement noise/material to recover the generating trajectory within numerical precision; increasing measurement errors broadens uncertainties.
- Likelihood: known-width Gaussian MLE reproduces the sample mean and $\sigma/\sqrt{N}$ uncertainty. Coverage check samples intervals around a fixed true parameter, not future estimates around today's interval.

## Integration conventions

Follow the existing Quarto/Reveal lecture widgets: offline assets, visible model assumptions, reset control and deterministic poster state; provide a static figure for PDF export. Keep original-source identifiers in captions and presenter notes. Existing Lecture 6 TPC and Cherenkov widgets can provide recap visuals; inspect their documented assumptions before extending them. No raw experimental event data were recovered from the slide images in this task.

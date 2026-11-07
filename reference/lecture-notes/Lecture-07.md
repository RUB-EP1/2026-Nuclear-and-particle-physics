# Lecture 7: calorimeters and particle identification

Mikhail Mikhasenko, 11 November 2025. [Source PDF](../Lecture-07.pdf) · [Page-by-page transcription and previews](Lecture-07-transcript.md) · [Sources](SOURCES.md).

This is last year's source deck, not a newly published 2026 lecture. The current Lecture 6 already covers interaction mechanisms, electromagnetic/hadronic showers, Cherenkov emission and historical detectors. Use these as a short recap; the new learning is how a detector converts them into energy and particle-type measurements.

## Calorimetry (pages 2–11)

A calorimeter absorbs energy and converts part of it into measurable ionization or light. It measures both charged particles and neutral particles such as photons and neutrons. A linear calibrated response means signal is proportional to deposited energy; leakage, invisible energy and non-compensation complicate the relation to incident energy.

- **Pages 3–6: shower foundations.** Electrons radiate bremsstrahlung photons; photons produce electron–positron pairs. Multiplication competes with ionization losses near the critical energy. Hadronic showers include nuclear interactions, electromagnetic subshowers and nuclear breakup. Distinguish radiation length $X_0$ from nuclear interaction length $\lambda_I$.
- **Page 4: radiation length.** In the high-energy radiative approximation, $-dE/dx=E/X_0$, so $E(x)=E_0e^{-x/X_0}$. This describes a mean radiative loss, not an exact single-particle trajectory. The approximate material formula on the slide should be replaced by a verified PDG value rather than retyped from the problematic expression.
- **Page 7: construction.** In a homogeneous calorimeter the absorber is also active. In a sampling calorimeter, dense passive absorber alternates with active layers; only a fraction of the deposited energy is measured directly.
- **Page 8: signal chain.** Energy deposit → scintillation/ionization → light or charge collection → electronics. This is the natural bridge to next year's DAQ material.
- **Page 9: resolution.** With $e=E/(1\,\mathrm{GeV})$, write

$$\frac{\sigma_E}{E}=\sqrt{\frac{a^2}{e}+b^2+\frac{c^2}{e^2}}.$$

Here $a$ is the stochastic coefficient, $b$ the constant term and $c$ a noise coefficient under this unit convention. Independent contributions add in quadrature, not linearly. Their values depend on detector and particle type; the slide's coefficient ranges are not universal.

- **Page 10: LHCb example.** Shashlik sampling calorimetry illustrates absorber/active layers and light collection. The displayed resolution expressions appear to put an energy denominator under the second term; verify against the cited detector paper before using numerical coefficients. Use the general resolution formula above in the meantime.
- **Page 11: upgrade example.** Fibre-based SpaCal/PicoCal concept; treat its performance numbers as design targets tied to a particular source/version, not measurements of an installed system.

## Particle identification (pages 12–19)

**Time of flight, page 13.** Combine path length $L$, momentum $p$ and measured flight time $t$. With masses in GeV/$c^2$, momenta in GeV/$c$, and $c$ retained in the flight-time factor,

$$t(p,m)=\frac{L}{c}\sqrt{1+(mc/p)^2},\qquad
m^2=\frac{p^2}{c^2}\left[(ct/L)^2-1\right].$$

At high momentum the difference between species decreases approximately as $1/p^2$. The slide suggests a 5 m GlueX example. For a toy $\pi/K$ comparison at 2 GeV/$c$, $L=5$ m gives about 0.46 ns separation; timing, path-length and momentum uncertainties all matter.

**Cherenkov/RICH, pages 14–16.** Radiation requires $\beta n>1$ and

$$\cos\theta_C=\frac{1}{n\beta},\qquad p_{\rm th}=\frac{mc}{\sqrt{n^2-1}}.$$

Mirrors focus photons into rings. A measured angle plus track momentum distinguishes particle hypotheses. The band plot on page 16 is a measured detector-performance example; its source is INSPIRE record 1775496. The ring display and optical geometry on page 15 lack explicit individual attribution in the PDF.

**Pages 17–18: applications.** Reactor glow and water-Cherenkov neutrino detection. Do not infer radiation dose from a photograph; the unfinished dose prompt on page 17 has no sufficient data. Retain Super-Kamiokande as an application or optional closing example.

**Transition radiation, page 19.** Radiation arises at dielectric interfaces. At the same momentum electrons have much greater Lorentz factor than pions, enabling electron/hadron discrimination. Yield depends on radiator and photon-energy band; avoid presenting a globally linear dependence on $\gamma$.

## Optional examples (pages 20–21)

CERN-to-Gran-Sasso beam timing and OPERA detector components: emulsion bricks, target tracker and muon spectrometer. Useful for a later neutrino lecture; not essential to the calorimetry/PID learning objectives.

## Suggested interactive reuse

1. Resolution explorer: vary $a,b,c$ and display each term versus energy; distinguish relative and absolute resolution.
2. TOF explorer: vary momentum, path length and timing resolution; plot arrival-time distributions for $\pi,K,p$.
3. RICH explorer: vary refractive index and momentum; show thresholds and overlapping angle distributions, not only ideal rings.

These are proposed new teaching models, not digitizations of experimental data. [Implementation briefs](INTERACTIVE-MATERIAL.md).

# Lecture 9: reconstruction, particle identification and data analysis

Marian Stahl, WS 2025/26; 23 pages. [Source PDF](../Lecture-09.pdf) · [Full transcription with previews](Lecture-09-transcript.md) · [Sources](SOURCES.md).

## Tracking, alignment and calibration (pages 2–7)

Page 2 recalls the whole measurement chain. Pages 3–5 reprise Lecture 8 tracking, parameterization and Kalman fitting. Use one recap rather than duplicate explanations.

Alignment determines where detector elements actually sit. Mechanical surveys constrain positions; reconstructed tracks constrain residual misalignments. Calibration converts electronic signals into physical observables. Both affect final physics measurements.

A rigid detector element has three translation and three rotation degrees of freedom before constraints. Page 7's “3 alignment constants for translation and rotation” is ambiguous: teach six geometric parameters, distinguish constrained/unobservable global modes, and explain that the fit may use fewer independent degrees of freedom. Track fitting and alignment are coupled; weak modes can bias momentum without obvious residuals.

## Reconstructing particle identity (pages 8–16)

| Method | Measured information | Main limitation / reconstruction issue | Source pages |
|---|---|---|---|
| Time of flight | Arrival time, path length, momentum | Species converge as momentum grows; time-zero and path calibration | 9 |
| Ionization loss | Repeated charge measurements along a track | Long energy-loss tails; use a truncated mean, with detector-dependent truncation | 10 |
| RICH | Photon pattern conditional on track and mass hypothesis | Overlapping rings, backgrounds, optics/calibration | 11–12 |
| Transition radiation | X-ray-associated charge or pulse shape | Radiator response and $\gamma$ dependence; electron/hadron separation | 13 |
| Calorimetry | Cluster energy, shape, track matching | Leakage, overlapping clusters, bremsstrahlung recovery | 14 |
| Muon system | Penetration and compatible downstream hits | Hadron punch-through, random matches, scattering in absorbers | 15 |
| Combined PID | Likelihoods or classifier outputs from several systems | Correlations, simulation mismodelling, calibration data | 16 |

For TOF use $\beta=L/(ct)$ and $m^2=(p^2/c^2)(\beta^{-2}-1)$. For RICH compare photon-pattern likelihoods for competing mass hypotheses, e.g. $\Delta\log L=\log L_K-\log L_\pi$. A positive difference favours one hypothesis relative to another; it is not itself a calibrated probability.

Page 12 uses LHCb-FIGURE-2025-016, **charmless $B\to hh'$ mass distributions in 2024 data**. These demonstrate the effect of hadron PID on selected mass spectra; they are not standalone PID-efficiency curves. The upstream record is identified; direct retrieval currently returns a bot-protection page. The embedded slide figures remain available locally.

For the residual-based muon matching statistic on page 15, write

$$\chi^2=\boldsymbol\delta^T C^{-1}\boldsymbol\delta.$$

If using separate $x,y$ terms, explain the assumed block structure. The source writes matrices $V$ without inverse signs: this is valid only if $V$ denotes a weight/inverse covariance, not the covariance itself.

The claim on page 16 that modern experiments have “at least” a given detector combination is too universal. Detector choices depend on the physics program and geometry.

## Simulation (pages 17–18)

Generation → particle transport through geometry/material → detector response and digitization → the same reconstruction/selection chain as data. Add noise and spillover at the appropriate response stage. Simulation truth enables efficiency and resolution studies, but agreement must be checked with data. Distinguish generated particles, deposited energy, digitized signals and reconstructed objects.

## Statistical inference (pages 19–23)

**Probability models, page 20.** For a continuous observable, $P(a<X<b)=\int_a^b f(x\mid\theta)dx$, with $f\geq0$ and $\int f\,dx=1$. A density has inverse-observable units; its value is not a point probability. For counts, probabilities sum to one.

**Gaussian distribution, page 21.**

$$f(x\mid\mu,\sigma)=\frac{1}{\sqrt{2\pi}\sigma}\exp\left[-\frac{(x-\mu)^2}{2\sigma^2}\right].$$

The central limit theorem applies to suitably normalized sums/means under conditions; it does not make every detector observable Gaussian. A central Gaussian interval $\mu\pm\sigma$ contains approximately 68.27%. A one-sided Gaussian tail at $Z=5$ is about $2.87\times10^{-7}$. A p-value is not the probability that a hypothesis is true; mapping a p-value to $Z$ is a convention, not a consequence of the CLT alone.

**Mass measurement, page 22.** A fitted invariant-mass spectrum yields an estimate and uncertainties. The cited publication is LHCb, PRD 99, 052006 (2019). The prose on the slide transposes digits (5769.7); the cited mass is **5796.70 MeV/$c^2$**, with statistical, systematic and reference-mass uncertainties kept separate. Verify numerical use against the original paper.

A frequentist 68.3% confidence procedure produces intervals covering the fixed true parameter in 68.3% of repeated experiments. It does **not** say that 68.3% of future point estimates fall within the particular interval already observed. A Bayesian credible interval has a posterior probability conditional on model, prior and data; do not silently identify the two intervals.

**Likelihood, page 23.** For independent observations,

$$L(\theta)=\prod_{i=1}^{n}f(x_i\mid\theta),\qquad \hat\theta=\arg\max_\theta\log L(\theta).$$

This is a function of parameters at fixed data; it is not generally normalized over parameters. A shape-only likelihood conditions on sample size. To measure yields, use an appropriate count/extended likelihood.

Under regularity and large-sample conditions, MLEs are consistent and asymptotically efficient; finite-sample bias is possible. The covariance approximation is the inverse Hessian of the **negative** log likelihood at the minimum. For one profiled parameter, $\Delta(-\log L)=1/2$ (equivalently $-2\Delta\log L=1$) gives an approximate 68% interval under the usual asymptotic conditions. Boundaries, low counts and non-Gaussian likelihoods require care.

## Scope and follow-up

This deck introduces inference, but does not constitute a full analysis course. Poisson counting, background modelling, efficiency corrections, systematic nuisance parameters and goodness-of-fit are useful additions, explicitly labelled as new material. A separate reconstruction/PID lecture followed by a statistics lecture is more teachable than compressing all 23 pages into the DAQ session.

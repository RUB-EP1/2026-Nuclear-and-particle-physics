# Lecture 8: DAQ, trigger and reconstruction

Marian Stahl, WS 2025/26; 19 pages. [Source PDF](../Lecture-08.pdf) · [Full transcription with previews](Lecture-08-transcript.md) · [Sources](SOURCES.md).

## Why a detector is not yet a measurement (pages 2–6)

Page 2 recalls RICH particle identification. Pages 3–4 connect detector hardware to a physics publication: front-end signals → DAQ and trigger → reconstructed particles → statistical inference → comparison with theory. The arrow back to theory is the purpose of the chain.

Pages 5–6 give accelerator history and FCC context. Keep these optional: their numerical comparisons and planning times are historical illustrations, not a current status report. The pipeline diagram is a stronger opening for this lecture than a long accelerator digression.

## Acquiring data (pages 7–8)

The front end amplifies/shapes and digitizes signals. Readout transfers channel data; event building combines fragments belonging to the same event; logging writes data; slow control handles configuration and monitoring.

The simplest design repeatedly reads a detector with a CPU and writes to disk. It immediately raises questions about conversion time, transfer time, asynchronous arrivals and sustained bandwidth. A useful teaching relation is

$$B=R\,S,$$

where $R$ is event rate and $S$ mean stored event size. For an explicitly illustrative $R=40$ MHz and $S=1$ MB, $B=40$ TB/s in decimal units. Bunch crossings, interactions and recorded events are different counts; never silently equate them.

## Trigger decisions, dead time and buffering (pages 9–10)

A trigger makes an early decision about which information to keep. The selection must fit available readout, compute and storage while retaining the physics signals of interest. The cross-section plot motivates the rarity of some processes; it is not a trigger-efficiency measurement.

Dead-time fraction is time unable to accept an event divided by elapsed time. A buffer absorbs bursts and decouples processing stages, but cannot solve a sustained input rate above service capacity. Buffer-full losses and ADC-busy losses are separate mechanisms; the wording on page 10 should not imply that a non-full buffer itself makes the DAQ busy.

For an added teaching model with Poisson arrivals and fixed non-paralyzable dead time $\tau$,

$$r=\frac{R}{1+R\tau},\qquad f_{\rm dead}=\frac{R\tau}{1+R\tau}.$$

This formula is not a general finite-buffer queue model and is not stated in the source slides. For queues, specify service time, buffer capacity, arrival process and drop policy separately.

## Real systems (pages 11–13)

- **ATLAS Run 2, page 11:** hardware Level-1, buffered readout and software high-level trigger; subsequent storage, distribution and offline reconstruction. Keep the Run-2 label. The original publication is *Operation of the ATLAS trigger system in Run 2*, JINST 15 P10004, arXiv:2007.12539.
- **LHCb Run 3, page 12:** full detector readout followed by a GPU first software stage and an asynchronous CPU second stage. “No hardware trigger” means no hardware physics-selection level of the former L0 type; timing, readout electronics and protective controls still exist. Reducing the stored event representation can be as important as rejecting events. The diagram has no explicit source link in the supplied slide; preserve that attribution gap.
- **Page 13:** optimize the whole chain, not only one fast algorithm. Lost raw information cannot be recovered later. Trigger choices shape the dataset and must enter efficiency estimates.

## Turning hits into particles (pages 14–19)

**Raw data, page 15.** Encoded channel identifiers and signals are translated into measurements. Geometry and alignment connect local sensor coordinates to global positions. An event display is a reconstruction product, not the raw data.

**Tracking, page 16.** Find candidate seeds, extend them across layers, fit tracks and resolve competing hit assignments. Occupancy creates a combinatorial problem. The slide lists doublets/triplets, Hough transforms, cellular automata and graph/ML methods; introduce the task before surveying algorithms.

**Track parameters, page 17.** Example state $\mathbf{x}=(d_0,z_0,\phi_0,\theta,q/p)^T$ plus a covariance matrix. The parameters refer to a surface/reference convention; they are not five independent Cartesian position/momentum components. Timing can add another parameter.

**Track fitting, page 18.** Predict the next state, update with a measurement, and smooth using information from the whole track. Propagate measurement errors and process noise from material effects. A useful conceptual equation is

$$P^-_k=F_kP_{k-1}F_k^T+Q_k.$$

A scattering kick broadens the prediction uncertainty; it should not be treated as a badly measured hit. A full matrix derivation belongs in an advanced follow-up.

**Vertexing, page 19.** Cluster compatible tracks to identify primary vertices; reconstruct secondary vertices for displaced decays. Fit using track uncertainties, then optionally apply decay-chain kinematic constraints. Distinguish impact parameter, flight distance and their significances.

## Teaching boundary

DAQ/trigger pages 7–13 make a coherent lecture core. Tracking pages 14–19 are a bridge or the start of the following lecture. Lecture 9 pages 3–5 repeat pages 16–18 almost directly; do not teach both versions in full.

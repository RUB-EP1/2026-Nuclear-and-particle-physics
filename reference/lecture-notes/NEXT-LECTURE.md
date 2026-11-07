# Next lecture: from detector signals to recorded events

Planning basis: lecturer confirmed on 7 November 2026 that Lecture 7 calorimetry/PID is covered. Assume a 90-minute slot; adjust using the 60-minute variant below. This is a proposed scope, not a scheduled event or finished slide deck.

## Central question

**We can detect a particle. How do we decide what to read out, process and keep?**

Use one event throughout: charged tracks and calorimeter signals appear, front ends digitize them, event fragments arrive, a trigger makes a decision, and a recorded event becomes the input to reconstruction. The students should leave able to explain why a trigger is part of the measurement, not just a computing convenience.

## Outcomes

Students should be able to:

1. Distinguish digitization, readout, event building, trigger, storage and reconstruction.
2. Estimate bandwidth from event rate and event size with correct units.
3. Explain dead time, latency, buffering and sustained throughput, and why they differ.
4. Describe the tradeoff between signal efficiency and accepted event rate.
5. Compare a hardware-plus-software trigger with a fully software physics trigger at a conceptual level.
6. Explain how the selection changes the recorded sample and why efficiency matters downstream.

## 90-minute teaching sequence

| Minutes | Topic and classroom activity | Material |
|---|---|---|
| 0–7 | Recall: a particle has made charge/light. Ask what the computer actually receives. Show the measurement chain. | L07 p8; L08 p4, p15 |
| 7–20 | Front end, ADC, channel data, event identifiers, event building and storage. Draw one small detector with three fragments per event. | L08 pp7–8; Neufeld source pp16–19 |
| 20–30 | Bandwidth estimate: 40 MHz × 1 MB = 40 TB/s. Compare 1 kHz × 1 MB = 1 GB/s. Explicitly label these as toy numbers, not one experiment's current specification. | L08 p9 |
| 30–47 | Dead time and finite buffers. Predict losses before running a queue demo; compare a burst with persistent overload. Distinguish latency from throughput. | L08 p10; new queue model |
| 47–52 | Short pause / check: can a larger buffer fix an input rate above output capacity forever? | Answer: no |
| 52–67 | Trigger as a physics selection. Move an energy or momentum threshold; track accepted rate, signal efficiency and composition. Show why a small output rate alone is not success. | L08 pp9,13; new threshold toy |
| 67–79 | Two architectures: ATLAS Run 2 versus LHCb Run 3. Follow one event through each; emphasize stages, buffering and what is saved. | L08 pp11–12; original ATLAS Fig. 1 |
| 79–86 | Bridge to reconstruction: encoded hits → track candidates → fitted particles. Show ACTS diagram; no five-parameter/Kalman derivation yet. | L08 pp15–16 |
| 86–90 | Exit questions and next-lecture preview. | Below |

Suggested title sequence: Why not save everything? → What is an event? → Digitization → Event building → Rate × size → Busy detector → Buffer → Trigger decision → Physics bias → ATLAS → LHCb → Hits to tracks → Summary.

## What to defer

- Accelerator timeline and FCC map (L08 pp5–6): optional context, not needed for the data-flow argument.
- Detailed track parameterization, matrix Kalman equations and vertex fits (L08 pp17–19): next lecture.
- Repeated tracking introduction in L09 pp3–5: merge into one treatment later.
- Full PID reconstruction, alignment and simulation: next reconstruction lecture.
- PDFs, likelihood fits, confidence intervals and significance: a subsequent analysis lecture. Do not rush these into the end of DAQ.

## Two interactive priorities

**1. Event queue.** Controls: arrival rate, conversion time, processing time, buffer depth and burst mode. Display accepted/dropped events, occupancy, busy fraction and output rate. Offer separate non-paralyzable dead-time and buffered-queue modes so their assumptions are visible. A fixed random seed permits comparisons. Prediction: increasing the buffer helps bursts, but not indefinitely when average arrivals exceed service capacity.

**2. Trigger threshold.** Show labelled toy signal/background distributions and vary a threshold under a bandwidth budget. Display signal efficiency, background acceptance, output rate and sample composition. Keep generated events fixed while moving the threshold. Prediction: tightening a threshold reduces load but changes physics acceptance.

Use original diagrams as source/reference panels; build the interactive models from explicit equations and synthetic samples. Do not animate a measured curve as though it provided event-level data. Detailed specifications are in [INTERACTIVE-MATERIAL.md](INTERACTIVE-MATERIAL.md).

## Exit questions / homework

1. An experiment records 5 kHz with mean event size 200 kB. What is the storage bandwidth? **1 GB/s**, decimal units, before overhead/compression effects.
2. Mean arrival rate is 12 kHz and service capacity is 10 kHz. Can any finite buffer guarantee loss-free operation indefinitely? **No.**
3. Does low trigger acceptance imply high signal purity? **No; relative signal/background efficiencies and prior rates matter.**
4. Why must a measured cross section account for trigger efficiency? **The recorded sample is selected, not an unbiased copy of all produced events.**
5. Optional homework: propose a trigger for an energetic muon signal, then name a physics process it could systematically miss. State the efficiency variable you would measure.

## 60-minute variant

Recall 5 min; DAQ chain 10; bandwidth 8; dead time/buffers 14; trigger threshold 12; architecture comparison 7; exit questions 4. Omit the reconstruction bridge and leave it as the next lecture's opener.

## Follow-on sequence

- **Following lecture:** hits → tracks → vertices → reconstructed PID; alignment/calibration and simulation as the supporting chain. Base on L08 pp14–19 and L09 pp6–18, avoiding repeated tracking slides.
- **Then:** reconstructed observable → probability model → likelihood → uncertainty; one invariant-mass example. Base on L09 pp19–23, with corrected interval interpretation and explicit count/shape distinctions.

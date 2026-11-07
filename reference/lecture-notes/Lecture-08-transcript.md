# Lecture 08: page-by-page source extraction

Source: [original PDF](../Lecture-08.pdf). Mechanical text extraction; equations and image-only text may be incomplete. Page previews are authoritative for layout. See the edited lecture notes for corrected formulas.

## Page 1

[Slide preview](pages/L08-01.jpg)

```text
Introduction to Nuclear and Particle Physics

Week 4: DAQ - Trigger - Reconstruction and Data Analysis      Marian Stahl
```

## Page 2

[Slide preview](pages/L08-02.jpg)

```text
Ring Imaging Cherenkov detectors (RICH)




                                                                  Kolanoski , Wermes, Teilchendetektoren
                                                                  book (german), Open Access through RUB




2 Recap   Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://link.springer.com/book/10.1007/978-3-662-45350-6

## Page 3

[Slide preview](pages/L08-03.jpg)

```text
?




3 Motivation   Introduction to Nuclear and Particle Physics WS 25/26
```

## Page 4

[Slide preview](pages/L08-04.jpg)

```text
Detector                                             DAQ (data-acquisition) & Trigger




                                                               JINST 3 S08004 (CMS)



                     NIM A 666, 147
                                        Data analysis / publications                            Belle II event display




                                                                                                                             Event
    Model / Theory




                                                                                                                         Reconstruction
                                                       PLB 716, 1




4 Motivation   Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://doi.org/10.1016/j.nima.2011.03.009

- https://iopscience.iop.org/article/10.1088/1748-0221/3/08/S08004

- https://display.belle2.org/#/event-display

- https://doi.org/10.1016/j.physletb.2012.08.020

## Page 5

[Slide preview](pages/L08-05.jpg)

```text
Timeline of Accelerators at the Energy-frontier
  Time horizons in HEP grow bigger. So do accelerators, detectors, collaborations…
  ACO: ~22 m circumference, ~10^4 detector readout channels, ~30 collaborators, ~3 yr construction time
  SPS: ~7 km circumference, ~10^5 detector readout channels, ~200 collaborators, ~6 yr construction time
  LHC: ~27 km circumference, ~10^9 detector readout channels, ~15k collaborators, ~14 yr construction time




                                                                                                Rev Mod Phys 93 015006




5 Motivation    Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- http://dx.doi.org/10.1103/RevModPhys.93.015006

## Page 6

[Slide preview](pages/L08-06.jpg)

```text
FCC




                                                                       CDS link




6 Motivation   Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://cds.cern.ch/record/2929353

## Page 7

[Slide preview](pages/L08-07.jpg)

```text
DAQ & Trigger systems (TDAQ)




                                                                 Grupen, Shwartz,
                                                                 Particle Detectors,
                                                                 Chapter 13




7 TDAQ   Introduction to Nuclear and Particle Physics WS 25/26
```

## Page 8

[Slide preview](pages/L08-08.jpg)

```text
DAQ
Trivial DAQ system:

  ●      Analog to Digital Conversion (digitisation, “frontend”)
  ●      CPU: periodic readout and processing
  ●      Store processed data to disk
  ●      Scaling? Limitations?

Tasks in general:

  ●      Gather data from detector frontends
         (Readout network)
  ●      Form complete events (Event Building)                                                                 slide by N. Neufeld


  ●      Store event data (Data logging)
  ●      Provide control, configuration and                         LHC experiments: ~100 million detector channels
         monitoring facilities (Slow control)


8 TDAQ           Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://indico.cern.ch/event/43007/contributions/1065030/attachments/927884/1313738/trigger-daq-analysis-esi09-neufeld1.pdf

## Page 9

[Slide preview](pages/L08-09.jpg)

```text
Trigger motivation
LHC with a trivial DAQ system:

  ●      LHC experiments deliver up to ~40 TB/s
  ●      Not every collision is worth saving




   Global Instantaneous Internet traffic
   ~150 TB/s in 2022




                 link

                                                                       arXiv:2011.01638




9 TDAQ         Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://wdr2021.worldbank.org/stories/crossing-borders/

- https://arxiv.org/abs/2011.01638

## Page 10

[Slide preview](pages/L08-10.jpg)

```text
Adding a Trigger                                            slides by N. Neufeld




  Trigger selects events for            Dead time: ratio between                 Buffers de-randomize data
  processing based on                   DAQ busy and total time
                                                                                 DAQ busy during ADC
  (partial) data
                                        “Something interesting”                  conversion time and buffer
  What happens when ADC                 happens randomly at                      not full
  busy?                                 experiments (given time between
                                        collisions < time for DAQ to process 1   Adapt buffer size to dead
                                        event)                                   time


10 TDAQ      Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://indico.cern.ch/event/43007/contributions/1065030/attachments/927884/1313738/trigger-daq-analysis-esi09-neufeld1.pdf

## Page 11

[Slide preview](pages/L08-11.jpg)

```text
Example: ATLAS in LHC Run 2                JINST 15 P10004




  Hardware-based L1 trigger

  Read-Out System acts as Buffer

  Software-based High Level Trigger

  Tier-0 will distribute data to “the
  grid” (WLCG Worldwide LHC Computing Grid)

  Reconstruction and analysis offline




11 TDAQ        Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- http://dx.doi.org/10.1088/1748-0221/15/10/P10004

## Page 12

[Slide preview](pages/L08-12.jpg)

```text
Example: LHCb in Run 3
  No Hardware trigger

  2 software trigger stages:
  1st on GPU, 2nd on CPU (asynchronous)

  Beauty and charm: MHz rate @ LHC

  Too much signal: reduce event size

  Reconstruction Online -- No margin
  for error

  Trigger (mostly) written by analysts




12 TDAQ     Introduction to Nuclear and Particle Physics WS 25/26
```

## Page 13

[Slide preview](pages/L08-13.jpg)

```text
Recap Trigger and DAQ
  ●       DAQ has become a data-challenge at modern HEP experiments
           ○  How can we process several TB/s of data in real-time?
  ●       Optimisation problem with many variables
           ○  Frontend electronics
           ○  Which raw information to store
           ○  Network infrastructure and throughput
           ○  Buffer sizes
           ○  Processing power and complexity in Trigger
           ○  Limited offline storage (moving towards Exabyte storage)
           ○  …
  ●       Need to be smart enough to not remove events that could (dis)prove a future theory
           ○  Only one chance to record data




13 TDAQ          Introduction to Nuclear and Particle Physics WS 25/26
```

## Page 14

[Slide preview](pages/L08-14.jpg)

```text
Event reconstruction




                                                                            Frühwirth, Strandlie,
                                                                            Pattern Recognition,
                                                                            Tracking and Vertex
                                                                            Reconstruction in
                                                                            Particle Detectors,
                                                                            OpenAccess book




14 Reconstruction   Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://link.springer.com/book/10.1007/978-3-030-65771-0

## Page 15

[Slide preview](pages/L08-15.jpg)

```text
Raw data
 What you want:                                                         What you get:




                                                                              Raw data in encoded format to
                                                                              save storage space

                                                                              Usually detector hits/clusters in
                                                                              “local” coordinates (e.g. channel ID) can
                                                                              fit in 16 or 32 bit “word”
                                                                              16 bit is short int in C++


                                                                              Detector position in global frame
                                                                              → survey position + alignment
   ATLAS-PHOTO-2020-031-1


15 Reconstruction     Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://cds.cern.ch/images/ATLAS-PHOTO-2020-031-1

## Page 16

[Slide preview](pages/L08-16.jpg)

```text
Charged particle reconstruction (Tracking)
   Typical workflow:
                                                                            ACTS docs

   Build seed tracklets from hits
   Combinatorics is challenging
   Proximity in latent space→here: cluster in φ?
   Various algorithms on the market:
   Doublet/Triplet seeding, Hough transform, Cellular Automata,
   Graph-based/ML approaches or hybrids thereof


   Extend track to further layers / trackers
   Hugely dependent on detector layout
   Similar algorithms available as for seeding
    + Combinatorial Kalman Filter
   Track selection / pruning at last step



16 Reconstruction   Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://acts.readthedocs.io/en/latest/tracking.html

## Page 17

[Slide preview](pages/L08-17.jpg)

```text
Track parameterization
   At each point along its trajectory, a track is
   described by state-vector
   Usually 5D, with symmetric covariance matrix.                                                                     ACTS docs
   Time information can be added

   Global vs local, helical vs cylindrical or
   cartesian
   Detector layout: e.g. LHCb vs. ATLAS

   Example on the right: x = (d0,z0,ϕ0,θ,q/p)T
    Symbol                   Meaning                                                Notes

  d0           transverse impact parameter          Distance of closest approach (DCA) to beamline in the xy-plane
  z0           longitudinal impact parameter        z-coordinate at DCA
  ϕ0           azimuthal angle of momentum at DCA Defines direction in xy-plane
  θ            polar angle                          Related to pseudorapidity

  q/p          charge divided by momentum           Curvature in B field


17 Reconstruction    Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://acts.readthedocs.io/en/latest/tracking.html

## Page 18

[Slide preview](pages/L08-18.jpg)

```text
Track fitting
                                                                                                    CERN-THESIS-2005-040

   Track fitting handles:
   Measurement errors
   Multiple scattering and energy loss
   Outliers or missing hits

   Kalman filter
   State xk-1 measurement mk-1 at node k-1

   Measurements added node-by-node; Minimize
   χ2 of measurements on track in 3 steps:

     ●     Predict state in next node xkk-1 from filtered state xk-1 ; add noise Qk to covariance
     ●     Filter step adds information of measurement mk
     ●     Smoother gives best estimates of states at all previous nodes. Result is track χ2




18 Reconstruction   Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://repository.cern/records/8axnk-w9f84

## Page 19

[Slide preview](pages/L08-19.jpg)

```text
Vertexing
   Primary vertex finding (seeding)
   Points of closest approach of tracks to beamline                         slides K. Okubo

   Plot along beamline axis to find clusters/peaks

   Secondary vertices
   Part of selection algorithms (trigger or offline)
   Crucial variables for selection shown in plot

   Vertex fits
   Minimize sum of squared distances
   Take track covariances into account

   Kinematic fits
   Impose kinematic and geometric constraints to fit
   entire decay chains



19 Reconstruction   Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://indico.cern.ch/event/867266/contributions/4582191/attachments/2340945/3990883/ATHIC_ver5.pdf

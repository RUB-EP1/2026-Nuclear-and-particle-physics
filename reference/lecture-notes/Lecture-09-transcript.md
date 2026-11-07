# Lecture 09: page-by-page source extraction

Source: [original PDF](../Lecture-09.pdf). Mechanical text extraction; equations and image-only text may be incomplete. Page previews are authoritative for layout. See the edited lecture notes for corrected formulas.

## Page 1

[Slide preview](pages/L09-01.jpg)

```text
Introduction to Nuclear and Particle Physics

Lecture 9: Reconstruction II and Data Analysis                   Marian Stahl
```

## Page 2

[Slide preview](pages/L09-02.jpg)

```text
Recap
   We are doing high energy physics to probe the Standard Model (SM) of Particle physics
   Within the SM: e.g. understand emergent phenomena of the strong force
   Beyond the SM (BSM): e.g. Dark matter? Dark energy? Distinguish between direct and
   indirect searches for BSM physics

   Accelerators and Detectors: Need high rates for rare processes or
    higher precision measurements. Needs improved (higher granularity,
    faster response time, radiation hard etc.) detectors.
   Detectors need to measure:
   Event topology (Primary, secondary vertices)
   Kinematics (Momentum, Energy)
   Particle type (photon, electron, muon, pion, kaon, proton,...)                          NIM A 666, 147




   Established detector layout follows energy-loss of particles in material

   Detectors produce huge amounts of data that needs to be processed in real-time to not
    miss a rare event and to store necessary information of events of interest

2 Recap       Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://doi.org/10.1016/j.nima.2011.03.009

## Page 3

[Slide preview](pages/L09-03.jpg)

```text
Charged particle reconstruction (Tracking)
                                                                           ACTS docs

   Typical workflow:

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



3 Reconstruction   Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://acts.readthedocs.io/en/latest/tracking.html

## Page 4

[Slide preview](pages/L09-04.jpg)

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


4 Reconstruction     Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://acts.readthedocs.io/en/latest/tracking.html

## Page 5

[Slide preview](pages/L09-05.jpg)

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




5 Reconstruction   Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://repository.cern/records/8axnk-w9f84

## Page 6

[Slide preview](pages/L09-06.jpg)

```text
Alignment and calibration
   Want to find r,φ,z coordinate of a hit
   In a 28 m diameter detector
   With μm precision please!

   Optical monitoring (during shutdown)
   precise to ~10-100 μm
   Detector elements can move when
   switching Magnet on/off

   Internal and external alignment
   Within detector system
   With respect to other sub-detectors

   Group into sensible entities
   Which degrees of freedom?


6 Reconstruction   Introduction to Nuclear and Particle Physics WS 25/26
```

## Page 7

[Slide preview](pages/L09-07.jpg)

```text
Alignment and calibration
   3 alignment constants for translation and rotation
    relative to survey positions -- Not all are physical

   Insert alignment constants in track fit;
    iterate smoothing step with global covariance
    of all track states in an event [NIMA 600 471]
    or of selected events with kinematic constraints [NIMA 712 48]




7 Reconstruction   Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://www.sciencedirect.com/science/article/pii/S0168900208017567

- https://www.sciencedirect.com/science/article/pii/S0168900213001861

## Page 8

[Slide preview](pages/L09-08.jpg)

```text
Methods for particle identification (PID)
        Need to separate
        Electrons from hadrons -- Electromagnetic Calorimeter, Transition Radiation Detector
        Muons from other charged particles -- Muon detector
        Pions, kaons, protons, light nuclei (low momentum) -- Time of flight, dE/dX
        Pions, kaons, protons etc. (high momentum) -- Cherenkov

        Identify and measure energy
        Neutral particles (photon, K0L, neutron)




                                                                                       NIM A 666, 147


8 Reconstruction   Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://doi.org/10.1016/j.nima.2011.03.009

## Page 9

[Slide preview](pages/L09-09.jpg)

```text
Time of Flight reconstruction


  Separation for low momentum particles
                                                                     J. Phys. G 39 123001

  Special use-cases: LHCb with SMOG (gas target)
        LHCb-DP-2025-004
                                                                                            L~2.2 m




9 Reconstruction   Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://inspirehep.net/literature/2958467

- https://iopscience.iop.org/article/10.1088/0954-3899/39/12/123001

## Page 10

[Slide preview](pages/L09-10.jpg)

```text
Ionisation Energy loss (dE/dX)
 Measure charge signal in many layers (e.g. up to 159 in ALICE
 Time Projection Chamber)
 Apply Truncated mean to estimate specific loss

 Used in
 ALICE, Belle II -- (low p) global PID
 ATLAS, CMS -- searches for high p,
  highly ionizing (z>1) particles
 LHCb -- 3He identification




                                                                            Plots from Grupen
EPJP 131, 168


10 Reconstruction   Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://link.springer.com/article/10.1140/epjp/i2016-16168-5

## Page 11

[Slide preview](pages/L09-11.jpg)

```text
PID reconstruction with Cherenkov detectors
                                                                            slides C. Gotti


   Main purpose to separate pions, kaons and protons

   Typical state-of-the-art algorithm
   For each track state and type hypothesis, generate
   & trace Cherenkov photons and simulate their
   detector response.

   Start with pion hypothesis & compute global
   likelihood; change hypothesis iteratively.
   → Finally, compute likelihood differences for each
   particle

   Requires good modelling/calibration and is
   computationally heavy



11 Reconstruction   Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://indico.gsi.de/event/20387/contributions/90417/attachments/51821/79016/Conf_20250918_RICH2025_Upgrade2.pdf

## Page 12

[Slide preview](pages/L09-12.jpg)

```text
Hadron separation with LHCb RICH                LHCb-FIGURE-2025-016




12 Reconstruction   Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://cds.cern.ch/record/2937714/

## Page 13

[Slide preview](pages/L09-13.jpg)

```text
Transition radiation (TR) detectors
                                                                            NIMA 881, 88

     Main purpose: separate electrons from pions
     Intensity of TR ∝ γ, opening angle ∝ 1/γ
     Lorentz boost γ higher for e than for π at given p

     ATLAS TRTracker
     Detects large energy
      deposits from TR
     Uses pulse shape

     ALICE TRD
     TR photons absorbed
      in gas mixture,
      producing charges that
      arrive at late drift times



13 Reconstruction   Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://www.sciencedirect.com/science/article/pii/S0168900217309981

## Page 14

[Slide preview](pages/L09-14.jpg)

```text
CALO reconstruction
   Estimate PID from deposited energy
   Combine with tracking information for
    charged particle ID
   Recover Bremsstrahlung of e

   Reconstruct energy of individual
    particles by clustering algorithms
   Use shower shape information


                                                                            Algorithms for CALO
                                                                             reconstruction one of the
                                                                             first to adapt machine learning
                                                                             in production environment



14 Reconstruction   Introduction to Nuclear and Particle Physics WS 25/26
```

## Page 15

[Slide preview](pages/L09-15.jpg)

```text
Muon detection
     Global algorithms combine track fitting and hits in the muon detector

     Example LHCb: simple IsMuon algorithm as p-dependent coincidence of hits in muon stations
     More advanced variable computes correlates spatial residuals of hits δx, δy w.r.t. extrapolation
                                          χ2corr= δxT Vx δx + δyT Vy δy.
     Multiple scattering in calorimeters and absorbers and hit correlation enters in V




                                                     Example of
                                                     same χ2corr
                                                     ←Combinatorial hits
                                                     Real muon→


                                                       JINST 15 12, T12005



15 Reconstruction   Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://doi.org/10.1088/1748-0221/15/12/T12005

## Page 16

[Slide preview](pages/L09-16.jpg)

```text
PID recap
     Modern experiments use more than one method for PID
     At least a Muon system, calorimeters + method for hadron ID

     Informations from different systems is usually combined
      using likelihood methods or machine learning
                                                                            EPJC 85 11, 1237
     Combined methods can be difficult
      to simulate and calibrate …




16 Reconstruction   Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://doi.org/10.1140/epjc/s10052-025-14627-7

## Page 17

[Slide preview](pages/L09-17.jpg)

```text
Simulation                                                                 slides P. Ilten




   Generation step
   Simulate collisions (here pp)
   Several generators on the market (e.g. Pythia 8)

   Simulation step
   Detector response (e.g. GEANT4)
   → needs detector geometry
   → interaction with material

   Digitization
   Detector hits from simulated events
   Add noise, spillover etc.

   Data Processing
   From here on like real data
   Match reconstructed to simulated objects
                                                                       Comput. Softw. Big Sci. 7:6


17 Reconstruction   Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://indico.cern.ch/event/689514/contributions/2928355/attachments/1630712/2599360/ilten.pdf

- https://doi.org/10.1007/s41781-023-00099-5

## Page 18

[Slide preview](pages/L09-18.jpg)

```text
Detector                                             DAQ (data-acquisition) & Trigger




                                                            JINST 3 S08004 (CMS)



                  NIM A 666, 147
                                     Data analysis / publications                            Belle II event display




                                                                                                                          Event
     Model / Theory




                                                                                                                      Reconstruction
                                                    PLB 716, 1




18          Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://doi.org/10.1016/j.nima.2011.03.009

- https://iopscience.iop.org/article/10.1088/1748-0221/3/08/S08004

- https://display.belle2.org/#/event-display

- https://doi.org/10.1016/j.physletb.2012.08.020

## Page 19

[Slide preview](pages/L09-19.jpg)

```text
Statistical data analysis
   Books                                                              slides L. Lista
   Data Analysis in High Energy Physics,
   Behnke et al.
   Statistical Data Analysis, Cowan




19 Analysis   Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://onlinelibrary.wiley.com/doi/book/10.1002/9783527653416

- https://academic.oup.com/book/54868

- https://www.ggi.infn.it/ggilectures/ggilectures2023/img/Lista_GGI-school-2023.pdf

## Page 20

[Slide preview](pages/L09-20.jpg)

```text
Probability density functions
   Discrete random variable
   Assign a probability to each individual value


   Continuous variable
   Ill-defined probability for an individual real value

   A probability density quantifies the probability in the interval dx



          is called probability density function and satisfies




20 Analysis      Introduction to Nuclear and Particle Physics WS 25/26
```

## Page 21

[Slide preview](pages/L09-21.jpg)

```text
Gaussian distribution              PDG 2024, statistics review



   PDF

   Central limit theorem (CLT)
   Distribution of normalized sample mean converges to a
    standard normal distribution (under appropriate conditions)
   →Parameter estimation, detector resolution

   Confidence intervals and p-values
   Due to CLT, confidence intervals in parameter estimation
    and p-values (one-sided α) in hypothesis testing are
    converted to Gaussian standard deviations
    → Usually 1σ uncertainties or 90 or 95% confidence intervals
       are reported
    →In hypothesis tests, usually report “evidence” at 3σ,
      “discovery/observation” at 5σ (rejection of bkg-only hypothesis)



21 Analysis    Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- https://pdg.lbl.gov/2024/reviews/rpp2024-rev-statistics.pdf

## Page 22

[Slide preview](pages/L09-22.jpg)

```text
Parameter estimation: Meaning
                                                                           PRD 99 052006
     Example: Measure mass of decaying particle



     More general: infer a parameter of interest from
      fits to observables
     Obtain central value and statistical uncertainty
       here: 68.3% confidence interval (1σ)


     Frequentist: Probability corresponds to frequency of
      outcomes if experiment would be repeated infinitely
      many times (here: 68.3% of repeated experiments measure
                        m(Ξb) in [5769,7-0.39-..., 5769,7+0.39+...] MeV)
     Bayesian: Probability as degree of belief
       (here: Probability that true value of m(Ξb) is contained in
        [5769,7-0.39-..., 5769,7+0.39+...] MeV is 68.3%)

     HEP ideal for frequentist statistics
22 Analysis        Introduction to Nuclear and Particle Physics WS 25/26
```

Embedded links:

- http://dx.doi.org/10.1103/PhysRevD.99.052006

## Page 23

[Slide preview](pages/L09-23.jpg)

```text
Parameter estimation: Likelihood
   Likelihood L encodes the information the data provides about a (set of) parameter(s) θ

   Given n independent and identically distributed (iid) measurements, the likelihood function is
    the product of the individual conditional p.d.f.s


   Best fit value is the (set of) parameter(s) maximising     : maximum likelihood estimate (MLE)
   MLE is unbiased (large n) and efficient (lowest estimator variance)

   Uncertainties (covariance matrix) from Hessian matrix:


   Alternatively (MINOS): guided search for the 1σ confidence interval given by




23 Analysis   Introduction to Nuclear and Particle Physics WS 25/26
```

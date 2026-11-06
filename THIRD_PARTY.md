# Media sources and license scope

Source audit: 20 October 2026. Covers the media inserted into Lectures 1–3,
including images embedded as data URLs and the externally hosted videos.
A source attribution is not a grant of permission to redistribute media.

## Scope of the MIT license

[LICENSE](LICENSE) applies to the contributors’ original architecture, build
scripts, teaching text, diagrams, plots and interactive demonstrations, to the
extent the contributors own the rights. It does not cover third-party works
embedded in, linked from, or reproduced in the HTML slides or exported PDFs.
Video stills and screenshots retain the underlying work’s rights.

The original layout is from
[Data-Analysis-Block-Course-2026](https://github.com/RUB-EP1/Data-Analysis-Block-Course-2026),
fetched by CI at commit `901d7cbf1a2cc223ef9a4ca74adc395a90f73ebf`.
No top-level license was found in that repository during this check; this
repository’s MIT license does not grant rights in upstream contributions owned
by others. Quarto, Reveal.js and other dependencies retain their own licenses.
Institutional logos, third-party exercise text and cited books are also excluded.

## Videos

| Use | Original source / attribution | Verification and terms |
| --- | --- | --- |
| Lecture 1: cloud chamber | ESA, [Cloud chamber — classroom demonstration video, VP03](https://www.esa.int/ESA_Multimedia/Videos/2014/07/Cloud_chamber_-_classroom_demonstration_video_VP03), 30 July 2014. | Publisher page confirms ESA credit and the [ESA Standard Licence](https://www.esa.int/ESA_Multimedia/Terms_and_conditions_of_use_of_images_and_videos_available_on_the_esa_website). The slides stream the ESA-hosted MP4. Not MIT. |
| Lecture 1: QGP formation | [`qgp_formation.mp4` in the collected clip library](https://github.com/MindaugasSarpis/slidev-videos/releases/tag/videos-shared). | **Original creator and reuse terms unresolved.** The registry names only a local `released/` source. [Piotr Traczyk / CERN, QGP animations](https://videos.cern.ch/record/2301156) is a verified related original, but has not been established as the source of this particular clip. |
| Lecture 1: CERN aerial view | [`cern_overview_short.mp4` in the collected clip library](https://github.com/MindaugasSarpis/slidev-videos/releases/tag/videos-shared). | **Original creator and reuse terms unresolved.** The registry describes an 11-second CERN aerial shot and names only a local `released/` source. A CERN subject does not establish CERN authorship. |
| Lecture 1: ATLAS shaft descent | ATLAS / CERN, identifier `ATLAS-FOOTAGE-2022-004-002`; [`atlas_footage_2022_004_002.mp4`](https://github.com/MindaugasSarpis/slidev-videos/releases/tag/videos-shared). | The registry identifies a 29-second shaft descent and a CERN master filename. **The original catalogue record, individual creator and applicable reuse terms remain unverified.** Credit is supported by the collector’s metadata, not an independently retrieved original record. |
| Lecture 2: garage paradox | 100SekundenPhysik, [Das Garagen-Paradoxon](https://www.youtube.com/watch?v=CdSjy7PFnB0), 29 October 2017. | Original YouTube page and oEmbed metadata confirm the title and channel. Embedded via YouTube; no separate open-content license verified. Not MIT. |

The collected clips’ provenance notes are in
[`src/slidev_videos/shared.toml`](https://github.com/MindaugasSarpis/slidev-videos/blob/main/src/slidev_videos/shared.toml).
A license for that repository’s player or tooling should not be taken as a
license for every hosted film. The unresolved entries above need original
records or rights-holder confirmation before any claim of open reuse.

## Images, diagrams and posters

| Use | Source / attribution | Verification and terms |
| --- | --- | --- |
| Lecture 2: cosmic-ray shower illustration | **DESY Zeuthen**, reproduced on Universität Hamburg’s [Unsichtbares Universum](https://ct.uhh.de/de/wieallesbegann/unsichtbares-universum.html), section “Funkenkammer”; [image file](https://ct.uhh.de/assets/1666095689629.jpg). | Hamburg’s page explicitly credits DESY Zeuthen. The slide’s earlier “Universität Hamburg / Cosmic@Web” credit has been corrected. No open reuse license was verified. Not MIT. |
| Lecture 2: Mentimeter joining QR image | Mentimeter joining slide for [the Lecture 2 quiz](https://www.menti.com/albqthd7x8pu?source=qr-slide-editor). | Slide notes record copying it on 19 October 2026. Treated as third-party platform output, not as an original course illustration. Joining codes may change. |
| Lectures 1–2: interaction vertices and hadron sketches | Local TeX/TikZ drawings in `slides/lectures/Lecture_1/feynman/` and `slides/lectures/Lecture_2/figures/quiz/hadron-sketches.tex`; SVGs embedded in the QMD. | Local drawing sources support course-generated provenance. These are schematic teaching diagrams, not imported experimental images. |
| Lecture 2: Lorentz-factor plot; Lecture 3: double-slit and box-state plots | Local numerical plotting code in `slides/lectures/Lecture_2/scripts/plots.py`; Lecture 3 SVGs in `slides/lectures/Lecture_3/figures/`. | Generated from mathematical expressions in the local script. Original course plots. The script and some editing sources are local working files rather than tracked publication inputs. |
| Lecture 3: recap and Mandelstam diagrams | Original SVG drawings (two frames with one event, light cone, boosted axes with the invariant hyperbola, s/t/u-channel diagrams, a generic 2 → 2 process, the momentum transfer) in `slides/lectures/Lecture_3/figures/`, written for this course and not copied from any book. They illustrate the content of Thomson, *Modern Particle Physics*, Fig. 2.1 and 2.2. | Course-generated; no third-party media. |
| Lecture 3: Mentimeter joining QR code | Generated locally with the `segno` library from the public join link `https://www.menti.com/?code=56562487`; no Mentimeter artwork. | Self-generated; encodes a URL only. The code belongs to the 22 October 2026 quiz and may change. |
| Lecture 4: π⁰ summary table (`figures/pi0_pdg_crop.png`) | Particle Data Group, *Review of Particle Physics* 2026, [`rpp2026-sum-mesons.pdf`](https://pdg.lbl.gov/2026/tables/rpp2026-sum-mesons.pdf) page 2, cropped and rendered at 250 dpi; the PDG citation line (F. Takahashi et al., Int. J. Mod. Phys. A 41, 2630011 (2026)) is part of the crop. | Credited on the slide. The 2026 Review states CC BY 4.0 “except where otherwise noted” (checked 26 October 2026 via [pdglive.lbl.gov](https://pdglive.lbl.gov/)); the 2023 edition used CC BY-NC 4.0. Not MIT. The earlier screenshot `pi0_pdg.png` is no longer used. |
| Lecture 4: Mentimeter joining QR code | Generated locally with the `segno` library from the public join link `https://www.menti.com/?code=79487325`; no Mentimeter artwork. | Self-generated; encodes a URL only. The code belongs to the 26 October 2026 quiz and may change. |
| Lecture 4: figures and widgets | Original SVGs (π⁰ branching fractions, K⁺ → π⁺νν̄ results, cross-section ladder, impact parameter, helicity) generated by a local script from published numbers; Feynman diagrams (π⁰ decays, Primakoff effect) drawn with TikZ-Feynman in `scripts/feynman/`; five widgets with posters (phase space, two-body decay, Dalitz plot, luminosity, e⁻p scattering). Numbers from the PDG, NA62 (arXiv:2010.07644, 2412.12015, 2607.16413), TOTEM (arXiv:1712.06153), LHCb (PRL 118, 052002) and ATLAS/CMS (arXiv:2309.03501). | Course-generated; the data points are redrawn from the quoted numbers, no third-party artwork. |
| Lecture 4: cross sections and rates at the LHC (`figures/xsec-lhc.svg`) | Original plot drawn by `scripts/figures.py` from published numbers: TOTEM total pp cross sections (EPL 96 (2011) 21002, 8 TeV luminosity-independent result, 13 TeV 110.6 mb); ATLAS W and Z totals (EPJC 77 (2017) 367, PLB 759 (2016) 601, arXiv:2403.12902); NNLO+NNLL top-pair values from the LHC Top WG twiki; Higgs cross sections from the LHC HXSWG Yellow Report twiki pages (ggF + VBF + VH + ttH, 125 GeV). The twiki values were read on 27 October 2026. | Course-generated; the data points are redrawn from the quoted numbers, no third-party artwork. The idea follows the familiar σ-versus-√s overview plots, which are not reproduced. |
| Teaching widgets and their posters | Local HTML/JavaScript demonstrations: spin rotation, particle properties, invariant mass and wave packets; for Lecture 3 also scattering resolution, width and lifetime, the golden rule, neutrino oscillations and angular distributions. The widgets use rounded PDG values for the particle presets and no external data files. | Course-generated illustrations and interfaces. Particle-property references (PDG/CERN) are factual references, not sources of copied artwork. The wave-packet poster represents the local demonstration. |

Original course drawings are covered by MIT where contributor-owned. This
audit does not establish the ownership of every historical edit or clear the
third-party assets for redistribution. The remaining source gaps are retained
explicitly rather than assigning guessed authors or licenses.

## Lecture 5: interaction of particles with matter

Lecture 5 uses eight PDG figures under the library's CC BY 4.0 license,
credited on the slides to S. Navas et al. (Particle Data Group),
Phys. Rev. D 110, 030001 (2024). Original figure URLs and transformations are
listed in [Lecture 5 sources](slides/lectures/Lecture_5/SOURCES.md).

TPC illustrations/data are credited to LCTPC and ALICE / Heidelberg. Their
source pages do not state an explicit open reuse license; these third-party
teaching illustrations are not covered by the repository's MIT license.
The supplied 2025 PDF and its extracted personal radiograph remain in the local,
ignored Lecture 5 temporary workspace and are not included as teaching assets.

Lecture 5 also includes the 75-second ALICE Masterclass TPC operating-principle
animation, converted locally to browser-compatible VP9/H.264. Its educational
source and attribution are listed in Lecture 5's `SOURCES.md`; no explicit open
license is stated on the source page. The Cherenkov widget was supplied by the
lecturer and adapted for full-slide display.

## Lecture 7: particle detectors I

Images were collected on 5 November 2026. Licences were read from the Wikimedia
Commons file metadata, from the arXiv abstract page (link to the Creative
Commons licence) or from the paper itself; credits are printed on each slide.
Share-alike images (CC BY-SA) are shown unmodified except for cropping and
resizing. The original drawings (layer figure, sagitta, drift tube, silicon
strip) and the momentum-resolution widget are course-generated.

| Slide image | Source / attribution | Licence and verification |
| --- | --- | --- |
| CMS solenoid (`cms-solenoid.jpg`); triple GEM (`gem-triple.png`) | CMS Collaboration, JINST 19 (2024) P05064, [arXiv:2309.05466](https://arxiv.org/abs/2309.05466), Figs. 2 and 76. | CC BY 4.0: arXiv abstract page and “© 2024 CERN for the benefit of the CMS Collaboration. CC-BY-4.0 license” on page 1. The captions say “from Ref. […]”; the earlier papers were not checked. |
| Micromegas (`micromegas.png`) | S. Aune et al. (sPHENIX), [arXiv:2403.13789](https://arxiv.org/abs/2403.13789), Fig. 3. | CC BY 4.0 on the arXiv abstract page. |
| Bent ALPIDE sensors (`alpide-bent.png`) | B.-M. Blidaru et al., JINST 17 (2022) C09006, [arXiv:2112.10414](https://arxiv.org/abs/2112.10414), Fig. 2a,b. | CC BY 4.0 on the arXiv abstract page. |
| LHCb VELO module, ATLAS SCT module, ATLAS straw-tube prototype (`velo-module.jpg`, `sct-module.jpg`, `straw-wheel.jpg`) | Rama, Wikimedia Commons (photographs at the CERN Microcosm exhibition). | CC BY-SA 3.0 fr (Commons licence field). |
| Belle II central drift chamber (`belle2-cdc.jpg`) | N. Taniguchi / Belle II Collaboration, Wikimedia Commons. | CC BY-SA 4.0 (Commons licence field). |
| MOSS sensor (`moss.jpg`) | M. Suljic, Wikimedia Commons. | CC BY-SA 4.0 (Commons licence field). |
| Photomultiplier (`pmt.jpg`) | ScAvenger, Wikimedia Commons (Hamamatsu R446). | CC BY-SA 4.0 (Commons licence field). |
| Silicon photomultiplier (`sipm.jpg`) | Wikimedia Commons, user GLevi (IRST Trento device). | CC BY-SA 3.0 (Commons licence field); the author credit is assumed by Commons. |
| Lecture 7 recap: PDG figures 34.2, 34.7, 34.13, 34.15(b), 34.26 and two own drawings (shower cascade, hadronic energy flow) | Reused from Lecture 6 (`dedx_table_98.png`, `bichsel_thick.png`, `encrit_cu.png`, `photon-lead.png`, `cherenkov_radiation.png`); S. Navas et al. (Particle Data Group), Phys. Rev. D 110, 030001 (2024). | CC BY 4.0, as listed for Lecture 5 and 6. The two SVGs are course drawings. |
| ATLAS inner detector material map (`atlas-id-material-map.png`) | ATLAS Collaboration, JINST 12 (2017) P12009, [arXiv:1707.02826](https://arxiv.org/abs/1707.02826), Fig. 4, rendered from the arXiv PDF and cropped. | CC BY 3.0 on the [IOP journal page](https://iopscience.iop.org/article/10.1088/1748-0221/12/12/P12009); the arXiv listing carries only the arXiv licence, and the arXiv figures were not compared with the published ones. |
| ATLAS ITk material against η (`itk-material-eta.png`) | ATLAS Collaboration, JINST 20 (2025) P02018, [arXiv:2412.15090](https://arxiv.org/abs/2412.15090), Fig. 5. | CC BY 4.0 (arXiv abstract page and a note in the PDF). |
| LHCb VELO fluence against radius (`velo-fluence.png`) | LHCb VELO group, JINST 8 (2013) P08002, [arXiv:1302.5259](https://arxiv.org/abs/1302.5259), Fig. 4a (cropped to the left panel). | CC BY 3.0 on the arXiv abstract page (Crossref lists the same). |
| MWPC schematic (`mwpc-schematic.png`) | Michael Schmid, Wikimedia Commons, “Wire chamber schematic.svg”, rendered and cropped. | CC BY-SA 3.0 (Commons licence field). |
| Plastic scintillator (`plastic-scintillator.jpg`) | Fermilab, via Wikimedia Commons. | Public domain (Commons licence field). Low resolution. |
| CERN photographs and figures: ATLAS toroid (CDS 910381), LHCb magnet (P. Ginter, CDS 1124307), Georges Charpak and his multiwire chamber (CERN-HI-7008008, CDS 39073), LHCb VELO timing figure (CERN Courier, March/April 2023, “LHCb looks forward to the 2030s”, credit LHCb) | CERN / LHCb. | **Not redistributed.** [CERN’s terms for audiovisual media](https://copyright.web.cern.ch/) allow free use for educational and informational purposes with credit to CERN, but not distribution to third parties. The files live in the git-ignored `figures/local/` folder; the public deck shows a placeholder. The Courier page states only “Copyright © CERN” with no open licence. The CC BY 4.0 that Commons states for two of the photographs could not be confirmed on CDS (the server blocks automated access). |

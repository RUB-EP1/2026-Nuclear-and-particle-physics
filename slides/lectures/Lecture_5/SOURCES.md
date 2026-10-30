# Lecture 5 sources and reconstruction

Teaching source: Mikhail Mikhasenko, *Interaction of particles with matter*,
Lecture 05, 4 November 2025, supplied as `/Users/mikhailmikhasenko/Downloads/Lecture-05.pdf`.
The source PDF has 20 pages, including a handwritten recap page.

## Extracted source (local only)

`tmp/pages/page-NN.pdf`, `.jpg`, and `.txt` preserve each original page.
`tmp/extracted/` contains the 48 embedded image/mask files produced by Poppler.
`tmp/previous-lecture.txt` is the layout-preserving text extraction.
`tmp/contact.jpg` is an overview of all 20 source pages.
These include the original personal radiograph and annotations; they are not assets of the new deck.

## Coverage map

| Previous PDF pages | New deck section |
|---|---|
| 1 | Board recap prompt (40 minutes reserved) |
| 2–3 | Title, cross-section bridge, charged-particle interaction overview |
| 4–6 | Stopping-power units, Bethe–Bloch, MIPs, energy-loss regimes |
| 7 | Track demonstration replaced by the interactive TPC widget |
| 8–10 | TPC principle, many-track display, measured ionization bands |
| 11 | Energy-loss fluctuations and most-probable deposit |
| 12–14 | Bremsstrahlung, electrons/positrons, critical energy |
| 15 | Multiple scattering; full expression in backup |
| 16–18 | Photon processes, cross sections, pair production; brief shower synthesis |
| 19 | Cherenkov radiation and threshold exercise |
| 20 | X-ray and cosmic-proton conceptual questions (no personal scan reproduced) |

## PDG figures

S. Navas et al. (Particle Data Group), Phys. Rev. D 110, 030001 (2024).
Figure library: https://pdg.lbl.gov/2024/figures/figures.html
License explicitly stated by the library: CC BY 4.0.
Review: https://pdg.lbl.gov/2024/reviews/rpp2024-rev-passage-particles-matter.pdf

The following PDFs were downloaded from
`https://pdg.lbl.gov/2024/figures/passage/figures/` and rasterized by Poppler
at 1900 pixels on the longest side, without content changes. The `photon-lead.png` derivative additionally crops to
the complete lower (lead) panel, preserving its axes and labels. Original PDFs
remain in `tmp/`; their PNG derivatives are in `figures/`.

| File stem | Figure | Subject |
|---|---|---|
| `dedx_table_98` | 34.2 | Heavy-particle stopping power in different materials |
| `rpp_icru49_cu_col` | 34.1 | Muon energy-loss regimes in copper |
| `bichsel_thick` | 34.7 | Energy-deposit distribution in silicon |
| `elossfrac_06` | 34.11 | Electron/positron fractional energy loss in lead |
| `encrit_cu` | 34.13 | Electron critical energy in copper |
| `multscat` | 34.10 | Multiple-scattering geometry |
| `sigma_both_06` | 34.15 | Photon cross sections in carbon and lead |
| `cherenkov_radiation` | 34.26 | Cherenkov wavefront construction |

## TPC illustrations

- `tpc-principle.jpg`: LCTPC, *Working Principle of a TPC*.
  Page: https://www.lctpc.org/e8/e57671
  Image: https://www.lctpc.org/sites/sites_custom/site_lctpc/content/e8/e57671/e21013/TPCeng.jpg
- `tpc-dedx.jpg`: ALICE particle-identification data shown by Silvia Masciocchi's Heidelberg group.
  Page: https://www.physi.uni-heidelberg.de/~sma/research/tpc.php
  Image: https://www.physi.uni-heidelberg.de/~sma/research/dEdx.jpg
- `tpc-tracks.jpg`: ALICE TPC time-frame track display on the same Heidelberg page.
  Image: https://www.physi.uni-heidelberg.de/~sma/research/TF_50khz_2ms_tracks_tpc_color.jpg

TPC images are credited to their originating collaborations/websites. No explicit
open reuse license was found on these pages; they remain third-party teaching
illustrations, not covered by this repository's MIT license.

## Scientific clarifications

- Separate geometric stopping power (MeV/cm) from mass stopping power (MeV cm²/g).
- The minimum is near beta-gamma 3–4, with material dependence.
- The physical finite-transfer distribution has a finite mean; the ideal Landau
  approximation does not. Very thin gas cells need more detailed modeling.
- Radiation length is a conventional material property for electrons; mass-squared
  suppression refers to bremsstrahlung for comparable heavy charged leptons.
- Do not use one muon critical-energy number for all materials or only bremsstrahlung.
- Photoelectric dominance is energy- and material-dependent, not true of all nuclear gamma rays.
- Cherenkov emission requires speed above the phase velocity c/n, never above vacuum c.

Accessed 30 October 2026.

## Added media and interactive explanation

- **ALICE TPC operating principle**, 75-second silent animation from ALICE
  Masterclass Support Materials, item 5:
  https://physicsmasterclasses.org/exercises/ALICE-2013/MasterClassSupportMaterials.html
  Original: https://physicsmasterclasses.org/exercises/ALICE-2013/TPC_xvid.avi
  Local derivatives: `media/alice-tpc.webm` (VP9), `media/alice-tpc.mp4` (H.264),
  and a poster frame at 36 seconds. No cuts, narration or content changes.
  The animation shows historical ALICE readout specifications; presenter notes
  distinguish these from the current GEM-based TPC. Third-party educational
  media: no explicit open license stated on the source page, not MIT-licensed.
- **TPC widget** (`widgets/tpc.html`, poster `widgets/tpc-poster.png`): written for this
  course; replaces the ALICE video on the main track, which moved to backup. A 3D chamber
  (drag to rotate; 3D, End and Side views) shows one track, its ionization clusters drifting
  to the end plates, the pad hits and the fitted helix, next to a dE/dx-versus-momentum plot
  filled by the recorded tracks. Toy model: ALICE-like geometry (85–245 cm, 80 pad rows,
  half-length 250 cm, v_d = 2.58 cm/µs, diffusion 220 µm/√cm, B = 0.5 T) after ALICE
  Collaboration, NIM A 622 (2010) 316, arXiv:1001.1950; ALEPH-type Bethe–Bloch
  parametrisation; Poisson primary clusters with 1/k^2.2 sizes; 60% truncated mean. No
  external code or assets; works offline. `?present=1` full-slide layout, `?still=1` no
  autoplay. The poster is a Playwright screenshot of the widget.
- **Explore LHCb** (https://explore-lhcb.web.cern.ch/, source https://gitlab.cern.ch/cburr/explore-lhcb):
  linked only, as homework (RICH get richer, Track fitter, story "How LHCb simulates a
  collision"). No code or assets copied.
- **Two Cherenkov cones**: lecturer-supplied HTML,
  `/Users/mikhailmikhasenko/Downloads/cherenkov-cones.html`.
  Copied to `widgets/cherenkov-cones.html`. Added an optional `?present=1`
  full-slide layout and an Explanation toggle preserving the complete original
  derivation and spacetime plot. Removed remote font requests so the widget works
  offline with its existing system-font fallbacks. Physics and controls preserved.
  `?still=1` pauses the initial state for the local PNG export poster.

The many-track ALICE illustration and the ALICE TPC video are now in backup.

## Lecture 4 recall added to Lecture 5

Adapted kinematics from the author’s 2026-ESHEP/slides/lectures/Lecture_2/sections/20-kinematics.qmd: invariant measure, counting coordinates, two-body phase space, recursive three-body phase space and Dalitz projections. Local copies of shape-orientation.html, dalitz-phasespace.html, common.js, widget.css and three poster images are in widgets/eshep/. The Λb decay is used solely as a kinematic example; no pentaquark, resonance-model or spin-analysis slides were imported. Fixed-target and collider rate derivations and six recall questions were written for this course.

AEPSHEP layout update: footer script adapted from slides/scripts/layout.html with RUB course metadata; coloured phase-space blocks from Lecture_2/lecture-2.css and sections/20-kinematics.qmd. The original hm-counting.png figure is copied to figures/ with an explanation of the energy/orientation conventions.

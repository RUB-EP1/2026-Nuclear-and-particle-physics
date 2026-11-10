# Lecture 8: sources, assets and models

Prepared 10 November 2026. Lecture 8 (accelerators) was moved ahead of DAQ and trigger (now Lecture 9) so that the lecture sequence follows an experiment: accelerate → collide → detect → select → measure. Content follows standard introductory accelerator material (CERN Accelerator School, CERN summer-student and graduate introductions, Wiedemann, Martin & Shaw, Thomson). Numbers are rounded, well-documented design or operating values; speaker notes show the arithmetic.

## Photographs and external figures

All photographs come from Wikimedia Commons, where the licence and author of each file are recorded. They were downloaded via the Commons API at 2400 px width (the LEAR dipole and the QW quadrupole at 960 px) and resized to at most 2000 px (the CERN complex to 3000 px). No other changes were made.

| Local asset | Source | Author / credit | Licence |
|---|---|---|---|
| `figures/cyclotron-27inch-1935.jpg` | [Lawrence 27 inch cyclotron dees 1935.jpg](https://commons.wikimedia.org/wiki/File:Lawrence_27_inch_cyclotron_dees_1935.jpg) | John B. Livingood | Public domain |
| `figures/cyclotron-patent.png` | [Cyclotron patent.png](https://commons.wikimedia.org/wiki/File:Cyclotron_patent.png), from US patent 1,948,384 | Ernest O. Lawrence | Public domain |
| `figures/lhc-tunnel.jpg` | [Views of the LHC tunnel sector 3-4, tirage 1.jpg](https://commons.wikimedia.org/wiki/File:Views_of_the_LHC_tunnel_sector_3-4,_tirage_1.jpg) | Maximilien Brice, CERN | CC BY-SA 3.0 |
| `figures/lhc-tunnel-wide.jpg` | [Views of the LHC tunnel sector 3-4, tirage 2.jpg](https://commons.wikimedia.org/wiki/File:Views_of_the_LHC_tunnel_sector_3-4,_tirage_2.jpg) | Maximilien Brice, CERN | CC BY-SA 3.0 |
| `figures/srf-cavity.jpg` | [A 1.3 GHz nine-cell superconducting radio frequency.JPG](https://commons.wikimedia.org/wiki/File:A_1.3_GHz_nine-cell_superconducting_radio_frequency.JPG) (cavity at Fermilab) | Z22 | CC BY-SA 4.0 |
| `figures/cern-accelerator-complex.png` | [CERN accelerator complex 2022.png](https://commons.wikimedia.org/wiki/File:CERN_accelerator_complex_2022.png) | CERN (F. Landua); CDS CERN-GRAPHICS-2022-001 | CC BY 4.0 |
| `figures/cockcroft-walton.jpg` | [Cockcroft–Walton generator 2012.JPG](https://commons.wikimedia.org/wiki/File:Cockcroft%E2%80%93Walton_generator_2012.JPG) (Science Museum, London) | Geni | CC BY-SA 4.0 |
| `figures/lear-dipole.jpg` | [LEAR magnet.jpg](https://commons.wikimedia.org/wiki/File:LEAR_magnet.jpg) (one of the four LEAR bending magnets) | CERN PhotoLab | CC BY 4.0 |
| `figures/cern-qw-quadrupole.jpg` | [CERN type QW magnet.jpg](https://commons.wikimedia.org/wiki/File:CERN_type_QW_magnet.jpg) (quadrupole on display in the AD hall) | Unnerving duck | CC BY-SA 4.0 |
| `figures/lhc-video-poster.jpg` | Thumbnail of [Oxford Sparks: A quick look around the LHC](https://www.youtube.com/watch?v=BEnaEMMAO_s), embedded via youtube-nocookie | OxfordSparks | YouTube thumbnail, used only as the link preview and PDF stand-in |
| `figures/lhc-magnet-types.jpg` | [LHC magnet types.jpg](https://commons.wikimedia.org/wiki/File:LHC_magnet_types.jpg) (dipole and quadrupole cross-section exhibits) | Ajheindel | CC0 |
| `figures/nsls2-light-source.jpg` | [NSLS-II Aerial.jpg](https://commons.wikimedia.org/wiki/File:NSLS-II_Aerial.jpg) | Zxcvbnm789 | CC BY-SA 4.0 |
| `figures/stirling-cross-sections.png` | W. J. Stirling, [2010 LHC lecture](https://indico.cern.ch/event/94815/contributions/1282690/attachments/1106827/1579062/LBLMIT_Stirling_v2.pdf), slide 22 | W. J. Stirling | Copied from Lecture 9 assets; reuse licence not verified, attribution retained |
| `figures/cms-run2-pileup.png` | [CMS luminosity public results](https://twiki.cern.ch/twiki/bin/view/CMSPublic/LumiPublicResults) | CMS Collaboration | Copied from Lecture 9 assets; CMS public result |

The CERN Document Server search is protected by a bot check and was not used. The CERN complex graphic is the CC BY 4.0 copy on Commons. CC BY-SA images are shown unmodified, with attribution on the slide and in the notes.

## Reproducible teaching plots

Regenerate them with `.venv-pdf/bin/python slides/lectures/Lecture_8/scripts/make_plots.py`. All are analytic calculations, not measured data.

| Asset | Calculation |
|---|---|
| `fixed-target-collider.svg` | √s = 2E (symmetric collider) vs √(2 m_p E + 2 m_p²) (proton beam on a proton at rest). |
| `collider-history.svg` | Rounded maximum √s of e⁺e⁻, hadron and ep colliders. Most points are at the start year of collider operation. LEP2 (2000), RHIC pp 500 GeV (2009) and the LHC steps (2010, 2015, 2022) are at the year reached. The dashed guide line is ×10 per 15 years. The trend is the message, not the exact year. |
| `rf-phase-stability.svg` | sin φ voltage; early, synchronous and late phases 10°, 35° and 60° (below transition). |
| `bending-radius.svg` | ρ = p/(0.3 B) for 1.8, 8.33 and 16 T. Markers: SPS 450 GeV at 2.0 T, LHC 7 TeV at 8.33 T, FCC-hh 50 TeV at 16 T. |
| `fodo-trajectories.svg` | Thin-lens FODO cell, f = 1.2 L, 6 cells, three initial (x, x′); in the y plane the lens signs are swapped. The one-cell trace is 1.31, which is stable. |
| `magnet-fields.svg` | Field lines of an ideal dipole (B uniform) and quadrupole (B = g(y, x)), and the force q v × B on a proton moving into the page. Pole labels follow the field direction. |
| `radiation-pattern.svg` | Angular power distribution for acceleration perpendicular to velocity, in the orbit plane (Jackson, *Classical Electrodynamics*, eq. 14.44), for β = 0 and 0.9, each normalised to its maximum. |
| `synchrotron-loss.svg` | ΔE = 8.85×10⁻⁵ E⁴/ρ GeV. Electrons at ρ = 3096 m; protons at ρ = 2804 m, scaled by (m_e/m_p)⁴. |

## Additional widgets

- **`widgets/physics.js`:** the shared models, checked by `tests/physics.test.cjs`.
  - Cockcroft–Walton: the unloaded output is 2N·V₀ for N = 1–3, and a load lowers it.
  - RF: the gain at crest of one π-mode cell is 2/π, zero at 90°, follows cos φ, and adds over cells.
  - Emittance: drifts and lenses conserve the rms emittance, and acceleration divides it by the momentum ratio.
- **Magnet explorer:** the schematic is drawn from the LHC Design Report Vol. I, ch. 7. Facts are rounded:
  - 8.33 T at 11 850 A; 194 mm aperture spacing; 50 mm cold bore; beam screen at 5–20 K.
  - Thermal shield at 50–75 K; 914 mm vacuum vessel; about 27 t cold mass; three support posts.
  - About 7 600 km of cable; the 19 September 2008 bus-bar incident.
- **Race and memorable story:** the Tour de France Femmes passed LHC Point 5 on 3 August 2026 (CERN news, "Cyclists speed by CMS", 19 August 2026). CERN has bid for a 2029 Tour de France stage, reported as a 27 km individual time trial (La Télé). I found no openly licensed LHC-tunnel ride video, so none is embedded. The speaker notes list candidate links to check first: a 2019 Kinomap ride and CERN's 360° tunnel video.

## Ring designer widget

`widgets/ring.js` holds the analytic model and `widgets/designer.js` draws it.
- **Bending:** ρ = p/(0.2998 B).
- **Circumference:** 2πρ/0.66, the LHC dipole fill factor (17.6 km of 26.7 km).
- **Synchrotron loss:** as in the plot above.
- **Revolution frequency:** c/C.
- **Muons:** lab lifetime γτ with τ = 2.197 µs.
- **Collision energy:** √s collider = 2E; fixed target on a proton.

The model has no RF, focusing, beam–beam or engineering limits. `tests/ring.test.cjs` checks it against the LHC (ρ, C, 6.7 keV/turn, f_rev), LEP2 (3.4 GeV/turn at ρ = 3096 m), the fixed-target √s, the impossibility of a 7 TeV electron ring at 8.33 T, and the muon lifetime and mass⁴ scaling.

## Key numbers used

- **LHC design:** 7 TeV, 8.33 T, 1232 dipoles × 14.3 m, f_rev = 11 245 Hz, n_b = 2808, N = 1.15×10¹¹, ε_N = 3.75 µm, β* = 0.55 m, σ* ≈ 16.7 µm, F ≈ 0.84, L = 10³⁴ cm⁻²s⁻¹ (LHC Design Report Vol. I, CERN-2004-003).
- **LHC RF:** 400 MHz, 8 cavities and 16 MV per beam.
- **LEP2:** 104.5 GeV per beam, ≈3.4 GeV per turn.
- **CERN injector chain:** Linac4 160 MeV → PSB 2 GeV → PS 26 GeV → SPS 450 GeV.
- **Cross sections at 13 TeV:** inelastic ≈ 80 mb, W→ℓν ≈ 20 nb, Higgs ≈ 50–55 pb.
- **Medical:** electron linacs 6–18 MV, proton therapy 70–250 MeV, PET cyclotrons 11–18 MeV.

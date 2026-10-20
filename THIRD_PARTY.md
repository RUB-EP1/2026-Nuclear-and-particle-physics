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
| Teaching widgets and their posters | Local HTML/JavaScript demonstrations: spin rotation, particle properties, invariant mass and wave packets. | Course-generated illustrations and interfaces. Particle-property references (PDG/CERN) are factual references, not sources of copied artwork. The wave-packet poster represents the local demonstration. |

Original course drawings are covered by MIT where contributor-owned. This
audit does not establish the ownership of every historical edit or clear the
third-party assets for redistribution. The remaining source gaps are retained
explicitly rather than assigning guessed authors or licenses.

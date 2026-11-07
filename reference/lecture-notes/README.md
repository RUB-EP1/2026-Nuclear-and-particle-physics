# Lecture source archive and next-lecture plan

Prepared 7 November 2026 from the supplied 2025/26 lecture PDFs. Lecture 7 is already covered; the next planned topic is **DAQ and trigger**.

## Start here

- [Next lecture: 90-minute plan, with a 60-minute variant](NEXT-LECTURE.md)
- [Lecture 7: calorimeters and particle identification](Lecture-07.md)
- [Lecture 8: DAQ, trigger and reconstruction](Lecture-08.md)
- [Lecture 9: reconstruction and data analysis](Lecture-09.md)
- [Interactive-material briefs](INTERACTIVE-MATERIAL.md)
- [Sources, verification status and unresolved credits](SOURCES.md)
- [Figure catalogue](FIGURES.md)

## What is preserved

| Deck | Pages | Searchable source transcription | Original PDF |
|---|---:|---|---|
| Lecture 7, Mikhail Mikhasenko | 21 | [Transcript](Lecture-07-transcript.md) | [PDF](../Lecture-07.pdf) |
| Lecture 8, Marian Stahl | 19 | [Transcript](Lecture-08-transcript.md) | [PDF](../Lecture-08.pdf) |
| Lecture 9, Marian Stahl | 23 | [Transcript](Lecture-09-transcript.md) | [PDF](../Lecture-09.pdf) |

The edited notes explain the material and explicitly flag corrections/additions. Transcripts preserve mechanically extracted source wording; they are not corrected editions. Equations or labels stored as images can be absent from extracted text, so every page links to a rendered slide preview.

The archive includes **63 slide previews**, **172 embedded image entries** (including repeated logos and composite components), **45 distinct recovered reference URLs**, and **12 downloaded upstream assets**. Original ACTS SVGs are editable; upstream PDFs preserve vector figures. Some images remain traceable only to the supplied slide, and the source ledger states where original plots are still unavailable.

## Machine-readable records

- [references.json](references.json): stable reference IDs and slide locations.
- [slide-links.json](slide-links.json): all PDF hyperlink occurrences, including duplicates.
- [embedded-images.json](embedded-images.json): per-page image paths and SHA-256 hashes.
- [original-assets.json](original-assets.json): upstream URLs, download dates, checksums and reuse/verification status.

The supplied PDFs triggered non-fatal parser warnings about malformed number tokens and object offsets. All expected pages rendered and extracted; rendered previews are retained to resolve extraction ambiguities. The source PDFs were not modified.

## Important corrections before teaching

- L07 calorimeter resolution: use the stochastic, constant and noise terms consistently; the LHCb numerical formulas need source verification.
- L08 buffering: separate busy conversion, finite-buffer losses and sustained overload.
- L09 alignment: three translations **plus** three rotations for a rigid element, before constraints.
- L09 muon residual statistic: covariance must be inverted, unless the matrix is already defined as a weight.
- L09 mass example: the cited result is **5796.70**, not the 5769.7 typo in the explanatory prose.
- L09 confidence intervals: repeated intervals cover a fixed true parameter; future estimates are not guaranteed to fall in today's interval at the stated coverage.
- L09 likelihood: finite-sample MLEs need not be unbiased; Hessian/profile intervals are conditional approximations.

## Reproducing extraction

From the repository root, run `python reference/lecture-notes/extract_sources.py` with `pypdf` installed and Poppler `pdftotext` on PATH. This refreshes transcripts, raw link occurrences and embedded images only; it does not regenerate edited notes or verified source metadata.

Render previews using `pdftoppm -scale-to 1100 -jpeg reference/Lecture-07.pdf reference/lecture-notes/pages/L07`, and analogously for 08/09. Original upstream downloads have frozen hashes in the manifest; a mutable `latest` URL is not a version pin.

This archive and the three source PDFs are tracked for internal preparation. They are outside the website workflow's explicit render and resource lists, and no published lecture links to them. Committing them does not publish them to the course website. No existing lecture sources were changed.

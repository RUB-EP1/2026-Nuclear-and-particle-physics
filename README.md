# KT1 · 2026

Lecture materials for Nuclear and Particle Physics, using the Quarto/Reveal.js
infrastructure from `2026-RUB-ML`.

The workspace directory retains its existing name, `2027-RUB-KTI`.

- `slides/`: shared template, build tools, and lecture workspaces.
- `slides/lectures/Lecture_1/`: introduction to nuclear and particle physics,
  a quantum mechanics recap, selected physics films, and Thomson Chapter 1.
  A 67-slide draft includes a large, introductory four-vector preview.
- `slides/lectures/Lecture_2/`: relativistic kinematics, two-body decay, boosts,
  invariant mass, and production thresholds with board problems.
- `slides/lectures/Lecture_3/`: a 30-minute kinematics recap, three-question Menti
  quiz, quantum amplitudes, perturbation theory, and transition rates.
- `description/`: existing course descriptions.

Build or preview the first lecture:

```sh
make -C slides html
make -C slides live
```

See [the slide workflow](slides/README.md) for requirements and PDF export.

Build downloadable PDFs for every lecture from the course root:

```sh
make pdf-deps  # once: install Playwright, Chromium and ReportLab
make pdf
```

PDF export snapshots each slide at 1920 × 1080 and preserves external links.
Interactive demonstrations and films appear as still images. PDFs are written
beside the rendered slides. For a rendered website, use `make pdf HTML_ROOT=_site`.
The publishing workflow runs this command before uploading the site, and each
lecture card links to its PDF.

## Public source repository

The public Git repository tracks only `index.qmd`, the lecture QMD sources,
the root `Makefile`, PDF export scripts, `.github/workflows/pages.yml` and
`.gitignore`. The workflow fetches shared
layout files from the pinned Data-Analysis-Block-Course-2026 commit, creates
its Quarto website configuration, builds the lectures, and deploys to Pages.

Lecture 1's custom CSS, widget HTML and SVG diagrams are embedded in its QMD
so a clean checkout has all lecture-specific content. The separate local
widget and diagram files are editing aids, not CI inputs: future edits to them
must also update the corresponding embedded content in the QMD.

Public site: https://rub-ep1.github.io/2026-Nuclear-and-particle-physics/

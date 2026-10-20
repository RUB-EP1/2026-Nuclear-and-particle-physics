# Nuclear and Particle Physics · KT1 · 2026

[![Course website](https://img.shields.io/badge/website-lectures%20%26%20PDFs-007dc5)](https://rub-ep1.github.io/2026-Nuclear-and-particle-physics/)

Lecture slides, interactive demonstrations and exercises for Mikhail
Mikhasenko’s course at Ruhr-Universität Bochum, winter semester 2026/27.

## How it was made

Built with Quarto and Reveal.js, with assistance from **Codex**, **Claude Code**
and **Grok**. The original website and slide template comes from
[RUB-EP1/Data-Analysis-Block-Course-2026](https://github.com/RUB-EP1/Data-Analysis-Block-Course-2026).
GitHub Actions fetches a pinned template revision, renders the lectures,
generates PDFs and publishes the website.

## Build

With Quarto, Python 3 and the shared template files in place:

```sh
make html       # render lecture slides
make pdf-deps   # install PDF dependencies once
make pdf        # render slides and export all lecture PDFs
```

See [the publishing workflow](.github/workflows/pages.yml) for template setup.

## License and media credits

The original course material and repository architecture are available under
the [MIT license](LICENSE), to the extent owned by the contributors.
Third-party videos, images, logos, software and template components retain
their own terms; they are not relicensed here. See [media sources and license
scope](THIRD_PARTY.md), including source checks and unresolved attributions.

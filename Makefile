PYTHON ?= python3
PDF_PYTHON ?= .venv-pdf/bin/python
HTML_ROOT ?= .
PDF_ROOT ?= $(HTML_ROOT)
LECTURES := $(basename $(notdir $(wildcard slides/lectures/Lecture_*/Lecture_*.qmd)))

.PHONY: html pdf pdf-deps

html:
	@for lecture in $(LECTURES); do \
		quarto render "slides/lectures/$$lecture/$$lecture.qmd" || exit 1; \
	done

# Local builds render first; CI exports the already-rendered website.
ifeq ($(HTML_ROOT),.)
pdf: html
endif

pdf:
	$(PDF_PYTHON) scripts/export_pdf.py --html-root "$(HTML_ROOT)" --pdf-root "$(PDF_ROOT)" $(LECTURES)

pdf-deps:
	$(PYTHON) -m venv .venv-pdf
	$(PDF_PYTHON) -m pip install -r scripts/requirements-pdf.txt
	$(PDF_PYTHON) -m playwright install chromium

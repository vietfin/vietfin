# Minimal makefile for Sphinx documentation
# source: <https://github.com/python/devguide/blob/main/Makefile>

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SPHINXOPTS    = -W --keep-going
SOURCEDIR     = .
BUILDDIR      = _build
BUILDER       = html
JOBS          = auto
PAPER         =

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -b $(BUILDER) \
                  -d $(BUILDDIR)/doctrees \
                  -j $(JOBS) \
                  $(PAPEROPT_$(PAPER)) \
                  $(SPHINXOPTS) \
                  . $(BUILDDIR)/$(BUILDER)

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
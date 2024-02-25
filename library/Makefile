# Makefile for Sphinx documentation


# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build -E
PAPER = 
SOURCEDIR     = docs
BUILDDIR      = docs/_build
PROJECT  = PROJECT_NAME


.PHONY: docs
docs:
	@sphinx-apidoc -o ./$(SOURCEDIR)/source ./$(PROJECT)
	@sphinx-build -E -b html -d ./$(SOURCEDIR)/build/doctrees   ./$(SOURCEDIR) ./$(SOURCEDIR)/build/html
	@cp -a ./$(SOURCEDIR)/build/html/ docs_html

.PHONY: flake8
flake8:
	@flake8 PROJECT_NAME

.PHONY: lint
lint:
	@pylint PROJECT_NAME

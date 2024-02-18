# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build -E
PAPER = 
SOURCEDIR     = sphinx
BUILDDIR      = sphinx/_build



.PHONY: docs
docs:
	@sphinx-apidoc -o ./sphinx/source ./PROJECT_NAME
	@sphinx-build -E -b html -d ./sphinx/build/doctrees   ./sphinx ./sphinx/build/html
	@cp -a ./sphinx/build/html/ docs

.PHONY: flake8
flake8:
	@flake8 PROJECT_NAME

.PHONY: lint
lint:
	@pylint PROJECT_NAME

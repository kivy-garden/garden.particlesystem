.PHONY: tests build all

all: build tests

tests:
	py.test tests

build:
	python setup.py build_ext --inplace -f


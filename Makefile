install:
	pip install -r requirements.txt

test:
	python -m pytest -cov=main src/tests/*.py -v
lint:
	find ./src/main_workspace -name "*.py" -exec pylint --disable=R,C {} +
format:
	find ./src/main_workspace -name "*.py" -exec black {} +
	find ./src/tests -name "*.py" -exec black {} +
run:
	python src/main_workspace/main.py

all: install test lint format
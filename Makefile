PYTHON = env/bin/python
PIP = env/bin/pip
FLAKE8 = env/bin/flake8
MYPY = env/bin/mypy
PYTEST = env/bin/pytest
MAP ?= maps/easy/01_linear_path.txt

install:
	python3 -m venv env
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) main.py $(MAP)


debug:
	$(PYTHON) -m pdb main.py $(MAP)

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf .mypy_cache .pytest_cache

lint:
	$(FLAKE8) --exclude=env
	$(MYPY) --exclude env $(MYPY_FLAGS)

lint-strict:
	$(FLAKE8) --exclude=env
	$(MYPY) --exclude env --strict

test:
	$(PYTEST)

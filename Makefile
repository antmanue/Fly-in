install:
	python3 -m venv env
	env/bin/pip install -r requirements.txt

run:
	env/bin/python main.py


debug:
	DEBUG=1 env/bin/python main.py

clean:
	rm -rf __pycache__


lint:
	env/bin/flake8 .
	env/bin/mypy .


setup-dependencies:
	python3 -m pip install -r requirements.txt

setup-dependencies-and-checks:
	python3 -m pip install -r requirements.txt
	python3 -m pip install black isort flake8 commitizen pre-commit
	pre-commit install

clean:  ## Remove general artifact files
	find . -name '.coverage' -delete
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '.pytest_cache' -type d | xargs rm -rf
	find . -name '__pycache__' -type d | xargs rm -rf
	find . -name '.ipynb_checkpoints' -type d | xargs rm -rf

run-all-pre-commits:
	pre-commit run --all-files

env-sample:
	awk -F '=' '{print $$1 "="}' .env > .env.sample

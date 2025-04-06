.PHONY: test coverage clean

test:
	PYTHONPATH=src pytest tests

coverage:
	pytest --cov=src --cov-report=term-missing

clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
	rm -rf .pytest_cache .coverage layer/ python/ build/ dist/

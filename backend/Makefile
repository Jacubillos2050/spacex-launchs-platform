.PHONY: test coverage clean start-dynamodb migrate offline deploy

# Tests
test:
	PYTHONPATH=src pytest tests

coverage:
	pytest --cov=src --cov-report=term-missing

clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
	rm -rf .pytest_cache .coverage layer/ python/ build/ dist/

# DynamoDB Local
start-dynamodb:
	cd .dynamodb && java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb -port 8000

migrate:
	sls dynamodb migrate --stage dev

# Serverless
offline:
	sls offline start --stage dev

deploy:
	sls deploy --stage dev

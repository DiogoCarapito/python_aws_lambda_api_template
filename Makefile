install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	pytest -vv --cov=main --cov=utils tests/test_*.py

format:
	black . *.py

lint:
	pylint --disable=R,C,W0613 *.py utils/*.py tests/*.py

docker-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

build:
	docker build -t lambda-api-template .

refactor:
	format lint

deploy:
	echo "deploy not implemented"

all: install format lint test

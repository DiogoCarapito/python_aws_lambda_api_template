[![Github Actions Workflow](https://github.com/DiogoCarapito/python_aws_lambda_api_template/actions/workflows/main.yaml/badge.svg)](https://github.com/DiogoCarapito/python_aws_lambda_api_template/actions/workflows/main.yaml)

# python_aws_lambda_api_template

Personal AWS Lambda python template

## cheat sheet

### venv
create venv
```bash
python3 -m venv .venv
```

activate venv
```bash
source .venv/bin/activate
```

### Docker
build docker image
```bash
docker build -t main:latest .
```

```bash
docker run -p 8080:80 your-image:latest
```
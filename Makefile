.PHONY: help train test api mlflow

help:
	@echo "Available commands:"
	@echo "  make train        - Train model (uses your existing packages)"
	@echo "  make test         - Run tests (uses your existing packages)"
	@echo "  make api          - Run API server"
	@echo "  make mlflow       - Start MLflow UI"
	@echo "  make docker-build - Build Docker image"
	@echo "  make docker-run   - Run Docker container"

train:
	python src/train.py

test:
	pytest tests/ -v

api:
	uvicorn src.predict:app --reload --host 0.0.0.0 --port 8000

mlflow:
	mlflow ui --host 0.0.0.0 --port 5000

docker-build:
	docker build -t mlops-pipeline .

docker-run:
	docker run -p 8000:8000 -p 5000:5000 mlops-pipeline

# Install dependencies
install:
	pipenv install --dev

# Format code
format:
	pipenv run black src tests

# Lint code
lint:
	PATH=$(pipenv --venv)/bin:$(PATH) pipenv run pylint src tests || exit 0

# Run tests
test:
	PYTHONPATH=$(shell pwd) PATH=$(pipenv --venv)/bin:$(PATH) pipenv run pytest tests


# mlflow server start
mlflow-server:
	docker-compose -f docker/docker-compose.yaml up -d mlflow

# Train model
train: mlflow-server
	sleep 5 # даємо час на старт сервера MLflow
	pipenv run python src/model_training.py data/processed/train_bikes_processed.csv models/random_forest_model.joblib my-bucket random_forest_model.joblib

# Process data
preprocess:
	pipenv run python src/data_processing.py data/raw/train_bikes.csv data/processed/train_bikes_processed.csv data/processed/test_bikes_processed.csv

# Start LocalStack
localstack-up:
	docker-compose -f docker/docker-compose.yaml up -d localstack

# Stop LocalStack
localstack-down:
	docker-compose -f docker/docker-compose.yaml down

# Predict on test data
predict:
	pipenv run python src/batch_prediction.py data/raw/test_bikes.csv predictions.csv --model_path models/random_forest_model.joblib

# Monitoring
monitor: preprocess
	pipenv run python monitoring/monitor_model.py data/processed/train_bikes_processed.csv data/processed/test_bikes_processed.csv monitoring/report.html

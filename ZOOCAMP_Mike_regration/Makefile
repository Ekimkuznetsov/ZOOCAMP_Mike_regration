# Install dependencies
install:
	pipenv install --dev

# Format code
format:
	pipenv run black src tests

# Lint code
lint:
	PYTHONPATH=.:src pipenv run pylint src tests

# Run tests
test:
	PYTHONPATH=.:src pipenv run pytest tests

# Train model
train:
	pipenv run python src/model_training.py data/raw/train_bikes.csv models/random_forest_model.joblib

# Process data
preprocess:
	pipenv run python src/data_processing.py data/raw/train_bikes.csv data/processed/train_bikes_processed.csv

# Start LocalStack
localstack-up:
	docker-compose -f docker/docker-compose.yaml up -d

# Stop LocalStack
localstack-down:
	docker-compose -f docker/docker-compose.yaml down

# Predict on test data
predict:
	pipenv run python src/batch_prediction.py data/raw/test_bikes.csv predictions.csv --model_path models/random_forest_model.joblib

# Generate monitoring report
monitor:
	pipenv run python monitoring/monitor_model.py data/processed/train_bikes_processed.csv predictions.csv monitoring/report.html

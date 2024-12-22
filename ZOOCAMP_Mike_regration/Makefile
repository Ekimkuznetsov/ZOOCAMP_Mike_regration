# Install dependencies
install:
	pipenv install --dev

# Format code
format:
	pipenv run black src tests

# Lint code
lint:
	pipenv run pylint src tests

# Run tests
test:
	pipenv run pytest tests

# Train model
train:
	pipenv run python src/model_training.py data/raw/train_bikes.csv models/random_forest_model.joblib

# Process data
preprocess:
	pipenv run python src/data_processing.py data/raw/train_bikes.csv data/processed/train_bikes_processed.csv

# localstack-up:
	docker-compose -f docker/docker-compose.yaml up -d

# localstack-down:
	docker-compose -f docker/docker-compose.yaml down

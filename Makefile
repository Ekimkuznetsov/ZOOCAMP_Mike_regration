# Makefile for Bike Demand Prediction Pipeline

# Variables
PIPELINE_PATH = mage_pipeline_repo/pipelines/bike_demand_prediction
TESTS_PATH = tests
PYTHON = python3

.PHONY: all start_mage preprocess train predict monitor

# Start Mage
start_mage:
	mage start $(MAGE_PATH)

# Run unit tests
test_unit:
	PYTHONPATH=. python3 -m unittest discover -s tests/unit -p "test_*.py"


# Data processing
process:
	python3 mage_pipeline_repo/pipelines/bike_demand_prediction/data_processing.py

# Data processing
preprocess:
	$(PYTHON) $(PIPELINE_PATH)/data_ingestion.py

# Model training
train:
	python3 mage_pipeline_repo/pipelines/bike_demand_prediction/model_training.py

mlflow_server:
	mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 0.0.0.0 --port 5000


# Batch prediction
predict:
	python3 mage_pipeline_repo/pipelines/bike_demand_prediction/batch_prediction.py

# Monitoring
monitor:
	python3 mage_pipeline_repo/pipelines/bike_demand_prediction/monitoring.py

# Full pipeline execution
all: preprocess train predict monitor
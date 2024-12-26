# Makefile for Bike Demand Prediction Pipeline

# Variables
PIPELINE_PATH = mage_pipeline_repo/pipelines/bike_demand_prediction
TESTS_PATH = tests
PYTHON = python3

.PHONY: all start_mage preprocess train predict monitor

# Start Mage
start_mage:
	mage start $(MAGE_PATH)

# Run all tests
test_all:
	$(PYTHON) -m unittest discover $(TESTS_PATH)

# Run unit tests
test_unit:
	$(PYTHON) -m unittest discover -s $(TESTS_PATH)/unit -p "*.py"


# Data processing
preprocess:
	$(PYTHON) $(PIPELINE_PATH)/data_ingestion.py

# Model training
train:
	$(PYTHON) -c "from mage_pipeline_repo.pipelines.bike_demand_prediction import model_training; model_training()"

# Batch prediction
predict:
	$(PYTHON) -c "from mage_pipeline_repo.pipelines.bike_demand_prediction import batch_prediction; batch_prediction()"

# Monitoring
monitor:
	$(PYTHON) -c "from mage_pipeline_repo.pipelines.bike_demand_prediction import monitoring; monitoring()"

# Full pipeline execution
all: preprocess train predict monitor
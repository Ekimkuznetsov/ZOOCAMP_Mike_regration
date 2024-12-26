Bike Demand Prediction Pipeline

Objective

The goal of this project is to build an end-to-end machine learning pipeline for predicting bike demand, integrating industry-standard tools for experiment tracking, pipeline orchestration, and monitoring.

Problem Statement

This project involves building a complete ML workflow, including:

Dataset exploration and feature engineering.
Training models and tracking experiments.
Deploying the trained model for batch predictions.
Monitoring model performance in production.
Visualizing and orchestrating the pipeline using Mage.
Technologies Used

Cloud: AWS LocalStack
Experiment Tracking: MLflow
Workflow Orchestration: Mage
Monitoring: Evidently
CI/CD: GitHub Actions
Infrastructure as Code: Terraform (optional)
Project: Bike Demand Prediction

Description
The objective of this project is to forecast bike demand using historical rental data. By analyzing trends and creating a robust machine learning model, we aim to predict rental demand based on weather conditions, time of year, and day of the week.


[Data Ingestion]
   -> [Data Processing (Feature Engineering)]
      -> [Experiment Tracking (MLflow)]
         -> [Model Training & Evaluation]
            -> [Batch Prediction]
               -> [Monitoring & Reporting (Evidently)]
                  -> [Pipeline Visualization (Mage)]


Steps
1. Setup Environment

Install Python dependencies using pipenv:
pipenv install
Build Docker containers for the required infrastructure (LocalStack, MLflow):
docker-compose -f docker/docker-compose.yaml up -d
2. Data Processing

Preprocess raw bike rental data:
make preprocess
3. Model Training

Train the Random Forest model and log experiments to MLflow:
make train
4. Batch Prediction

Use the trained model to generate predictions on test data:
make predict
5. Monitoring

Generate a monitoring report for model performance:
make monitor
6. Pipeline Visualization with Mage

Start Mage and access the visualized pipeline:
mage start
Navigate to http://localhost:6789 to visualize the pipeline.
Current Progress
Model Results:

Algorithm: Random Forest Regressor
Performance Metrics:
Validation RMSE: 70.93
Validation R²: 0.85
Training RMSE: 60.36
Training R²: 0.89
Experiment Tracking:

MLflow Experiment: Experiment 0
MLflow Run Details: Run
Directory Structure
.
├── data
│   ├── raw
│   │   ├── test_bikes.csv
│   │   └── train_bikes.csv
│   └── processed
│       ├── test_bikes_processed.csv
│       └── train_bikes_processed.csv
├── src
│   ├── data_processing.py
│   ├── model_training.py
│   ├── batch_prediction.py
│   └── config.py
├── monitoring
│   └── report.html
├── mlruns
├── tests
│   └── unit
│       └── test_data_processing.py
├── Dockerfile
├── docker-compose.yaml
├── Makefile
├── Pipfile
├── README.md
└── requirements.txt
Automation via Makefile
The Makefile provides easy-to-use commands for automating tasks:

Command	Description
make install	Install dependencies.
make format	Format code with black.
make lint	Lint code using pylint.
make test	Run unit tests.
make preprocess	Preprocess raw data.
make train	Train the model and log experiments.
make predict	Generate batch predictions.
make monitor	Generate monitoring report.
make localstack-up	Start LocalStack for S3 emulation.
make localstack-down	Stop LocalStack.
How to Add Mage
Install Mage

pip install mage-ai
Initialize Mage in Your Project

mage init pipeline_name
Add a Mage Block for Each Step

Use Mage to define blocks for each step (data processing, training, prediction). Update your pipeline in Mage to reflect these steps.

Start Mage

Run Mage and visualize:

mage start

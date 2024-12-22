# Project Name

## Objective

The goal of this project is to apply everything we have learned in this course to build an end-to-end machine learning project.

## Problem Statement

For the project, we will build an end-to-end ML project. This includes:

1. Selecting a dataset of interest.
2. Training a model on that dataset while tracking experiments.
3. Creating a model training pipeline.
4. Deploying the model in batch, as a web service, or in streaming mode.
5. Monitoring the performance of the model.
6. Following the best practices for ML project development.

## Technologies

- **Cloud**: AWS localstack
- **Experiment tracking tools**: MLFlow
- **Workflow orchestration**: Mage
- **Monitoring**: Evidently
- **CI/CD**: GitHub Actions
- **Infrastructure as Code (IaC)**: Terraform?

## Project: Bike Demand Prediction

### Problem Description

This project aims to predict the demand for bicycles using real-world data from bicycle rental services. The objective is to analyze trends and create a robust machine learning model to forecast bike demand based on various features such as weather conditions, time of year, and day of the week.

### Steps
1. **Setup Environment**:
   - Install `pyenv` to manage Python versions:
     ```bash
     curl https://pyenv.run | bash
     ```
     Add `pyenv` to your shell:
     ```bash
     export PATH="$HOME/.pyenv/bin:$PATH"
     eval "$(pyenv init --path)"
     eval "$(pyenv init -)"
     ```
     Restart your terminal and install Python 3.9:
     ```bash
     pyenv install 3.9.0
     pyenv global 3.9.0
     ```
     Verify Python version:
     ```bash
     python --version
     ```
   - Use `pipenv` to manage dependencies:
     ```bash
     pipenv --python 3.9
     ```
     This will create a `Pipfile` for the project.
   - Install required libraries:
     ```bash
     pipenv install pandas numpy scikit-learn matplotlib seaborn mlflow boto3
     ```

2. **Data Analysis**:
   - Explore the dataset to understand the key features and relationships.
   - Visualize trends in bike rentals.

3. **Feature Engineering**:
   - Process raw data into features suitable for training.
   - Handle missing data, encode categorical variables, and normalize numerical data.

4. **Model Training**:
   - Train a machine learning model (Random Forest) to predict demand.
   - Track experiments and log metrics using MLflow.
   - Evaluate the model's performance using metrics like RMSE and R².

5. **Pipeline Creation**:
   - Build a training and prediction pipeline.

6. **Deployment**:
   - Deploy the model locally or on a cloud service using Docker.

7. **Batch Prediction**:
   - Use the trained model to make predictions on new data.
   - Save the predictions to a CSV file.

8. **Monitoring**:
   - Implement a monitoring solution to track model performance.

### Current Progress

#### Latest Model Results:
- **Algorithm**: Random Forest Regressor
- **Performance**:
  - **Validation RMSE**: 70.93
  - **Validation R²**: 0.85
  - **Training RMSE**: 60.36
  - **Training R²**: 0.89
  - **Training MAE**: 40.05
- **Experiment Tracking**:
  - MLflow experiment: [Experiment 0](http://localhost:5000/#/experiments/0)
  - MLflow run details: [Run](http://localhost:5000/#/experiments/0/runs/322fcdb2f7764f8790d08cfa75da7f31)

### Automation via Makefile
The project includes a `Makefile` for automating common tasks:

- **Install dependencies**:
  ```bash
  make install
  ```
- **Format code**:
  ```bash
  make format
  ```
- **Lint code**:
  ```bash
  make lint
  ```
- **Run tests**:
  ```bash
  make test
  ```
- **Train the model**:
  ```bash
  make train
  ```
- **Process data**:
  ```bash
  make preprocess
  ```
- **Start LocalStack**:
  ```bash
  make localstack-up
  ```
- **Stop LocalStack**:
  ```bash
  make localstack-down
  ```
- **Batch prediction**:
  ```bash
  make predict
  ```

### Resources

### Datasets

You can explore and select datasets from:
- [Santander Bike Rentals Dataset](https://www.kaggle.com/datasets)
- [Open Data for Bike Sharing](https://data.gov.uk/)

## Getting Started

1. Clone this repository.
2. Follow the setup instructions in `README.md`.
3. Start with the provided directory structure.

## Directory Structure

```
project-name/
├── data/                   # Directory for raw and processed data
│   ├── raw/
│   ├── processed/
├── notebooks/              # Jupyter notebooks for EDA and experiments
├── src/                    # Source code for the pipeline
│   ├── __init__.py
│   ├── data_processing.py  # Data cleaning and preprocessing functions
│   ├── model_training.py   # Code for model training
│   ├── batch_prediction.py # Batch prediction pipeline
├── tests/                  # Tests for code
│   ├── unit/
│   ├── integration/
├── models/                 # Saved models
├── monitoring/             # Scripts for monitoring
├── docker/                 # Docker-related files
│   ├── Dockerfile
│   ├── docker-compose.yaml
├── scripts/                # Shell scripts
│   ├── run_project.sh      # Script for running the pipeline
├── Makefile                # Automation tasks
├── requirements.txt        # Python dependencies
├── README.md               # Project description and instructions
├── .gitignore              # Ignored files
└── config.yaml             # Configuration file for pipeline parameters
```

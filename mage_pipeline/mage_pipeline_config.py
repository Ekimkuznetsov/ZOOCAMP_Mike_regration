# Mage pipeline setup
import os
from mage_ai.data_preparation.repo_manager import RepoManager
from mage_ai.data_preparation.models.pipeline import Pipeline
import mlflow
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, RegressionPreset

# Initialize Mage repository
REPO_PATH = 'mage_pipeline_repo'
PIPELINE_NAME = 'bike_demand_prediction'

os.makedirs(REPO_PATH, exist_ok=True)
RepoManager.init_repo(REPO_PATH)

# Create a new pipeline
pipeline = Pipeline.create(PIPELINE_NAME, REPO_PATH)

# Add blocks to the pipeline
pipeline.add_block('data_ingestion', 'data_loader')
pipeline.add_block('data_processing', 'transformer', upstream_blocks=['data_ingestion'])
pipeline.add_block('model_training', 'transformer', upstream_blocks=['data_processing'])
pipeline.add_block('batch_prediction', 'transformer', upstream_blocks=['model_training'])
pipeline.add_block('monitoring', 'transformer', upstream_blocks=['batch_prediction'])

# Example MLflow integration in model_training block
def model_training():
    """Train a Random Forest model and log results to MLflow.

    This function loads preprocessed training data, trains a Random Forest
    regression model, and logs the trained model, parameters, and metrics
    to MLflow for experiment tracking.

    Steps:
        1. Load preprocessed training data.
        2. Train a Random Forest regression model.
        3. Compute training RMSE.
        4. Log model, parameters, and metrics to MLflow.

    Raises:
        FileNotFoundError: If the data file is not found.
        Exception: For other runtime errors during training.
    """
    mlflow.set_experiment('Bike Demand Prediction')
    with mlflow.start_run():
        # Load data (replace with actual data paths)
        train_data = pd.read_csv('processed_train_data.csv')
        X_train = train_data.drop(columns=['count'])
        y_train = train_data['count']

        # Train model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Log model
        mlflow.sklearn.log_model(model, 'model')

        # Log parameters and metrics
        y_pred = model.predict(X_train)
        rmse = np.sqrt(mean_squared_error(y_train, y_pred))
        mlflow.log_metric('rmse', rmse)

# Example Evidently integration in monitoring block
def monitoring():
    """Generate monitoring reports using Evidently.

    This function loads predictions and actuals, compares them, and generates
    reports for data drift and model performance.

    Steps:
        1. Load test data and predictions.
        2. Compare distributions and model metrics.
        3. Generate and save reports as HTML.

    Raises:
        FileNotFoundError: If required files are not found.
        Exception: For other runtime errors during monitoring.
    """
    # Load data (replace with actual data paths)
    test_data = pd.read_csv('processed_test_data.csv')
    predictions = pd.read_csv('predictions.csv')

    # Merge data for comparison
    test_data['prediction'] = predictions['prediction']

    # Generate reports
    drift_report = Report(metrics=[DataDriftPreset()])
    regression_report = Report(metrics=[RegressionPreset()])

    drift_report.run(reference_data=test_data, current_data=test_data)
    regression_report.run(reference_data=test_data, current_data=test_data)

    # Save reports
    drift_report.save_html('drift_report.html')
    regression_report.save_html('regression_report.html')

# Save pipeline
pipeline.save()

print(f'Pipeline {PIPELINE_NAME} created successfully with Mage.')

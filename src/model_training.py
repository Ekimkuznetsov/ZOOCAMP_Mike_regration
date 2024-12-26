"""
Model training module for bike demand forecasting.

This script trains a Random Forest model to predict bike demand. 
It supports logging experiments with MLflow
and saving trained models to a local file system and an 
S3-compatible storage (e.g., AWS or LocalStack).
"""

import click
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_squared_error,
    r2_score,
)
import numpy as np
import mlflow
import mlflow.sklearn
import joblib
import boto3
from src.config import FEATURE_COLUMNS


def save_model_to_s3(model_path, bucket_name, s3_key):
    """
    Save a trained model to S3.

    :param model_path: Local path to the saved model file.
    :param bucket_name: Name of the S3 bucket.
    :param s3_key: Key for storing the model in the S3 bucket.
    """
    s3 = boto3.client("s3", endpoint_url="http://localhost:4566")
    s3.create_bucket(Bucket=bucket_name)
    s3.upload_file(model_path, bucket_name, s3_key)
    print(f"Model saved to s3://{bucket_name}/{s3_key}")


def train_random_forest_with_mlflow(train_path):
    """
    Train and log a Random Forest model with MLflow.

    :param train_path: Path to the training data file (CSV).
    :return: Trained Random Forest model.
    """
    # Enable MLflow autolog
    mlflow.sklearn.autolog()

    with mlflow.start_run():
        # Load and preprocess training data
        train_data = pd.read_csv(train_path)
        train_data["hour"] = pd.to_datetime(train_data["datetime"]).dt.hour
        train_data["is_weekend"] = (
            pd.to_datetime(train_data["datetime"]).dt.weekday >= 5
        ).astype(int)

        # Define features and target
        features = train_data[FEATURE_COLUMNS]
        target = train_data["count"]

        # Split data into training and validation sets
        features_train, features_val, target_train, target_val = train_test_split(
            features, target, test_size=0.2, random_state=42
        )

        # Initialize and train the model
        model = RandomForestRegressor(random_state=42, n_estimators=100, max_depth=10)
        model.fit(features_train, target_train)

        # Make predictions
        predictions = model.predict(features_val)

        # Evaluate the model
        mse = mean_squared_error(target_val, predictions)
        rmse = np.sqrt(mse)
        r2 = r2_score(target_val, predictions)

        print(f"Random Forest Model Performance:\nRMSE: {rmse}\nR²: {r2}")

        # Log metrics manually (optional, since autolog does this too)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)

        # Save the model locally and return it
        return model


@click.command()
@click.argument("train_path")
@click.argument("output_model_path")
@click.argument("bucket_name")
@click.argument("s3_key")
def train_model(train_path, output_model_path, bucket_name, s3_key):
    """
    CLI for training the model.

    :param train_path: Path to the training data file (CSV).
    :param output_model_path: Path to save the trained model locally.
    :param bucket_name: Name of the S3 bucket for saving the model.
    :param s3_key: Key for storing the model in the S3 bucket.
    """
    # Train the model
    model = train_random_forest_with_mlflow(train_path)

    # Save locally
    joblib.dump(model, output_model_path)
    print(f"Model saved locally to {output_model_path}")

    # Save to S3
    save_model_to_s3(output_model_path, bucket_name, s3_key)


if __name__ == "__main__":
    train_model()  # pylint: disable=no-value-for-parameter

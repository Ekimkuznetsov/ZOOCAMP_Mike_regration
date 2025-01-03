"""
Batch prediction module for bike demand forecasting.

This script provides a CLI for generating predictions on new data using
a pre-trained machine learning model. It supports loading models from both
local storage and S3.
"""

import click
import pandas as pd
import joblib
import boto3
from src.config import FEATURE_COLUMNS  # Import common feature list


def load_model_from_s3(bucket_name, s3_key, local_model_path):
    """
    Download the model from S3 and load it.

    :param bucket_name: Name of the S3 bucket.
    :param s3_key: Key of the model file in S3.
    :param local_model_path: Local path to save the model file.
    :return: Loaded model.
    """
    s3 = boto3.client("s3", endpoint_url="http://localhost:4566")
    s3.download_file(bucket_name, s3_key, local_model_path)
    return joblib.load(local_model_path)


def preprocess_data(data):
    """
    Apply feature engineering to the input data.

    :param data: DataFrame with raw input data.
    :return: DataFrame with processed features.
    """
    data["hour"] = pd.to_datetime(data["datetime"]).dt.hour
    data["is_weekend"] = (pd.to_datetime(data["datetime"]).dt.weekday >= 5).astype(int)
    return data[FEATURE_COLUMNS]  # Use the imported feature list


# pylint: disable=E1120
@click.command()
@click.argument("input_path")
@click.argument("output_path")
@click.option(
    "--model_path",
    default="models/random_forest_model.joblib",
    help="Path to the local model file.",
)
@click.option(
    "--bucket_name", default=None, help="S3 bucket name if loading the model from S3."
)
@click.option("--s3_key", default=None, help="S3 key if loading the model from S3.")
def predict(input_path, output_path, model_path, bucket_name, s3_key):
    """
    CLI for batch prediction.
    """
    # Load model
    if bucket_name and s3_key:
        model = load_model_from_s3(bucket_name, s3_key, model_path)
    else:
        model = joblib.load(model_path)

    # Load data
    input_data = pd.read_csv(input_path)

    # Preprocess data
    features = preprocess_data(input_data)

    # Predict
    predictions = model.predict(features)
    input_data["predictions"] = predictions

    # Save predictions
    input_data.to_csv(output_path, index=False)
    click.echo(f"Predictions saved to {output_path}")


if __name__ == "__main__":
    predict()

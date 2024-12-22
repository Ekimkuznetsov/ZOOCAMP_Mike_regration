import click
import pandas as pd
import joblib
import boto3


def load_model_from_s3(bucket_name, s3_key, local_model_path):
    """Download the model from S3 and load it."""
    s3 = boto3.client("s3", endpoint_url="http://localhost:4566")
    s3.download_file(bucket_name, s3_key, local_model_path)
    return joblib.load(local_model_path)


def preprocess_data(data):
    """Apply feature engineering to the data."""
    data["hour"] = pd.to_datetime(data["datetime"]).dt.hour
    data["is_weekend"] = (pd.to_datetime(data["datetime"]).dt.weekday >= 5).astype(int)
    features = [
        "hour",
        "temp",
        "humidity",
        "windspeed",
        "season",
        "weather",
        "workingday",
        "is_weekend",
    ]
    return data[features]


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
    Arguments:
    - input_path: Path to the input data file (CSV).
    - output_path: Path to save the predictions (CSV).
    """
    # Load model
    if bucket_name and s3_key:
        model = load_model_from_s3(bucket_name, s3_key, model_path)
    else:
        model = joblib.load(model_path)

    # Load data
    data = pd.read_csv(input_path)

    # Preprocess data
    X = preprocess_data(data)

    # Predict
    predictions = model.predict(X)
    data["predictions"] = predictions

    # Save predictions
    data.to_csv(output_path, index=False)
    click.echo(f"Predictions saved to {output_path}")


if __name__ == "__main__":
    predict()

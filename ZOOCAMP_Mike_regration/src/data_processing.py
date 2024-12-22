import click
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def process_datetime(data):
    """Convert datetime and extract useful features."""
    data["datetime"] = pd.to_datetime(data["datetime"])
    data["hour"] = data["datetime"].dt.hour
    data["day"] = data["datetime"].dt.day
    data["month"] = data["datetime"].dt.month
    data["year"] = data["datetime"].dt.year
    data["weekday"] = data["datetime"].dt.weekday
    data["is_weekend"] = data["weekday"].apply(
        lambda x: 1 if x >= 5 else 0
    )
    return data


def encode_categorical(data):
    """Convert specific columns to categorical types."""
    categorical_cols = ["season", "weather", "workingday"]
    for col in categorical_cols:
        data[col] = data[col].astype("category")
    return data


def scale_features(data, feature_columns):
    """Scale numerical features."""
    scaler = StandardScaler()
    data[feature_columns] = scaler.fit_transform(data[feature_columns])
    return data


def preprocess_data(data):
    data = process_datetime(data)
    data = encode_categorical(data)
    feature_columns = ["temp", "atemp", "humidity", "windspeed", "season", "weather", "workingday"]
    data = scale_features(data, feature_columns)

    # Зберігайте всі необхідні колонки
    required_columns = ["datetime", "casual", "count", "day", "month", "registered", "weekday", "year"] + feature_columns
    return data[required_columns]




@click.command()
@click.argument("input_path")
@click.argument("train_output_path")
@click.argument("test_output_path")
@click.option("--test_size", default=0.2, help="Proportion of data to use as the test set.")
def split_and_process_data(input_path, train_output_path, test_output_path, test_size):
    """Load, preprocess, and split the data."""
    # Load data
    data = pd.read_csv(input_path)

    # Preprocess data
    processed_data = preprocess_data(data)

    # Split data
    train_data, test_data = train_test_split(processed_data, test_size=test_size, random_state=42)

    # Save train and test data
    train_data.to_csv(train_output_path, index=False)
    test_data.to_csv(test_output_path, index=False)

    click.echo(f"Data split and saved: train -> {train_output_path}, test -> {test_output_path}")


if __name__ == "__main__":
    split_and_process_data()

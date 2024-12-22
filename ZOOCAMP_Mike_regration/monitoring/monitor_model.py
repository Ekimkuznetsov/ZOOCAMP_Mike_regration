import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, RegressionPreset


def validate_columns(data, required_columns, dataset_name):
    """
    Validate that all required columns are present in the dataset.

    :param data: DataFrame to validate.
    :param required_columns: List of required columns.
    :param dataset_name: Name of the dataset for better error reporting.
    """
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        raise KeyError(f"Columns {missing_columns} are missing in {dataset_name}")


def generate_monitoring_report(train_data_path, test_data_path, report_path):
    """
    Generate an Evidently monitoring report comparing training and test data.

    :param train_data_path: Path to the training dataset (CSV)
    :param test_data_path: Path to the test dataset (CSV)
    :param report_path: Path to save the HTML report
    """
    # Load datasets
    train_data = pd.read_csv(train_data_path)
    test_data = pd.read_csv(test_data_path)

    # Validate datetime column
    required_columns = ["datetime", "temp", "atemp", "humidity", "windspeed"]
    validate_columns(train_data, required_columns, "training data")
    validate_columns(test_data, required_columns, "test data")

    # Drop unnecessary columns for monitoring if they exist
    train_data = train_data[required_columns]
    test_data = test_data[required_columns]

    # Ensure datetime is in correct format
    train_data["datetime"] = pd.to_datetime(train_data["datetime"], errors="coerce")
    test_data["datetime"] = pd.to_datetime(test_data["datetime"], errors="coerce")

    # Create report
    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=train_data, current_data=test_data)

    # Save report
    report.save_html(report_path)
    print(f"Report saved to {report_path}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate monitoring report")
    parser.add_argument("train_data_path", type=str, help="Path to the training dataset")
    parser.add_argument("test_data_path", type=str, help="Path to the test dataset")
    parser.add_argument("report_path", type=str, help="Path to save the HTML report")

    args = parser.parse_args()

    generate_monitoring_report(args.train_data_path, args.test_data_path, args.report_path)

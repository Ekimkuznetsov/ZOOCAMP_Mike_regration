import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, RegressionPreset


def generate_monitoring_report(train_data_path, prediction_data_path, report_path):
    """
    Generate an Evidently monitoring report comparing training and prediction data.

    :param train_data_path: Path to the training dataset (CSV)
    :param prediction_data_path: Path to the dataset with predictions (CSV)
    :param report_path: Path to save the HTML report
    """
    # Load datasets
    train_data = pd.read_csv(train_data_path)
    prediction_data = pd.read_csv(prediction_data_path)

    # Define the report
    report = Report(metrics=[
        DataDriftPreset(),
        RegressionPreset()
    ])

    # Run the report
    report.run(reference_data=train_data, current_data=prediction_data)

    # Save report
    report.save_html(report_path)
    print(f"Report saved to {report_path}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate monitoring report")
    parser.add_argument("train_data_path", type=str, help="Path to the training dataset")
    parser.add_argument("prediction_data_path", type=str, help="Path to the dataset with predictions")
    parser.add_argument("report_path", type=str, help="Path to save the HTML report")

    args = parser.parse_args()

    generate_monitoring_report(args.train_data_path, args.prediction_data_path, args.report_path)
    
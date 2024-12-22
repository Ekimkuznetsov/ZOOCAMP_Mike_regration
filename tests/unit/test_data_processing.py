import pytest
import pandas as pd
from src.data_processing import preprocess_data


def test_preprocess_data():
    # Sample data
    data = pd.DataFrame(
        {
            "datetime": ["2023-01-01 00:00:00", "2023-01-01 01:00:00"],
            "season": [1, 2],
            "holiday": [0, 1],
            "workingday": [1, 0],
            "weather": [1, 2],
            "temp": [10.5, 20.3],
            "atemp": [12.3, 21.4],
            "humidity": [80, 50],
            "windspeed": [10, 15],
            "casual": [0, 0],
            "registered": [10, 20],
            "count": [10, 20],
        }
    )
    processed_data = preprocess_data(data)
    # Check for all expected columns
    expected_columns = [
        "datetime", "casual", "count", "registered", "weekday", "is_weekend",
        "hour", "day", "month", "year", "temp", "atemp", "humidity", "windspeed"
    ]
    for col in expected_columns:
        assert col in processed_data.columns, f"Missing column: {col}"


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
    assert "hour" in processed_data.columns
    assert "is_weekend" in processed_data.columns

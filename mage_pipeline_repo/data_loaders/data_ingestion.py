"""
Data ingestion block for bike demand prediction.

This block loads the raw dataset, performs initial checks, and saves the processed data.
"""

import pandas as pd
import os

RAW_DATA_PATH = 'data/raw'
PROCESSED_DATA_PATH = 'data/processed'

def execute(**kwargs):
    """Load raw data and save the processed data.

    This function reads raw training and testing datasets, ensures they have the correct
    structure, and saves them for further processing.

    Raises:
        FileNotFoundError: If the raw data files are not found.
        Exception: For any other runtime errors during data ingestion.
    """
    try:
        # Ensure processed data directory exists
        os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)

        # Load raw data
        train_file = os.path.join(RAW_DATA_PATH, 'train_bikes.csv')
        test_file = os.path.join(RAW_DATA_PATH, 'test_bikes.csv')

        train_data = pd.read_csv(train_file)
        test_data = pd.read_csv(test_file)

        # Perform basic checks
        assert 'datetime' in train_data.columns, "Train data missing 'datetime' column."
        assert 'datetime' in test_data.columns, "Test data missing 'datetime' column."

        # Save processed data
        train_data.to_csv(os.path.join(PROCESSED_DATA_PATH, 'train_bikes_processed.csv'), index=False)
        test_data.to_csv(os.path.join(PROCESSED_DATA_PATH, 'test_bikes_processed.csv'), index=False)

        print("Data ingestion completed successfully.")

    except FileNotFoundError as e:
        print(f"File not found: {e}")
        raise
    except Exception as e:
        print(f"An error occurred during data ingestion: {e}")
        raise

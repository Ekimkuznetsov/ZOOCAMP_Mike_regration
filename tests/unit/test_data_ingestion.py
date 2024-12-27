"""
Data ingestion block for bike demand prediction.
"""

from mage_ai.data_preparation.decorators import data_loader
import pandas as pd
import os

RAW_DATA_PATH = 'data/raw'
PROCESSED_DATA_PATH = 'data/processed'

@data_loader
def load_data(*args, **kwargs):
    """
    Load raw data and save the processed data.
    """
    try:
        print("Starting data ingestion...")

        # Ensure processed data directory exists
        os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)
        print(f"Processed data directory: {PROCESSED_DATA_PATH}")

        # Load raw data
        train_file = os.path.join(RAW_DATA_PATH, 'train_bikes.csv')
        test_file = os.path.join(RAW_DATA_PATH, 'test_bikes.csv')

        print(f"Loading train data from {train_file}")
        print(f"Loading test data from {test_file}")

        train_data = pd.read_csv(train_file)
        test_data = pd.read_csv(test_file)

        # Perform basic checks
        assert 'datetime' in train_data.columns, "Train data missing 'datetime' column."
        assert 'datetime' in test_data.columns, "Test data missing 'datetime' column."

        # Save processed data
        train_output = os.path.join(PROCESSED_DATA_PATH, 'train_bikes_processed.csv')
        test_output = os.path.join(PROCESSED_DATA_PATH, 'test_bikes_processed.csv')

        train_data.to_csv(train_output, index=False)
        test_data.to_csv(test_output, index=False)

        print(f"Train data saved to {train_output}")
        print(f"Test data saved to {test_output}")
        print("Data ingestion completed successfully.")

    except FileNotFoundError as e:
        print(f"File not found: {e}")
        raise
    except Exception as e:
        print(f"An error occurred during data ingestion: {e}")
        raise

if __name__ == "__main__":
    load_data()

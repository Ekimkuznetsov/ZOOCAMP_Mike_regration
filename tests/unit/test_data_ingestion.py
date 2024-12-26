"""
Unit tests for the data ingestion block.
"""

import os
import pandas as pd
import unittest
from mage_pipeline_repo.data_loaders.data_ingestion import execute


class TestDataIngestion(unittest.TestCase):
    """Test suite for the data ingestion block."""

    def test_execute(self):
        """Test the data ingestion block."""
        raw_path = 'data/raw'
        processed_path = 'data/processed'

        # Ensure raw data exists
        self.assertTrue(os.path.exists(raw_path), "Raw data path does not exist.")

        # Run the block
        execute()

        # Check processed files
        train_file = os.path.join(processed_path, 'train_bikes_processed.csv')
        test_file = os.path.join(processed_path, 'test_bikes_processed.csv')

        self.assertTrue(os.path.exists(train_file), "Processed train data not found.")
        self.assertTrue(os.path.exists(test_file), "Processed test data not found.")

        # Validate structure
        train_data = pd.read_csv(train_file)
        self.assertIn('datetime', train_data.columns, "'datetime' column missing in train data.")


if __name__ == "__main__":
    unittest.main()

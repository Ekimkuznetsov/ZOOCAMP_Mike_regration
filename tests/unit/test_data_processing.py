"""
Unit tests for the data processing block.
"""

import os
import pandas as pd
import unittest
from mage_pipeline_repo.pipelines.bike_demand_prediction.data_processing import execute


class TestDataProcessing(unittest.TestCase):
    """Test suite for the data processing block."""

    def test_execute(self):
        """Test the data processing block."""
        processed_path = 'data/processed'
        final_path = 'data/final'

        # Ensure processed data exists
        train_file = os.path.join(processed_path, 'train_bikes_processed.csv')
        test_file = os.path.join(processed_path, 'test_bikes_processed.csv')
        self.assertTrue(os.path.exists(train_file), "Processed train data not found.")
        self.assertTrue(os.path.exists(test_file), "Processed test data not found.")

        # Run the block
        execute()

        # Check final files
        train_final = os.path.join(final_path, 'train_bikes_final.csv')
        test_final = os.path.join(final_path, 'test_bikes_final.csv')
        self.assertTrue(os.path.exists(train_final), "Final train data not found.")
        self.assertTrue(os.path.exists(test_final), "Final test data not found.")

        # Validate structure
        train_data = pd.read_csv(train_final)
        self.assertIn('hour', train_data.columns, "'hour' column missing in train data.")
        self.assertIn('day_of_week', train_data.columns, "'day_of_week' column missing in train data.")


if __name__ == "__main__":
    unittest.main()

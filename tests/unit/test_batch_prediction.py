"""
Unit tests for the batch prediction block.
"""

import os
import unittest
from mage_pipeline_repo.pipelines.bike_demand_prediction.batch_prediction import execute


class TestBatchPrediction(unittest.TestCase):
    """Test suite for the batch prediction block."""

    def test_execute(self):
        """Test the batch prediction block."""
        final_path = 'data/final'
        predictions_path = 'data/predictions'

        # Ensure final test data exists
        test_file = os.path.join(final_path, 'test_bikes_final.csv')
        self.assertTrue(os.path.exists(test_file), "Final test data not found.")

        # Run the block
        execute()

        # Check if predictions are saved
        predictions_file = os.path.join(predictions_path, 'predictions.csv')
        self.assertTrue(os.path.exists(predictions_file), "Predictions file not found.")


if __name__ == "__main__":
    unittest.main()

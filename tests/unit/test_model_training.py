"""
Unit tests for the model training block.
"""

import os
import shutil
import unittest
from mage_pipeline_repo.pipelines.bike_demand_prediction.model_training import execute


class TestModelTraining(unittest.TestCase):
    """Test suite for the model training block."""

    def setUp(self):
        """Set up test environment."""
        self.test_model_path = 'models/test_random_forest_model'

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(self.test_model_path):
            shutil.rmtree(self.test_model_path)  # Remove directory if it exists

    def test_execute(self):
        """Test the model training block."""
        final_path = 'data/final'

        # Ensure final training data exists
        train_file = os.path.join(final_path, 'train_bikes_final.csv')
        self.assertTrue(os.path.exists(train_file), "Final training data not found.")

        # Run the block
        execute(model_path=self.test_model_path)

        # Check if model is saved
        self.assertTrue(os.path.exists(self.test_model_path), "Trained model directory not found.")


if __name__ == "__main__":
    unittest.main()

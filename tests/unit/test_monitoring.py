"""
Unit tests for the monitoring block.
"""

import os
import unittest
from mage_pipeline_repo.pipelines.bike_demand_prediction.monitoring import execute


class TestMonitoring(unittest.TestCase):
    """Test suite for the monitoring block."""

    def setUp(self):
        """Set up test environment."""
        self.reports_path = 'reports'

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(self.reports_path):
            for file in os.listdir(self.reports_path):
                os.remove(os.path.join(self.reports_path, file))

    def test_execute(self):
        """Test the monitoring block."""
        final_path = 'data/final'
        predictions_path = 'data/predictions'

        # Ensure necessary files exist
        test_file = os.path.join(final_path, 'test_bikes_final.csv')
        predictions_file = os.path.join(predictions_path, 'predictions.csv')
        self.assertTrue(os.path.exists(test_file), "Test data not found.")
        self.assertTrue(os.path.exists(predictions_file), "Predictions file not found.")

        # Run the block
        execute()

        # Check if the drift report is generated
        drift_report_file = os.path.join(self.reports_path, 'drift_report.html')
        self.assertTrue(os.path.exists(drift_report_file), "Drift report not generated.")


if __name__ == "__main__":
    unittest.main()

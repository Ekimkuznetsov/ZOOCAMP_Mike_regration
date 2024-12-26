# tests/unit/test_data_processing.py
import sys
import unittest
import pandas as pd
from pandas.testing import assert_frame_equal

# Adding the path to the src folder to be able to import modules from it
sys.path.append('src')

from data_processing import preprocess_data

class TestPreprocessData(unittest.TestCase):
    """
    Test class for testing the preprocess_data function from data_processing module.
    """

    def test_preprocess_data(self):
        """
        Test the preprocess_data function to ensure it correctly processes the input data.
        This test checks if the function correctly extracts features from the datetime column,
        drops unnecessary columns, and normalizes specified numeric features.
        """
        # Create test data
        data = pd.DataFrame({
            'datetime': ['2021-01-01 00:00:00', '2021-01-01 01:00:00'],
            'season': [1, 1],
            'holiday': [0, 0],
            'workingday': [0, 0],
            'weather': [1, 1],
            'temp': [9.84, 9.02],
            'atemp': [14.395, 13.635],
            'humidity': [81, 80],
            'windspeed': [0, 0],
            'casual': [3, 8],
            'registered': [13, 32],
            'count': [16, 40]
        })

        # Expected results after processing
        expected_data = data.copy()
        expected_data['hour'] = [0, 1]
        expected_data['day_of_week'] = [4, 4]
        expected_data['month'] = [1, 1]
        expected_data = expected_data.drop(['datetime', 'atemp'], axis=1)

        # Test the preprocess_data function
        processed_data = preprocess_data(data)
        assert_frame_equal(processed_data, expected_data)

if __name__ == '__main__':
    unittest.main()
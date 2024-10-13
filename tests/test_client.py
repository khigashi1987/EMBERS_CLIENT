import unittest
import pandas as pd
from embers_client import EMBERSClient

class TestEMBERSClient(unittest.TestCase):
    def setUp(self):
        self.client = EMBERSClient()

    def test_get_samples(self):
        conditions = {"Age": {"min": 45, "max": 55},
                    "BiologicalSex": ["Male"],
                    "BMI": {"min":25.0, "max":30.0},
                    "GeographicLocation": ["United States"]}
        sample_ids = self.client.get_samples(conditions)
        self.assertIsInstance(sample_ids, list)

    def test_get_composition_by_ids(self):
        sample_ids = ["ERS1015875", "SRS2836456"]
        composition_df = self.client.get_composition_by_ids(sample_ids)
        self.assertIsInstance(composition_df, pd.DataFrame)

    def test_get_composition_by_metadata(self):
        conditions = {"Age": {"min": 45, "max": 55},
                    "BiologicalSex": ["Male"],
                    "BMI": {"min":25.0, "max":30.0},
                    "GeographicLocation": ["United States"]}
        composition_df = self.client.get_composition_by_metadata(conditions)
        self.assertIsInstance(composition_df, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()

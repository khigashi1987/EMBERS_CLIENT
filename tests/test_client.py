import unittest
from embers_client import EMBERSClient

class TestEMBERSClient(unittest.TestCase):
    def setUp(self):
        self.client = EMBERSClient()

    def test_get_samples(self):
        conditions = {"Age": {"min": 20, "max": 30}}
        sample_ids = self.client.get_samples(conditions)
        self.assertIsInstance(sample_ids, list)

    def test_get_composition_by_ids(self):
        sample_ids = ["SRS000001", "SRS000002"]
        composition_df = self.client.get_composition_by_ids(sample_ids)
        self.assertIsInstance(composition_df, pd.DataFrame)

    def test_get_composition_by_metadata(self):
        conditions = {"country": ["USA", "Japan"]}
        composition_df = self.client.get_composition_by_metadata(conditions)
        self.assertIsInstance(composition_df, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()

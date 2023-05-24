import unittest
import os
from src.utils.DataExporter import DataExporter

class TestDataExporter(unittest.TestCase):
    def setUp(self):
        self.data_exporter = DataExporter()

    def test_export_data(self):
        data = {"test": "data"}
        filename = "test_export_data.json"
        self.data_exporter.export_data(data, filename)
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)

if __name__ == '__main__':
    unittest.main()

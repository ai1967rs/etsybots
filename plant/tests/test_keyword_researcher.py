import unittest
from src.researchers.KeywordResearcher import KeywordResearcher

class TestKeywordResearcher(unittest.TestCase):
    def setUp(self):
        self.keyword_researcher = KeywordResearcher()

    def test_get_best_keywords(self):
        product_details = {
            "title": "Test Product",
            "description": "This is a test product.",
            "price": "10.00",
            "tags": ["test", "product"],
        }
        keywords = self.keyword_researcher.get_best_keywords(product_details)
        # TODO: Add assertions to check if the best keywords were fetched correctly

if __name__ == '__main__':
    unittest.main()

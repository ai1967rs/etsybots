import unittest
from src.helpers.SeoHelper import SeoHelper

class TestSeoHelper(unittest.TestCase):
    def setUp(self):
        self.seo_helper = SeoHelper()

    def test_suggest_seo_improvements(self):
        product_details = {
            "title": "Test Product",
            "description": "This is a test product.",
            "price": "10.00",
            "tags": ["test", "product"],
        }
        seo_suggestions = self.seo_helper.suggest_seo_improvements(product_details)
        # TODO: Add assertions to check if the SEO suggestions were generated correctly

if __name__ == '__main__':
    unittest.main()

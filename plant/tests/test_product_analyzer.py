import unittest
from src.analyzers.ProductAnalyzer import ProductAnalyzer
from src.bots.EtsyBot import EtsyBot

class TestProductAnalyzer(unittest.TestCase):
    def setUp(self):
        self.bot = EtsyBot()
        self.bot.login()
        self.analyzer = ProductAnalyzer(self.bot.driver)

    def test_get_product_listings(self):
        self.bot.navigate_to_shop()
        product_urls = self.analyzer.get_product_listings()
        # TODO: Add assertions to check if the product listings were fetched correctly

    def test_get_product_details(self):
        self.bot.navigate_to_shop()
        product_urls = self.analyzer.get_product_listings()
        for url in product_urls:
            product_details = self.analyzer.get_product_details(url)
            # TODO: Add assertions to check if the product details were fetched correctly

    def tearDown(self):
        self.bot.logout()

if __name__ == '__main__':
    unittest.main()

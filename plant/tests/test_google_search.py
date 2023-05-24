import unittest
from src.utils.GoogleSearch import GoogleSearch
from src.bots.EtsyBot import EtsyBot

class TestGoogleSearch(unittest.TestCase):
    def setUp(self):
        self.bot = EtsyBot()
        self.bot.login()
        self.google_search = GoogleSearch(self.bot.driver)

    def test_search(self):
        self.google_search.search("test query")
        # TODO: Add assertions to check if the search was executed correctly

    def tearDown(self):
        self.bot.logout()

if __name__ == '__main__':
    unittest.main()

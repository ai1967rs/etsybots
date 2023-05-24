import logging
from EtsyBot import EtsyBot
from ProductAnalyzer import ProductAnalyzer
from SeoHelper import SeoHelper
from GoogleSearch import GoogleSearch
from KeywordResearcher import KeywordResearcher
from CompetitorAnalyzer import CompetitorAnalyzer
from DataExporter import DataExporter
from UserInteraction import UserInteraction
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

# Configure logging
logging.basicConfig(filename='etsy_bot.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def main():
    # Instantiate all the classes
    bot = EtsyBot()
    analyzer = ProductAnalyzer(bot.driver)
    seo_helper = SeoHelper()
    google_search = GoogleSearch(bot.driver)
    keyword_researcher = KeywordResearcher()
    competitor_analyzer = CompetitorAnalyzer()
    data_exporter = DataExporter()
    user_interaction = UserInteraction()

    # Start the process
    try:
        bot.login()
    except (NoSuchElementException, TimeoutException, WebDriverException) as e:
        logging.error(f"An error occurred during login: {str(e)}")
        return
    
    try:
        bot.navigate_to_shop()
        product_urls = analyzer.get_product_listings()

        for url in product_urls:
            product_details = analyzer.get_product_details(url)
            seo_suggestions = seo_helper.suggest_seo_improvements(product_details)
            keywords = keyword_researcher.get_best_keywords(product_details)
            competitor_analysis = competitor_analyzer.analyze_competitors(product_details)

            # Combine all the data
            data = {
                "product_details": product_details,
                "seo_suggestions": seo_suggestions,
                "keywords": keywords,
                "competitor_analysis": competitor_analysis,
            }

            # Export the data
            data_exporter.export_data(data, "product_analysis.json")

            # Handle user interaction
            user_interaction.handle_user_interaction()

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
    finally:
        bot.logout()

if __name__ == "__main__":
    main()

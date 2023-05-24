import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ProductAnalyzer:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.logger = logging.getLogger('ProductAnalyzer')

    def get_product_listings(self):
        try:
            product_listing_links = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "v2-listing-card__info")))
            self.logger.info("Successfully fetched product listings.")
            return [link.get_attribute("href") for link in product_listing_links]
        except TimeoutException as e:
            self.logger.error("Timeout occurred while fetching product listings.")
            raise e
        except Exception as e:
            self.logger.error("An error occurred while fetching product listings.")
            raise e

    def get_product_details(self, product_url):
        try:
            self.driver.get(product_url)
            title = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "wt-mb-xs-2"))).text
            description = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "wt-break-word"))).text
            price = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "wt-text-title-01"))).text
            tags = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "wt-display-inline-block")))
            tags = [tag.text for tag in tags]

            self.logger.info("Successfully fetched product details.")

            return {
                "title": title,
                "description": description,
                "price": price,
                "tags": tags,
            }
        except TimeoutException as e:
            self.logger.error("Timeout occurred while fetching product details.")
            raise e
        except Exception as e:
            self.logger.error("An error occurred while fetching product details.")
            raise e

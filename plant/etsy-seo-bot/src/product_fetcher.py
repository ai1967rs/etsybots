import logging

class ProductFetcher:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.logger = logging.getLogger('ProductFetcher')

    def get_product_details(self, product_url):
        try:
            self.driver.get(product_url)
            title = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "wt-mb-xs-2"))).text
            description = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "wt-break-word"))).text
            price = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "wt-text-title-01"))).text
            tags = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "wt-display-inline-block")))
            tags = [tag.text for tag in tags]

            self.logger.info("Successfully fetched product details for URL: {}".format(product_url))

            return {
                "title": title,
                "description": description,
                "price": price,
                "tags": tags,
            }
        except Exception as e:
            self.logger.error("An error occurred while fetching product details for URL: {}".format(product_url))
            raise e

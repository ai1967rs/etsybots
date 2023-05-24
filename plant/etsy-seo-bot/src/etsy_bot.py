import json
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

class EtsyBot:
    def __init__(self):
        with open('config.json') as f:
            config = json.load(f)
        self.username = config['username']
        self.password = config['password']
        self.driver = webdriver.Chrome(config['chrome_driver_path'])
        self.wait = WebDriverWait(self.driver, config['timeout'])
        self.logger = logging.getLogger('EtsyBot')

    def login(self):
        try:
            self.driver.get("https://www.etsy.com/signin")
            username_field = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
            username_field.clear()
            username_field.send_keys(self.username)

            password_field = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
            password_field.clear()
            password_field.send_keys(self.password)

            sign_in_button = self.wait.until(EC.presence_of_element_located((By.NAME, "submit_attempt")))
            sign_in_button.click()
            self.logger.info("Logged in successfully.")
        except (NoSuchElementException, TimeoutException, WebDriverException) as e:
            self.logger.error(f"An error occurred during login: {str(e)}")

    def logout(self):
        try:
            self.driver.get("https://www.etsy.com/your/profile")
            sign_out_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
            sign_out_link.click()
            self.logger.info("Logged out successfully.")
        except (NoSuchElementException, TimeoutException, WebDriverException) as e:
            self.logger.error(f"An error occurred while logging out: {str(e)}")

    def navigate_to_shop(self):
        try:
            self.driver.get("https://www.etsy.com/shop/LimitlessLifewea?ref=seller-platform-mcnav")
            self.logger.info("Navigated to the shop.")
        except (NoSuchElementException, TimeoutException, WebDriverException) as e:
            self.logger.error(f"An error occurred while navigating to the shop: {str(e)}")

    def handle_captcha(self):
        # Check if a CAPTCHA is present
        captcha = self.driver.find_elements_by_id('captcha')
        if captcha:
            print("CAPTCHA detected. Please solve it manually, then press Enter to continue.")
            input()  # Pause execution until the user presses Enter

    def login(self):
        self.login()
        self.handle_captcha()

    def navigate_to_shop(self):
        self.navigate_to_shop()
        self.handle_captcha()

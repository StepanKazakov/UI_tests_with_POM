from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_locators import accept_cookies_button


class CookieHandler:
    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, accept_cookies_button))).click()
        except TimeoutException:
            pass

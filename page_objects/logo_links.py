from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_locators import yandex_logo, scooter_logo_link, dzen_menu


class ClickLink:
    def __init__(self, driver):
        self.driver = driver

    def return_to_main_from_logo(self):
        self.driver.find_element(By.XPATH, scooter_logo_link).click()

    def go_to_yandex_from_logo(self):
        self.driver.find_element(By.XPATH, yandex_logo).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, dzen_menu)))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.faq_list_locators import *


class FAQPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def toggle_faq_question(self, index):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, faq_section_locator)))
        question_locator = faq_question_locator_template.format(index)
        question = self.wait.until(EC.element_to_be_clickable((By.XPATH, question_locator)))
        question.click()
        return question.get_attribute("aria-expanded") == "true"

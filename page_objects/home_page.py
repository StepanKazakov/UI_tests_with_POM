from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from locators.home_page_locators import *
from locators.scooter_order_locators import order_next_button
from page_objects.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def accept_cookies(self):
        try:
            self.click_element((By.XPATH, accept_cookies_button))
        except TimeoutException:
            pass

    def click_order_btn_in_header(self):
        self.click_element((By.XPATH, order_button_top))

    def click_order_btn_under_description(self):
        self.scroll_page_center()
        self.scroll_to_element((By.XPATH, order_button_big))
        self.click_element((By.XPATH, order_button_big))

    def click_scooter_logo(self):
        self.wait_for_clickable((By.XPATH, order_next_button))
        self.click_element((By.XPATH, scooter_logo_link))
        return self.current_url

    def go_to_yandex_from_logo(self):
        self.click_element((By.XPATH, yandex_logo))
        self.switch_to_new_window()
        self.wait_for_visibility((By.XPATH, dzen_menu))
        return self.current_url

    def toggle_faq_question(self, index):
        question_locator = faq_question_locator_template.format(index)
        answer_locator = faq_answer_locator_template.format(index)
        self.scroll_page_down()
        self.wait_for_clickable((By.XPATH, faq_section_locator))
        self.click_element((By.XPATH, question_locator))
        return self.get_text((By.XPATH, answer_locator))

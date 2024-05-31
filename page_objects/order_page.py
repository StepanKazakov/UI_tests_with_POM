import random
from selenium.webdriver.common.by import By

from locators.scooter_order_locators import *
from page_objects.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def make_order_step_1(self, name, surname, address, phone):
        self.input_text((By.XPATH, input_name), name)
        self.input_text((By.XPATH, input_surname), surname)
        self.input_text((By.XPATH, input_address), address)
        self.choose_metro_station()
        self.input_text((By.XPATH, input_phone), phone)
        self.click_next_button()

    def make_order_step_2(self, color, comment):
        self.set_date()
        self.choose_period()
        self.select_color(color)
        self.input_text((By.XPATH, input_comment), comment)
        self.submit_order()

    def choose_metro_station(self):
        self.click_element((By.XPATH, dropdown_metro))
        options = self.wait_for_all_elements((By.XPATH, list_of_metro_stations))
        random.choice(options).click()

    def click_next_button(self):
        self.scroll_to_element((By.XPATH, order_next_button))
        self.click_element((By.XPATH, order_next_button))

    def set_date(self):
        self.click_element((By.XPATH, input_date))
        random_day = random.randint(10, 28)
        self.click_element((By.XPATH, day_locator_template.format(random_day)))

    def choose_period(self):
        self.click_element((By.XPATH, dropdown_period))
        periods = self.wait_for_all_elements((By.XPATH, list_of_periods))
        random.choice(periods).click()

    def select_color(self, color):
        if color == "black":
            self.click_element((By.XPATH, checkbox_black))
        elif color == "grey":
            self.click_element((By.XPATH, checkbox_grey))

    def submit_order(self):
        self.click_element((By.XPATH, do_order_button))
        self.click_element((By.XPATH, confirm_order_button))

    def get_order_confirmation(self):
        return self.get_text((By.XPATH, order_success_message))

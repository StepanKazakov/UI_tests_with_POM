from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from locators.scooter_order_locators import *
from locators.base_locators import yandex_logo, scooter_logo_link, dzen_menu


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_order_button_top(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, order_button_top))).click()

    def click_order_button_big(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
        button = self.wait.until(EC.presence_of_element_located((By.XPATH, order_button_big)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        button.click()

    def make_order_step_1(self, name, surname, address, phone):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, input_name))).send_keys(name)
        self.driver.find_element(By.XPATH, input_surname).send_keys(surname)
        self.driver.find_element(By.XPATH, input_address).send_keys(address)
        self.choose_metro_station()
        self.driver.find_element(By.XPATH, input_phone).send_keys(phone)
        self.click_next_button()

    def make_order_step_2(self, color, comment):
        self.set_date()
        self.choose_period()
        self.select_color(color)
        self.driver.find_element(By.XPATH, input_comment).send_keys(comment)
        self.submit_order()

    def choose_metro_station(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_metro))).click()
        options = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, list_of_metro_stations)))
        random.choice(options).click()

    def click_next_button(self):
        next_button = self.wait.until(EC.presence_of_element_located((By.XPATH, order_next_button)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        next_button.click()

    def set_date(self):
        random_day = random.randint(10, 28)
        day_locator = f'.//div[contains(@class, "react-datepicker__day") and text()="{random_day:02d}"]'
        self.driver.find_element(By.XPATH, input_date).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, day_locator))).click()

    def choose_period(self):
        self.driver.find_element(By.XPATH, dropdown_period).click()
        periods = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, list_of_periods)))
        random.choice(periods).click()

    def select_color(self, color):
        if color == "black":
            self.driver.find_element(By.XPATH, checkbox_black).click()
        elif color == "grey":
            self.driver.find_element(By.XPATH, checkbox_grey).click()

    def submit_order(self):
        self.driver.find_element(By.XPATH, do_order_button).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, confirm_order_button))).click()

    def get_order_confirmation(self):
        confirmation_text = self.wait.until(EC.visibility_of_element_located((By.XPATH, order_success_message))).text
        return confirmation_text

    def go_to_order_status(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, see_order_status_button))).click()

    def return_to_main_from_logo(self):
        self.driver.find_element(By.XPATH, scooter_logo_link).click()

    def go_to_yandex_from_logo(self):
        self.driver.find_element(By.XPATH, yandex_logo).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait.until(EC.element_to_be_clickable((By.XPATH, dzen_menu)))

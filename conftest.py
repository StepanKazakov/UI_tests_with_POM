import pytest
from selenium import webdriver


base_url = 'https://qa-scooter.praktikum-services.ru/'

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.get(base_url)
    yield driver
    driver.quit()

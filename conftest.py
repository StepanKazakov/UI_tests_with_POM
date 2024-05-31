import pytest
from selenium import webdriver
from urls_data import base_url


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.get(base_url)
    yield driver
    driver.quit()


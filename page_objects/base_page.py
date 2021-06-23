import json
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from config.config_helper import load_test_config_json


class BasePage:

    def __init__(self, driver):
        test_settings = load_test_config_json()
        self.driver = driver
        self.time_list = test_settings['timeout_list']

    def open_url(self, url):
        self.driver.open(url)

    def get_actual_url(self):
        return self.driver.current_url

    def find_element(self, *element_locator):
        return self.driver.find_element(*element_locator)

    def wait_element_to_be_present(self, *element_locator, time):
        try:
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(*element_locator))
        except TimeoutException:
            print('Element not found: ' + element_locator[1])

    def wait_for_element_to_be_visible(self, *element_locator, time):
        try:
            WebDriverWait(self.driver, time).until(
                EC.visibility_of_element_located(*element_locator))
        except TimeoutException:
            print('Element was not visible: ' + element_locator[1])

    def click_element(self, *element_locator):
        element = self.find_element(*element_locator)
        element.click()

    def wait_and_click(self, *element_locator, time=30):
        self.wait_for_element_to_be_visible(*element_locator, time)
        element = self.find_element(*element_locator)
        element.click()

    def type_text(self, text, *element_locator, enter=True):
        input = self.wait_and_click(*element_locator)
        input.send_keys(text)
        if enter:
            input.send_keys(Keys.ENTER)

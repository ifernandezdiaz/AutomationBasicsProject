import json
import os
import logging
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from config.config_helper import load_test_config_json
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        test_settings = load_test_config_json()
        self.driver = driver
        self.time_list = test_settings['timeout_list']

    def __hover_over(self): #este metodo devuelve una instancia de ActionChains para poder hacer hover sobre algún elemento
        return ActionChains(self.driver)

    def open_url(self, url):
        self.driver.open(url)

    def get_actual_url(self):
        return self.driver.current_url

    def find_element(self, *element_locator):
        return self.driver.find_element(*element_locator)

    def find_elements(self, *element_locator):
        return self.driver.find_elements(*element_locator)

    def wait_element_to_be_present(self, time, *element_locator):
        try:
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(*element_locator))
        except TimeoutException:
            print('Element not found: ' + element_locator[1])

    def wait_for_element_to_be_visible(self, time, element_locator):
        try:
            WebDriverWait(self.driver, time).until(
                EC.visibility_of_element_located(element_locator))
        except TimeoutException:
            print('Element was not visible: ' + element_locator[1])

    def click_element(self, element_locator):
        element = self.find_element(*element_locator)
        element.click()

    def wait_and_click(self, time = 30, *element_locator):
        self.wait_for_element_to_be_visible(time, *element_locator)
        element = self.find_element(*element_locator)
        element.click()

    def type_text(self, text, enter=True, *element_locator):
        input = self.wait_and_click(*element_locator)
        input.send_keys(text)
        if enter:
            input.send_keys(Keys.ENTER)

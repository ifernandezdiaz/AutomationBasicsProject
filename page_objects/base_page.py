import json
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        with open(os.getcwd() + '/config/test_config.json') as test_config_file:
            test_settings = json.load(test_config_file)
            test_config_file.close()
        self.driver = driver
        self.timeout = test_settings['timeout']

    def open_url(self, url):
        self.driver.open(url)

    def get_actual_url(self):
        return self.driver.current_url

    def find_element(self, *element_locator):
        return self.driver.find_element(*element_locator)

    def find_elements(self, *element_locator):
        return self.driver.find_elements(*element_locator)

    def wait_element(self, *element_locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(element_locator))
        except TimeoutException:
            print('Element not found: ' + element_locator[1])

    def wait_and_click(self, *element_locator):
        self.wait_element(*element_locator)
        element = self.find_element(*element_locator)
        element.click()
        return element

    def type_text(self, text, *element_locator):
        input = self.wait_and_click(*element_locator)
        input.send_keys(text)
        input.send_keys(Keys.ENTER)

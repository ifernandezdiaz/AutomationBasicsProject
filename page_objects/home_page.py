from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import logging
from time import sleep
class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.btn_sign_in = (By.CLASS_NAME , 'login')


    def click_sign_in(self, time):
        self.wait_for_element_to_be_visible(self.btn_sign_in, time)
        self.click_element(self.btn_sign_in)

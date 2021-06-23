from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import logging
class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.btn_sign_in = (By.CLASS_NAME , 'login')


    def click_sign_in(self, time):
        self.wait_for_element_to_be_visible(time, *self.btn_sign_in,)
        self.click_element(self.btn_sign_in)
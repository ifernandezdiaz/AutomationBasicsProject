
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class HeaderPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.phone_location = (By.CSS_SELECTOR, '.shop-phone > strong')

    def get_phone(self):
        return self.find_element(*self.phone_location).text

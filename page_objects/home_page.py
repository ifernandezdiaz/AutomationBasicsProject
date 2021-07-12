from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import logging
from time import sleep
class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.btn_sign_in = (By.CLASS_NAME , 'login')
        self.frm_search_bar = (By.ID, "search_query_top")
        self.txt_logged_account_name = (By.CSS_SELECTOR, "a[title=\"View my customer account\"] >span")


    def click_sign_in(self, time):
        self.wait_and_click(self.btn_sign_in, time)

    def enter_text_on_search_bar(self, text):
        self.type_text(text, self.frm_search_bar, True)

    def get_logged_account_name(self):
        self.wait_for_element_to_be_visible(self.txt_logged_account_name)
        return (self.find_element(self.txt_logged_account_name).text)

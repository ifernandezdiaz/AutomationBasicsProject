from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.form_email = (By.ID, "email")
        self.form_password = (By.ID, "passwd")
        self.btn_sign_in = (By.ID, "SubmitLogin")

    def enter_email(self, text, time):
        self.wait_and_click(self.form_email, time)
        self.type_text(text, self.form_email)

    def enter_password(self, text, enter=False):
        self.wait_and_click(self.form_password)
        self.type_text(text, self.form_password, enter)

    def click_sign_in(self):
        self.wait_and_click(self.btn_sign_in)

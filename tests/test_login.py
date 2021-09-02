from tests.base_test import BaseTest
from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
import unittest

class LoginTest(BaseTest):


    def test_login_search_and_check_still_logged_in(self):
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        home_page.click_sign_in(self.time_list['very_low'])
        login_page.enter_email("lantola@sparkdigital.com", self.time_list['very_low'])
        login_page.enter_password("leonardo123")
        login_page.click_sign_in()
        home_page.enter_text_on_search_bar("dress")
        self.assertEqual(home_page.get_logged_account_name(), "leo exe")

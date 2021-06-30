from tests.base_test import BaseTest
from page_objects.home_page import HomePage

class LoginTest(BaseTest):

    def test_login(self):
        home_page = HomePage(self.driver)
        home_page.click_sign_in(self.time_list['very_low'])

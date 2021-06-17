from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from page_objects.header_page import HeaderPage

class TestMainPageValidations(BaseTest):

    def test_header_phone_validation(self):
        phone = HeaderPage(self.driver).get_phone()
        self.assertEqual(phone.text,'0123-456-789')

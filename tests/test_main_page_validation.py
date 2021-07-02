from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from page_objects.header_page import HeaderPage

class test_main_page_validations(BaseTest):



    def test_header_phone_validation(self):
        header_page = HeaderPage(self.driver)
        self.assertEqual(header_page.get_phone(),'0123-456-789')

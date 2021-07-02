from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from page_objects.body_page import BodyPage

class test_add_to_cart_validation(BaseTest):

    def test_add_to_cart_validation(self):
        body_page = BodyPage(self.driver)
        self.assertEqual(body_page.get_button_name(),'Add to cart')
        body_page.press_add_to_cart_button()
        self.assertEqual(body_page.get_item_cart(),'1')

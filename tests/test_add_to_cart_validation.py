from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from page_objects.body_page import BodyPage

class test_add_to_cart_validation(BaseTest):

    def test_add_to_cart_validation(self):
       
       self.assertEqual(BodyPage(self.driver).get_button_name(),'Add to cart')
       BodyPage(self.driver).press_add_to_cart_button()
       self.assertEqual(BodyPage(self.driver).get_item_cart(),'1')



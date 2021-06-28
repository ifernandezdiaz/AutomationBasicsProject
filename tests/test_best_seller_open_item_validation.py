from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from page_objects.body_page import BodyPage
import random

class test_best_seller_open_item_validation(BaseTest):

    def test_best_seller_open_item_validation(self):
       length = BodyPage(self.driver).click_best_sellers_tab()
       randomnum = random.randint(0, length-1)
       name = BodyPage(self.driver).get_best_seller_product_name(randomnum)
       BodyPage(self.driver).click_best_seller_product(randomnum)
       self.assertEqual(BodyPage(self.driver).get_product_detail_name(),name)

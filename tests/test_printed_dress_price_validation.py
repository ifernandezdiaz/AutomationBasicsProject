from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from page_objects.header_page import HeaderPage
from page_objects.body_page import BodyPage
import unittest

class test_printed_dress_price_validation(BaseTest):


    def test_printed_dress_price_validation(self):
        body_page = BodyPage(self.driver)
        body_page.click_women_dresses_evening_dresses_item()
        item = body_page.get_printed_dress_grid_item()
        self.assertEqual(body_page.get_item_price(item),'$50.99')

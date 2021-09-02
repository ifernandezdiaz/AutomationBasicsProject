from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from page_objects.header_page import HeaderPage
from page_objects.body_page import BodyPage
import unittest

class test_women_evening_dresses_validation(BaseTest):


    def test_women_evening_dresses_validation(self):
        body_page = BodyPage(self.driver)
        self.assertEqual(body_page.get_women_dresses_evening_dresses_item(),'Evening Dresses')
        body_page.click_women_dresses_evening_dresses_item()
        self.assertTrue(body_page.get_grid_list_count()>=1)

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from page_objects.header_page import HeaderPage
from page_objects.body_page import BodyPage
import unittest

class test_women_evening_dresses_validation(BaseTest):


    def test_filter_by_category_dresses(self):
        body_page = BodyPage(self.driver)
        body_page.click_on_dresses_menu_element()
        self.assertTrue(body_page.get_grid_list_count()==5)

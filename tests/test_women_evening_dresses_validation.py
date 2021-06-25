from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from page_objects.body_page import BodyPage

class test_women_evening_dresses_validation(BaseTest):

    def test_women_evening_dresses_validation(self):
       self.assertEqual(BodyPage(self.driver).get_women_dresses_evening_dresses_item(),'Evening Dresses')
       BodyPage(self.driver).click_women_dresses_evening_dresses_item()
       self.assertTrue(BodyPage(self.driver).get_grid_list_count()>=1)

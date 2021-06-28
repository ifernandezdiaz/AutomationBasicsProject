from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from page_objects.body_page import BodyPage

class test_main_page_printed_summer_dress_validation(BaseTest):

    def test_main_page_printed_summer_dress_validation(self):
       self.assertEqual(BodyPage(self.driver).get_printed_summerdress_from_main_page(),'Printed Summer Dress')
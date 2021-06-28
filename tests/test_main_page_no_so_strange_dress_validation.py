from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from page_objects.body_page import BodyPage

class test_main_page_no_so_strange_dress_validation(BaseTest):

    def test_main_page_no_so_strange_dress_validation(self):
       self.assertTrue(BodyPage(self.driver).get_not_so_strange_dress_from_main_page()==0)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from page_objects.body_page import BodyPage

class test_women_evening_dresses_validation(BaseTest):

    def test_women_evening_dresses_validation(self):
       self.assertEqual(BodyPage(self.driver).getWomenDressesEveningDressesItem(),'Evening Dresses')
       BodyPage(self.driver).clickWomenDressesEveningDressesItem()
       self.assertTrue(BodyPage(self.driver).getgridListCount()>=1)

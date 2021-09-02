from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from page_objects.body_page import BodyPage
from datetime import datetime
import unittest

class test_account_creation_validation(BaseTest):


    def test_account_creation_validation(self):
       BodyPage(self.driver).click_sign_in()
       mail = datetime.now().strftime("%d%m%Y%H%M%S")
       BodyPage(self.driver).initiate_account_creation("test"+mail+"@test.com")
       account_info = {
       "firstname": 'mauro',
       "lastname": 'prueba',
       "password": '123456',
       "day": '31',
       "month": '10',
       "year": '1983',
       "address": 'prueba1',
       "city": 'pruebacity',
       "state": 'Alaska',
       "zip": '41414',
       "country": 'United States',
       "phone": '123789654'}
       BodyPage(self.driver).complete_account_info(account_info)
       self.assertEqual(BodyPage(self.driver).click_register(),'MY ACCOUNT')

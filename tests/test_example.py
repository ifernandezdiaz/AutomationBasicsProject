from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from page_objects.base_page import BasePage

class TestExample(BaseTest):

    def test_phone_validation(self):
        #self.setUp() no se usa el setup porque la instancia de Driver la crea la clase padre, y el método SetUp es llamado por unitTest
        self.base_page = BasePage(self.driver)
        self.phone_location = (By.CSS_SELECTOR, '.shop-phone > strong')
        phone = self.base_page.find_element(*self.phone_location)
        self.assertEqual(phone.text,'0123-456-789')

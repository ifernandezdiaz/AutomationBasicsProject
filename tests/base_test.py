import HtmlTestRunner
import json
import os
import shutil
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.driver_manager import Driver

class BaseTest(unittest.TestCase):


    def setUp(self):
        self.driver  = Driver().connect()
        with open(os.getcwd() + '/config/test_config.json') as test_config_file:
            test_config = json.load(test_config_file)
            test_config_file.close()
        self.__screenshot_path = os.getcwd() + test_config['screenshot_dir']
        self.driver.get(test_config['baseUrl'])

    def tearDown(self):
        # Screenshots con nombre del test case relacionado
        screenshot_file_name = self.__screenshot_path + '/Screenshot_' + unittest.TestCase.id(self) + '.png'
        self.driver.save_screenshot(screenshot_file_name)
        self.driver.close()
        self.driver.quit()

    @classmethod
    def setUpClass(self):
        with open(os.getcwd() + '/config/test_config.json') as test_config_file:
            test_config = json.load(test_config_file)
            test_config_file.close()
        self.__screenshot_path = os.getcwd() + test_config['screenshot_dir']
        shutil.rmtree(self.__screenshot_path)
        os.mkdir(self.__screenshot_path)

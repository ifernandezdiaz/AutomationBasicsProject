import HtmlTestRunner
import json
import os
import shutil
import unittest
import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.driver_manager import Driver
from config.config_helper import load_test_config_json, get_screenshot_path

class BaseTest(unittest.TestCase):

    test_config = load_test_config_json()

    def setUp(self):
        self.driver  = Driver().connect()
        self.__screenshot_path = get_screenshot_path(platform.system())
        self.driver.get(self.test_config['baseUrl'])
        self.time_list = self.test_config['timeout_list']

    def tearDown(self):
        # Screenshots con nombre del test case relacionado
        screenshot_file_name = self.__screenshot_path + \
        '/Screenshot_' + unittest.TestCase.id(self) + '.png'
        self.driver.save_screenshot(screenshot_file_name)
        self.driver.close()
        self.driver.quit()

    @classmethod
    def setUpClass(self):
        self.__screenshot_path = get_screenshot_path(platform.system())
        shutil.rmtree(self.__screenshot_path)
        os.mkdir(self.__screenshot_path)

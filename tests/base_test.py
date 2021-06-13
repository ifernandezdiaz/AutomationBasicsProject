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


if __name__ == "__main__":
    # Definimos la ejecución de los tests aquí para excluirla de los test files
    test_suite = unittest.TestLoader().loadTestsFromTestCase()
    # Pueden configurar el tipo de log que quieren generar:
    # verbosity=0 -> Sin log (Loguea solo el resultado final)
    # verbosity=1 -> Lista solo el result de cada test
    # verbosity=2 -> Log mas detallado para cada test
    unittest.TextTestRunner(verbosity=1).run(test_suite)

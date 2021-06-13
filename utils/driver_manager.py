import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DriverManager(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(DriverManager, cls).__call__(*args, **kwargs)

        return cls._instances[cls]

class Driver(metaclass=DriverManager):
    connection = None
    options = None
    def connect(self):
        if self.connection is None:
            with open(os.getcwd() + '/config/driver_config.json') as driver_config_file:
                driver_settings = json.load(driver_config_file)
                driver_config_file.close()
            if self.options is None:
                self.options = Options()
            for argument in driver_settings["driverArgs"]:
                self.options.add_argument(argument)
        self.connection = webdriver.Chrome(options=self.options)
        return self.connection

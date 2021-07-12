import os
import json

def load_test_config_json():
  with open(os.getcwd() + '\\config\\test_config.json') as test_config_file:
      return json.load(test_config_file)


def get_screenshot_path(my_system):
  if my_system == "Windows":
      return os.getcwd() + \
      load_test_config_json()['screenshot_dir_windows']
  else:
      return os.getcwd() + \
      load_test_config_json()['screenshot_dir_linux']

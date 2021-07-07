import HtmlTestRunner
import unittest
import os
from datetime import datetime
from tests.test_women_evening_dresses_validation import test_women_evening_dresses_validation
from tests.test_login import LoginTest



# Método que nos permite listar todos los archivos de tests
#test_suite = unittest.TestSuite()
test_suite = unittest.defaultTestLoader.discover(".")
#test_suite.addTest(test_women_evening_dresses_validation('test_women_evening_dresses_validation'))
#test_suite.addTest(test_women_evening_dresses_validation('test_women_evening_dresses_validation_2'))
#test_suite.addTest(LoginTest('test_login_search_and_check_still_logged_in'))
# Definimos la carpeta del reporte (si la misma existe, no la vuelve a crear)
report_path = "./reports/"
os.makedirs(report_path, exist_ok=True)

# Abrimos el reporte y le cargamos los resultados
runner = HtmlTestRunner.HTMLTestRunner(output=report_path,report_name="automation_report",
                                verbosity=2,combine_reports=True)

print(test_suite)
runner.run(test_suite)

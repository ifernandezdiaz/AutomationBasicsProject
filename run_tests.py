import HtmlTestRunner
import unittest
import os
from datetime import datetime
from tests.test_dresses_validation import test_dresses_validation



# Método que nos permite listar todos los archivos de tests
#test_suite = unittest.defaultTestLoader.discover(".")
test_suite = unittest.TestSuite()
test_suite.addTest(test_dresses_validation('test_women_evening_dresses_validation'))
# Definimos la carpeta del reporte (si la misma existe, no la vuelve a crear)
report_path = "./reports/"
os.makedirs(report_path, exist_ok=True)

# Abrimos el reporte y le cargamos los resultados
runner = HtmlTestRunner.HTMLTestRunner(output=report_path,report_name="automation_report",
                            verbosity=2,combine_reports=True)
print(test_suite)
runner.run(test_suite)

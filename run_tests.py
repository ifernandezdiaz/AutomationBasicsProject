import unittest
import os
from datetime import datetime
import HtmlTestRunner

# Método que nos permite listar todos los archivos de tests
test_suite = unittest.defaultTestLoader.discover(".")

# Definimos el nombre del reporte
report_path = "./reports/"


# Abrimos el reporte y le cargamos los resultados
runner = HtmlTestRunner.HTMLTestRunner(output=report_path,report_name="automation_report",
                            verbosity=2,combine_reports=True)
runner.run(test_suite)

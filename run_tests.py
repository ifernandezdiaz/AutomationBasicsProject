import unittest
import os
from datetime import datetime
import HtmlTestRunner

# Método que nos permite listar todos los archivos de tests
test_suite = unittest.defaultTestLoader.discover(".")

# Definimos la carpeta del reporte (si la misma existe, no la vuelve a crear)
report_path = "./reports/"
os.makedirs(report_path, exist_ok=True)

# Abrimos el reporte y le cargamos los resultados
runner = HtmlTestRunner.HTMLTestRunner(output=report_path,report_name="automation_report",
                            verbosity=2,combine_reports=True)
runner.run(test_suite)

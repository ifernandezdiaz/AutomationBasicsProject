AutomationBasicsProject
=======================

Proyecto final del curso Automation Basics para Spark Digital La idea es que todos trabajemos en el mismo repositorio creando casos de prueba automatizados en lenguaje python utilizando Selenium Webdriver.

### Estructura del Proyecto

Este framework está pronto para utilizar. El mismo contiene un framework ya configurado y funcional, pronto para comenzar el proyecto de automatización de la web automationpractice.com

### Precondiciones

#### Chromedriver

En este proyecto ya no usaremos un ejecutable dentro del proyecto sino que usaremos el driver instalado directamente en nuestros equipos. A continuación les dejo los pasos para poder realizar esta instalación:

-	**Para macOS:**
	-	Desde una terminal ejecutar: `brew install --cask  chromedriver`
	-	Verificar instalación ejecutando `chromedriver -version`
		-	Este comando debe retornar la versión del driver
-	**Para Windows:**
	-	Debemos instalar `chocolatey`
		-	Para esto debemos ejecutar desde cmd (utilizando privilegios administrativos) el siguiente comando:`
			@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
			`
	-	Luego de instalado ejecutar `choco install chromedriver`
	-	Para confirmar que la instalación funcionó correctamente ejecutar `chromedriver -version`

### Agregar nuevos tests

Para agregar nuevos tests, deben crear un nuevo test file dentro de la carpeta `tests`. Cada test debe heredar de la clase `BaseTest`

### Agregar nuevos page objects

La clase 'BasePage' ofrece métodos muy útiles para el manejo de los page objects. Al momento de crear un nuevo page object, el mismo debe heredar de esta clase.

### Cómo ejecutar los tests?

Ejecutar desde consola (posicionados dentro de la carpeta del proyecto):

`python3 run_tests.py` -> Para Python 3+

`python run_tests.py` -> Para Python 2

### Posibles errores

#### ModuleNotFound error en macOS

Es posible que aquellos quienes ejecutan los tests dentro de un *virtual environment* puedan encontrarse con este error al momento de importar alguna de nuestras clases base. Para solucionar esto debemos agregar la carpeta del proyecto al `PYTHONPATH` de nuestro ambiente:

```
export PYTHONPATH="${PYTHONPATH}:<ruta_hacia_la_carpeta_del_proyecto>/AutomationBasicsProject/"
```

**Ejemplo:**

```
export PYTHONPATH="${PYTHONPATH}:/Users/nacho/Respaldo/dev/Spark/AutomationBasicsProject"
```

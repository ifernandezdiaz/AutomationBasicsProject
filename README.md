# AutomationBasicsProject

Proyecto final del curso Automation Basics para Spark Digital
La idea es que todos trabajemos en el mismo repositorio creando casos de prueba automatizados en lenguaje python utilizando Selenium Webdriver.

### Estructura del Proyecto
Este framework está pronto para utilizar. El mismo contiene un framework ya configurado y funcional, pronto para comenzar el proyecto de automatización de la web automationpractice.com

### Agregar nuevos tests
Para agregar nuevos tests, deben crear un nuevo test file dentro de la carpeta `tests`. Cada test debe heredar de la clase `BaseTest`

### Agregar nuevos page objects
La clase 'BasePage' ofrece métodos muy útiles para el manejo de los page objects. Al momento de crear un nuevo page object, el mismo debe heredar de esta clase.

### Cómo ejecutar los tests?
Ejecutar desde consola (posicionados dentro de la carpeta del proyecto):

`python3 -m unittest` -> Para Python 3+

`python -m unittest` -> Para Python 2


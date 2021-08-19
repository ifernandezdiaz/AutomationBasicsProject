import json
import os
import logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from config.config_helper import load_test_config_json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        test_settings = load_test_config_json()
        self.driver = driver
        self.time_list = test_settings['timeout_list']
        self.logger = logging.getLogger('Debug_logger')

    def __hover_over(self):
        """
        Este metodo devuelve una instancia
        de ActionChains para poder hacer hover sobre algún elemento
        Returns:
        ActionChains
        """
        return ActionChains(self.driver)

    def open_url(self, url):
        """
        Este método abre una url

        Parameters:
        url(str): nombre de la url
        """
        self.driver.open(url)

    def get_actual_url(self):
        """
        Este método devuelve la url actual

        Returns:
        str: url de la página actual
        """
        return self.driver.current_url

    def find_element(self, element_locator):
        """
        Este método busca el webelement de acuerdo a un locator

        Parameters:
        element_locator(tuple): By y el nombre del locator correspondiente

        Returns:
        WebElement: Devuelve el WebElement si es que lo encuentra
        """
        return self.driver.find_element(*element_locator)

    def find_elements(self, element_locator):
        """
        Este método busca todos los elementos con ese locator

        Parameters:
        element_locator(tuple): By y el nombre del locator correspondiente

        Returns:
        Lista WebElements: Devuelve los WebElements encontrados
        """
        return self.driver.find_elements(*element_locator)

    def wait_element_to_be_present(self, element_locator, time=30):
        """
        Este método espera un determinado tiempo a que el elemento este presente

        Parameters:
        time(int): El tiempo que debe esperar
        element_locator(tuple): By y el nombre del locator correspondiente
        """
        try:
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(element_locator))
        except TimeoutException:
            print('Element not found: ' + element_locator[1])

    def wait_for_element_to_be_visible(self, element_locator, time=30):
        """
        Este método espera un determinado tiempo a que el elemento este visible

        Parameters:
        time(int): El tiempo que debe esperar
        element_locator(tuple): By y el nombre del locator correspondiente
        """
        try:
            WebDriverWait(self.driver, time).until(
                EC.visibility_of_element_located(element_locator))
        except TimeoutException:
            print('Element was not visible: ' + element_locator[1])

    def click_element(self, element_locator, web_element=False):
        """
        Si le paso un element_locator como parametro, busca el elemento y lo clickea
        Si le paso un webelement, simplemente lo clickeo

        Parameters:
        element_locator(tuple): By y el nombre del locator correspondiente
        """
        if web_element:
            element_locator.click()
        else:
            element = self.find_element(element_locator)
            element.click()



    def wait_and_click(self, element_locator, time=30):
        """
        Este método espera un determinado tiempo a que el elemento este visible,
        lo busca y lo clickea

        Parameters:
        element_locator(tuple): By y el nombre del locator correspondiente
        time(int): El tiempo que debe esperar
        """
        self.wait_for_element_to_be_visible(element_locator, int(time))
        element = self.find_element(element_locator)
        element.click()
        return element

    def type_text(self, text, element_locator, enter=False):
        """
        Este método ingresa texto en un formulario

        Parameters:
        text(str): el texto a ingresar
        element_locator(tuple): By y el nombre del locator correspondiente
        enter(bool): debe apretar enter si es verdadero
        """
        input = self.wait_and_click(element_locator)
        input.send_keys(text)
        if enter:
            input.send_keys(Keys.ENTER)

    def move_to_element(self, element, by_locator):
        """
        Este método hace que el mouse se mueva a un elemento, se puede pasar un
        WebElement o el locator completo de tal

        Parameters:
        element(WebElement): El elemento con el cual interactuar
        element_locator(tuple): By y el nombre del locator correspondiente
        """
        if bylocator:
            a = ActionChains(self.driver)
            self.find_element(element)
            a.move_to_element(element).perform()
        else:
            a = ActionChains(self.driver)
            a.move_to_element(element).perform()


    def save_screenshot_of_element(self, element_locator, web_element=False):
        if web_element:
            element_locator.screenshot("/element.png")
        else:
            element = self.find_element(element_locator)
            element.screenshot("/element.png")

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from page_objects.body_page import BodyPage
import random
import unittest

class test_best_seller_open_item_validation(BaseTest):


    def test_best_seller_open_item_validation(self):
        body_page = BodyPage(self.driver)
        length = body_page.click_best_sellers_tab() #clickear en el tab "Best Sellers" y obtener la cantidad de items en la grilla de esa categoria
        randomnum = random.randint(0, length-1) #elegir un numero aleatoriamente dentro de la cantidad de items en la grilla de la categoria
        name = body_page.click_best_seller_product(randomnum) #hacer click en el item elegido aleatoriamente y obtener el nombre del item elegido aleatoriamente
        self.assertEqual(body_page.get_product_detail_name(),name) #verificar que el nombre del item elegido en la grilla sea igual al nombre mostrado en la pagina de detalle del item

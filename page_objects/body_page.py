
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class BodyPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.add_to_cart = (By.CSS_SELECTOR, 'li.ajax_block_product  > div.product-container > div.right-block > div.button-container > a.button')
        self.confirmation_modal = (By.ID,'#layer_cart')
        self.cart_amount = (By.CSS_SELECTOR,'div.shopping_cart > a > span.ajax_cart_quantity')
        self.card = (By.CSS_SELECTOR, 'li.ajax_block_product  > div.product-container > div.right-block > h5 > a.product-name')
        self.menu_elements = (By.CSS_SELECTOR,'#block_top_menu>ul>li')
        self.submenu_elements = (By.CSS_SELECTOR,'ul>li')
        self.submenu_items = (By.CSS_SELECTOR,'ul>li')
        self.product_list_grid = (By.CSS_SELECTOR,'.product_list')

    def hover_card(self):
        card = self.find_element(*self.card)
        self.wait_element(self.card)
        a = ActionChains(self.driver)
        a.move_to_element(card).perform()

    def hover_over(self): #este metodo devuelve una instancia de ActionChains para poder hacer hover sobre algún elemento
        return ActionChains(self.driver)

    def get_button_name(self):
        self.find_element(*self.add_to_cart)
        self.wait_element(*self.add_to_cart)
        return self.find_element(*self.add_to_cart).text

    def press_add_to_cart_button(self):
        self.find_element(*self.add_to_cart).click()
        self.wait_element(*self.confirmation_modal)

    def get_item_cart(self):
        self.wait_element(*self.cart_amount)
        return self.find_element(*self.cart_amount).text

    def getMenuElements(self): #este método devuelve todos los elementos del menú
        return self.find_elements(*self.menu_elements)

    def getMenuElementByTitle(self,m_title): #este método devuelve dinámicamente un elemento del menú según el título que se pase por parámetro
        elements = self.getMenuElements()
        menuelement = None
        for elem in elements:
            if elem.find_element(By.CSS_SELECTOR,'a').get_attribute("title")==m_title:
                menuelement = elem
        return menuelement

    def getSubMenuElements(self,m_title): #este método devuelve dinámicamente los subelementos del elemento del menu que se pase por parámetro
        return self.getMenuElementByTitle(m_title).find_elements(*self.submenu_elements)

    #este método devuelve dinámicamente un subelemento del elemento del menu
    #segun el subelemento y el elemento que se pasen por parámetro
    def getSubMenuElementByTitle(self,m_title,sm_title):
        sm_elements = self.getSubMenuElements(m_title)
        sub_element = None
        for elem in sm_elements:
            try:
                if elem.find_element(By.CSS_SELECTOR,'a').get_attribute("title")==sm_title:
                    sub_element = elem
            except:
                break
        return sub_element

        #este método devuelve dinámicamente los items del subelemento del menu
        #segun el subelemento y el elemento que se pasen por parámetro
    def getSubMenuItems(self,m_title,sm_title):
        return self.getSubMenuElementByTitle(m_title,sm_title).find_elements(*self.submenu_items)

    #este método devuelve dinámicamente un item del subelemento del menu
    #segun el subelemento, el elemento y el item que se pasen por parámetro
    def getSubMenuItemByTitle(self,m_title,sm_title,it_title):
        sm_items = self.getSubMenuItems(m_title,sm_title)
        sm_item = None
        for elem in sm_items:
            try:
                if elem.find_element(By.CSS_SELECTOR,'a').get_attribute("title")==it_title:
                    sm_item = elem
            except:
                break
        return sm_item

    #este método devuelve el titulo del item Evening Dreses del subelemento del menu Dresess, del elemento del menu Women
    def getWomenDressesEveningDressesItem(self):
        return self.getSubMenuItemByTitle('Women','Dresses','Evening Dresses').find_element(By.CSS_SELECTOR,'a').get_attribute("title")

    #este método desplaza el mouse y hace click sobre el item Evening Dreses del subelemento del menu Dresess, del elemento del menu Women
    def clickWomenDressesEveningDressesItem(self):
        self.hover_over().move_to_element(self.getMenuElementByTitle('Women')).move_to_element(self.getSubMenuItemByTitle('Women','Dresses','Evening Dresses')).click().perform()
        self.wait_element(*self.product_list_grid)

    #este método cuenta la cantidad de items que existen en la grilla de productos
    def getgridListCount(self):
        return len(self.find_elements(*self.product_list_grid))

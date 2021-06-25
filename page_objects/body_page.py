
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


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

    def get_menu_elements(self): #este método devuelve todos los elementos del menú
        return self.find_elements(*self.menu_elements)

    def get_menu_element_by_title(self,m_title): #este método devuelve dinámicamente un elemento del menú según el título que se pase por parámetro
        elements = self.get_menu_elements()
        menuelement = None
        for elem in elements:
            if elem.find_element(By.CSS_SELECTOR,'a').get_attribute("title")==m_title:
                menuelement = elem
        return menuelement

    def get_sub_menu_elements(self,m_title): #este método devuelve dinámicamente los subelementos del elemento del menu que se pase por parámetro
        return self.get_menu_element_by_title(m_title).find_elements(*self.submenu_elements)

    #este método devuelve dinámicamente un subelemento del elemento del menu
    #segun el subelemento y el elemento que se pasen por parámetro
    def get_sub_menu_element_by_title(self,m_title,sm_title):
        sm_elements = self.get_sub_menu_elements(m_title)
        sub_element = None
        for elem in sm_elements:
            try:
                if elem.find_element(By.CSS_SELECTOR,'a').get_attribute("title")==sm_title:
                    sub_element = elem
            except:
                continue
        return sub_element

    #este método devuelve dinámicamente los items del subelemento del menu
    #segun el subelemento y el elemento que se pasen por parámetro
    def get_sub_menu_items(self,m_title,sm_title):
        return self.get_sub_menu_element_by_title(m_title,sm_title).find_elements(*self.submenu_items)

    #este metodo identifica un item del menu según su el valor del atributo titulo
    def compara_menuitem_por_atributo_titulo(elem,it_title):
        try:
            if elem.find_element(By.CSS_SELECTOR,'a').get_attribute("title")==it_title:
                return True
            else:
                return False
        except:
            pass

    #este método devuelve dinámicamente un item del subelemento del menu
    #segun el subelemento, el elemento y el item que se pasen por parámetro
    def get_sub_menu_item_by_title(self,m_title,sm_title,it_title):
        sm_items = self.get_sub_menu_items(m_title,sm_title)
        sm_item = list(filter(lambda elem: BodyPage.compara_menuitem_por_atributo_titulo(elem,it_title),sm_items))
        return sm_item

    #este método devuelve el titulo del item Evening Dreses del subelemento del menu Dresess, del elemento del menu Women
    def get_women_dresses_evening_dresses_item(self):
        return self.get_sub_menu_item_by_title('Women','Dresses','Evening Dresses')[0].find_element(By.CSS_SELECTOR,'a').get_attribute("title")

    #este método desplaza el mouse y hace click sobre el item Evening Dreses del subelemento del menu Dresess, del elemento del menu Women
    def click_women_dresses_evening_dresses_item(self):
        #el metodo hover_over es privado y por eso se invoca asi: _BasePage__hover_over
        self._BasePage__hover_over().move_to_element(self.get_menu_element_by_title('Women')).move_to_element(self.get_sub_menu_item_by_title('Women','Dresses','Evening Dresses')[0]).click().perform()
        self.wait_element(*self.product_list_grid)

    #este método cuenta la cantidad de items que existen en la grilla de productos
    def get_grid_list_count(self):
        return len(self.find_elements(*self.product_list_grid))

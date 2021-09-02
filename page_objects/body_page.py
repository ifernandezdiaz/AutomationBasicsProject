import time
import logging
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
        self.product_list_grid = (By.CSS_SELECTOR,'.product_list > li')
        self.main_page_popular_products = (By.CSS_SELECTOR,'#homefeatured > li.ajax_block_product')
        self.main_page_best_seller_tab = (By.CSS_SELECTOR,'#home-page-tabs .blockbestsellers')
        self.main_page_best_seller_product_list = (By.CSS_SELECTOR,'#blockbestsellers.product_list')
        self.main_page_best_seller_product_list_items = (By.CSS_SELECTOR,'#blockbestsellers > li.ajax_block_product .product-container .right-block > h5 > a')
        self.product_detail = (By.CSS_SELECTOR,'.primary_block .pb-center-column > h1')
        self.sign_in_button = (By.CSS_SELECTOR,'.header_user_info > .login')
        self.new_user_email_input = (By.CSS_SELECTOR,'#email_create')
        self.create_account_button = (By.CSS_SELECTOR,'#SubmitCreate')
        self.customer_gender_male = (By.CSS_SELECTOR,'#id_gender1')
        self.customer_gender_female = (By.CSS_SELECTOR,'#id_gender2')
        self.customer_firstname = (By.CSS_SELECTOR,'#customer_firstname')
        self.customer_lastname = (By.CSS_SELECTOR,'#customer_lastname')
        self.customer_email = (By.CSS_SELECTOR,'#email')
        self.customer_password = (By.CSS_SELECTOR,'#passwd')
        self.customer_birth_day = (By.CSS_SELECTOR,'#days')
        self.customer_birth_month = (By.CSS_SELECTOR,'#months')
        self.customer_birth_year = (By.CSS_SELECTOR,'#years')
        self.customer_address_firstname = (By.CSS_SELECTOR,'#firstname.form-control')
        self.customer_address_lastname = (By.CSS_SELECTOR,'#lastname.form-control')
        self.customer_address = (By.CSS_SELECTOR,'#address1.form-control')
        self.customer_address_city = (By.CSS_SELECTOR,'#city.form-control')
        self.customer_address_state = (By.CSS_SELECTOR,'#id_state')
        self.customer_address_zipcode = (By.CSS_SELECTOR,'#postcode')
        self.customer_address_country = (By.CSS_SELECTOR,'#id_country')
        self.customer_address_mobphone = (By.CSS_SELECTOR,'#phone_mobile')
        self.customer_address_alias = (By.CSS_SELECTOR,'#alias')
        self.customer_register_button = (By.CSS_SELECTOR,'#submitAccount')
        self.customer_myaccount = (By.CSS_SELECTOR,'#center_column > h1')

    def hover_card(self):
        card = self.find_element(self.card)
        self.wait_for_element_to_be_visible(self.card)
        self.move_to_element(card)

    def get_button_name(self):
        self.find_element(self.add_to_cart)
        self.wait_for_element_to_be_visible(self.add_to_cart)
        return self.find_element(self.add_to_cart).text

    def press_add_to_cart_button(self):
        self.find_element(self.add_to_cart).click()
        self.wait_for_element_to_be_visible(self.confirmation_modal)

    def get_item_cart(self):
        self.wait_for_element_to_be_visible(self.cart_amount)
        return self.find_element(self.cart_amount).text

    def get_menu_elements(self): #este método devuelve todos los elementos del menú
        return self.find_elements(self.menu_elements)

    def get_menu_element_by_title(self, m_title): #este método devuelve dinámicamente un elemento del menú según el título que se pase por parámetro
        elements = self.get_menu_elements()
        menuelement = None
        for elem in elements:
            if elem.find_element(By.CSS_SELECTOR,'a').get_attribute("title") == m_title:
                menuelement = elem
        return menuelement

    def get_sub_menu_elements(self, m_title):
        """
        Este método devuelve dinámicamente los subelementos
        del elemento del menu que se pase por parámetro
        """
        self.logger.info(self.get_menu_element_by_title(m_title))
        return self.get_menu_element_by_title(m_title).find_elements(*self.submenu_elements)


    def get_sub_menu_element_by_title(self, m_title, sm_title):
        """
        Este método devuelve dinámicamente un subelemento del elemento del menu
        segun el subelemento y el elemento que se pasen por parámetro
        """
        sm_elements = self.get_sub_menu_elements(m_title)
        sub_element = None
        for elem in sm_elements:
            try:
                if elem.find_element(By.CSS_SELECTOR,'a').get_attribute("title")==sm_title:
                    sub_element = elem
            except:
                continue
        return sub_element


    def get_sub_menu_items(self, m_title, sm_title):
        """
        Este método devuelve dinámicamente los items del subelemento del menu
        segun el subelemento y el elemento que se pasen por parámetro
        """
        return self.get_sub_menu_element_by_title(m_title, sm_title).find_elements(*self.submenu_items)


    def compara_menuitem_por_atributo_titulo(elem, it_title):
        """
        Este metodo identifica un item del menu según su el valor del atributo titulo
        """
        try:
            if elem.find_element(By.CSS_SELECTOR,'a').get_attribute("title")==it_title:
                return True
            else:
                return False
        except:
            pass


    def get_sub_menu_item_by_title(self, m_title, sm_title, it_title):
        """
        Este método devuelve dinámicamente un item del subelemento del menu
        segun el subelemento, el elemento y el item que se pasen por parámetro
        """
        sm_items = self.get_sub_menu_items(m_title, sm_title)
        sm_item = list(filter(lambda elem: BodyPage.compara_menuitem_por_atributo_titulo(elem, it_title), sm_items))
        return sm_item

    def get_women_dresses_evening_dresses_item(self):
        """
        Este método devuelve el titulo del item Evening Dreses del subelemento
        del menu Dresess, del elemento return self.get_menu_element_by_title(m_title).find_elements(self.submenu_elements)
        del menu Women
        """
        return self.get_sub_menu_item_by_title('Women','Dresses','Evening Dresses')[0].find_element(By.CSS_SELECTOR,'a').get_attribute("title")

    #este método desplaza el mouse y hace click sobre el item Evening Dreses del subelemento del menu Dresess, del elemento del menu Women
    def click_women_dresses_evening_dresses_item(self):
        #el metodo hover_over es privado y por eso se invoca asi: _BasePage__hover_over
        self._BasePage__hover_over().move_to_element(self.get_menu_element_by_title('Women')).move_to_element(self.get_sub_menu_item_by_title('Women','Dresses','Evening Dresses')[0]).click().perform()
        self.wait_for_element_to_be_visible(self.product_list_grid)

    #este método hace click sobre el elemento del menu "Dresses"
    def click_on_dresses_menu_element(self):

        self.get_menu_element_by_title('Dresses').click()
        self.wait_for_element_to_be_visible(self.product_list_grid)

    #este método cuenta la cantidad de items que existen en la grilla de productos
    def get_grid_list_count(self):
        return len(self.find_elements(self.product_list_grid))

    def get_popular_product_from_main_page(self,it_title):
        popular_prods = self.find_elements(self.main_page_popular_products)
        pop_prod = list(filter(lambda elem: BodyPage.compara_menuitem_por_atributo_titulo(elem,it_title),popular_prods))
        return pop_prod

    def get_printed_summerdress_from_main_page(self):
        return self.get_popular_product_from_main_page(
            'Printed Summer Dress')[0].find_element(By.CSS_SELECTOR,'a').get_attribute("title")

    def get_not_so_strange_dress_from_main_page(self):
        return len(self.get_popular_product_from_main_page(
            'Not so Strange Dress'))

    def click_best_sellers_tab(self):
        self.find_element(self.main_page_best_seller_tab).click()
        self.wait_for_element_to_be_visible(self.main_page_best_seller_product_list)
        return len(self.find_elements(self.main_page_best_seller_product_list_items))

    def click_best_seller_product(self,item):
        product = self.find_elements(self.main_page_best_seller_product_list_items)[item]
        name = product.get_attribute("title")
        product.click()
        self.wait_for_element_to_be_visible(self.product_detail)
        return name

    def get_product_detail_name(self):
        return self.find_element(self.product_detail).text

    def click_sign_in(self):
        self.find_element(self.sign_in_button).click()
        self.wait_for_element_to_be_visible(self.create_account_button)

    def initiate_account_creation(self,text):
        self.type_text(text, self.new_user_email_input)
        self.find_element(self.create_account_button).click()
        self.wait_for_element_to_be_visible(self.customer_register_button)

    def complete_account_info(self,account_info):
        self.find_element(self.customer_gender_male).click()
        self.type_text(account_info["firstname"],self.customer_firstname)
        self.type_text(account_info["lastname"],self.customer_lastname)
        day = self.find_element(self.customer_birth_day)
        Select(day).select_by_value(account_info["day"])
        month = self.find_element(self.customer_birth_month)
        Select(month).select_by_value(account_info["month"])
        year = self.find_element(self.customer_birth_year)
        Select(year).select_by_value(account_info["year"])
        self.type_text(account_info["address"],self.customer_address)
        self.type_text(account_info["city"],self.customer_address_city)
        Select(self.find_element(self.customer_address_state)).select_by_visible_text(account_info["state"])
        self.type_text(account_info["zip"],self.customer_address_zipcode)
        Select(self.find_element(self.customer_address_country)).select_by_visible_text(account_info["country"])
        self.type_text(account_info["phone"],self.customer_address_mobphone)
        self.type_text(account_info["password"],self.customer_password)
        self.find_element(self.customer_register_button).click()

    def click_register(self):
        self.wait_for_element_to_be_visible(self.customer_myaccount)
        return self.find_element(self.customer_myaccount).text

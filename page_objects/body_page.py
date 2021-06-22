
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


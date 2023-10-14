from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def message_contains_product_title(self, title):
        title_shown = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE_IN_NOTIFICATION).text
        assert title_shown == title, f'Actual text is: <{title_shown}>, expected <{title}>'

    def total_price_equal_to_product_price(self, price):
        price_shown = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_IN_NOTIFICATION).text
        assert price_shown == price, f'Actual price is: <{price_shown}>, expected <{price}>'

    def get_product_title(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_not_have_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_TITLE_IN_NOTIFICATION), 'Success message is shown'

    def should_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_TITLE_IN_NOTIFICATION), 'Success message is not disappeared'

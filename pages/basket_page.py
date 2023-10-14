from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_be_empty(self):
        self.should_have_no_products()
        self.should_have_empty_basket_message()

    def should_have_no_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT), 'Something is in the basket!'

    def should_have_empty_basket_message(self):
        text = 'Your basket is empty. Continue shopping'
        visible_message = self.browser.find_element(*BasketPageLocators.TOP_MESSAGE).text
        assert visible_message == text, f'Expected text:{text}, actual text: {visible_message}'

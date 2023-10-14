from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, "[class~=basket-mini] [class='btn btn-default']")


class BasketPageLocators():
    TOP_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_CONTENT = (By.CSS_SELECTOR, '#basket_formset')


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')


class ProductPageLocators():
    ADD_TO_BASKET = (By.ID, 'add_to_basket_form')
    PRODUCT_TITLE_IN_NOTIFICATION = (By.CSS_SELECTOR, '#messages > div:nth-child(1) strong')
    BASKET_TOTAL_IN_NOTIFICATION = (By.CSS_SELECTOR, '#messages > div:nth-child(3) strong')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    btn_buy = (By.CSS_SELECTOR, '[data-position-index="0"] .button-ui.button-ui_brand')
    cart = (By.CSS_SELECTOR, '.cart-modal')
    count_of_items = (By.CSS_SELECTOR, '.cart-link__badge')
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def find_button_buy(self, time=10):
        button_buy = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(self.btn_buy),
                                                     message=f'Поиск по элементу "{self.btn_buy}" не дал результатов')
        button_buy.click()

    def visible_cart(self, time=10):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(self.cart),
                                                    message=f'Поиск по элементу "{self.cart}" не дал результатов')
        return True

    def count(self, time=10):
        number = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(self.count_of_items),
                                               message=f'Поиск по элементу "{self.count_of_items}" не дал результатов')
        return number.text

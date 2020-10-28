from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

path = r'chromedriver.exe'


class Dnselements:

    btn_sale = (By.CSS_SELECTOR, '.homepage-actions__title.ui-link')
    page_items = (By.XPATH, '//*[@id="actions-page"]/div[2]/div[2]/div[1]/div[3]/div/div[2]/a')
    btn_buy = (By.CSS_SELECTOR, '[data-position-index="0"] .button-ui.button-ui_brand')
    cart = (By.CSS_SELECTOR, '.cart-modal')
    count_of_items = (By.CSS_SELECTOR, '.cart-link__badge')

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.maximize_window()

    # передача ссылки на страницу
    def get_request(self, url):
        return self.driver.get(url)

    # поиск элемента
    def find_element(self, elements):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(elements),
                                                    message=f'Поиск по элементу "{elements}" не дал результатов')

    # поиск всплывающей корзины
    def visible_cart(self, cart):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(cart),
                                                    message=f'Поиск по элементу "{cart}" не дал результатов')

    # клик на элемент
    @staticmethod
    def click_on_element(elem):
        elem.click()

    # сравнение количества товаров в корзине
    @staticmethod
    def count(number):
        assert '1' == number, f'Количество товаров не равно "{number}"'

    def link_check(self, link):
        assert link == self.driver.current_url, f'Мы не перешли на "{link}"'

    def segment_link(self, string):
        link = self.driver.current_url
        link = link.split('/')
        assert string == link[-2], f'Мы не перешли на "{string}"'

    def quit(self):
        self.driver.quit()
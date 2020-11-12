import pytest
from src.conftest import browser
from src.index_page import IndexPage
from src.sales_page import SalesPage
from src.product_page import ProductPage


@pytest.mark.usefixtures("browser")
class Test01:

    def test_01(self):
        self.index_page = IndexPage(self.driver)
        self.sales_page = SalesPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.index_page.go_to_page()
        assert 'https://www.dns-shop.ru/actions/' in self.driver.current_url, f'Мы не перешли на страницу' #доделать
        assert self.sales_page.first_link() == self.sales_page.segment_link(), f'Мы не перешли на страницу'
        self.product_page.find_button_buy()
        assert self.product_page.visible_cart() == True, f'Окно с товарами в корзине не появилось'
        assert '1' == self.product_page.count() , f'Число товаров в корзине не равно 1'
        print('все окей')

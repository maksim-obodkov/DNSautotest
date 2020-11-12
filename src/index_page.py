from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IndexPage:
    btn_sale = (By.CSS_SELECTOR, '.homepage-actions__title.ui-link')
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self, time=10):
        btn = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(self.btn_sale),
                                        message=f'Поиск по элементу "{self.btn_sale}" не дал результатов')
        btn.click()




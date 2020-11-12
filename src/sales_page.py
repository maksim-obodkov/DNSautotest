from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SalesPage:
    list_of_elements = (By.CSS_SELECTOR, '.action-card__product-link.ui-link.ui-link_blue')
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def first_link(self, time=10):
        link = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(self.list_of_elements),
                                  message=f'Поиск по элементу "{self.list_of_elements}" не дал результатов')
        attr = link.get_attribute('data-commerce-target')
        link.click()
        return attr

    def segment_link(self):
        attr_name = self.driver.current_url
        attr_name = attr_name.split('/')

        return attr_name[-2]
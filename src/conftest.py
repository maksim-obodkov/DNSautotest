import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser(request):
    driver = webdriver.Chrome(executable_path='../chromedriver.exe')
    request.cls.driver = driver
    driver.maximize_window()
    driver.get('https://www.dns-shop.ru/')
    yield driver
    driver.quit()

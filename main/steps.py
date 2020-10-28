from DNSautotest.main.functions import DnsElements

page_request = DnsElements()


def dns():

    # переход на сайт
    page_request.get_request("https://www.dns-shop.ru/")

    # поиск кнопки "акции"
    # переход на страницу
    # проверка что перешли на страницу "акции"
    ui = page_request.find_element(page_request.btn_sale)
    page_request.click_on_element(ui)
    page_request.link_check('https://www.dns-shop.ru/actions/')

    # поиск на странице первой акции
    # поиск атрибута (далее для проверки)
    # переход на страницу
    # проверка по атрибуту
    ui = page_request.find_element(page_request.page_items)
    link = ui.get_attribute('data-commerce-target')
    page_request.click_on_element(ui)
    page_request.segment_link(link)

    # поиск и клик по кнопке "купить" (далее должно появится всплывающее окно с текущеми товарами в корзине)
    # проверка открытия всплывающего окна с текущими товарами в корзине
    # сравнение количество товаров в корзине с количеством 1 (выставил в сам из головы)
    ui = page_request.find_element(page_request.btn_buy)
    page_request.click_on_element(ui)
    page_request.visible_cart(page_request.cart)
    number = page_request.find_element(page_request.count_of_items)
    number = number.text
    page_request.count(number)


if __name__ == '__main__':
    dns()
    page_request.quit()
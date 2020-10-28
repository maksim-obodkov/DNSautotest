from func import Dnselements

page_request = Dnselements()


def dns():

    page_request.get_request("https://www.dns-shop.ru/")

    ui = page_request.find_element(page_request.btn_sale)
    page_request.click_on_element(ui)
    page_request.link_check('https://www.dns-shop.ru/actions/')

    ui = page_request.find_element(page_request.page_items)
    link = ui.get_attribute('data-commerce-target')
    page_request.click_on_element(ui)
    page_request.segment_link(link)

    ui = page_request.find_element(page_request.btn_buy)
    page_request.click_on_element(ui)
    page_request.visible_cart(page_request.cart)
    number = page_request.find_element(page_request.count_of_items)
    number = number.text
    page_request.count(number)


if __name__ == '__main__':
    dns()
    page_request.quit()
from selenium.webdriver.support import expected_conditions as ec
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_page_contain_add_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector("#add_to_basket_form button.btn.btn-add-to-basket")
    assert ec.presence_of_element_located(button)

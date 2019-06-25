import time
import math
import pytest
from selenium import webdriver

answer = math.log(int(time.time()))

links_array = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', links_array)
class TestOpenPage(object):
    def test_open_page(self, browser, link):
        link = "{}".format(links_array)
        browser.get(link)
        browser.find_element_by_class_name('text_area').send_keys(answer)


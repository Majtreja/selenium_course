from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button.trollface").click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_element = browser.find_element_by_css_selector("[id=input_value]")
x = x_element.text
y = calc(x)

answer = browser.find_element_by_id("answer").send_keys(y)

button = browser.find_element_by_css_selector("button.btn").click()


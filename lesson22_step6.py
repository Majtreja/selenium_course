from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector("[id=input_value]")
x = x_element.text
y = calc(x)

answer = browser.find_element_by_css_selector("[id='answer']")
answer.send_keys(y)
check = browser.find_element_by_css_selector("[id='robotCheckbox']").click()
browser.execute_script("window.scrollBy(0, 100);")
radio = browser.find_element_by_css_selector("[id='robotsRule']").click()

button = browser.find_element_by_css_selector("button.btn").click()




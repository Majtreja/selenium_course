from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector("[id=input_value]")
x = x_element.text
y = calc(x)

answer = browser.find_element_by_css_selector("[id='answer']")
answer.send_keys(y)
check = browser.find_element_by_css_selector("[id='robotCheckbox']").click()
radio = browser.find_element_by_css_selector("[id='robotsRule']").click()
time.sleep(5)
button = browser.find_element_by_css_selector("button.btn").click()




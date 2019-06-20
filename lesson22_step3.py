from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element_by_id("num1").text
num2 = browser.find_element_by_id("num2").text

x = str(int(num1) + int(num2))

print(x)

select = Select(browser.find_element_by_tag_name("select")).select_by_value(x)

button = browser.find_element_by_css_selector("button.btn").click()




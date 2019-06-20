from selenium import webdriver
import os


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

name = browser.find_element_by_css_selector("[name='firstname']").send_keys("lalalal")
surname = browser.find_element_by_css_selector("[name='lastname']").send_keys("bla")
email = browser.find_element_by_css_selector("[name='email']").send_keys("bla@test.com")

butt = browser.find_element_by_css_selector("[name='file']").send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn").click()




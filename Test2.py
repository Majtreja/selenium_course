from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys

# browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# browser = webdriver.Chrome()

link = "http://suninjuly.github.io/registration2.html"
browser.get(link)

# Ваш код, который заполняет обязательные поля
browser.find_element_by_css_selector("input[placeholder*='имя']").send_keys("Daniel")
browser.find_element_by_css_selector("input[placeholder*='фамилию']").send_keys("Pace")
browser.find_element_by_css_selector("input[placeholder*='Email']").send_keys("blahblah@gmail.com")

# Отправляем заполненную форму и ждем загрузки страницы
button = browser.find_element_by_css_selector("button.btn").click()
wait = WebDriverWait(browser, 10)
# находим элемент, содержащий текст
element = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))

# записываем в переменную welcome_text текст из элемента element
welcome_text = element.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

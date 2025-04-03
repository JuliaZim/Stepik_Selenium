from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

#Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
price = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

#Нажать на кнопку "Book"
Button_book = browser.find_element(By.ID, "book")
Button_book.click()

#Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
x = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x.text
y = calc(x)
browser.find_element(By.ID, "answer").send_keys(y)
browser.find_element(By.CSS_SELECTOR,"body > form > div > div > button").click()

#Получить значение с алерта:
alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text)
value = alert_text.split(" ")
print(value[-1])

#Закрыть браузер
time.sleep(10)
browser.quit()

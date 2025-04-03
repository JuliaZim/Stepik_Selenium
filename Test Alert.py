from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#Открыть браузер
brr2 = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
brr2.get(link)

#Нажать на кнопку
button1 = brr2.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
button1.click()

#Принять confirm
confirm = brr2.switch_to.alert
confirm.accept()

#Посчитать и отправить х
x = brr2.find_element(By.ID, "input_value")
x = x.text
y = calc(x)
brr2.find_element(By.ID, "answer").send_keys(y)
brr2.find_element(By.CSS_SELECTOR,"body > form > div > div > button").click()

#Получить значение с алерта:
alert = brr2.switch_to.alert
alert_text = alert.text
print(alert_text)
value = alert_text.split(" ")
print(value[-1])

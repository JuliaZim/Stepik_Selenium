import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#Открыть страницу
brr3 = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
brr3.get(link)

#нажать на кнопку
magic_button = brr3.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
magic_button.click()

#Переключиться на новую вкладку
window_name = brr3.window_handles[1]
brr3.switch_to.window(window_name)


#Решить капчу
x = brr3.find_element(By.ID, "input_value")
x = x.text
y = calc(x)
brr3.find_element(By.ID, "answer").send_keys(y)
brr3.find_element(By.CSS_SELECTOR,"body > form > div > div > button").click()

#Получить значение с алерта:
alert = brr3.switch_to.alert
alert_text = alert.text
print(alert_text)
value = alert_text.split(" ")
print(value[-1])

#Закрыть браузер
time.sleep(10)
brr3.quit()
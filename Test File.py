import os
from selenium import webdriver
from selenium.webdriver.common.by import By

brr1 = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
brr1.get(link)

#Заполнить поля данными:
first_name = brr1.find_element(By.NAME, 'firstname')
first_name.send_keys("тест")
last_name = brr1.find_element(By.NAME, 'lastname')
last_name.send_keys("Тест")
email = brr1.find_element(By.NAME, "email")
email.send_keys("aa@bb.ru")

#Прикрепить файл
get_file = brr1.find_element(By.CSS_SELECTOR, "#file")
file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.txt')
get_file.send_keys(file_path)

#Нажать кнопку submit
submit_button = brr1.find_element(By.CSS_SELECTOR, "body > div > form > button")
submit_button.click()


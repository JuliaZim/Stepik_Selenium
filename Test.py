from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Задали переменную
link = 'http://suninjuly.github.io/huge_form.html'
try:
    #Запустили драйвер
    browser = webdriver.Chrome()
    #Открыли ссылку в браузере
    browser.get(link)
    #Нашли кнопку
    elements = browser.find_elements(By.TAG_NAME, "input")
    i=0
    for element in elements:
        element.send_keys(f'ням {i}')
        i+=1

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    print('end')
    #Закрываем браузер(все вкладки) и заквершили процесс драйвера
    #browser.quit()
    # функция browser.close() закрывает только текущую вкладку


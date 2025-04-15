import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAuth(unittest.TestCase):
    def testRegistration(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element(By.CSS_SELECTOR, '.first')
        first_name.send_keys('Julia')
        last_name = browser.find_element(By.CSS_SELECTOR, '.second')
        last_name.send_keys('Zimina')
        email = browser.find_element(By.CSS_SELECTOR, '.third')
        email.send_keys('zimtest@py.ru')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "тут описание ошибки")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    if __name__ == '__main__':
        testRegistration()
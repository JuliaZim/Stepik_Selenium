import time
import math
from selenium.webdriver.support import expected_conditions as EC

import pytest
from Tools.scripts.linktree import linknames
from numpy.distutils.command.config import config
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import os
import json

from selenium.webdriver.support.wait import WebDriverWait

answer = math.log(int(time.time()))
link = 'https://stepik.org/catalog?auth=login'
links = ['https://stepik.org/lesson/236895/step/1','https://stepik.org/lesson/236896/step/1','https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1']

@pytest.fixture(scope="class")
def load_config():
    with open('data.json', 'r') as config_file:
        config = json.load(config_file)
        return config
class TestLogin:
    def test_authorization(self, browser, load_config):
        link_1 = "https://stepik.org/lesson/236895/step/1"
        login = load_config['login_stepik']
        password = load_config['password_stepik']
        browser.get(link)
        try:
            login_input = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.NAME, 'login'))
            )
            password_input = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.NAME, 'password'))
            )

            login_input.send_keys(login)
            password_input.send_keys(password)

            # Явное ожидание для кнопки "Войти"
            login_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#login_form > button"))
            )
            login_button.click()

        except TimeoutException:
            print("Не удалось найти элементы авторизации или нажать на кнопку 'Войти' после 10 секунд.")
            raise  # Перебросить исключение, чтобы тест не продолжался

    @pytest.mark.parametrize("linklist", links)
    def test_stepik_links(self, browser, linklist):
        browser.get(linklist)
        # Явное ожидание для textarea и кнопки отправки
        try:
            textarea = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//textarea'))
            )
            textarea.send_keys(answer)
            submit_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[text()="Отправить"]'))
            )


            submit_button.click()
            time.sleep(5)
        except TimeoutException:
            print(f"Не удалось найти textarea или кнопку отправки на странице {linklist} после 10 секунд.")
            raise  # Перебросить исключение, чтобы тест не продолжался





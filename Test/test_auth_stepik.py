import pytest
from numpy.distutils.command.config import config
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import json

link = 'https://stepik.org/catalog?auth=login'

@pytest.fixture(scope="session")
def load_config():
    with open('data.json', 'r') as config_file:
        config = json.load(config_file)
        return config
class TestLogin:
    def test_authorization(self, browser, load_config):
        link_1 = "https://stepik.org/lesson/236895/step/1"
        login = load_config['login_stepik']
        password = load_config['password_stepik']
        browser.get(link_1)


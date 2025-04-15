from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser")
    time.sleep(10)
    browser.quit()

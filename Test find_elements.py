from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'https://fake-shop.com/book2.html'
brauser = webdriver.Chrome()
brauser.get(link)

add_button = brauser.find_element(By.CSS_SELECTOR, ".add")
add_button.click()

# открываем корзину
brauser.get("https://fake-shop.com/basket.html")

# ищем все добавленные товары
goods = brauser.find_elements(By.CSS_SELECTOR, ".good")

# проверяем, что количество товаров равно 2
assert len(goods) == 2
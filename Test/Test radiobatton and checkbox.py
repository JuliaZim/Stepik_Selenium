import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link_site = 'https://suninjuly.github.io/math.html'
br = webdriver.Chrome()
br.get(link_site)

x_value = br.find_element(By.ID, "input_value")
x = x_value.text
y = calc(x)

input_res = br.find_element(By.ID, 'answer')
input_res.send_keys(y)


checkbox_robot = br.find_element(By.ID, "robotCheckbox")
if not checkbox_robot.get_attribute('checked'):
  checkbox_robot.click()

radio_robot = br.find_element(By.ID, "robotsRule")
radio_robot.click()

button = br.find_element(By.CSS_SELECTOR, "body > div > form > button")
button.click()

time.sleep(15)
br.quit()
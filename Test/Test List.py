import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link_list = "https://suninjuly.github.io/selects1.html"
brr = webdriver.Chrome()
brr.get(link_list)

num1 = brr.find_element(By.ID, 'num1').text
num2 = brr.find_element(By.ID, 'num2').text
y = int(num1) + int(num2)
y1 = str(y)
print(num1, num2, y1)

select = Select(brr.find_element(By.TAG_NAME, "select"))
print(select)
select.select_by_value(y1)

brr.find_element(By.CSS_SELECTOR,"body > div > form > button").click()
time.sleep(10)
brr.quit()



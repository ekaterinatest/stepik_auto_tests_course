from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "num1")
    y_element = browser.find_element(By.ID, "num2")
    x = x_element.text
    y = y_element.text
    z = (int(x) + int(y))

    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(z))
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

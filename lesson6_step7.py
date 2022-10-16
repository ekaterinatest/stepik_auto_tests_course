from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("a")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("a")
    input3 = browser.find_element(By.NAME, "firstname")
    input3.send_keys("a")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("a")
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


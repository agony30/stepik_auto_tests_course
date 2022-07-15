from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    input_1 = browser.find_element(By.CLASS_NAME, 'btn, btn-primary')
    input_1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    input2 = browser.find_element(By.ID, 'answer')
    input2.send_keys(y)

    input_3 = browser.find_element(By.CLASS_NAME, 'btn, btn-primary')
    input_3.click()



finally:
    time.sleep(4)
    browser.quit()

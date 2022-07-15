from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    button_1 = browser.find_element(By.ID, "book")
    button_1.click()

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    input2 = browser.find_element(By.ID, 'answer')
    input2.send_keys(y)

    input_3 = browser.find_element(By.ID, 'solve')
    print(input_3.text)
    input_3.click()



finally:
    time.sleep(10)
    browser.quit()

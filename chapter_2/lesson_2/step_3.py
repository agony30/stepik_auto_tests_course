from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


try:
    link = 'http://suninjuly.github.io/selects2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # поиск суммы для ответа
    num_1_element = browser.find_element(By.ID, 'num1')
    num_1 = int(num_1_element.text)
    num_2_element = browser.find_element(By.ID, 'num2')
    num_2 = int(num_2_element.text)
    answer = num_1 + num_2

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_visible_text(str(answer))
    input4 = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    time.sleep(2)  # что бы понять что произошло
    input4.click()

finally:
    time.sleep(10)
    browser.quit()

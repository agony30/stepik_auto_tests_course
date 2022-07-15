from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys('Rinat')
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys('Davletyarov')
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys('email')

    input4 = browser.find_element(By.NAME, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    input4.send_keys(file_path)

    input5 = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    input5.click()

finally:
    time.sleep(4)
    browser.quit()

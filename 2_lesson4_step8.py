from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

def nothing():
  print('nothing') 
 
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID,'price'),'$100')
    )
    browser.find_element(By.ID,'book').click()

    x = browser.find_element(By.ID,'input_value').text
    y = calc(x)
    browser.find_element(By.TAG_NAME,'input').send_keys(y)
    browser.find_element(By.XPATH,'//button[text()="Submit"]').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

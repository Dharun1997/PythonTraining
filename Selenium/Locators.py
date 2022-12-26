import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service("C:\Driver\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input#Email").clear()
driver.find_element(By.CSS_SELECTOR,"input[type=password]").clear()
count = driver.find_elements(By.TAG_NAME,"input")
print(len(count))
time.sleep(5)
driver.close()
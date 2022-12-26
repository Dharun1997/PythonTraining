import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service("C:\Driver\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()

alertwindow=driver.switch_to.alert
print(alertwindow.text)

alertwindow.send_keys("Hi")
alertwindow.accept()
time.sleep(5)
#alertwindow.dismiss() - for choosing cancel option in alert

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(5)
driver.quit()
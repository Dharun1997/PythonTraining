import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import os
location=os.getcwd()

def chrome_setup():
    ser_obj=Service("C:\Driver\chromedriver_win32\chromedriver.exe")
    preferences={"download.default_directory":location}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option('prefs',preferences)
    driver = webdriver.Chrome(service=ser_obj, options=ops)
    return driver

driver=chrome_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
driver.maximize_window()
time.sleep(5)
alerts=driver.switch_to.alert
alerts.dismiss()
driver.find_element(By.XPATH,"//*[@id='table-files']/tbody/tr[1]/td[5]/a").click()
time.sleep(10)
driver.close()

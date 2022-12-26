import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

ser_obj=Service("C:\Driver\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(3)
#driver.get_screenshot_as_file(os.getcwd()+"\\sc.png")
newtab=Keys.CONTROL+Keys.RETURN
driver.find_element(By.LINK_TEXT,"Register").send_keys(newtab)
driver.switch_to.new_window('tab')
driver.get("https://www.opencart.com/")
time.sleep(5)
driver.close()
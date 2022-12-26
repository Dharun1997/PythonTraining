import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import os
def headless():
    ser_obj=Service("C:\Driver\chromedriver_win32\chromedriver.exe")
    ops=webdriver.ChromeOptions()
    ops.headless=True
    driver=webdriver.Chrome(service=ser_obj, options=ops)
    return driver

driver=headless()
driver.get("https://demo.nopcommerce.com/")
print(len(driver.get_cookies()))
driver.add_cookie({"name":"Tharun","value":"26"})
print(len(driver.get_cookies()))
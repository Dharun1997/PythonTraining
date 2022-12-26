import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
ser_obj=Service("C:\Driver\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
#def launchBrowser():
    #chrome_options=Options()
    #chrome_options.binary_location="../Google Chrome"
   # chrome_options.add_argument("start-maximized")
    #driver=webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://admo.nopcommerce.com/loginin-dem")
#driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(10)
driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("Tharun")
time.sleep(10)
   # return driver
#launchBrowser()
driver.close()

#dr
#driver.find_element(By.NAME,"username").clear()
#driver.find_element(By.NAME,"username").send_keys("Admin")





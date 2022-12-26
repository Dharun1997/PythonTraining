import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser_obj=Service("C:\Driver\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()
time.sleep(5)

self_name=driver.find_element(By.XPATH,"//a[contains(text(),'PTC India')]/self::a").text
print("Self element is",self_name)

parent_name=driver.find_element(By.XPATH,"//a[contains(text(),'PTC India')]/parent::td").text
print("Parent element is",parent_name)

child_name=driver.find_elements(By.XPATH,"//a[contains(text(),'PTC India')]/ancestor::tr/child::td")
print(len(child_name))

following=driver.find_elements(By.XPATH,"//a[contains(text(),'PTC India')]/ancestor::tr/following::*")
print(len(following))

descendant=driver.find_elements(By.XPATH,"//a[contains(text(),'PTC India')]/ancestor::tr/descendant::*")
print(len(descendant))


driver.close()


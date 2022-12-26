import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service("C:\Driver\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

driver.get("https://text-compare.com/")
driver.maximize_window()
time.sleep(3)

input1=driver.find_element(By.XPATH,"//*[@id='inputText1']")
input1.send_keys("Krijeshan is a dash")

#CTRL+A
act=ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#CTRL+C
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

#tab
act.send_keys(Keys.TAB).perform()

#CTRL+V
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(20)
driver.close()
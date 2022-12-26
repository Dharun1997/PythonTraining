import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser_obj=Service("C:\Driver\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Search' and @type='text']").send_keys("Products")
driver.find_element(By.XPATH,"//div[@class='tt-dataset tt-dataset-pages']//div[1]//h5[1]").click()
selobj=Select(driver.find_element(By.XPATH,"//select[@id='SearchWarehouseId']"))
selobj.select_by_index(2)
#driver.find_element(By.XPATH,"//div[@class='tt-dataset tt-dataset-pages']//div[1]//h5[1]").click()
time.sleep(5)
driver.close()

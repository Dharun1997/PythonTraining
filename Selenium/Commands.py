import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser_obj=Service("C:\Driver\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

driver.get("https://admin-demo.nopcommerce.com/admin/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(5)

driver.find_element(By.XPATH,"//button[@type='submit']").click()
#driver.find_element(By.XPATH,"//div[@id='configuration-steps-card']//i[@class='fas fa-plus']").click()
driver.find_element(By.XPATH,"//a[@class='configuration-step-link theme-step']//h5[1]").click()
driver.find_element(By.XPATH,"//button[@aria-label='Close Tour']//span[@aria-hidden='true'][normalize-space()='×']").click()
driver.find_element(By.XPATH,"//input[@id='StoreInformationSettings_DisplayEuCookieLawWarning']").click()
#checkbox=driver.find_element(By.XPATH,"//input[@id='StoreInformationSettings_DisplayEuCookieLawWarning']")
#print(checkbox.is_selected())
button=driver.find_element(By.XPATH,"//input[@value='http://www.facebook.com/nopCommerce']")
print(button.is_displayed())
print(button.is_enabled())
driver.back()
driver.forward()
time.sleep(5)

driver.quit()
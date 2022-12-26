import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service("C:\Driver\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(3)

#customized xpath
rows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))
columns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr/th"))

for r in range(2,rows+1):
    for c in range(1,columns+1):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data,end='     ')
    print("\n")

driver.close()


import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service("C:\Driver\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

driver.get("http://deadlinkcity.com/")
driver.maximize_window()

links=driver.find_elements(By.TAG_NAME,'a')
count=0

for link in links:
    try:
        url=link.get_attribute('href')
    except:
        None

    response=requests.head(url)
    if response.status_code>=400:
        count=count+1
        print(url," is a broken link")
    else:
        print(url," is a valid link")

print("Total no of broken link ", count)




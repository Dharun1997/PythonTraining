import time
import openpyxl

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Selenium12 import Utility

ser_obj=Service("C:\Driver\chromedriver_win32\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
driver=webdriver.Chrome(service=ser_obj,options=options)


driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
driver.implicitly_wait(20)


file="C:\\Users\\DHARUN R\\Desktop\\sample.xlsx"
rows=Utility.rowcount(file,"Sheet1")
columns=Utility.columncount(file,"Sheet1")

for r in range(2,rows+1):
        principal=Utility.readData(file,"Sheet1",r,1)
        roi=Utility.readData(file,"Sheet1",r,2)
        period1=Utility.readData(file,"Sheet1",r,3)
        period2=Utility.readData(file,"Sheet1",r,4)
        frequency=Utility.readData(file,"Sheet1",r,5)
        exp_maturity=Utility.readData(file,"Sheet1",r,6)

        driver.find_element(By.XPATH,"//*[@id='principal']").send_keys(principal)
        driver.find_element(By.XPATH,"//*[@id='interest']").send_keys(roi)
        driver.find_element(By.XPATH,"//*[@id='tenure']").send_keys(period1)
        driver.find_element(By.XPATH,"//*[@id='tenurePeriod']").send_keys(period2)
        driver.find_element(By.XPATH,"//*[@id='frequency']").send_keys(frequency)
        act_maturity=driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text

        if exp_maturity==act_maturity:
            print("Passed")
            Utility.writeData(file,"Sheet1",r,7,"Passed")
            Utility.green(file,"Sheet1",r,7)
        else:
            print("Passed")
            Utility.writeData(file,"Sheet1",r,7,"Passed")
            Utility.red(file,"Sheet1",r,7)

        driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
        time.sleep(5)








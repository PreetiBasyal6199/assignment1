from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://hamrobazaar.com/c112-real-estate")
catagories=driver.find_elements(By.XPATH,'//*[@id="tab_cat1"]/table/tbody/tr/td/font/a/b')
for catagory in catagories:
    print(catagory.text)

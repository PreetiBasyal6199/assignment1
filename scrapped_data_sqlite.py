import sqlite3
from selenium.common import exceptions
import time
# create connection
conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('''CREATE TABLE details(item_name TEXT, general_details TEXT,description TEXT)''')

from selenium import webdriver
# import pandas as pd
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
templist=[]
driver.get("https://hamrobazaar.com/c112-real-estate")
for i in range (4,30):
    for table in driver.find_elements(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table['+ str(i) +']/tbody'):
       items= table.find_elements(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table['+ str(i) +']/tbody/tr[1]/td[3]/a[1]')
       for item in items:
            item.click()
            driver.switch_to.window(driver.window_handles[-1])
            selling_item=driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table[4]/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr/td[1]/span/b/font').text
            general_details=driver.find_element(By.XPATH,'//*[@id="lblue"]/tbody').text
            description=driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table[4]/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td[1]/table[3]/tbody/tr/td/table/tbody').text
           
           
            
            c.execute('''INSERT INTO details VALUES(?,?,?)''',(selling_item,general_details,description))
            driver.switch_to.window(driver.window_handles[0])
           
conn.commit()

driver.close()
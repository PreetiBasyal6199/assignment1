from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://hamrobazaar.com/c112-real-estate")
data=[]
for table in driver.find_elements(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table/tbody'):
        selling_item = [item.text for item in table.find_elements(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table/tbody/tr[1]/td[3]/a[1]/font/b')]   
        seller_name=[item.text for item in table.find_elements(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table/tbody/tr[1]/td[3]/a[2]')]
        seller_address=[item.text for item in table.find_elements(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table/tbody/tr[1]/td[3]/font[2]')]
        price=[item.text for item in table.find_elements(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table/tbody/tr[1]/td[5]/b')]
        date =[item.text for item in table.find_elements(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table/tbody/tr[1]/td[4]')]
print("***********Selling Items***************")
print(selling_item)
print("***********Seller Name***************")
print(seller_name)
print("***********Seller Adddress***************")
print(seller_address)
print("***********Item Price***************")
print(price)
print("***********Posted Date***************")
print(date)


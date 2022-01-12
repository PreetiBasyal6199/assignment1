from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://hamrobazaar.com/c112-real-estate")
data=[]
for i in range (4,9):
    
    for table in driver.find_elements(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table[4]/tbody'):
        
       
        selling_item = [item.text for item in table.find_elements(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table['+ str(i) +']/tbody/tr[1]/td[3]/a[1]/font/b')]   
        seller_name=[item.text for item in table.find_elements(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table['+ str(i)+']/tbody/tr[1]/td[3]/a[2]')]
        seller_address=[item.text for item in table.find_elements(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table['+ str(i)+']/tbody/tr[1]/td[3]/font[2]')]
        price=[item.text for item in table.find_elements(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table['+ str(i)+']/tbody/tr[1]/td[5]/b')]
        date =[item.text for item in table.find_elements(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table['+str(i)+']/tbody/tr[1]/td[4]')]
        data.append([selling_item,seller_name,seller_address,price,date])
       
print(data)
   
    



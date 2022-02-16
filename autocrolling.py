from pandas import value_counts
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

from sympy import appellf1



project =[]
corpName =[]
corpNum =[]
manager = []
phone = []
email = []
endflag = '주식회사 씨앤엠'
lastpage = 6
find = False
### 접속 ###
driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://1st.smart-factory.kr/login.do")

### 로그인 ###
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/span[2]/a").click()
id = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/form/dl/dd[1]/input')
id.send_keys("tipa103")
pw=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/form/dl/dd[2]/input')
pw.send_keys("rlwjddnjs@123")
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div[1]/a').click()

### 요건검토 접속 ###
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/div[1]/a[1]").click()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[1]/ul/li[3]/a').click()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[1]/ul/li[3]/div/a[1]').click()

### 사업 선택 ###
select = Select(driver.find_element_by_id('searchBsnsSeCd'))
select.select_by_value('0000004I')
time.sleep(0.2)
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[4]/a').send_keys("Keys.Return")
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[4]/a').click()
time.sleep(0.2)

for j in range(1,lastpage):

    for i in range(1,11):
        print(str((10*(j-1))+i))
        
        if j >=2:
            time.sleep(0.3)
            page = '/html/body/div[2]/div[2]/div/div[6]/div[2]/div/a['+str(j+2)+']'
            driver.find_element_by_xpath(page).click()
        
        time.sleep(0.3)
        driver.find_element_by_id(str((10*(j-1))+i)).click()
        time.sleep(0.3)
        corpNameTemp = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[6]/form/div/table/tbody/tr[2]/td[1]').text
        print("corpTemp : ", corpNameTemp)
        if corpNameTemp == endflag:
            print("Stop by Endflag")
            find = True
            break
        project.append(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[6]/form/div/table/tbody/tr[1]/td/div/input').get_attribute("value"))
        corpName.append(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[6]/form/div/table/tbody/tr[2]/td[1]').text) 
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[5]/span[2]/a').click()
        time.sleep(0.3)
        corpNum.append((driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[6]/form/div[1]/table/tbody/tr[2]/td[1]').text))
        manager.append((driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[6]/form/div[5]/table/tbody/tr[1]/td[1]').text))
        phone.append((driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[6]/form/div[5]/table/tbody/tr[3]/td[1]').text))
        email.append((driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[6]/form/div[5]/table/tbody/tr[3]/td[2]').text))
        driver.back()
        time.sleep(0.3)
        driver.back()
    time.sleep(0.3)
    if find:
        break

    
print(project, corpName, corpNum, manager, phone, email)
"""
### 과제 선택 ###
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[6]/div[1]/div[3]/div[3]/div/table/tbody/tr[2]").click()
time.sleep(2)

### 기업 정보 수집 ###
project.append(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[6]/form/div/table/tbody/tr[1]/td/div/input').get_attribute("value"))
corpName.append(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[6]/form/div/table/tbody/tr[2]/td[1]').text) 
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[5]/span[2]/a').click()
time.sleep(2)
corpNum.append((driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[6]/form/div[1]/table/tbody/tr[2]/td[1]').text))
manager.append((driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[6]/form/div[5]/table/tbody/tr[1]/td[1]').text))
phone.append((driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[6]/form/div[5]/table/tbody/tr[3]/td[1]').text))
email.append((driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[6]/form/div[5]/table/tbody/tr[3]/td[2]').text))


print(project, corpName, corpNum, manager, phone, email)

driver.back()
time.sleep(0.5)
driver.back()
time.sleep(0.5)
"""

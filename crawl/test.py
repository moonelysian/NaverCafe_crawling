from selenium import webdriver
import chromedriver_binary
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os
import sys
import re

driver = webdriver.Chrome()
driver.get('http://www.bananany.com/Login')

user_id = ''
user_pw = ''

#로그인
driver.find_element_by_xpath('//*[@id="user_id"]').send_keys(user_id)
driver.find_element_by_xpath('//*[@id="user_pwd"]').send_keys(user_pw)
driver.find_element_by_xpath('//*[@id="login_frame1"]/input[3]').click()

elemente = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.jquery-modal.blocker.current"))
    )

imgList = elemente.find_element_by_id('gd_listimg').get_attribute('innerHTML')
section = elemente.find_elements_by_xpath('//*[@id="pro_pop"]/ul/li[2]/section')

for x in section:
    context = bs(x.get_attribute('innerHTML'), 'html.parser')

titleList = context.select('#pro_name')
proInfoList = context.select('#pro_info')

for title in titleList:
    print(title.get_text())

infoLi = []

for pro_info in proInfoList:
    infoLi = pro_info.select('li')

details = []

for li in infoLi:
    details.append(li.get_text())

detail = "\n".join(details)
print(detail)



# soup = bs(imgList, 'html.parser')

# imgs = soup.find_all('img')
# divs = soup.find_all('div')

# for div in divs:
#     if(div.get_text()):
#         print(div.get_text())

# for img in imgs:
#     print(img.attrs['src'])

    

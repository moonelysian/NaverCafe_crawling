from selenium import webdriver
import chromedriver_binary
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import pandas as pd
import time
import os
import sys
import re

driver = webdriver.Chrome()
driver.get('https://sinsangmarket.kr')

user_id = ''
user_pw = ''

driver.execute_script("$('#login_container').css('display', '');") 

time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="login_container"]/div[2]/div[2]/form/input[1]').send_keys(user_id)
driver.find_element_by_xpath('//*[@id="login_container"]/div[2]/div[2]/form/input[2]').send_keys(user_pw)
driver.find_element_by_xpath('//*[@id="login_container"]/div[2]/div[2]/form/div/button[1]').click()

time.sleep(1)

driver.get('https://sinsangmarket.kr/v3/goodsDetail?gid=31576017')

time.sleep(2)

soup = bs(driver.page_source, 'html.parser')

time.sleep(1)

title = soup.select('div.goods_name')[0].get_text()
details = soup.find_all('td')

content = ''

for detail in details:
    content += (detail.get_text()+'\n')

# samples = soup.find_all('img', height=80)

# img_urls = []

# for url in samples:
#     r = re.compile('src="(.*?)&amp')
#     m = r.search(str(url))
#     if m:
#         img_urls.append(str(m.group(1))+'&h=800&w=800')
        
# print(img_urls)

driver.quit()
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

driver.find_element_by_xpath('//*[@id="login_container"]/div[2]/div[2]/form/input[1]').send_keys(user_id)
driver.find_element_by_xpath('//*[@id="login_container"]/div[2]/div[2]/form/input[2]').send_keys(user_pw)
driver.find_element_by_xpath('//*[@id="login_container"]/div[2]/div[2]/form/div/button[1]').click()

time.sleep(2)

driver.get('https://sinsangmarket.kr/v3/goodsDetail?gid=31576017')
time.sleep(1)
soup = bs(driver.page_source, 'html.parser')
sample = soup.find_all('img', height=80)

print(sample)
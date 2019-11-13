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

time.sleep(3)

driver.find_element_by_xpath('//*[@id="hl_list4"]/li[1]/figure/a').click()
elemente = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.jquery-modal.blocker.current"))
    )

test = elemente.find_element_by_id('gd_listimg').get_attribute('innerHTML')

soup = bs(test, 'html.parser')

imgs = soup.find_all('img')
div = soup.find_all('div')

for d in div:
    if(d.get_text()):
        print(d.get_text())

for img in imgs:
    print(img.attrs['src'])

    

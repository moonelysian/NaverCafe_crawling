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

time.sleep(2)

#찜목록으로 이동
# driver.get('http://byamber.co.kr/Mypage?m=3#/')

#제품 클릭 기다리기
elemente = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.jquery-modal.blocker.current"))
    )

imgList = elemente.find_element_by_id('gd_listimg').get_attribute('innerHTML')
section = elemente.find_elements_by_xpath('//*[@id="pro_pop"]/ul/li[2]/section')

for x in section:
    context = bs(x.get_attribute('innerHTML'), 'html.parser')

titleList = context.select('#pro_name')
proInfoList = context.select('#pro_info')

details = []

#제품명 가져오기
for t in titleList:
    title = t.get_text().split('[')[0]

details.append(title)

#이미지 리스트
soup = bs(imgList, 'html.parser')

#img tag
imgs = soup.find_all('img')

#제품 정보
sizeInfo = soup.find_all('div')

for size in sizeInfo:
    if(size.get_text()):
        details.append(size.get_text())


download_path  = "C:\\Users\\JSPARK\\Downloads\\" + title + "\\"

# if not(os.path.exists(download_path)):
#             os.makedirs(download_path)

# for key, value in enumerate(imgs):
#     img_url = urlopen(value.attrs['src']).read()
    
#     filename = download_path + str(key) + '.jpg'

    #해당 파일이 있으면 저장하지 않고 없으면
    # if not(os.path.exists(filename)):
    #     with open(filename,"wb") as f:
    #         f.write(img_url)
    #     print("Image Save Success")

detail_Li = []
options = []

for pro_info in proInfoList:
    detail_Li = pro_info.select('li > div > p')
    options = pro_info.select('li > select > option')
    total_li = pro_info.select('li')

for t in range(7):
    print(total_li[t].get_text())

for li in detail_Li:
    details.append(li.get_text())

for option in options:
    details.append(option.get_text())

detail = "\n".join(details)
print(detail)


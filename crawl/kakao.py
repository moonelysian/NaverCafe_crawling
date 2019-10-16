from selenium import webdriver
import chromedriver_binary
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import pandas as pd
import time
import os
import sys
import json
import re


class KakaoCrawling:
    def kakao_crawling(url, downloadpath):
        driver = webdriver.Chrome()

        driver.get('https://accounts.kakao.com/login/kakaostory')
        
        user_id = ''
        user_pw = ''

        driver.find_element_by_xpath('//*[@id="id_email_2"]').send_keys(user_id)
        driver.find_element_by_xpath('//*[@id="id_password_3"]').send_keys(user_pw)
        driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button').click()

        time.sleep(2)

        splitUrl = url.rsplit('/',2)
        storeURL = splitUrl[0]

        driver.get(url)

        soup = bs(driver.page_source, 'html.parser')
        script = str(soup.find_all('script')[1]).split('\n')

        test = script[1].replace("boot.parseInitialData(",'')
        test = test.replace( ");" , '')

        data = json.loads(test)
        
        img_urls = []

        for img in data['activity']['media']:
            img_urls.append( img['origin_url'] )

        for index in range(len(img_urls)):
            
            #원본url 읽어오기
            t = urlopen(img_urls[index]).read() 
            
            #폴더 없으면 생성
            if not(os.path.exists(downloadpath)):
                os.makedirs(downloadpath)

            filename = downloadpath + "/" + str(index) + '.jpg'

            #해당 파일이 있으면 저장하지 않고 없으면
            if not(os.path.exists(filename)):
                with open(filename,"wb") as f:
                    f.write(t)
                print("Image Save Success")

        print("Done!")
        driver.quit()
       
        return True
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

        driver.get(url)

        soup = bs(driver.page_source, 'html.parser')
        script = str(soup.find_all('script')[1]).split('\n')

        #sripte 태그 + 불필요한 부분 제거 + 제이슨 형식으로 변경
        test = script[1].replace("boot.parseInitialData(",'')
        test = test.replace( ");" , '')

        textfile = downloadpath + "/" + "info" + ".txt"

        try:
            data = json.loads(test)
            createdDate = data['activity']['created_at'].split('T')
            date = "제품 업로드 날짜: " + str(createdDate[0]) + "\n"
        
            #제품 정보
            info = data['activity']['content']
            images = data['activity']['media']

        except:
            r = re.compile('"content":(.*?),"require')
            m = r.search(test)
            
            if m:
                context = m.group(1)
 
            
            i = re.compile('"media":(.*?),"content"')
            j = i.search(test)
            
            if j:
                images = json.loads(j.group(1))
                


        #image 원본 url 저장할 배열
        img_urls = [] 
        

        #원본 url 저장
        for img in images:
            img_urls.append( img['origin_url'] )

        #이미지 다운로드
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

        #제품 올린 날짜
        # createdDate = data['activity']['created_at'].split('T')
        # date = "제품 업로드 날짜: " + str(createdDate[0]) + "\n"
        
        # #제품설명 가져오기
        # info = data['activity']['content']
        # textfile = downloadpath + "/" + "info" + ".txt"

        #제품설명txt파일 쓰기
        f = open(textfile, "w" , -1, "utf-8")
        f.write(date)
        for i in info: 
            f.write(i)
        
        f.close()

        print("Done!")
        driver.quit()
       
        return True
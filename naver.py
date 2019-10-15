from selenium import webdriver
import chromedriver_binary
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import pandas as pd
import time
import os
import sys

class NaverCrawling:
    def naver_crawling(page, downloadPath):

        driver = webdriver.Chrome()

        # driver = webdriver.Chrome('chromedriver')
        driver.get('https://nid.naver.com/nidlogin.login')

        user_id = ''
        user_pw = ''

        driver.execute_script("document.getElementsByName('id')[0].value=\'" + user_id + "\'")
        driver.execute_script("document.getElementsByName('pw')[0].value=\'" + user_pw + "\'")
        driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

        time.sleep(1)

        base_url = 'https://cafe.naver.com/ArticleList.nhn?search.clubid=29179343&search.menuid=6&search.boardtype=L&search.totalCount=151'


        driver.get(base_url + "&search.page=" + page)
        driver.switch_to.frame('cafe_main')

        article_list = driver.find_elements_by_css_selector('span.aaa > a.m-tcol-c')
        article_urls = [ i.get_attribute('href') for i in article_list ]
        res_list = []

        for article in article_urls:
            driver.get(article)
            driver.switch_to.frame('cafe_main')
            soup = bs(driver.page_source, 'html.parser')
            
            title = soup.select('div.tit-box span.b')[0].get_text()
            
            #원본url이 써있는 script 가져옴
            photoAlbum = soup.find_all('script',{'filename':'externalFile.jpg'}) 

            for i in enumerate(photoAlbum):
                index = str(i[0])
                downloadEnd = False
                #이미지 저장위치지정
                # downloadPath = "C:/Users/JSPARK/Downloads/"
                filepath = downloadPath + title
                
                #원본url 읽어오기
                t = urlopen(i[1].attrs['fileurl']).read() 
                
                #폴더 없으면 생성
                if not(os.path.exists(downloadPath + title)):
                    os.makedirs(filepath)

                filename = filepath + "/" + index + '.jpg'

                #해당 파일이 있으면 저장하지 않고 없으면
                if not(os.path.exists(filename)):
                    with open(filename,"wb") as f:
                        f.write(t)
                    print("Image Save Success")

                else:
                    downloadEnd = True
                    print("pass")
                    break

            if downloadEnd :
                print("done!!")
                break
            
        driver.quit()

        return True
        


    
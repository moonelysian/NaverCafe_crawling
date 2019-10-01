from selenium import webdriver
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import pandas as pd
import time
import os
driver = webdriver.Chrome('chromedriver')
driver.get('https://nid.naver.com/nidlogin.login')

user_id = ""
user_pw = ""

driver.execute_script("document.getElementsByName('id')[0].value=\'" + user_id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + user_pw + "\'")
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

time.sleep(1)

base_url = 'https://cafe.naver.com/ArticleList.nhn?search.clubid=29179343&search.menuid=6&search.boardtype=L&search.totalCount=151'

print("page 번호 입력")
page = input()


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
    tbody = soup.find('div',{'id':'tbody'})
    img = tbody.find_all('img')    
    
    for i in enumerate(img[1:]):
        index = str(i[0])
        downloadPath = "C:/Users/JSPARK/Downloads/"
        filepath = downloadPath + title
        t = urlopen(i[1].attrs['src']).read()

        if not(os.path.exists(downloadPath + title)):
            os.makedirs(filepath)

        filename = filepath + "/" + index + '.jpg'

        if not(os.path.exists(filename)):
            with open(filename,"wb") as f:
                f.write(t)
        else:
            print("pass")
            break

    print("Image Save Success")
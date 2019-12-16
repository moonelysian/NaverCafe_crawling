from selenium import webdriver
import chromedriver_binary
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import time
import os
import re


class NaverBlog:
    driver = webdriver.Chrome()
    driver.get('https://blog.naver.com/monica4460/221720703860')

    driver.switch_to.frame('mainFrame')
    soup = bs(driver.page_source, 'html.parser')

    test1 = soup.select('div.se-module')
    for t in test1:
        print(t.get_text())

    test2 = soup.select('img.se-image-resource')

    download_path = "C:\\Users\\JSPARK\\Downloads\\"

    for index, url in enumerate(test2):
        filename = download_path + "/" + str(index) + ".jpg"
        original = url.attrs['src'].split('?')[0].replace('postfiles','blogfiles')
        
        if not(os.path.exists(filename)):
            with open(filename, 'wb') as f:
                f.write(urlopen(original).read())
            print('success')


from selenium import webdriver
import chromedriver_binary
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import sys

driver = webdriver.Chrome()

url = 'http://www.thist.co.kr/Login'
driver.get(url)


# http://www.thist.co.kr/Login 디스티
# http://www.brownsoul.co.kr/Login 브라운소울
# http://www.mayone.co.kr/Login 메이원
# http://www.thehaemil.co.kr/Login 해밀
# http://www.dduddu.co.kr/Login 뚜뚜
# http://www.j-factory.co.kr/Login 제이팩토리
# http://www.gaudistyle.co.kr/Login 가우디
# http://www.bleestyle.com/Login 블리
# http://www.babyshu.co.kr/Login 베이비슈
# http://www.thevera.co.kr/Login 베라
# http://www.terrior.co.kr/Login 라임
# http://www.dks08.co.kr/Login 닥스
# http://www.thedoorim.com/Login 두림
# http://www.bymun.co.kr/Login 문
# http://www.ban-hana.co.kr/Login 반하나
# http://www.siutimtim.com/Login 시우팀팀
# http://byamber.co.kr/Login 엠버
# http://byundercover.com/Login 언더커버
# http://www.bananany.com/Login 바나나뉴욕



if(url=='http://www.j-factory.co.kr/Login'):
    user_id = ''
    user_pw = ''

else:
    user_id = ''
    user_pw = ''

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
        details.append('\n')

for pro_info in proInfoList:
    #제품 비침, 신축성, 두께감 정보
    detail_info = pro_info.select('li > div > p')
    #색상, 사이즈 옵션 
    options = pro_info.select('li > select > option')
    #가격, 혼용률 정보
    price_etc = pro_info.select('li')

for i in range(7):
    #8번째 li까지 - 도매가, 혼용률, 중량, 원산지, 등록일자, 모델 정보
    details.append(price_etc[i].get_text())

details.append('\n')

for li in detail_info:
    #제품 비침, 신축성, 두께감 정보 추가
    details.append(li.get_text())

details.append('\n')

for option in options:
    #색상, 사이즈 옵션 추가
    details.append(option.get_text())

details.append('\n')

detail = "\n".join(details)

#다운로드 경로
download_path  = "C:\\Users\\JSPARK\\Downloads\\" + title + "\\"
#제품정보 저장할 파일
info_file = download_path + "\\" + "info" + ".txt"

if not(os.path.exists(download_path)):
            os.makedirs(download_path)

f = open(info_file, "w" , -1, "utf-8")
for d in detail:
    f.write(d)

for key, value in enumerate(imgs):
    img_url = urlopen(value.attrs['src']).read()
    
    filename = download_path + str(key) + '.jpg'

    #해당 파일이 있으면 저장하지 않고 없으면 저장
    if not(os.path.exists(filename)):
        with open(filename,"wb") as f:
            f.write(img_url)
        print("Image Save Success")
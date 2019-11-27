import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

# from selenium import webdriver
import chromedriver_binary

sys.path.insert(0, "./crawl")

from crawl.naver import NaverCrawling as nc
from crawl.kakao import KakaoCrawling as kc
from crawl.test import WebCrawling as wc

form_class = uic.loadUiType("./ui/crawling.ui")[0]

class WindowClass(QMainWindow, form_class) :
    
    def __init__(self) :
        super().__init__()

        path = "C:\\Users\\JSPARK\\Downloads\\"
        # path = "C:\\Users\\Seoyoung\\Downloads\\"
        # path = "D:\\이연주"

        self.setupUi(self)

        self.download_naver.setText(path)
        self.download_kakao.setText(path)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('READY')
        
        #tab1 - 카스 네이버
        self.btn_crawling.clicked.connect(self.startCrawling)
        self.btn_clear.clicked.connect(self.clean)
        self.pushButton.clicked.connect(self.findPath_kakao)
        self.pushButton_2.clicked.connect(self.findPath_naver)

        #tab2 - 개별 웹페이지
        #가우디
        self.gaudistyle.clicked.connect(lambda state, button=self.gaudistyle : self.pageCrawling(state, button))
        #닥스
        self.dks08.clicked.connect(lambda state, button=self.dks08 : self.pageCrawling(state, button))
        #두림
        self.thedoorim.clicked.connect(lambda state, button=self.thedoorim : self.pageCrawling(state, button))
        #디스티
        self.thist.clicked.connect(lambda state, button=self.thist : self.pageCrawling(state, button))
        # 라임
        self.terrior.clicked.connect(lambda state, button=self.terrior : self.pageCrawling(state, button))
        # 문
        self.bymun.clicked.connect(lambda state, button=self.bymun : self.pageCrawling(state, button))
        # 메이원
        self.mayone.clicked.connect(lambda state, button=self.mayone : self.pageCrawling(state, button))
        # 바나나뉴욕
        self.bananany.clicked.connect(lambda state, button=self.bananany : self.pageCrawling(state, button))
        # 브라운소울
        self.brownsoul.clicked.connect(lambda state, button=self.brownsoul : self.pageCrawling(state, button))
        # 블리
        self.bleestyle.clicked.connect(lambda state, button=self.bleestyle : self.pageCrawling(state, button))
        # 베라
        self.thevera.clicked.connect(lambda state, button=self.thevera : self.pageCrawling(state, button))
        # 베이비슈
        self.thist.clicked.connect(lambda state, button=self.babyshu : self.pageCrawling(state, button))
        # 반하나
        self.babyshu.clicked.connect(lambda state, button=self.banhana : self.pageCrawling(state, button))
        # 시우팀팀
        self.siutimtim.clicked.connect(lambda state, button=self.siutimtim : self.pageCrawling(state, button))
        # 언더커버
        self.byundercover.clicked.connect(lambda state, button=self.byundercover : self.pageCrawling(state, button))
        # 엠버
        self.byamber.clicked.connect(lambda state, button=self.byamber : self.pageCrawling(state, button))
        # 제이팩토리
        self.jfactory.clicked.connect(lambda state, button=self.jfactory : self.pageCrawling(state, button))
        # 뚜뚜
        self.dduddu.clicked.connect(lambda state, button=self.dduddu : self.pageCrawling(state, button))
        # 해밀
        self.thehaemil.clicked.connect(lambda state, button=self.thehaemil : self.pageCrawling(state, button))
    
    def pageCrawling(self, state, button):
        buttonName = button.text()
        print(buttonName)
        if buttonName == '가우디':
            wc.web_crawling('http://www.gaudistyle.co.kr/')
        
        elif buttonName == '닥스':
            wc.web_crawling('http://www.dks08.co.kr/')
        
        elif buttonName == '두림':
            wc.web_crawling('http://www.thedoorim.com/')
        
        elif buttonName == '디스티':
            wc.web_crawling('http://www.thist.co.kr/')

        elif buttonName == '라임':
            wc.web_crawling('http://www.terrior.co.kr/')

        elif buttonName == '문':
            wc.web_crawling('http://www.bymun.co.kr/')
        
        elif buttonName == '메이원':
            wc.web_crawling('http://www.mayone.co.kr/')
        
        elif buttonName == '바나나뉴욕':
            wc.web_crawling('http://www.bananany.com/')
        
        elif buttonName == '브라운소울':
            wc.web_crawling('http://www.brownsoul.co.kr/')
        
        elif buttonName == '블리':
            wc.web_crawling('http://www.bleestyle.com/')
        
        elif buttonName == '베라':
            wc.web_crawling('http://www.thevera.co.kr/')
        
        elif buttonName == '베이비슈':
            wc.web_crawling('http://www.babyshu.co.kr/')
        
        elif buttonName == '반하나':
            wc.web_crawling('http://www.ban-hana.co.kr/')
        
        elif buttonName == '시우팀팀':
            wc.web_crawling('http://www.siutimtim.com/ ')
        
        elif buttonName == '언더커버':
            wc.web_crawling('http://byundercover.com/')
        
        elif buttonName == '엠버':
            wc.web_crawling('http://byamber.co.kr/')
        
        elif buttonName == '제이팩토리':
            wc.web_crawling('http://www.j-factory.co.kr/')
        
        elif buttonName == '뚜뚜':
            wc.web_crawling('http://www.dduddu.co.kr/')
        
        elif buttonName == '해밀':
            wc.web_crawling('http://www.thehaemil.co.kr/')

    def startCrawling(self) :

        page = self.pagenum.text()
        url = self.url.text()
        self.statusBar.showMessage('WORKING')

        downloadpath_naver = self.download_naver.text()
        downloadpath_kakao = self.download_kakao.text()

        if page != '':
            if(nc.naver_crawling(page, downloadpath_naver)):
                self.statusBar.showMessage('DONE')

        if url != '':
            if(kc.kakao_crawling(url, downloadpath_kakao)):
                self.statusBar.showMessage('DONE')
    
    def clean(self):

        path = "C:\\Users\\JSPARK\\Downloads\\"
        # path = "C:\\Users\\Seoyoung\\Downloads\\"
        # path = "D:\\이연주"
        
        self.pagenum.clear()
        self.url.clear()

        self.download_naver.clear()
        self.download_kakao.clear()

        self.download_naver.setText(path)
        self.download_kakao.setText(path)

        self.statusBar.showMessage('READY')
    
    def findPath_kakao(self):
        fname = QFileDialog.getExistingDirectory(self)
        self.download_kakao.setText(fname)

    def findPath_naver(self):
        fname = QFileDialog.getExistingDirectory(self)
        self.download_naver.setText(fname)



if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
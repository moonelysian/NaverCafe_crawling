import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

# from selenium import webdriver
import chromedriver_binary

sys.path.insert(0, "./crawl")

from crawl.naver import NaverCrawling as nc
from crawl.kakao import KakaoCrawling as kc

form_class = uic.loadUiType("./ui/crawling.ui")[0]


class WindowClass(QMainWindow, form_class) :
    
    def __init__(self) :
        super().__init__()

        path = "C:\\Users\\JSPARK\\Downloads\\"
        # path = "C:\\Users\\Seoyoung\\Downloads\\"

        self.setupUi(self)

        self.download_naver.setText(path)
        self.download_kakao.setText(path)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('READY')
        
        self.btn_crawling.clicked.connect(self.startCrawling)
        self.btn_clear.clicked.connect(self.clean)
        self.pushButton.clicked.connect(self.findPath_kakao)
        self.pushButton_2.clicked.connect(self.findPath_naver)
        

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
        #path = "C:\\Users\\Seoyoung\\Downloads\\"

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
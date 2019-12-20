import sys
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from crawl.shop import WebCrawling as wc
from crawl.kakao import KakaoCrawling as kc
from crawl.sinsang import SinsangCrwaling as sc
from crawl.naver import NaverCrawling as nc

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 750, 600)

        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        self.show()
class MyTabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout()
        dt = str(datetime.today()).split(' ')[0]
        # path = 'C:\\Users\\hkchoi\\Desktop\\쇼핑몰\\00_제품사진\\1_의류\\'
        path = "..\\" + dt + '\\'
        # path = "C:\\Users\\Seoyoung\\Downloads\\"
        # path = "D:\\이연주"

        f = open("./shops.txt", 'r',  encoding='UTF8')
        data = f.read().split('\n')
        f.close()

        shopes = {}

        for i in range(len(data)):
            if i%2 == 0:
                shopes[data[i]] = data[i+1]
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(500, 200)

        # Add tabs
        self.tabs.addTab(self.tab1, "거래처")
        self.tabs.addTab(self.tab2, "기타")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        
        for index, (key, value) in enumerate(shopes.items()):
            buttonName = 'button' + str(index)
            self.buttonName = QPushButton(key)
            self.tab1.layout.addWidget(self.buttonName)
            self.buttonName.clicked.connect((lambda state, path=path, url=value, shop=key : self.pageCrawling(state, path, url, shop)))
        self.tab1.setLayout(self.tab1.layout)

        #Create second tab
        self.tab2.layout = QVBoxLayout(self)
        
        #카카오
        self.groupbox1 = QGroupBox("카카오스토리")
        self.gbox = QGridLayout()
        
        self.groupbox1.setLayout(self.gbox)

        self.l1 = QLabel()
        self.l1.setText('url')
        self.kakaoUrl = QLineEdit()
        self.gbox.addWidget(self.l1, 0, 0)
        self.gbox.addWidget(self.kakaoUrl, 0, 1)

        self.l2 = QLabel()
        self.l2.setText('다운로드 경로')
        self.kakaoPath = QLineEdit()
        self.kakaoPath.setText(path)

        self.fileButton1 = QPushButton('File')
       
        self.gbox.addWidget(self.l2, 1, 0)
        self.gbox.addWidget(self.kakaoPath, 1, 1)
        self.gbox.addWidget(self.fileButton1, 1, 3)
       
        self.kakaoButton = QPushButton('Crawl')
        self.gbox.addWidget(self.kakaoButton, 2,3)

        # 신상마켓
        self.groupbox2 = QGroupBox("신상마켓")
        self.gbox = QGridLayout()
        
        self.groupbox2.setLayout(self.gbox)

        self.l3 = QLabel()
        self.l3.setText('url')
        self.sinsangUrl = QLineEdit()
        self.gbox.addWidget(self.l3, 0, 0)
        self.gbox.addWidget(self.sinsangUrl, 0, 1)

        self.l8 = QLabel()
        self.l8.setText('다운로드 경로')
        self.sinsangPath = QLineEdit()
        self.sinsangPath.setText(path)

        self.fileButton4 = QPushButton('File')
       
        self.gbox.addWidget(self.l8, 1, 0)
        self.gbox.addWidget(self.sinsangPath, 1, 1)
        self.gbox.addWidget(self.fileButton4, 1, 3)

        self.sinsangButton = QPushButton('Crawl')
        self.gbox.addWidget(self.sinsangButton, 2,3)

        # 네이버 블로그
        self.groupbox4 = QGroupBox("네이버 블로그")
        self.gbox = QGridLayout()
        
        self.groupbox4.setLayout(self.gbox)

        self.l4 = QLabel()
        self.l4.setText('url')
        self.blogUrl = QLineEdit()
        self.gbox.addWidget(self.l4, 0, 0)
        self.gbox.addWidget(self.blogUrl, 0, 1)

        self.l5 = QLabel()
        self.l5.setText('다운로드 경로')
        self.blogPath = QLineEdit()
        self.blogPath.setText(path)

        self.fileButton2 = QPushButton('File')
       
        self.gbox.addWidget(self.l5, 1, 0)
        self.gbox.addWidget(self.blogPath, 1, 1)
        self.gbox.addWidget(self.fileButton2, 1, 3)

        self.blogButton = QPushButton('Crawl')
        self.gbox.addWidget(self.blogButton, 2,3)

        #네이버 카페
        self.groupbox3 = QGroupBox("네이버 카페")
        self.gbox = QGridLayout()
        
        self.groupbox3.setLayout(self.gbox)

        self.l6 = QLabel()
        self.l6.setText('page')
        self.cafePage = QLineEdit()
        self.gbox.addWidget(self.l6, 0, 0)
        self.gbox.addWidget(self.cafePage, 0, 1)

        self.l7 = QLabel()
        self.l7.setText('다운로드 경로')
        self.cafePath = QLineEdit()
        self.cafePath.setText(path)

        self.fileButton3 = QPushButton('File')
       
        self.gbox.addWidget(self.l7, 1, 0)
        self.gbox.addWidget(self.cafePath, 1, 1)
        self.gbox.addWidget(self.fileButton3, 1, 3)

        self.cafeButton = QPushButton('Crawl')
        self.gbox.addWidget(self.cafeButton, 2,3)
        
        #tab2 layout set
        self.tab2.layout.addWidget(self.groupbox1)
        self.tab2.layout.addWidget(self.groupbox2)
        self.tab2.layout.addWidget(self.groupbox3)
        self.tab2.layout.addWidget(self.groupbox4)
        self.tab2.setLayout(self.tab2.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        # 버튼 click function 연결
        self.fileButton1.clicked.connect(( lambda state, number=1 : self.findPath(state, number)))
        self.fileButton2.clicked.connect(( lambda state, number=2 : self.findPath(state, number)))
        self.fileButton3.clicked.connect(( lambda state, number=3 : self.findPath(state, number)))
        self.fileButton4.clicked.connect(( lambda state, number=4 : self.findPath(state, number)))
        
        self.kakaoButton.clicked.connect(self.kakaoCrawling)
        self.sinsangButton.clicked.connect(self.sinsangCrawling)
        self.blogButton.clicked.connect(self.blogCrawling)
        self.cafeButton.clicked.connect(self.cafeCrawling)

    @pyqtSlot()
    def pageCrawling(self, state, path, url, shop):
        wc.web_crawling(str(url), path, shop)

    def findPath(self, state, number):
        fname = QFileDialog.getExistingDirectory(self)
        if number == 1:
            self.kakaoPath.setText(fname)
        elif number == 2:
            self.blogPath.setText(fname)
        elif number == 3:
            self.cafePath.setText(fname)
        else:
            self.sinsanPath.Text(fname)

    def kakaoCrawling(self):
        url = self.kakaoUrl.text()
        downloadpath_kakao = self.kakaoPath.text()
        kc.kakao_crawling(url, downloadpath_kakao)

    def sinsangCrawling(self):
        url = self.sinsangUrl.text()
        path = self.sinsangPath.text()
        sc.singsang_crawling(url, path)

    def blogCrawling(self):
        url = self.blogUrl.text()
        download_blog = self.blogPath.text()
        nc.naver_blog(url, download_blog)
    
    def cafeCrawling(self):
        download_path = self.cafePath.text()
        page = self.cafePage.text()
        nc.naver_cafe(page, download_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
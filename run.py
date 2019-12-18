import sys
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
        self.setGeometry(100, 100, 500, 600)

        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        self.show()
class MyTabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout()
        path = "C:\\Users\\metasoft\\Downloads"
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
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        
        for index, (key, value) in enumerate(shopes.items()):
            buttonName = 'button' + str(index)
            self.buttonName = QPushButton(key)
            self.tab1.layout.addWidget(self.buttonName)
            self.buttonName.clicked.connect((lambda state, url=value, shop=key : self.pageCrawling(state, url, shop)))
        self.tab1.setLayout(self.tab1.layout)

        #Create second tab
        self.tab2.layout = QVBoxLayout(self)
        
        #카카오
        self.groupbox1 = QGroupBox("카카오")
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

        self.fileButton = QPushButton('File')
       
        self.gbox.addWidget(self.l2, 1, 0)
        self.gbox.addWidget(self.kakaoPath, 1, 1)
        self.gbox.addWidget(self.fileButton, 1, 3)
       
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
    
        self.sinsangButton = QPushButton('Crawl')
        self.gbox.addWidget(self.sinsangButton, 0,2)

        # 네이버 블로그
        self.groupbox4 = QGroupBox("모니카")
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

        self.fileButton = QPushButton('File')
       
        self.gbox.addWidget(self.l5, 1, 0)
        self.gbox.addWidget(self.blogPath, 1, 1)
        self.gbox.addWidget(self.fileButton, 1, 3)

        self.blogButton = QPushButton('Crawl')
        self.gbox.addWidget(self.blogButton, 2,3)
        
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
        self.fileButton.clicked.connect(self.findPath_kakao)
        self.kakaoButton.clicked.connect(self.kakaoCrawling)
        self.sinsangButton.clicked.connect(self.sinsangCrawling)
        self.blogButton.clicked.connect(self.blogCrawling)

    @pyqtSlot()
    def pageCrawling(self, state, url, shop):
        # path = "C:\\Users\\Seoyoung\\Downloads\\"
        path = "C:\\Users\\metasoft\\Downloads"
        # path = "D:\\이연주"
        wc.web_crawling(str(url), path, shop)

    def findPath_kakao(self):
        fname = QFileDialog.getExistingDirectory(self)
        self.kakaoPath.setText(fname)

    def kakaoCrawling(self):
        url = self.kakaoUrl.text()
        downloadpath_kakao = self.kakaoPath.text()
        kc.kakao_crawling(url, downloadpath_kakao)

    def sinsangCrawling(self):
        # path = "C:\\Users\\Seoyoung\\Downloads\\"
        path = "C:\\Users\\metasoft\\Downloads"
        # path = "D:\\이연주"
        url = self.sinsangUrl.text()
        sc.singsang_crawling(url, path)

    def blogCrawling(self):
        url = self.blogUrl.text()
        download_blog = self.blogPath.text()
        nc.naver_blog(url, download_blog)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from crawl.test import WebCrawling as wc
from crawl.kakao import KakaoCrawling as kc

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 250)

        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        self.show()
class MyTabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout()
        path = "C:\\Users\\JSPARK\\Downloads\\"
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
        self.urlBox = QLineEdit()
        self.gbox.addWidget(self.l1, 0, 0)
        self.gbox.addWidget(self.urlBox, 0, 1)

        self.l2 = QLabel()
        self.l2.setText('다운로드 경로')
        self.pathBox = QLineEdit()
        self.pathBox.setText(path)

        self.fileButton = QPushButton('File')
       
        self.gbox.addWidget(self.l2, 1, 0)
        self.gbox.addWidget(self.pathBox, 1, 1)
        self.gbox.addWidget(self.fileButton, 1, 3)
        

        self.clearButton = QPushButton('Clear')
        self.kakaoButton = QPushButton('Crawl')

        self.gbox.addWidget(self.clearButton, 2,0)
        self.gbox.addWidget(self.kakaoButton, 2,3)
        
        #네이버 카페
        self.groupbox2 = QGroupBox("미엘")
        self.tab2.layout.addWidget(self.groupbox1)
        self.tab2.layout.addWidget(self.groupbox2)
        self.tab2.setLayout(self.tab2.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        self.fileButton.clicked.connect(self.findPath_kakao)
        self.kakaoButton.clicked.connect(self.kakaoCrawling)

    @pyqtSlot()
    def pageCrawling(self, state, url, shop):
        path = "C:\\Users\\JSPARK\\Downloads\\"
        wc.web_crawling(str(url), path, shop)

    def findPath_kakao(self):
        fname = QFileDialog.getExistingDirectory(self)
        self.pathBox.setText(fname)

    def kakaoCrawling(self) :
        url = self.urlBox.text()

        downloadpath_kakao = self.pathBox.text()
        kc.kakao_crawling(url, downloadpath_kakao)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
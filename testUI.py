import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from crawl.test import WebCrawling as wc

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 350, 250)

        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        self.show()


class MyTabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout()

        f = open("C:/Users/JSPARK/Desktop/myj/crawling/shops.txt", 'r',  encoding='UTF8')
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
        self.tabs.resize(350, 200)

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

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def pageCrawling(self, state, url, shop):
        path = "C:\\Users\\JSPARK\\Downloads\\"
        wc.web_crawling(str(url), path, shop)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
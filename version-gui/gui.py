import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from getdata import startpr

class MyApp (QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.label1 = QLabel('년도  입력 : ', self)
        self.labelex = QLabel('광역시/도 목록 : \n\n서울특별시, 부산광역시, 대구광역시, 인천광역시, \n울산광역시, 대전광역시, 광주광역시, 세종특별자치시, \n강원도, 경기도, 경상남도, 경상북도, \n충청남도, 충청북도, 전라남도, 전라북도, 제주특별자치도 ', self)
        self.label2 = QLabel('시/도 입력 : ', self)
        self.label4 = QLabel('저장위치 : ', self)


        self.qle1 = QLineEdit(self)
        self.qle2 = QLineEdit(self)
        self.qle3 = QLineEdit(self)

        self.btn1 = QPushButton('시작', self)
        self.btn1.clicked.connect(self.on_click)
        self.btn2 = QPushButton('종료', self)
        self.btn2.clicked.connect(QCoreApplication.instance().quit)



        #qle1.setText("입력")
        #txt1 = self.qle1.toPlainText()

        self.label3 = QLabel(self)


        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.labelex)
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.label1)
        hbox2.addWidget(self.qle1)
        hbox2.addStretch(1)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.label2)
        hbox3.addWidget(self.qle2)
        hbox3.addStretch(1)
        
        hbox6 = QHBoxLayout()
        hbox6.addStretch(1)
        hbox6.addWidget(self.label4)
        hbox6.addWidget(self.qle3)
        hbox6.addStretch(1)

        hbox4 = QHBoxLayout()
        hbox4.addStretch(1)
        hbox4.addWidget(self.btn1)
        hbox4.addWidget(self.btn2)
        hbox4.addStretch(1)

        hbox5 = QHBoxLayout()
        hbox5.addStretch(1)
        hbox5.addWidget(self.label3)
        hbox5.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addStretch(1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox6)
        vbox.addStretch(1)
        vbox.addLayout(hbox4)
        vbox.addStretch(1)
        vbox.addLayout(hbox5)
        vbox.addStretch(2)



        self.setWindowTitle('GETDATA(smartchoice)')
        self.setWindowIcon(QIcon('smartchoice_icon.png')) # 왼쪽 위의 아이콘
        self.setFixedSize(400, 400)
        self.setLayout(vbox)
        self.show()

    def on_click(self):
        result = startpr(self.qle1.text(),self.qle2.text(),self.qle3.text())
        if result:
            self.label3.setText("done")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

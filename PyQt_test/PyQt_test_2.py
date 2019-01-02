import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
import signal
from PyQt5.QtWidgets import *
from PyQt5 import uic


form_class = uic.loadUiType("main_window.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #객체의 이벤트에서 connect 함수를 호출하고 인자에 이벤트 처리기에서 수  행하는 함수를 기재한다.
        self.pushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        QMessageBox.about(self, "message", "clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()



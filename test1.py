import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic


class Form(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = uic.loadUi("UI/ui_text1.ui", self)            ## uic.loadUi 하는 방법은 여러가지가 있다. 글로벌 변수로 ui = uic.loadUi("UI/ui_text1.ui", self)[0]으로 라이브러리 밑에다 써도 된다. 이때 무조권 Form 클래스에 하나 더 추가 시킨다.
        self.ui.show()


        ## 두번째 라벨 설정
        label2 = QLabel("",self)

        ## 타이머 설정
        self.ui.timer = QTimer(self)
        self.ui.timer.start(1000)  ## 이벤트 발생 빈도 1초로 설정 Interval setting
        self.ui.timer.timeout.connect(self.timeout)

    @pyqtSlot()
    def slot_1st(self):
        pixmap = QPixmap('image/drugking.jpg')
        pixmap_resized = pixmap.scaled(480, 240, Qt.KeepAspectRatio)
        self.ui.label.setPixmap(pixmap_resized)
        self.ui.label2.setText("")

    @pyqtSlot()
    def slot_2nd(self):
        pixmap = QPixmap('image/aquaman.jpg')
        pixmap_resized = pixmap.scaled(480, 240, Qt.KeepAspectRatio)
        self.ui.label.setPixmap(pixmap_resized)

    @pyqtSlot()
    def slot_3rd(self):
        pixmap = QPixmap('image/swingkids.jpg')
        pixmap_resized = pixmap.scaled(480, 240, Qt.KeepAspectRatio)
        self.ui.label.setPixmap(pixmap_resized)

    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyForm = Form()
    MyForm.show()
    app.exec_()
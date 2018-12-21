import sys, os
import Dataset_Frame

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic

## ui에 관한 설정을 클래서 밖에서 할 수 있다.
## ui = uic.loadUiType("mywindow.ui")[0]          ## 뒤에 [0]를 제외하면 에러가 터진다... 왜 터지는지는 알 수 없지만 나중에 알아야겠다.

class Form(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = uic.loadUi("UI/ui_text11.ui", self)
        self.setWindowTitle("MOVIE REGERVATION")
        self.setWindowIcon(QIcon("image/icon.png"))

        self.title_ui()

        ## Time settings
        self.timer = QTimer(self)
        self.timer.start(1000)  ## 이벤트 발생 빈도 1초로 설정 Interval setting
        self.timer.timeout.connect(self.timeout)

        self.ui.show()

    @pyqtSlot()    ## 데커레이터 : 시그널과 슬롯을 연결할 때 데커레이터를 적어주면 더 좋다.
    def slot_1st(self):
        pixmap = QPixmap('image/drugking.jpg')
        pixmap_resized = pixmap.scaled(480, 240, Qt.KeepAspectRatio)    ## 원래의 이미지 크기가 상당히 컸기 때문에 scaled를 통해서 줄였다.
        self.label.setPixmap(pixmap_resized)

        ## pandas를 이용해서 dataset을 만들어 기입하자
        self.label_2.setText("마약왕")                  ## QT designeer에서의 objectname을 소스코드 안에서 제대로 알고 사용해야 원하는 방향으로 작동할 수 있다.

    @pyqtSlot()
    def slot_2nd(self):
        pixmap = QPixmap('image/aquaman.jpg')
        pixmap_resized = pixmap.scaled(480, 240, Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap_resized)

        ## pandas를 이용해서 dataset을 만들어 기입하자
        self.label_2.setText("아쿠아맨")

    @pyqtSlot()
    def slot_3rd(self):
        pixmap = QPixmap('image/swingkids.jpg')
        pixmap_resized = pixmap.scaled(480, 240, Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap_resized)

        ## pandas를 이용해서 dataset을 만들어 기입하자
        self.label_2.setText("스윙키즈")

    # @pyqtSlot(int, int)  ## 데커레이터에도 들어올 데이터 타입을 적어주어야한다.
    # def signal2_emitted(self, arg1, arg2):
    #     print("signal2 emitted", arg1, arg2)

    ## 윈도우 하단에 시간을 보여주는 메서드, 나중에 따로 메서드 만들지말고 하나에 메서드에 추가만 해도 될 것 같다.
    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("현재시간 : hh:mm:ss")
        self.statusBar().showMessage(str_time)

    def title_ui(self):
        label_3 = QLabel(self)
        pixmap3 = QPixmap("image/naver_movie.png")
        fixed_pixmap = pixmap3.scaled(200, 200)
        label_3.setPixmap(fixed_pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyForm = Form()
    MyForm.show()
    app.exec_()
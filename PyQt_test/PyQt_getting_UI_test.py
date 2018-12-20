import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("mywindow.ui")[0]          ## 뒤에 [0]를 제외하면 에러가 터진다... 왜 터지는지는 알 수 없지만 나중에 알아야겠다.

class MySignal(QObject):
    signal1 = pyqtSignal()              ## 인스턴스 변수로 만드는 것이 아니라 클래스 변수로 만들어야한다.
    signal2 = pyqtSignal(int,int)       ## 전달하고자 하는 데이터 타입을 기술

    def run(self):
        self.signal1.emit()             ## emit()을 이용하여 호출이 가능하다.
        self.signal2.emit(1,2)

class MyWindow(QMainWindow, form_class):        ## 클래스를 정의 할때 QMainWindow와 form_class로 다중 상속을 받는다.
    def __init__(self):
        super().__init__()

        ## Mysignal 객체를 생성
        mysignal = MySignal()    ## 인스턴스 변수로 만드는 것이 아니라 클래스 변수로 만들어야한다.
        mysignal.signal1.connect(self.signal1_emitted)
        mysignal.signal2.connect(self.signal2_emitted)
        mysignal.run()

        ## 위젯 생성코드
        self.setupUi(self)    ## setupUI()메서드는 form_class에서 정의된 메서드다.
        self.pushButton.clicked.connect(self.btn_clicked)

        self.timer = QTimer(self)
        self.timer.start(1000)  ## 이벤트 발생 빈도 1초로 설정 Interval setting
        self.timer.timeout.connect(self.timeout)

    @pyqtSlot()     ## 데커레이터 : 시그널과 슬롯을 연결할 때 데커레이터를 적어주면 더 좋다.
    def signal1_emitted(selfs):
        print("signal1 emitted")

    @pyqtSlot(int,int)  ## 데커레이터에도 들어올 데이터 타입을 적어주어야한다.
    def signal2_emitted(self, arg1, arg2):
        print("signal2 emitted", arg1, arg2)

    ## 윈도우 하단에 시간을 보여주는 메서드, 나중에 따로 메서드 만들지말고 하나에 메서드에 추가만 해도 될 것 같다.
    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)

    def btn_clicked(self):
        print("버튼 클릭")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
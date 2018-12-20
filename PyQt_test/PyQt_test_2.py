import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ###MyWindow 클래스의 생성자 코드를 살펴보면 super().__init__() 이라는 코드가 있습니다. 여기서 super()는 파이썬의 내장 함수 (파이썬이 설치되면 기본적으로 제공되는 함수)입니다. MyWindow 클래스는 QMainWindow 클래스를 상속 받는데 자식 클래스가 부모 클래스에 정의된 함수를 호출하려면 'self.부모클래스_메서드()' 처럼 적으면 됩니다. 그런데 __init__() 이라는 생성자는 자식 클래스에도 있고 부모 클래스에도 있습니다. 이 경우 'self.__init__()' 이라고 적으면 자식 클래스 (MyWindow)의 생성자를 먼저 호출하게 됩니다. 따라서 부모 클래스에 정의된 생성자를 명시적으로 호출하려고 상속 구조에서 부모 클래스를 찾아서 리턴해주는 super()를 적은 후 __init__() 메서드를 호출하는 겁니다.

        ## 위젯 생성코드
        self.setGeometry(200,200,400,400)
        self.setWindowTitle("Movie Ticket Record")      ## Window "name" settings
        self.setWindowIcon(QIcon("image/icon.png"))     ## 지금 아이콘 적용이 안되고 있음... 디테일한 부분이니까 나중에..해도됨 12/20

        btn = QPushButton("Button1", self)
        btn.move(10,10)
        btn.clicked.connect(self.btn_clicked)

        btn2 = QPushButton("Button2", self)
        btn2.move(10, 40)

    ## 이벤트 처리 코드
    def btn_clicked(self):
        print("Button Clicked")

## QApplication 객체 생성 및 이벤트 루프 생성 코드
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
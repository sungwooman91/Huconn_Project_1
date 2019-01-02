import sys
import Dataset_Frame as df
import numpy as np
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic

## 전역변수
ticket_title = ["drugking","aquaman","swingkids"]
drugking_couunt = 0
aquaman_count = 0
swingkids_count = 0

## matplotlib 한글화
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
## ui에 관한 설정을 클래서 밖에서 할 수 있다.
form_class = uic.loadUiType("UI/ui_text11.ui")[0]
## 뒤에 [0]를 제외하면 에러가 터진다... 왜 터지는지는 알 수 없지만 나중에 알아야겠다.

class Mywindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.ui = uic.loadUi("UI/ui_text11.ui", self)
        self.setWindowTitle("MOVIE REGERVATION")
        self.resize(700,1000)
        self.setWindowIcon(QIcon("image/icon.png"))

        ##Title image
        self.title_image = QPixmap("image/naver_movie.png")
        self.title_resized = self.title_image.scaled(320, 480, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.label_3.setPixmap(self.title_resized)
        ## Time settings
        self.timer = QTimer(self)
        self.timer.start(1000)  ## 이벤트 발생 빈도 1초로 설정 Interval setting
        self.timer.timeout.connect(self.timeout)

        ## push action
        self.pushButton.clicked.connect(self.ticket_clicked)
        self.pushButton_2.clicked.connect(self.ticket_clicked)
        self.pushButton_3.clicked.connect(self.ticket_clicked)
        self.pushButton_4.clicked.connect(self.showgraph)
        self.show()

    ## 데커레이터 : 시그널과 슬롯을 연결할 때 데커레이터를 적어주면 더 좋다.
    @pyqtSlot()
    def slot_1st(self):
        pixmap = QPixmap('image/drugking.jpg')
        ## 원래의 이미지 크기가 상당히 컸기 때문에 scaled를 통해서 줄였다.
        pixmap_resized = pixmap.scaled(320, 480, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.label.setPixmap(pixmap_resized)
        # self.pushButton.clicked.connect(self.showMessageBox)  ## Message 창이 중복으로 뜬다.

        ## pandas를 이용해서 dataset을 만들어 기입하자
        ## QT designeer에서의 objectname을 소스코드 안에서 제대로 알고 사용해야 원하는 방향으로 작동할 수 있다.
        self.label_2.setText(df.movie_text(df.movie_url)[0].replace('\xa0','\n'))
        ## 예매한 관객 수
        self.drugking_count += 1

    @pyqtSlot()
    def slot_2nd(self):
        pixmap = QPixmap('image/aquaman.jpg')
        pixmap_resized = pixmap.scaled(320, 480, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.label.setPixmap(pixmap_resized)
        # self.pushButton_2.clicked.connect(self.showMessageBox) ## Message 창이 중복으로 뜬다.

        ## pandas
        self.label_2.setText(df.movie_text(df.movie_url)[1].replace('\xa0', '\n'))
        ## 예매한 관객 수
        self.aquaman_count += 1

    @pyqtSlot()
    def slot_3rd(self):
        pixmap = QPixmap('image/swingkids.jpg')
        pixmap_resized = pixmap.scaled(320, 480, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.label.setPixmap(pixmap_resized)
        # self.pushButton_3.clicked.connect(self.showMessageBox)  ## Message 창이 중복으로 뜬다.

        ## pandas
        self.label_2.setText(df.movie_text(df.movie_url)[2].replace('\xa0', '\n'))
        ## 예매한 관객 수
        self.swingkids_count += 1

    # @pyqtSlot(int, int)  ## 데커레이터에도 들어올 데이터 타입을 적어주어야한다.
    # def signal2_emitted(self, arg1, arg2):
    #     print("signal2 emitted", arg1, arg2)

    ## 윈도우 하단에 시간을 보여주는 메서드, 나중에 따로 메서드 만들지말고 하나에 메서드에 추가만 해도 될 것 같다.
    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("현재시간 : hh:mm:ss")
        self.statusBar().showMessage(str_time)

    ## 예매 하기 메세지 박스
    # def showMessageBox(self):
    #     msgbox = QMessageBox(self)
    #     msgbox.question(self, 'Message', '이 영화를 예매하시겠습니까?', QMessageBox.Yes | QMessageBox.No)

    ## 예매 현황 보기
    ## 디비에 저장되어 있는 티켓 수를 뽑아서 저장시켜야함
    def showgraph(self):
        y1_value = (21.6, 23.6, 45.8, 77.0, 102.2, 133.3, 327.9, 348.0, 137.6, 49.3, 53.0, 24.9)
        x_name = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
        n_groups = len(x_name)
        index = np.arange(n_groups)

        plt.bar(index, y1_value, tick_label=x_name, align='center', color='blue')

        plt.xlabel('월')
        plt.ylabel('평균강수량 (mm)')
        plt.title('날씨 그래프')
        plt.xlim(-1, n_groups)
        plt.ylim(0, 400)
        plt.show()

    # 조회버튼 클릭 함수
    def ticket_clicked(self):
        QMessageBox.information(self, "message", "예매 1매 성공!!")

    # 클릭시 데이터 삽입 알림창 출력후 삽입 함수 실행
    def btn_add_clicked(self):
        return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyForm = Mywindow()
    MyForm.show()
    app.exec_()
import sys, pymysql
import Dataset_Frame as df
import numpy as np
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic

## pymysql
con = pymysql.connect(user='root',
                      password='123456',
                      host='localhost',
                      port=3307,
                      database='ticket'
                      )
## 전역변수
ticket_title = ["drugking","aquaman","swingkids"]

## matplotlib 한글화
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

## ui에 관한 설정을 클래서 밖에서 할 수 있다.
form_class = uic.loadUiType("UI/ui_text11.ui")[0]

## 뒤에 [0]를 제외하면 에러가 터진다... 왜 터지는지는 알 수 없지만 나중에 알아야겠다.
def insertTable(movie1, movie2, movie3):
    cur = con.cursor()
    #sql = "DELETE FROM melon_chart"
    #cur.execute(sql)
    sql = "INSERT INTO movie (drugking, aquaman, swingkids) VALUES (%d, %d, %d)"
    cur.execute(sql,(movie1,movie2,movie3))
    con.commit()

class Mywindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.ui = uic.loadUi("UI/ui_text11.ui", self)
        self.setWindowTitle("MOVIE REGERVATION")
        self.resize(700,1000)
        self.setWindowIcon(QIcon("image/icon.png"))
        ## 예매 관객 변수
        self.clickcount = 0
        self.clickcount1 = 0
        self.clickcount2 = 0
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
        self.pushButton.clicked.connect(self.on_click)
        self.pushButton_2.clicked.connect(self.ticket_clicked)
        self.pushButton_2.clicked.connect(self.on_click1)
        self.pushButton_3.clicked.connect(self.ticket_clicked)
        self.pushButton_3.clicked.connect(self.on_click2)
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

    @pyqtSlot()
    def slot_2nd(self):
        pixmap = QPixmap('image/aquaman.jpg')
        pixmap_resized = pixmap.scaled(320, 480, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.label.setPixmap(pixmap_resized)
        # self.pushButton_2.clicked.connect(self.showMessageBox) ## Message 창이 중복으로 뜬다.

        ## pandas
        self.label_2.setText(df.movie_text(df.movie_url)[1].replace('\xa0', '\n'))

    @pyqtSlot()
    def slot_3rd(self):
        pixmap = QPixmap('image/swingkids.jpg')
        pixmap_resized = pixmap.scaled(320, 480, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.label.setPixmap(pixmap_resized)
        # self.pushButton_3.clicked.connect(self.showMessageBox)  ## Message 창이 중복으로 뜬다.

        ## pandas
        self.label_2.setText(df.movie_text(df.movie_url)[2].replace('\xa0', '\n'))

    # @pyqtSlot(int, int)  ## 데커레이터에도 들어올 데이터 타입을 적어주어야한다.
    # def signal2_emitted(self, arg1, arg2):
    #     print("signal2 emitted", arg1, arg2)

    ## 윈도우 하단에 시간을 보여주는 메서드, 나중에 따로 메서드 만들지말고 하나에 메서드에 추가만 해도 될 것 같다.
    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("현재시간 : hh:mm:ss")
        self.statusBar().showMessage(str_time)

    ## 예매 관객 카운트
    def on_click(self): # 마약왕
        self.clickcount += 1
        print(self.clickcount)

    def on_click1(self): # 아쿠아맨
        self.clickcount1 += 1
        print(self.clickcount1)

    def on_click2(self): # 스윙키즈
        self.clickcount2 += 1
        print(self.clickcount2)

    ## 예매 현황 보기
    def showgraph(self):
        # insertTable(moive1 =self.clickcount, movie2=self.clickcount1, movie3=self.clickcount2)
        y1_value = (self.clickcount, self.clickcount1, self.clickcount2)
        x_name = (ticket_title[0], ticket_title[1], ticket_title[2])
        n_groups = len(x_name)
        index = np.arange(n_groups)

        plt.bar(index, y1_value, tick_label=x_name, align='center', color='blue')
        plt.xlabel('영화명')
        plt.ylabel("예매 관객 수")
        plt.title('영화 예매 현황')
        plt.xlim(-1, n_groups)
        plt.ylim(0, 50)
        plt.show()

    # 조회버튼 클릭 함수
    def ticket_clicked(self):
        QMessageBox.information(self, "message", "영화 예매 1매 성공!!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyForm = Mywindow()
    MyForm.show()
    app.exec_()
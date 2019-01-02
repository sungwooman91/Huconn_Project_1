import pymysql
import sys
import requests
from matplotlib import pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from bs4 import BeautifulSoup

#matplotlib 한글 깨짐현상 방지
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
# 같은폴더상의 ui 파일을 불러온다.
form_class = uic.loadUiType("melon2.ui")[0]
#전역변수? 설정
RANK_CHART = 5
RANK = 100 # 1위부터 최대 100위까지 설정 가능
# melon사이트의 주소를 가져옴
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
req = requests.get('https://www.melon.com/chart/index.htm', headers=header)
#받아온 소스 전체를 텍스트화
html = req.text
#BeautifulSoup 을 통해 html 소스들을 파싱한다.
parse = BeautifulSoup(html, 'html.parser')

# 각각의 div class 이름과 동일한 부분을 찾고 저장한다.
# 동일한 부분이 있는 전체 html 소스를 가져온다.
titles = parse.find_all("div", {"class": "ellipsis rank01"})
singers = parse.find_all("div", {"class": "ellipsis rank02"})
albums = parse.find_all("div", {"class": "ellipsis rank03"})

rank =[]
title = []
singer = []
album = []

#pymysql 을 통해 MYSQL과 파이썬을 연동시킨다.
conn = pymysql.connect(
    host='localhost',
    user='hu_hcm',
    password='gbzjs',
    db='huconn_melon',
    charset='utf8'
)

# 소스중 특정 조건 안에 있는 텍스트만 골라서 각 리스트에 저장
for t in titles:
    title.append(t.find('a').text)
for s in singers:
    singer.append(s.find('span', {"class": "checkEllipsis"}).text)
for a in albums:
    album.append(a.find('a').text)

#저장이 잘 되었는지 출력으로 확인
for i in range(RANK):
    print('%3d위 : %s - %s - %s' %(i+1, title[i], singer[i], album[i]))


# DB에 저장되어있는 멜론차트 SELECT문 실행
def selectTableList(self):
    cur = conn.cursor()
    sql = "SELECT singer,title, album FROM melon_chart"
    cur.execute(sql)
    rows = cur.fetchall()
    return rows

# 멜론차트를 크롤링하여 데이터 삽입
def insertTable(_title, _singer, _album):
    cur = conn.cursor()
    #sql = "DELETE FROM melon_chart"
    #cur.execute(sql)
    sql = "INSERT INTO melon_chart (title, singer, album) VALUES (%d, %d, %d)"
    cur.execute(sql,(_title,_singer,_album))
    conn.commit()

#QT디자인 구현부분
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('멜론 차트 TOP 100 크롤링')
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.pushButton.clicked.connect(self.refesh_clicked)
        self.pushButton.clicked.connect(self.btn_add_clicked)
        self.pushButton_2.clicked.connect(self.static_clicked)
        # 테이블 클릭시 수정변경이 불가하도록 해줌
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)


    # 조회버튼 클릭 함수
    def refesh_clicked(self):
        try:
            QMessageBox.information(self, "message", "조회")
            cur = conn.cursor()
            sql = "DELETE FROM melon_chart"
            cur.execute(sql)
            self.refresh()
        except Exception as e:
            QMessageBox.warning(self, "[Error Message]", "에러타입 : " + str(type(e)) + "\n에러 내용 : " + str(e))
            print(e)
            print(type(e))


    # 클릭시 데이터 삽입 알림창 출력후 삽입 함수 실행
    def btn_add_clicked(self):
        try:
            QMessageBox.information(self, "message", "데이터 삽입중")
            for i in range (RANK):
                insertTable(_title=title[i],_singer=singer[i],_album=album[i])
            #삽입 후 자동 조회(새로고침)
            self.refresh()
        except Exception as e:
            QMessageBox.warning(self, "[Error Message]", "에러타입 : " + str(type(e)) + "\n에러내용 : " + str(e))
            print(e)
            print(type(e))

    #클릭시 통계 알림창 출력 후 Graph 출력 함수 실행
    def static_clicked(self):
        try:
            QMessageBox.information(self, "message", "통계")
            self.graph()
        except Exception as e:
            QMessageBox.warning(self, "[Error Message]", "에러타입 : " + str(type(e)) + "\n에러 내용 : " + str(e))
            print(e)
            print(type(e))

    #데이터 표로 출력(조회)
    def refresh(self):
        # selectTableList 함수로 부터 select된 데이터들을 n * m 형태의 리스트를 가져옴
        rows = selectTableList(self)
        self.tableWidget.setRowCount(len(rows))
        count = 0
        for row in rows:
            self.tableWidget.setItem(count, 0, QTableWidgetItem(str(count+1)))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(row[0]))
            self.tableWidget.setItem(count, 2, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(count, 3, QTableWidgetItem(row[2]))
            count += 1

    # 그래프 출력 부분
    # 기존 x 축에는 TOP 100 안에 있는 모든 가수들, Y축에는 그 가수의 TOP 100 안에서의 곡 보유수 이다.
    # 새로운 x 축에는 TOP 5 안에 있는 가수들, Y축에는 그 가수의 TOP 100 안에서의 곡 보유수이다
    def graph(self):
        x = []
        y = []
        new_x= []
        new_y= []
        # 중복되지 않게 TOP100의 가수를 X축 리스트에 추가시키고
        # Y축에 해당 가수의 TOP 100의 보유곡을 순서에 맞게 추가시킨다.
        for i in singer:
            #중복되지 않게 하기위한 코드
            if not i in x:
                x.append(i)
                y.append(singer.count(i))
        # 설정한 RANK_CHART의 숫자의 순위만큼 추려낸다.
        # 가장 높은 보유곡의 가수부터 그래프로 나타낸다.
        for i in range(RANK_CHART):
            new_x.append(x[y.index(max(y))])
            x.pop(y.index(max(y)))
            new_y.append(max(y))
            y.pop(y.index(max(y)))
        print(new_x)
        print(new_y)
        plt.xlabel('가수')
        plt.ylabel('곡 수')
        plt.title('TOP ' + str(RANK_CHART) + ' 가수별 곡 수')
        plt.bar(new_x, new_y, width=0.5, color="green")
        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
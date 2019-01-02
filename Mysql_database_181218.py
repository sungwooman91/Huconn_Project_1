import pymysql.cursors

con = pymysql.connect(user='root', password='123456',host='localhost',    ### pymysql을 하면 버그가 하나 뜨는데 아직까지는
                        port=3307, database='movie_title')                ### 왜 그런지는 모르겠다능... 이유를 찾았다!!! db이름이 잘못되어 있었음!! 12/18

cursor = con.cursor()

# Create SQL
sql = '''CREATE TABLE seller(
            drugking int(10) unsigned NOT NULL AUTO_INCREMENT,
            aquaman int(10) unsigned NOT NULL,
            swingkids int(10) unsigned OT NULL
            );
            '''

## Execute 실행하기
cursor.execute(sql)

## Complete in DB (DB에 Complete 하기)
# db.commit()
con.commit()

## Close DB (DB연결 닫기)
# db.close()
con.close()
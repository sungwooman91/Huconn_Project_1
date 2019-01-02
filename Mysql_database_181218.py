import pymysql.cursors

con = pymysql.connect(user='root',
                      password='123456',
                      host='localhost',
                      port=3307,
                      database='ticket'
                      )

cursor = con.cursor()

# Create SQL
sql = '''CREATE TABLE movie(
            drugking int(10) unsigned NOT NULL,
            aquaman int(10) unsigned NOT NULL,
            swingkids int(10) unsigned NOT NULL
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
import pymysql.cursors
import  mysql.connector

# database connection
# db = mysql.connector.connect(user='root', password='123456',host='localhost',
#                               port='3307', database='project')

con = pymysql.connect(user='root', password='123456',host='localhost',    ### pymysql을 하면 버그가 하나 뜨는데 아직까지는
                        port=3307, database='movie_title')                ### 왜 그런지는 모르겠다능... 이유를 찾았다!!! db이름이 잘못되어 있었음!! 12/18

# get cursor
# cursor = db.cursor()
cursor = con.cursor()

# Create SQL
sql = '''CREATE TABLE Title(
            id INT UNSIGNED NOT NULL AUTO_INCREMENT,
            name VARCHAR(20) NOT NULL,
            model_num VARCHAR(10) NOT NULL,
            model_type VARCHAR(10) NOT NULL,
            PRIMARY KEY(id)
            );
            '''

## Execute
cursor.execute(sql)

## Complete in DB
# db.commit()
con.commit()

## Close DE
# db.close()
con.close()
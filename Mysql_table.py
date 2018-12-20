import mysql.connector

## connect to mysql db using username and password
con = mysql.connector.connect(user='root', password='123456',host='localhost',
                              port='3307', database='project')

## create cursor
cursor = con.cursor()

## create table
cursor.execute("CREATE table stud(id int, name varchar(20))")

print("table created successfully")

cursor.close()
con.close()
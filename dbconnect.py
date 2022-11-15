# dbconnect.py
# mariadb와 연동

import pymysql

hostname='localhost'
portNum=3306
userName='root'
password='rootroot'
dbName='join'

db = pymysql.connect(host = hostname,
                        port = portNum,
                        user = userName,
                        passwd = password,
                        db = dbName,
                        charset = 'utf8')
def insert_func(query):
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()

        
def read_func(query):
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()

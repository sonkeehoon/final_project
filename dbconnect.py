# dbconnect.py

import pymysql

hostname = 'localhost'
portNum = 3306
userName = 'root'
password = ''
dbName = 'join'

db_write = pymysql.connect(host = hostname,
                        port = portNum,
                        user = userName,
                        passwd = password,
                        db = dbName,
                        charset = 'utf8')

db_read = pymysql.connect(host = hostname,
                        port = portNum,
                        user = userName,
                        passwd = password,
                        db = dbName,
                        charset = 'utf8')
def insert_func(query):
    cursor = db_write.cursor()
    cursor.execute(query)
    db_write.commit()

        
def read_func(query):
    cursor = db_read.cursor()
    cursor.execute(query)
    return cursor.fetchall()

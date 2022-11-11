# mariadb와 연동
import pymysql

def insert(query):
    
    db = pymysql.connect(host='kh-database.cmvilgp6lmfg.ap-northeast-2.rds.amazonaws.com',
                        port=3306,
                        user='admin',
                        passwd='adminadmin',
                        db='finalProject',
                        charset='utf8')
    try:
        with db.cursor() as cursor:
            cursor.execute(query)
            db.commit()
    finally:
        db.close()

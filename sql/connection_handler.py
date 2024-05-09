import pymysql

con = pymysql.connect(host='localhost',
                      user='root', password='sandroo1231',
                      database='students')
cur = con.cursor()
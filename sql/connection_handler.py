import pymysql


def sql_connection():
    con = pymysql.connect(host='localhost',
                          user='root',
                          password='sandroo1231',
                          database='students')

    return con


def sql_names():
    con = pymysql.connect(host='localhost',
                          user='root',
                          password='sandroo1231',
                          database='students')

    cursor = con.cursor()


    cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'students'")
    results = cursor.fetchall()
    column_names = [result[0] for result in results]

    cursor.close()
    con.close()
    return column_names

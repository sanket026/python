import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='hellodb')
    print("Database connected!")
except Exception as e:
    print(e)

cur=dbcon.cursor()
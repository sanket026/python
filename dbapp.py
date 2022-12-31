
from logging import exception
from turtle import update
import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='hellodb')
    print("Database connected!")
except Exception as e:
    print(e)


    #cur=dbcon.cursor()

# Create Table
"""cur=dbcon.cursor()

create_table="create table stname (id int primary key,name text, sub text,city text)"

try:
    cur.execute(create_table)
    
    print('table created')
except exception as e:
    print(e)    
"""


"""
#insert data
cur=dbcon.cursor()
insert_data="insert into stname values(1,'sanket','python','rajkot'),(2,'sanket','python','rajkot'),(3,'sanket','python','rajkot')"


try:
    cur.execute(insert_data)
    dbcon.commit()
    print('table created')
except Exception as e:
    print(e)
"""
#update data

cur=dbcon.cursor()
update_data="update stname set name='jay' where id=2"

try:
    cur.execute(update_data)
    dbcon.commit()
    print("record updated")
except Exception as e:
    print(e)   

#tables required:
import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='mysqlpass@123')
cur=conn.cursor()
cur.execute('create database BANK')

import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='mysqlpass@123',database="bank")
cur=conn.cursor()
cur.execute('create table data(User_Name varchar(200),Password int)')
cur.execute('create table transactions(ACCOUNT_NUMBER int, DATE_TIME date, WITHDRAWN_AMOUNT int, CREDIT_AMOUNT int)')
cur.execute('create table user_details(ACCOUNT_NUMBER int,ACCOUNT_TYPE varchar(200),PHONE_NUMBER bigint,ADDRESS varchar(200),BALANCE_AMOUNT int )')


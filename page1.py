#bnk mngmt sys.
import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='mysqlpass@123',database='bank')
cur = conn.cursor()
print('======================================================================================WELCOME TO DEHRADUN PUBLIC BANK==============================================================================================')
import datetime as dt
print(dt.datetime.now())
print('1.REGISTER')
print()
print('2.LOGIN')
print()

n=int(input('enter your choice='))
print()

if n== 1:
     name=input('Enter a Username=')
     print()
     passwd=int(input('Enter a 4 DIGIT Password='))
     print()
     V_SQLInsert="INSERT INTO DATA (User_name,Password) values (' " + name + " '," +  str (passwd) + ") "
     cur.execute(V_SQLInsert)
     conn.commit()
     print()
     print('USER created succesfully')
     import event

if  n==2 :
     name=input('Enter your Username=')
     print()
     passwd=int(input('Enter your 4 DIGIT Password='))
     V_Sql_Sel="select * from Data where Password='"+str (passwd)+"' and User_Name=  ' " +name+ " ' "
     cur.execute(V_Sql_Sel)
     if cur.fetchone() is  None:
          print()
          print('Invalid username or password')
     else:
          print()
          import event
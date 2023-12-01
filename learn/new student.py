import mysql.connector

def login():
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Gkarunakar@1432',
        database='record_maintaince'
    )
    return mydb

s_name=input('enter s_name:- ')
age=int(input('enter age:- '))
d_id=int(input('enter d_id:- '))
duretion=input('enter duretion:- ')
fee=int(input('enter fee:- '))
paid=int(input('enter paid amount:- '))
if paid==fee:
    status='yes'
elif paid>fee:
    status='extra'
else:
    status='no'
colleg = login()
mycursor = colleg.cursor()
sql='INSERT INTO fee (fee, paid, status) VALUES (%s,%s,%s)'
val=(fee, paid, status)
mycursor.execute(sql,val)
colleg.commit()

colleg = login()
mycursor = colleg.cursor()
mycursor.execute('select s_id from fee')
for i in mycursor:
    a=int(i[0])

colleg = login()
mycursor = colleg.cursor()
sql='INSERT INTO `record_maintaince`.`student` (`s_id`, `s_name`, `age`, `d_id`, `duretion`) VALUES (%s,%s,%s,%s,%s)'
val=(a,s_name, age, d_id, duretion)
mycursor.execute(sql,val)
colleg.commit()

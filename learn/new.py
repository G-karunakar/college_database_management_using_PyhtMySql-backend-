import mysql.connector

def login():
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Gkarunakar@1432',
        database='record_maintaince'
    )
    return mydb
f_name=input('enter f_name:- ')
age=input('enter age:-')
d_id=int(input('enter d_id:- '))
designetion=input('enter designetion:- ')

colleg = login()
mycursor = colleg.cursor()
sql='INSERT INTO faculty (`f_name`, `age`, `d_id`, `designetion`) VALUES (%s,%s,%s,%s)'
val=(f_name, age, d_id, designetion)
mycursor.execute(sql,val)
colleg.commit()
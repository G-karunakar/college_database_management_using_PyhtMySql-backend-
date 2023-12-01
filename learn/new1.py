import mysql.connector

def login():
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Gkarunakar@1432',
        database='record_maintaince'
    )
    return mydb
d_name=input('enter d_name:- ')
hod=input('enter hod:- ')

colleg = login()
mycursor = colleg.cursor()
sql="INSERT INTO deportment (`d_name`, `hod`) VALUES (%s,%s)"
val=(d_name, hod)
mycursor.execute(sql,val)
colleg.commit()
#################################################################
colleg = login()
mycursor = colleg.cursor()
mycursor.execute('select d_id from deportment')
for i in mycursor:
    a=int(i[0])
f_name=hod
age=int(input('enter age of hod:- '))
d_id=a
designetion=hod
colleg = login()
mycursor = colleg.cursor()
sql='INSERT INTO faculty (`f_name`, `age`, `d_id`, `designetion`) VALUES (%s,%s,%s,%s)'
val=(f_name, age, d_id, designetion)
mycursor.execute(sql,val)
colleg.commit()
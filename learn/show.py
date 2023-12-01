import mysql.connector

def login():
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Gkarunakar@1432',
        database='record_maintaince'
    )
    return mydb
########################################################################################################
########################################################################################################
'''details=input(' 1). deportment id\n 2). student_id\n 3). student name \n 4). deportment name\n 5). hod\n 6). student fee\n 7). student paid\n 8). student fee status\n 9).student duretion\n\n enter your value sapareted by camas:- ')
details=list(details.split(','))
detailing={'1':'deportment.d_id','2':'student.s_id','3':'student.s_name','4':'deportment.d_name','5':'deportment.hod','6':'fee.fee','7':'fee.paid','8':'fee.status','9':'student.duretion'}
reference=''
for i in details:
    if i==details[0]:
        reference=detailing[i]
    else:
        reference=reference+','+detailing[i]
print(reference)


colleg = login()
mycursor = colleg.cursor()
mycursor.execute(f'select {reference} from fee,student,deportment where status="yes" and fee.s_id=student.s_id and student.d_id=deportment.d_id')
print(reference)
for i in mycursor:
    print(i)
'''
colleg = login()
mycursor = colleg.cursor()
a=int(input(" 1:'student'\n 2:'fee'\n 3:'deportment'\n 4:'faculty'\n\n enter your responce:- "))
tables={1:'student',2:'fee',3:'deportment',4:'faculty'}
head={1:"`s_id`, `s_name`, `age`, `d_id`, `duretion`",2:"`s_id`, `fee`, `paid`, `status`",3:"`d_id`, `d_name`, `hod`",4:"`f_id`, `f_name`, `age`, `d_id`, `designetion`"}
print(head[a])
mycursor.execute(f'select * from {tables[a]}')
for i in mycursor:
    print(i)
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
def tables():
    a=input('1). open the required table\n2). show all tables')
    if a==1:
        colleg = login()
        mycursor = colleg.cursor()
        a = int(input(" 1:'student'\n 2:'fee'\n 3:'deportment'\n 4:'faculty'\n\n enter your responce:- "))
        tables = {1: 'student', 2: 'fee', 3: 'deportment', 4: 'faculty'}
        head = {1: "`s_id`, `s_name`, `age`, `d_id`, `duretion`", 2: "`s_id`, `fee`, `paid`, `status`",
                3: "`d_id`, `d_name`, `hod`", 4: "`f_id`, `f_name`, `age`, `d_id`, `designetion`"}
        print(head[a])
        mycursor.execute(f'select * from {tables[a]}')
        for i in mycursor:
            print(i)
    else:
        colleg = login()
        mycursor = colleg.cursor()
        mycursor.execute('show tables')
        for i in mycursor:
            print(i)
########################################################################################################
########################################################################################################
def update_fee():
    s_id = int(input("enter student id:- "))
    colleg = login()
    mycursor = colleg.cursor()
    mycursor.execute(f'select paid from fee where s_id={s_id}')
    for i in mycursor:
        a = i[0] + int(input(f'enter amount(paid={i[0]}):- '))
        print(a)
########################################################################################################

    colleg = login()
    mycursor = colleg.cursor()
    mycursor.execute(f'select fee from fee where s_id={s_id}')
    for i in mycursor:
        b=int(i[0])
    colleg = login()
    mycursor = colleg.cursor()

    if a == b:
        sql = f"UPDATE fee SET paid = {a}, status = 'yes' WHERE s_id = {s_id}"
        print('no dues')
    elif a > b:
        sql = f"UPDATE fee SET paid = {b - a}, status = 'extra' WHERE s_id = {s_id}"
        print(f'extra payment of {a - b}')
    else:
        sql = f"UPDATE fee SET paid = {a}, status = 'no' WHERE s_id = {s_id}"
        print(f'need to pay {b - a} Rs')

    if a == 100000:
        sql = f"UPDATE fee SET paid = {a}, status = 'yes' WHERE s_id = {s_id}"
        print('no dues')
    elif a > 100000:
        sql = f"UPDATE fee SET paid = {100000 - a}, status = 'extra' WHERE s_id = {s_id}"
        print(f'extra payment of {a - 100000}')
    else:
        sql = f"UPDATE fee SET paid = {a}, status = 'no' WHERE s_id = {s_id}"
        print(f'need to pay {100000 - a} Rs')

    mycursor.execute(sql)
    colleg.commit()
########################################################################################################
########################################################################################################
def new_facolty():
    f_name = input('enter f_name:- ')
    age = input('enter age:-')
    d_id = int(input('enter d_id:- '))
    designetion = input('enter designetion:- ')
########################################################################################################
    colleg = login()
    mycursor = colleg.cursor()
    sql = 'INSERT INTO faculty (`f_name`, `age`, `d_id`, `designetion`) VALUES (%s,%s,%s,%s)'
    val = (f_name, age, d_id, designetion)
    mycursor.execute(sql, val)
    colleg.commit()
########################################################################################################
########################################################################################################
def new_deportiment():
    d_name = input('enter d_name:- ')
    hod = input('enter hod:- ')

    colleg = login()
    mycursor = colleg.cursor()
    sql = "INSERT INTO deportment (`d_name`, `hod`) VALUES (%s,%s)"
    val = (d_name, hod)
    mycursor.execute(sql, val)
    colleg.commit()
    #################################################################
    colleg = login()
    mycursor = colleg.cursor()
    mycursor.execute('select d_id from deportment')
    for i in mycursor:
        a = int(i[0])
    f_name = hod
    age = int(input('enter age of hod:- '))
    d_id = a
    designetion = hod
########################################################################################################
    colleg = login()
    mycursor = colleg.cursor()
    sql = 'INSERT INTO faculty (`f_name`, `age`, `d_id`, `designetion`) VALUES (%s,%s,%s,%s)'
    val = (f_name, age, d_id, designetion)
    mycursor.execute(sql, val)
    colleg.commit()

def new_student():
    s_name = input('enter s_name:- ')
    age = int(input('enter age:- '))
    d_id = int(input('enter d_id:- '))
    duretion = input('enter duretion:- ')
    fee = int(input('enter fee:- '))
    paid = int(input('enter paid amount:- '))
    if paid == fee:
        status = 'yes'
    elif paid > fee:
        status = 'extra'
    else:
        status = 'no'
    colleg = login()
    mycursor = colleg.cursor()
    sql = 'INSERT INTO fee (fee, paid, status) VALUES (%s,%s,%s)'
    val = (fee, paid, status)
    mycursor.execute(sql, val)
    colleg.commit()

    colleg = login()
    mycursor = colleg.cursor()
    mycursor.execute('select s_id from fee')
    for i in mycursor:
        a = int(i[0])

    colleg = login()
    mycursor = colleg.cursor()
    sql = 'INSERT INTO `record_maintaince`.`student` (`s_id`, `s_name`, `age`, `d_id`, `duretion`) VALUES (%s,%s,%s,%s,%s)'
    val = (a, s_name, age, d_id, duretion)
    mycursor.execute(sql, val)
    colleg.commit()
def show_details():
    details = input(
        ' 1). deportment id\n 2). student_id\n 3). student name \n 4). deportment name\n 5). hod\n 6). student fee\n 7). student paid\n 8). student fee status\n 9).student duretion\n\n enter your value sapareted by camas:- ')
    details = list(details.split(','))
    detailing = {'1': 'deportment.d_id', '2': 'student.s_id', '3': 'student.s_name', '4': 'deportment.d_name',
                 '5': 'deportment.hod', '6': 'fee.fee', '7': 'fee.paid', '8': 'fee.status', '9': 'student.duretion'}
    reference = ''
    for i in details:
        if i == details[0]:
            reference = detailing[i]
        else:
            reference = reference + ',' + detailing[i]
    print(reference)
    print()
    cond=input('--->>enter the condition for search:- ')
    if cond==None:
        cond=None
    else:
        cond=f'and {cond}'
    colleg = login()
    mycursor = colleg.cursor()
    mycursor.execute(
        f'select {reference} from fee,student,deportment where fee.s_id=student.s_id and student.d_id=deportment.d_id {cond}')
    print(reference)
    for i in mycursor:
        print(i)


################################################################################
################################################################################
################################################################################
print(' 1). show tables\n 2). update fee\n 3). new faculty\n 4). new deportment\n 5). new student\n 6). show details ')
select=int(input('...................select one of the above...................\n\nenter your response:- '))
print()
if select==1:
    print('-->>tables in your database')
    tables()
elif select==2:
    print('-->>please provide required details')
    update_fee()
elif select==3:
    print('--->> please provide the required details of new professor')
    new_facolty()
elif select==4:
    print('--->> please provide the required details of new deportment')
    new_deportiment()
elif select==5:
    print('--->> please provide the required details of new student')
    new_student()
elif select==6:
    print('--->> please provide required details')
    show_details()
else:
    print('-->>enter valid value')



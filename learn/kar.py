import mysql.connector


def login():
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Gkarunakar@1432',
        database='record_maintaince'
    )
    return mydb
def update_fee():
    s_id = int(input("enter student id:- "))
    colleg = login()
    mycursor = colleg.cursor()
    mycursor.execute(f'select paid from fee where s_id={s_id}')
    for i in mycursor:
        a = i[0] + int(input(f'enter amount(paid={i[0]}):- '))
        print(a)
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

    mycursor.execute(sql)
    colleg.commit()



update_fee()
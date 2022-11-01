# creating a database for industrial gate management system
# importing mysql.connector
import datetime
import mysql.connector as sq
password = input("Enter your password: ")

# database creation

def database():
    mycon = sq.connect(host='localhost', user='root', password=password)
    mycursor = mycon.cursor()
    mycursor.execute("CREATE DATABASE employee")
    mycursor.execute("CREATE DATABASE vehicle")
    mycursor.execute("CREATE DATABASE visitor")
    mycursor.execute("CREATE DATABASE residential")


def emp():
    mycon = sq.connect(host='localhost', user='root', password=password, database='employee')
    cur = mycon.cursor()
    cur.execute("CREATE TABLE employee_entry(NAME varchar(30) not null,"
                "EMP_CODE int not null unique,"
                "TIME time not null,DEPARTMENT varchar(30))")
    mycon.commit()


def veh():
    mycon = sq.connect(host='localhost', user='root', password=password, database='vehicle')
    cur = mycon.cursor()
    cur.execute("CREATE TABLE vehicle_entry(VEHICLE_NUMBER int,"
                "DRIVER_NAME varchar(30) not null,"
                "TIME time not null,MATERIAL varchar(30))")


def vis():
    mycon = sq.connect(host='localhost', user='root', password=password, database='visitor')
    cur = mycon.cursor()
    cur.execute("CREATE TABLE visitor_entry(NAME varchar(30) not null,"
                "TIME time not null,"
                "MOBILE_NUMBER int unique,"
                "REASON varchar(90))")


def res():
    mycon = sq.connect(host='localhost', user='root', password=password, database='residential')
    cur = mycon.cursor()
    cur.execute("CREATE TABLE residential_entry(NAME varchar(30) not null,"
                "TIME time not null,"
                "HOUSE_NUMBER varchar(10) not null)")

try:
    database()
    veh()
    emp()
    vis()
    res()

except:
    pass


def date_time():
    return datetime.datetime.now()


def sql_emp(N, C, T, D):
    data = sq.connect(host='localhost', user='root', password=password, database='employee')
    cur = data.cursor()
    q = "INSERT INTO employee_entry(NAME,EMP_CODE,TIME,DEPARTMENT) VALUES(%s,%s,%s,%s)"
    val = (N, C, T, D)
    cur.execute(q, val)
    data.commit()
    data.close()


def sql_update(Sr):
    data = sq.connect(host='localhost', user='root', password=password, database='employee')
    cur = data.cursor()
    print('WHAT DO YOU WANT TO '
          'CHANGE \n PRESS 1 FOR NAME: \n PRESS 2 FOR CODE: \n PRESS 3 FOR DEPARTMENT: \n '
          'PRESS 4 FOR LAST ENTERED DATA TO CHANGE')
    i = int(input('enter number'))
    if i == 1:
        n = input('ENTER NAME')
        cur.execute(f"UPDATE employee_entry SET NAME='{n}' WHERE NAME='{Sr}'")
        data.commit()
    elif i == 2:
        n1 = int(input("enter code"))
        cur.execute("UPDATE employee_entry SET EMP_CODE={} WHERE NAME={}".format(n1, Sr))
        data.commit()
    elif i == 3:
        n2 = input("enter department")
        cur.execute("UPDATE employee_entry SET DEPARTMENT='{}' WHERE NAME='{}'".format(n2, Sr))
        data.commit()
    elif i == 4:
        n3 = input("enter name")
        n4 = int(input("enter emp_code"))
        n5 = input("enter department")
        cur.execute("UPDATE employee_entry SET NAME={},EMP_CODE={},DEPARTMENT={} WHERE NAME={}".format(n3, n4, n5, Sr))
        data.commit()
    data.close()


def sql_vehicle(VN, DN, T, M):
    data = sq.connect(host='localhost', user='root', password=password, database='vehicle')
    cur = data.cursor()
    q = "INSERT INTO vehicle_entry(VEHICLE_NUMBER,DRIVER_NAME,TIME,MATERIAL) VALUES(%s,%s,%s,%s)"
    val = (VN, DN, T, M)
    cur.execute(q, val)
    data.commit()
    data.close()


def sql_vehupdate(veh_Sr):
    data = sq.connect(host='localhost', user='root', password=password, database='vehicle')
    cur = data.cursor()
    print(
        'WHAT DO YOU WANT TO CHANGE \n PRESS 1 FOR VEHICLE NUMBER:'
        ' \n PRESS 2 FOR DRIVER NAME: \n PRESS 3 FOR MATERIAL: \n PRESS 4 FOR LAST ENTERED DATA TO CHANGE:')
    i = int(input('enter number'))
    if i == 1:
        n = input('ENTER VEHICLE NUMBER')
        cur.execute("UPDATE vehicle_entry SET VEHICLE_NUMBER={} WHERE VEHICLE_NUMBER={}".format(n, veh_Sr))
        data.commit()
    elif i == 2:
        n1 = int(input("ENTER DRIVER NAME: "))
        cur.execute("UPDATE vehicle_entry SET DRIVER_NAME='{}' WHERE VEHICLE_NUMBER={}".format(n1, veh_Sr))
        data.commit()
    elif i == 3:
        n2 = input("Enter material: ")
        cur.execute("UPDATE vehicle_entry SET MATERIAL='{}' WHERE VEHICLE_NUMBER={}".format(n2, veh_Sr))
        data.commit()
    elif i == 4:
        n3 = input("Enter vehicle number: ")
        n4 = int(input("Enter driver name: "))
        n5 = input("Enter material: ")
        cur.execute("UPDATE vehicle_entry SET VEHICLE_NUMBER={},"
                    "DRIVER_NAME='{}',"
                    "MATERIAL='{}' WHERE VEHICLE_NUMBER={}".format(n3, n4, n5, veh_Sr))
        data.commit()
    data.close()


def sql_visitor(N, T, MN, R):
    data = sq.connect(host='localhost', user='root', password='admin', database='visitor')
    cur = data.cursor()
    q = "INSERT INTO visitor_entry(NAME,TIME,MOBILE_NUMBER,REASON) VALUES(%s,%s,%s,%s)"
    val = (N, T, MN, R)
    cur.execute(q, val)
    data.commit()
    data.close()


def sql_residential(N, T, H):
    data = sq.connect(host='localhost', user='root', password=password, database='residential')
    cur = data.cursor()
    q = "INSERT INTO residential_entry(NAME,TIME,HOUSE_NUMBER) VALUES(%s,%s,%s)"
    val = (N, T, H)
    cur.execute(q, val)
    data.commit()
    data.close()


def sql_residentialupdate(res_Sr):
    data = sq.connect(host='localhost', user='root', password=password, database='residential')
    cur = data.cursor()
    print(
        'WHAT DO YOU WANT TO CHANGE ? \n PRESS 1 FOR NAME:'
        ' \n PRESS 2 FOR HOUSE NUMBER: \n PRESS 3 FOR LAST ENTERED DATA TO CHANGE:')
    i = int(input("enter number"))
    if i == 1:
        n = input('ENTER NAME')
        cur.execute("UPDATE residential_entry SET NAME='{}' WHERE NAME='{}'".format(n, res_Sr))
        data.commit()
    elif i == 2:
        n1 = eval(input("ENTER HOUSE NUMBER"))
        cur.execute("UPDATE residential_entry SET HOUSE_NUMBER={} WHERE NAME='{}'".format(n1, res_Sr))
        data.commit()
    elif i == 3:
        n3 = input("Enter NAME: ")
        n4 = eval(input("Enter HOUSE NUMBER: "))
        cur.execute(
            "UPDATE residential_entry SET NAME={},HOUSE_NUMBER={} WHERE RESIDENTIAL_SERIAL_no={}".format(
                n3, n4, res_Sr))
        data.commit()
    data.close()


def employee():
    data = sq.connect(host='localhost', user='root', password=password, database='employee')
    cur = data.cursor()
    cur.execute('select * from employee_entry')
    dat = cur.fetchall()
    for i in dat:
        print(i)
    print("IF YOU WANT TO CHANGE ANY DATA ENTER Y/y")
    rr = input()
    if rr == 'Y' or rr == 'y':
        print('Which employee data you want to change: ')
        rr = int(input('Enter employee code of the employee: '))
        change_emp(rr)


def change_emp(rr):
    data = sq.connect(host='localhost', user='root', password=password, database='employee')
    cur = data.cursor()
    n1 = input('Enter name of employee: ')
    n3 = input('Enter department: ')
    n4 = int(input('Enter employee code: '))
    cur.execute(f'UPDATE employee_entry set NAME = "{n1}",EMP_CODE = {n4},DEPARTMENT = "{n3}" WHERE EMP_CODE = {rr}')
    data.commit()
    i = True
    while i:
        print('Want to change data or want to delete the data? ')
        print('Press Y/y to change or D/d to delete the data...')
        t = input('Enter: ')
        if t == 'Y' or t == 'y':
            na = input('Enter name: ')
            change_emp(na)
        elif t == 'D' or t == 'd':
            n4 = int(input('Enter emp code whose data you want to delete: '))
            cur.execute(f"delete from employee_entry where EMP_CODE = {n4}")
        else:
            i = False


def vehicle():
    data = sq.connect(host='localhost', user='root', password=password, database='vehicle')
    cur = data.cursor()
    cur.execute('select * from vehicle_entry')
    dat = cur.fetchall()
    print('\n')
    for i in dat:
        print(i)


def residential():
    data = sq.connect(host='localhost', user='root', password=password, database='residential')
    cur = data.cursor()
    cur.execute('select * from residential_entry')
    dat = cur.fetchall()
    for i in dat:
        print(i)


def visitor():
    data = sq.connect(host='localhost', user='root', password=password, database='visitor')
    cur = data.cursor()
    cur.execute('select * from visitor_entry')
    dat = cur.fetchall()
    for i in dat:
        print(i)


print("|===========================INDUSTRIAL GATE MANAGEMENT SYSTEM============================|")
abcd = 'T'
while (abcd == "T"):
    print('Press one "1" to enter data in the system: ')
    print('Press one "2" to retrieve data from the system: ')
    i = input('Enter 1/2: ')

    # CODE TO ENTER THE DATA INTO THE DATABASE

    if (i == '1'):
        print("Enter 1 for EMPLOYEE ENTRY: ")
        print("Enter 2 for VEHICLE ENTRY: ")
        print("Enter 3 for RESIDENTIAL ENTRY: ")
        print("Enter 4 for VISITOR ENTRY: ")
        i1 = input('Enter your choice press 1,2,3,4 = ')
        if (i1 == '1'):
            k = True
            while k:
                n = input('Enter name of employee: ')
                c = int(input('Enter employee code of the employee: '))
                t = date_time()
                d = input('Enter department of the employee: ')
                sql_emp(n, c, t, d)
                print("DATA SUCCESSFULLY ENTERED OF EMPLOYEE NUMBER:", c)
                print(f"EMPLOYEE NAME: {n}")
                print("DO YOU WANT TO CHANGE LAST ENTERED DATA PRESS Y/y else N/n: ")
                i2 = input()
                if i2 == 'y' or i2 == 'Y':
                    sql_update(n)
                print('DO YOU WANT TO ENTER EMPLOYEE DATA AGAIN PRESS Y/y: ')
                K1 = input('Enter y/Y else press any key: ')
                if K1 == 'Y' or K1 == 'y':
                    k = True
                else:
                    k = False
            else:
                pass
        elif (i1 == '2'):
            vn = int(input('enter vehicle number: '))
            dn = input("enter driver name: ")
            vt = date_time()
            ma = input("enter material name: ")
            sql_vehicle(vn, dn, vt, ma)
            print(f"DATA SUCCESSFULLY ENTERED vehicle number: {vn}")
            print("IF YOU WANT TO CHANGE LAST ENTERED DATA PRESS Y/y: ")
            i3 = input()
            if i3 == 'Y' or i3 == 'y':
                sql_vehupdate(vn)
        elif (i1 == '3'):
            rn = input("Enter name of the person: ")
            rt = date_time()
            hn = input("Enter house number: ")
            sql_residential(rn, rt, hn)
            print(f"DATA SUCCESSFULLY ENTERED NAME: {rn}")
            print("IF YOU WANT TO CHANGE LAST ENTERED DATA PRESS Y/y: ")
            i4 = input()
            if (i4 == 'Y' or i4 == 'y'):
                sql_residentialupdate(rn)
        elif (i1 == '4'):
            vn = input('Enter name of visitor: ')
            vt = date_time()
            vm = int(input('Enter mobile number of the visitor: '))
            vr = input('Enter reason to visit the area: ')
            sql_visitor(vn, vt, vm, vr)
            print(f"DATA SUCCESSFULLY ENTERED NAME: {vn}")
    # CODE TO READ THE ENTERED DATA
    elif (i == '2'):
        print('SPECIFY WHICH DATABASE YOU WANT TO ACCESS')
        print('=================================================================')
        print("ENTER 1 TO RETRIEVE EMPLOYEE DATA:")
        print("ENTER 2 TO RETRIEVE VEHICLE DATA: ")
        print("ENTER 3 TO RETRIEVE VISITOR DATA: ")
        print("ENTER 4 TO RETRIEVE RESIDENTIAL DATA: ")
        r1 = input('Enter number: ')
        if r1 == '1':
            employee()
        elif r1 == '2':
            vehicle()
        elif r1 == '3':
            visitor()
        elif r1 == '4':
            residential()
    abcd = input("Whether you want to continue press T: ")

else:
    print("==================INDUSTRIAL GATE MANAGEMENT SYSTEM========================")
    print("===========================================================================")

print("********************************************************************************")

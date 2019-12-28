import pyodbc
from db import dataBase as database
from manufacturer import manufacturer
from employee import employee
from incentive import incentive
print("Welcome to OverDrive Information System.....");
print("Enter User Id")
userId = input("")
print("Enter Password")
password = input("")
will="yes"
while will == "yes":
    if userId == "admin" and password == "admin" :
        dbobj = database();
        cursor = dbobj.dbConn();
        mfg = manufacturer()
        emp = employee()
        inc = incentive()
        print("Welcome to OverDrive Information System.....")

        print("Choose Option:")
        print("1. Manufacturers")
        print("2. Employee")
        print("3. Customers")
        print("4. Orders")
        print("5. Incentive")
        c = int(input("Enter your choice"));

        if c == 1:
            print("Choose Option:")
            print("1. View All Manufacturers")
            print("2. View by name")
            print("3. Add Manufacturer data")
            print("4. Update Manufacturer data")

            m = int(input("Enter your choice"));
            if m == 1:
                mfg.selectAllManufacturers(cursor)
            elif m == 2:
                mfg.selectBasedOnName(cursor)
            elif m == 3:
                mfg.addManufacturer(cursor)
            elif m == 4:
                mfg.updateManufacturer(cursor)

        if c == 2:
            print("Choose Option:")
            print("1. View All Employees")
            print("2. View Employee by name")
            print("3. Add Employee data")
            print("4. Update Employee data")

            m = int(input("Enter your choice"));
            if m == 1:
                emp.selectAllEmployees(cursor)
            elif m == 2:
                emp.selectBasedOnName(cursor)
            elif m == 3:
                emp.addEmployee(cursor)
            elif m == 4:
                emp.updateEmployee(cursor)

        if c == 5:
            print("Choose Option:")
            print("1. View Incentives in previous n days")
            print("2. View Incentive by name")
            print("3. Add Incentive ")

            m = int(input("Enter your choice"));
            if m == 1:
                inc.selectAllIncentive(cursor)
            elif m == 2:
                inc.selectBasedOnName(cursor)
            elif m == 3:
                inc.addIncentive(cursor)


    else:
        print("Invalid credentials");
    will = input("do you want to continue ?")
    if will =='yes':
        print("Enter User Id")
        userId = input("")
        print("Enter Password")
        password = input("")
    else:
            break;




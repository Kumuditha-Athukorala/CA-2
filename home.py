import pyodbc
from db import dataBase as database
print("Welcome to OverDrive Information System.....");
print("Enter User Id")
userId = input("")
print("Enter Password")
password = input("")
will="yes"
while will=="yes":
    if userId=="admin" and password=="admin" :
        dbobj = database();

        cursor = dbobj.dbConn();
        cursor.execute('SELECT * FROM dbo.Incentive')

        for row in cursor:
            print(row[0])

        print("Welcome to OverDrive Information System.....")

        print("Choose Option:")
        print("1. Manufacturers")
        print("2. Employee")
        print("3. Customers")
        c = (int)(input("Enter your choice"));
        if c == 1:
            print();

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




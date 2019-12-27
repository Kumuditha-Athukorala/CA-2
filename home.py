import pyodbc
from db import dataBase as database
from customer import Customer
print("Welcome to OverDrive Information System.....");
print("Enter User Id")
userId = input("")
print("Enter Password")
password = input("")
will="yes"
while will == "yes":
    if userId=="admin" and password=="admin" :
        dbobj = database();

        cursor = dbobj.dbConn();



        cust = Customer()
        print("Welcome to OverDrive Information System.....")

        print("Choose Option:")
        print("1. Manufacturers")
        print("2. Employee")
        print("3. Customers")
        print("4. Orders")
        c = int(input("Enter your choice"));
        if c == 1:
            cursor.execute('SELECT * FROM dbo.Manufacturer')
            for row in cursor:
                print(row[1])
        if c == 2:
            cursor.execute('SELECT * FROM dbo.Employee')
            for row in cursor:
                print(row[1])
        if c == 3:
            print("Choose Customer related option")
            print("1. Search All Cutomers")
            print("2. Search Customers by Name")
            userInput = int(input("Please Enter the selected option"))

            if(userInput == 1):
                cust.searchAllCustomers(cursor)
            if(userInput == 2):
                cust.searchCustomerByName(cursor)
        if c == 4:
            cursor.execute('SELECT * FROM dbo.Customer_Order')
            for row in cursor:
                print(row[1])



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




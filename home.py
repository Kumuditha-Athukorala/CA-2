import pyodbc
from db import dataBase as database
from customer import Customer
from customer_order import CustomerOrder
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
        customerOrder = CustomerOrder()
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
            print("3. Add New Customer")
            print("4. Update Customer Record")
            userInput = int(input("Please Enter the selected option"))

            if(userInput == 1):
                cust.searchAllCustomers(cursor)
            if(userInput == 2):
                cust.searchCustomerByName(cursor)
            if(userInput == 3):
                cust.addCustomer(dbobj,cursor)
            if(userInput == 4):
                cust.updateCustomer(dbobj, cursor)

        if c == 4:
            print("Choose Customer Order related option")
            print("1. Search All Cutomer Orders")
            print("2. Search Customer Orders by Customer Id")
            print("3. Search Customer Orders by Related Employee Id")
            print("4. Add New Customer Order Record")
            print("5. Update Customer Order Record")
            userInput = int(input("Please Enter the selected option"))

            if(userInput == 1):
                customerOrder.serachAllCustomerOrders(cursor)
            if(userInput == 2):
                customerOrder.searchOrderByCustomerId(cursor)
            if(userInput == 3):
                customerOrder.searchOrderByEmpolyeeId(cursor)
            if(userInput == 4):
                customerOrder.addCustomerOrder(dbobj,cursor)
            if(userInput == 5):
                customerOrder.updateCustomerOrder(dbobj, cursor)
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




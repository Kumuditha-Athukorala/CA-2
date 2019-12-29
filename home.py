import pyodbc
from db import dataBase as database
from manufacturer import manufacturer
from employee import employee
from incentive import incentive
from customer import Customer
from customer_order import CustomerOrder
from inventory import Inventory

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
        cust = Customer()
        customerOrder = CustomerOrder()
        inventory = Inventory()

        print("Welcome to OverDrive Information System.....")

        print("Choose Option:")
        print("1. Manufacturers")
        print("2. Employee")
        print("3. Customers")
        print("4. Orders")
        print("5. Incentive")
        print("6. Inventory")

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

            cursor.execute('SELECT * FROM dbo.Employee')
            for row in cursor:
                print(row[1])

        if(c==6):
            print("Choose Inventory related option")
            print("1. Search All Inventory")
            print("2. Add New Inventory Record")
            print("3. Update Inventory Record")
            print("4. View Available Cars")
            userInput = int(input("Please Enter the selected option"))

            if (userInput == 1):
                inventory.searchAllInvenrotyRecords(cursor)
            if (userInput == 2):
                inventory.addInventoryRecord(dbobj,cursor)
            if (userInput == 3):
                inventory.updateInventoryRecord(dbobj,cursor)
            if (userInput == 4):
                inventory.viewAvailableCars(dbobj,cursor)
                
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




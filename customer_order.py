import pyodbc
from customer import Customer

class CustomerOrder:

    def __init__(self):
        self.__customerOderId=""
        self.__customerOderDate=""
        self.__customerOrderDeliveryDate=""
        self.__customerOrderSellingPrice=""
        self.__customerId=""
        self.__employeeId=""


    def serachAllCustomerOrders(self,cursor):

        cursor.execute('SELECT * FROM dbo.Customer_Order')
        dash = '-' * 250
        print(dash)
        print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Customer Order Id", "Order Date", "Order Delivery Date", "Selling Price","Customer Id", "Employee Id" ))
        print(dash)
        for row in cursor:
            print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], str(row[3]),row[4], row[5]))


    def searchOrderByCustomerId(self,cursor):

        customerId = input("Please enter the Customer Id")
        sql =  'SELECT * FROM Customer_Order co WHERE co.customer_id =?'
        cursor.execute(sql,customerId)
        resultSet = cursor.fetchall()

        if(len(resultSet) != 0):
            dash = '-'*200
            print(dash)
            print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Customer Order Id", "Order Date", "Order Delivery Date", "Selling Price","Customer Id", "Employee Id" ))
            print(dash)
            for row in resultSet:
                print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], str(row[3]),row[4], row[5]))
        else:
            print("No Customer Order with that Customer ID!")


    def searchOrderByEmpolyeeId(self,cursor):

        employeeId = input("Please enter the Employee Id")
        sql =  'SELECT * FROM Customer_Order co WHERE co.employee_id =?'
        cursor.execute(sql,employeeId)
        resultSet = cursor.fetchall()

        if(len(resultSet) != 0):
            dash = '-'*200
            print(dash)
            print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Customer Order Id", "Order Date", "Order Delivery Date", "Selling Price","Customer Id", "Employee Id" ))
            print(dash)
            for row in resultSet:
                print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], str(row[3]),row[4], row[5]))
        else:
            print("No Customer Order with that Employee ID!")


    def addCustomerOrder(self, database, cursor):

        customer = Customer()
        customer.searchCustomerByName(cursor)

        self.__customerOderDate = input("Please Enter the Date of Order Placed.")
        self.__customerOrderDeliveryDate = input("Please Enter the Date of Order Delivered.")
        self.__customerOrderSellingPrice = int(input("Please Enter the Selling Price."))
        self.__customerId = input("Please Enter the above Customer Id.")
        self.__employeeId = input("Please Enter the Employee Id")

        database.insertCustomerOrderRecord(self.__customerOderDate, self.__customerOrderDeliveryDate, self.__customerOrderSellingPrice,
                                          self.__customerId, self.__employeeId)
        print("Customer Order record added successfully..!")


    def updateCustomerOrder(self,database, cursor):

        customer = Customer()
        customer.searchCustomerByName(cursor)

        customerOrder = CustomerOrder()
        customerOrder.searchOrderByCustomerId(cursor)

        self.__customerOderId = input("Please Enter the Customer Order Id which needs to be updated")
        self.__customerOderDate = input("Please Enter the New or Same Date of Order Placed.")
        self.__customerOrderDeliveryDate = input("Please Enter the New or Same Date of Order Delivered.")
        self.__customerOrderSellingPrice = int(input("Please Enter the New or Same Selling Price."))
        self.__customerId = input("Please Enter the New or Same Customer Id.")
        self.__employeeId = input("Please Enter the New or Same Employee Id")

        database.updateCustomerOrderRecord(self.__customerOderId,self.__customerOderDate,self.__customerOrderDeliveryDate,
                                           self.__customerOrderSellingPrice,self.__customerId,self.__employeeId)
        print("Customer Order Record Updated Successfully.!")







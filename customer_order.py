import pyodbc

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




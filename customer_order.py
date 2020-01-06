import pyodbc
from customer import Customer
from employee import employee
from validator import Validator

validator = Validator()

class CustomerOrder:

    def __init__(self):
        self.__customerOderId=""
        self.__customerOderDate=""
        self.__customerOrderDeliveryDate=""
        self.__customerOrderSellingPrice=""
        self.__customerId=""
        self.__employeeId=""


    def serachAllCustomerOrders(self,cursor):
       try:
            cursor.execute('SELECT * FROM dbo.Customer_Order')
            dash = '-' * 175
            print(dash)
            print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Customer Order Id", "Order Date", "Order Delivery Date", "Selling Price","Customer Id", "Employee Id" ))
            print(dash)
            for row in cursor:
                print('{:<15s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], str(row[3]),row[4], row[5]))
       except:
           print ("Something went wrong.!! Contact the administrator.!")


    def searchOrderByCustomerId(self,cursor):
       try:
            customer = Customer()
           #   customer.searchCustomerByName(cursor)

            name = input("Please enter the Customer Name")
            args = ['%' + name + '%']
            sql = 'SELECT c.customer_id, c.customer_name, c.customer_phone FROM Customer c WHERE c.customer_name LIKE ?'
            cursor.execute(sql, args)
            resultSet = cursor.fetchall()

            if (len(resultSet) != 0):
                dash = '-' * 75
                print(dash)
                print('{:>7s}{:>30s}{:>35s}'.format("Id", "Name", "Phone Number"))
                print(dash)
                for row in resultSet:
                    print('{:>7s}{:>30s}{:>30s}'.format(row[0], row[1], row[2]))
                customerId = input("Please enter the Customer Id")
                sql = 'SELECT * FROM Customer_Order co WHERE co.customer_id =?'
                cursor.execute(sql, customerId)
                resultSet = cursor.fetchall()

                if (len(resultSet) != 0):
                    dash = '-' * 175
                    print(dash)
                    print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Customer Order Id", "Order Date",
                                                                             "Order Delivery Date", "Selling Price",
                                                                             "Customer Id", "Employee Id"))
                    print(dash)
                    for row in resultSet:
                        print('{:<15s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2],
                                                                                  str(row[3]), row[4], row[5]))
                else:
                    print("No Customer Order with that Customer ID!")
            else:
                print("No Customer found with that name.!")
       except:
           print("Something went wrong.!! Contact the administrator.!")



    def searchOrderByEmpolyeeId(self,cursor):
        try:
         #   emp = employee()
         #   emp.selectBasedOnName(cursor)

            name = input("Enter name of employee. !")
            args = ['%' + name + '%']

            cursor.execute('SELECT * FROM dbo.Employee where employee_name like ?', args)
            dash = '-' * 180
            data = cursor.fetchall()

            if len(data) != 0:
                print(dash)
                print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Id", "Name", "Designation", "DOB", "PPS",
                                                                         "Salary"))
                print(dash)
                for row in data:
                    print(
                        '{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], row[4], row[5],
                                                                           str(row[6])))
                employeeId = input("Please enter the Employee Id")
                sql = 'SELECT * FROM Customer_Order co WHERE co.employee_id =?'
                cursor.execute(sql, employeeId)
                resultSet = cursor.fetchall()

                if (len(resultSet) != 0):
                    dash = '-' * 175
                    print(dash)
                    print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Customer Order Id", "Order Date",
                                                                             "Order Delivery Date", "Selling Price",
                                                                             "Customer Id", "Employee Id"))
                    print(dash)
                    for row in resultSet:
                        print('{:<15s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], str(row[3]),
                                                                                  row[4], row[5]))
                else:
                    print("No Customer Order with that Employee ID!")
            else:
                print("No employee found with that name!")
        except:
            print("Something went wrong.!! Contact the administrator.!")


    def addCustomerOrder(self, database, cursor):
      try:
        # customer = Customer()
        #customer.searchCustomerByName(cursor)

        name = input("Please enter the Customer Name")
        args = ['%' + name + '%']
        sql = 'SELECT c.customer_id, c.customer_name, c.customer_phone FROM Customer c WHERE c.customer_name LIKE ?'
        cursor.execute(sql, args)
        resultSet = cursor.fetchall()

        if (len(resultSet) != 0):
            dash = '-' * 75
            print(dash)
            print('{:>7s}{:>30s}{:>35s}'.format("Id", "Name", "Phone Number"))
            print(dash)
            for row in resultSet:
                print('{:>7s}{:>30s}{:>30s}'.format(row[0], row[1], row[2]))
            orderDate = input("Please Enter the Date of Order Placed.")
            while not validator.dateValidate(orderDate):
                orderDate = input("Please Enter the Date of Order Placed.")
            self.__customerOderDate = orderDate

            deliveryDate = input("Please Enter the Date of Order Delivered.")
            while not validator.dateValidate(deliveryDate):
                deliveryDate = input("Please Enter the Date of Order Delivered.")
            self.__customerOrderDeliveryDate = deliveryDate

            sellingPrice = input("Please Enter the Selling Price.")
            while not validator.priceValidate(sellingPrice):
                sellingPrice = input("Please Enter the Selling Price.")
            self.__customerOrderSellingPrice = sellingPrice

            self.__customerId = input("Please Enter the above Customer Id.")

            emp = employee()
            emp.selectAllEmployees(cursor)

            self.__employeeId = input("Please Enter the Employee Id from the above list")

            database.insertCustomerOrderRecord(self.__customerOderDate, self.__customerOrderDeliveryDate,
                                               self.__customerOrderSellingPrice,
                                               self.__customerId, self.__employeeId)
            print("Customer Order record added successfully..!")

        else:
            print("No Customer found with that name.!")

      except:
          print ("Something went wrong.!! Contact the administrator.!")


    def updateCustomerOrder(self,database, cursor):
      try:
            customer = Customer()
            customer.searchCustomerByName(cursor)

            customerOrder = CustomerOrder()
            customerOrder.searchOrderByCustomerId(cursor)

            self.__customerOderId = input("Please Enter the Customer Order Id which needs to be updated")

            orderDate = input("Please Enter the New or Same Date of Order Placed.")
            while not validator.dateValidate(orderDate):
                orderDate = input("Please Enter the New or Same Date of Order Placed.")
            self.__customerOderDate = orderDate

            deliveryDate = input("Please Enter the New or Same Date of Order Delivered.")
            while not validator.dateValidate(deliveryDate):
                deliveryDate = input("Please Enter the New or Same Date of Order Delivered.")
            self.__customerOrderDeliveryDate = deliveryDate

            sellingPrice = input("Please Enter the New or Same Selling Price.")
            while not validator.priceValidate(sellingPrice):
                sellingPrice = input("Please Enter the New or Same Selling Price.")
            self.__customerOrderSellingPrice = sellingPrice

            self.__customerId = input("Please Enter the New or Same Customer Id.")

            emp = employee()
            emp.selectAllEmployees(cursor)

            self.__employeeId = input("Please Enter the New or Same Employee Id")

            database.updateCustomerOrderRecord(self.__customerOderId,self.__customerOderDate,self.__customerOrderDeliveryDate,
                                               self.__customerOrderSellingPrice,self.__customerId,self.__employeeId)
            print("Customer Order Record Updated Successfully.!")
      except:
            print("Something went wrong.!! Contact the administrator.!")

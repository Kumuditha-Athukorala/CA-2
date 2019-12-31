import pyodbc
from customer import Customer
from customer_order import CustomerOrder

class report:
    def __init__(self):
        self.__inventoryId=""
        self.__inventoryDate=""
        self.__inventoryStatus=""
        self.__manufacturerOrderId=""
        self.__customerOrderId=""
        self.__customerId=""


    def getCustomerSpecificOrders(self,cursor):

        customer = Customer()
        customer.searchAllCustomers(cursor)

        self.__customerId = input("Please Enter the Customer Id")

        sql = "EXEC uspCustomer_Order_Details_with_Id ?"
        cursor.execute(sql,self.__customerId)
        dash = '-' * 250
        print(dash)
        print('{:<5s}{:>30s}{:>60s}{:>60s}{:>60s}{:>60s}{:>60s}{:>60s}'.format("Customer Id", "Customer Name",
                        "Address","Phone Number", "Order Id","Order Date", "Delivery Date","Selling Price"))
        print(dash)
        for row in cursor:
            print('{:<5s}{:>30s}{:>60s}{:>60s}{:>60s}{:>60s}{:>60s}{:>60s}'.format(str(row[0]), row[1], row[2] , row[3],
                    str(row[4]), row[5], row[6],str(row[7])))
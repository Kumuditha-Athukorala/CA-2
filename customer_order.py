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
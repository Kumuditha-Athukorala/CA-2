import pyodbc

class Customer:
    def __init__(self):
        self.__customerId=""
        self.__customerName=""
        self.__customerAddress=""
        self.__customerPhoneNumber=""

    def searchAllCustomers(self,cursor):
        cursor.execute('SELECT * FROM dbo.Customer')
        dash = '-' * 250
        print(dash)
        print('{:<5s}{:>30s}{:>60s}{:>30s}'.format("Id", "Name", "Address", "Phone Number"))
        print(dash)
        for row in cursor:
            print('{:<5s}{:>30s}{:>60s}{:>30s}'.format(str(row[0]), row[1], row[2], row[3]))
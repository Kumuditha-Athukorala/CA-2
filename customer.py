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

    def searchCustomerByName(self,cursor):

        name = input("Please enter the Customer Name")
        args = ['%'+name+'%']
        sql = 'SELECT c.customer_id, c.customer_name, c.customer_phone FROM Customer c WHERE c.customer_name like ?'
        cursor.execute(sql,args)
        resultSet = cursor.fetchall()

        if(len(resultSet) != 0):
            dash = '-'*150
            print(dash)
            print('{:<5s}{:>30s}{:>30s}'.format("Id", "Name","Phone Number"))
            print(dash)
            for row in resultSet:
                print('{:<5s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2]))
        else:
            print("No Customer found with that name.!")

    def addCustomer(self, databse,cursor):

        self.__customerName = input("Enter name of Customer.")
        self.__customerAddress = input("Enter Customer Address.")
        self.__customerPhoneNumber = input("Enter Customer Phone Number.")
        databse.insertCustomerRecord(self.__customerName,self.__customerAddress,self.__customerPhoneNumber)
        print("Customer Record added successfully..!")


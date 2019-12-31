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
        sql = 'SELECT c.customer_id, c.customer_name, c.customer_phone FROM Customer c WHERE c.customer_name LIKE ?'
        cursor.execute(sql,args)
        resultSet = cursor.fetchall()

        if(len(resultSet) != 0):
            dash = '-'*200
            print(dash)
            print('{:<5s}{:>30s}{:>30s}'.format("Id", "Name","Phone Number"))
            print(dash)
            for row in resultSet:
                print('{:<5s}{:>30s}{:>30s}'.format(row[0], row[1], row[2]))
        else:
            print("No Customer found with that name.!")


    def addCustomer(self, databse, cursor):

        self.__customerName = input("Enter name of Customer.")

        self.__customerPhoneNumber = input("Enter Customer Phone Number.")

        print("Enter customer address.")
        street = input("Enter street")
        bldng = input("Enter building/house name")
        room = input("Enter room no/house no")
        county = input("Enter county name")
        areacode = input("Enter area code")

        self.__customerAddress = "<Address><Street>" + street + "</Street><Building>" + bldng + "</Building><RoomNo>" + room + "</RoomNo><County>" + county + "</County><AreaCode>" + areacode + "</AreaCode></Address>"

        databse.insertCustomerRecord(self.__customerName,self.__customerAddress,self.__customerPhoneNumber)
        print("Customer Record added successfully..!")


    def updateCustomer(self, database, cursor):

        name = input("Enter name of the Customer. !")
        args = ['%'+name+'%']
        sql = 'SELECT * FROM dbo.Customer WHERE customer_name LIKE ?'

        cursor.execute(sql,args)
        dash = '-' * 200
        result = cursor.fetchall()

        if len(result) != 0:
            print("Customer found with name entered.! ")
            print(dash)
            print('{:<5s}{:>30s}{:>30s}{:>30s}'.format("Id", " Customer Name", "Customer Address", " Customer Phone Number"))
            print(dash)
            for row in result:
                print('{:<5s}{:>30s}{:>30s}{:>30s}'.format(row[0], row[1], row[2], row[3]))
                self.__customerId = row[0]

            self.__customerName = input("Enter new name of the Customer.")
            print("Enter customer address.")
            street = input("Enter street")
            bldng = input("Enter building/house name")
            room = input("Enter room no/house no")
            county = input("Enter county name")
            areacode = input("Enter area code")

            self.__customerAddress = "<Address><Street>" + street + "</Street><Building>" + bldng + "</Building><RoomNo>" + room + "</RoomNo><County>" + county + "</County><AreaCode>" + areacode + "</AreaCode></Address>"

            self.__customerPhoneNumber = input("Enter phone number of the Customer")
            database.updateCustomerRecord(self.__customerId, self.__customerName, self.__customerAddress, self.__customerPhoneNumber)
            print("Customer Record Updated Successfully.!")
        else:
            print("No Customer found with that name.!")
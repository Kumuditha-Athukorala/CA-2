import pyodbc
from validator import Validator as validator
validator = validator()


class Customer:
    def __init__(self):
        self.__customerId=""
        self.__customerName=""
        self.__customerAddress=""
        self.__customerPhoneNumber=""


    def searchAllCustomers(self,cursor):
        try:
            cursor.execute('SELECT * FROM dbo.Customer')
            dash = '-' * 75
            print(dash)
            print('{:>7s}{:>30s}{:>35s}'.format("Id", "Name", "Phone Number"))
            print(dash)
            for row in cursor:
                print('{:>7s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[3]))
        except:
            ("Something went wrong.!! Contact the administrator.!")


    def searchCustomerByName(self,cursor):
      try:
        name = input("Please enter the Customer Name")
        args = ['%'+name+'%']
        sql = 'SELECT c.customer_id, c.customer_name, c.customer_phone FROM Customer c WHERE c.customer_name LIKE ?'
        cursor.execute(sql,args)
        resultSet = cursor.fetchall()

        if(len(resultSet) != 0):
            dash = '-'*75
            print(dash)
            print('{:>7s}{:>30s}{:>35s}'.format("Id", "Name","Phone Number"))
            print(dash)
            for row in resultSet:
                print('{:>7s}{:>30s}{:>30s}'.format(row[0], row[1], row[2]))

        else:
            print("No Customer found with that name.!")
      except:
            ("Something went wrong.!! Contact the administrator.!")


    def addCustomer(self, databse, cursor):
       try:
            self.__customerName = input("Enter name of Customer.")
            mname = self.__customerName
            while not validator.nameValidate(mname):
                mname = input("Enter name of Customer.")
            self.__customerName = mname

            self.__customerPhoneNumber = input("Enter Customer Phone Number.")
            addr = self.__customerPhoneNumber
            while not validator.numberValidate(addr):
                addr = input("Enter Customer Phone Number.")
            self.__customerPhoneNumber = addr

            print("Enter customer address.")
            street = input("Enter street")
            bldng = input("Enter building/house name")
            room = input("Enter room no/house no")
            county = input("Enter county name")
            areacode = input("Enter area code")

            self.__customerAddress = "<Address><Street>" + street + "</Street><Building>" + bldng + "</Building><RoomNo>" + room + "</RoomNo><County>" + county + "</County><AreaCode>" + areacode + "</AreaCode></Address>"

            databse.insertCustomerRecord(self.__customerName,self.__customerAddress,self.__customerPhoneNumber)
            print("Customer Record added successfully..!")

       except:
           ("Something went wrong.!! Contact the administrator.!")


    def updateCustomer(self, database, cursor):
       try:
            name = input("Enter name of the Customer.")
            args = ['%'+name+'%']
            sql = 'SELECT * FROM dbo.Customer WHERE customer_name LIKE ?'

            cursor.execute(sql,args)
            dash = '-' * 75
            result = cursor.fetchall()

            if len(result) != 0:
                print("Customer found with name entered.! ")
                print(dash)
                print('{:>7s}{:>30s}{:>35s}'.format("Id", " Customer Name", " Customer Phone Number"))
                print(dash)
                for row in result:
                    print('{:>7s}{:>30s}{:>30s}'.format(row[0], row[1], row[3]))

                self.__customerId = input("Enter the Customer Id which needs to be updated")
                self.__customerName = input("Enter Same or New Name of the Customer.")
                mname = self.__customerName
                while not validator.nameValidate(mname):
                    mname = input("Enter Same or New Name of the Customer.")
                self.__customerName = mname

                self.__customerPhoneNumber = input("Enter Customer New or Same Phone Number.")
                addr = self.__customerPhoneNumber
                while not validator.numberValidate(addr):
                    addr = input("Enter Customer Phone Number.")
                self.__customerPhoneNumber = addr

                print("Enter Customer address.")
                street = input("Enter street")
                bldng = input("Enter building/house name")
                room = input("Enter room no/house no")
                county = input("Enter county name")
                areacode = input("Enter area code")

                self.__customerAddress = "<Address><Street>" + street + "</Street><Building>" + bldng + "</Building><RoomNo>" + room + "</RoomNo><County>" + county + "</County><AreaCode>" + areacode + "</AreaCode></Address>"

                database.updateCustomerRecord(self.__customerId, self.__customerName, self.__customerAddress, self.__customerPhoneNumber)
                print("Customer Record Updated Successfully.!")
            else:
                print("No Customer found with that name.!")
       except:
           ("Something went wrong.!! Contact the administrator.!")
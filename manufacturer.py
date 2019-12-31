import pyodbc
from db import dataBase as database
from validator import Validator as validator
validator = validator()
class manufacturer:

    def __init__(self):
        self.manufacturerId = ""
        self.manufacturerName = ""
        self.manufacturerAddr = ""
        self.manufacturerEmail = ""
        self.manufacturerPhno = ""

    def selectAllManufacturers (self, cursor):

        cursor.execute('SELECT * FROM dbo.Manufacturer')
        dash = '-' * 150
        print(dash)
        print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Id", "Name", "Location", "Email", "phonenumber"))
        print(dash)
        for row in cursor:
            print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], row[3], row[4]))

    def selectBasedOnName(self, cursor):
        name = input("Enter name of manufacturer. !")
        args = ['%' + name + '%']

        cursor.execute('SELECT * FROM dbo.Manufacturer where manufacturer_name like ?', args)
        dash = '-' * 150
        data = cursor.fetchall()

        if len(data) != 0:
            print(dash)
            print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Id", "Name", "Location", "Email", "Phone-number"))
            print(dash)
            for row in data:
                print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], row[3], row[4]))
        else:
            print("No manufacturer found with that name.!")

    def addManufacturer(self, cursor):

        db = database()

        self.manufacturerName = input("Enter name of manufacturer.")
        mname = self.manufacturerName
        while not validator.nameValidate(mname):
            mname = input("Enter name of manufacturer.")
        self.manufacturerName = mname

        self.manufacturerAddr = input("Enter manufacturer's address.")
        addr = self.manufacturerAddr
        while not validator.addrValidate(addr):
            addr = input("Enter manufacturer's address.")
        self.manufacturerAddr = addr

        self.manufacturerEmail = input("Enter manufacturer's email.")
        addr = self.manufacturerEmail
        while not validator.emailValidate(addr):
            addr = input("Enter manufacturer's email.")
        self.manufacturerEmail = addr

        self.manufacturerPhno = input("Enter manufacturer's contact number.")
        addr = self.manufacturerPhno
        while not validator.numberValidate(addr):
            addr = input("Enter manufacturer's contact number.")
        self.manufacturerPhno = addr



        db.insertMf(self.manufacturerName, self.manufacturerAddr, self.manufacturerEmail, self.manufacturerPhno)
        print("Record inserted successfully in Manufacturer table.!")



    def updateManufacturer(self, cursor):

        name = input("Enter name of manufacturer. !")
        args = ['%' + name + '%']

        cursor.execute('SELECT * FROM dbo.Manufacturer where manufacturer_name like ?', args)
        dash = '-' * 150
        data = cursor.fetchall()

        if len(data) != 0:
            print("Manufacturer found with name entered.! ")
            print(dash)
            print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Id", "Name", "Location", "Email", "Phone-number"))
            print(dash)
            for row in data:
                print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], row[3], row[4]))
            for row in data:
                self.manufacturerId = row[0]
            db = database()
            self.manufacturerName = input("Now Enter new/same name of manufacturer.")
            self.manufacturerAddr = input("Enter new/same manufacturer address.")
            self.manufacturerEmail = input("Enter new/same manufacturer email.")
            self.manufacturerPhno = input("Enter new/same manufacturer contact number.")
            db.updateMf(self.manufacturerName, self.manufacturerAddr, self.manufacturerEmail, self.manufacturerPhno,self.manufacturerId)
            print("Record updated successfully in Manufacturer table.!")
        else:
            print("No manufacturer found with that name.!")









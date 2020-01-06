from db import dataBase as database
from validator import Validator as validator
validator = validator()
class employee:

    def __init__(self):
        self.employeeId = ""
        self.employeeName = ""
        self.employeeDesignation = ""
        self.employeeDob = ""
        self.employeePps = ""
        self.employeeSalary = 0

    def selectAllEmployees(self, cursor):
        try:
            cursor.execute('SELECT * FROM dbo.Employee')
            dash = '-' * 180
            print(dash)
            print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Id", "Name", "Designation", "DOB", "PPS", "Salary"))
            print(dash)
            for row in cursor:
                print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], row[4],row[5],str(row[6])))
        except:
            ("Something went wrong.!! Contact the administrator.!")

    def selectBasedOnName(self, cursor):
        try:
            name = input("Enter name of employee. !")
            args = ['%' + name + '%']

            cursor.execute('SELECT * FROM dbo.Employee where employee_name like ?', args)
            dash = '-' * 180
            data = cursor.fetchall()

            if len(data) != 0:
                print(dash)
                print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Id", "Name", "Designation", "DOB", "PPS", "Salary"))
                print(dash)
                for row in data:
                    print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], row[4], row[5],
                                                                             str(row[6])))
            else:
                print("No employee found with that name.!")
        except:
            print("Something went wrong.!! Contact the administrator.!")

    def addEmployee(self, cursor):
      try:
            db = database()

            self.employeeName = input("Enter name of employee.")
            mname = self.employeeName
            while not validator.nameValidate(mname):
                mname = input("Enter name of employee.")
            self.employeeName = mname


            self.employeeDesignation = input("Enter employee designation.")
            mname = self.employeeDesignation
            while not validator.nameValidate(mname):
                mname = input("Enter employee designation.")
            self.employeeDesignation = mname

            self.employeeDob = input("Enter employee dob.")

            self.employeePps = input("Enter employee pps number.")
            addr = self.employeePps
            while not validator.validatePPS(addr):
                addr = input("Enter employee pps number.")
            self.employeePps = addr

            self.employeeSalary = input("Enter employee salary") ;
            addr = self.employeeSalary
            while not validator.numberValidate(addr):
                addr = input("Enter employee salary")
            self.employeeSalary = addr

            print("Enter employee address.")
            street = input("Enter street")
            bldng = input("Enter building/house name")
            room = input("Enter room no/house no")
            county = input("Enter county name")
            areacode = input("Enter area code")

            address = "<Address><Street>"+street+"</Street><Building>"+bldng+"</Building><RoomNo>"+room+"</RoomNo><County>"+county+"</County><AreaCode>"+areacode+"</AreaCode></Address>"

            db.insertEmp(self.employeeName, self.employeeDesignation, self.employeeDob, self.employeePps,self.employeeSalary,address)
            print("Record inserted successfully in Employee table.!")
      except:
            print("Something went wrong.!! Contact the administrator.!")

    def updateEmployee(self, cursor):
      try:
        name = input("Enter name of employee. !")
        args = ['%' + name + '%']

        cursor.execute('SELECT * FROM dbo.Employee where employee_name like ?', args)
        dash = '-' * 180
        data = cursor.fetchall()

        if len(data) != 0:
            print("Employee found with name entered.! ")
            print(dash)
            print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Id", "Name", "Designation", "DOB", "PPS", "Salary"))
            print(dash)
            for row in data:
                print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], row[4], row[5],
                                                                         str(row[6])))
                self.employeeId = row[0]
            db = database()
            self.employeeName = input("Enter name of employee.")
            mname = self.employeeName
            while not validator.nameValidate(mname):
                mname = input("Enter name of employee.")
            self.employeeName = mname

            self.employeeDesignation = input("Enter employee designation.")
            mname = self.employeeDesignation
            while not validator.nameValidate(mname):
                mname = input("Enter employee designation.")
            self.employeeDesignation = mname

            self.employeeDob = input("Enter employee dob.")

            self.employeePps = input("Enter employee pps number.")
            addr = self.employeePps
            while not validator.numberValidate(addr):
                addr = input("Enter employee pps number.")
            self.employeePps = addr

            self.employeeSalary = input("Enter employee salary");
            addr = self.employeeSalary
            while not validator.numberValidate(addr):
                addr = input("Enter employee salary")
            self.employeeSalary = addr
            print("Enter employee address.")
            street = input("Enter street")
            bldng = input("Enter building/house name")
            room = input("Enter room no/house no")
            county = input("Enter county name")
            areacode = input("Enter area code")

            address = "<Address><Street>" + street + "</Street><Building>" + bldng + "</Building><RoomNo>" + room + "</RoomNo><County>" + county + "</County><AreaCode>" + areacode + "</AreaCode></Address>"

            db.updateEmp(self.employeeName, self.employeeDesignation, self.employeeDob, self.employeePps,
                        self.employeeSalary,self.employeeId, address)
            print("Record updated successfully in Employee table.!")
        else:
            print("No employee found with that name.!")
      except:
            print("Something went wrong.!! Contact the administrator.!")
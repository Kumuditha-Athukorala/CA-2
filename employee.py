from db import dataBase as database

class employee:

    def __init__(self):
        self.employeeId = ""
        self.employeeName = ""
        self.employeeDesignation = ""
        self.employeeDob = ""
        self.employeePps = ""
        self.employeeSalary = 0

    def selectAllEmployees(self, cursor):
        cursor.execute('SELECT * FROM dbo.Employee')
        dash = '-' * 180
        print(dash)
        print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Id", "Name", "Designation", "DOB", "PPS", "Salary"))
        print(dash)
        for row in cursor:
            print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], row[4],row[5],str(row[6])))

    def selectBasedOnName(self, cursor):
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

    def addEmployee(self, cursor):

        db = database()
        self.employeeName = input("Enter name of employee.")
        self.employeeDesignation = input("Enter employee designation.")
        self.employeeDob = input("Enter employee dob.")
        self.employeePps = input("Enter employee pps number.")
        self.employeeSalary = int(input("Enter employee salary")) ;
        db.insertEmp(self.employeeName, self.employeeDesignation, self.employeeDob, self.employeePps,self.employeeSalary)
        print("Record inserted successfully in Employee table.!")

    def updateEmployee(self, cursor):

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
            self.employeeName = input("Enter new/same name of employee.")
            self.employeeDesignation = input("Enter new/same employee designation.")
            self.employeeDob = input("Enter new/same employee dob.")
            self.employeePps = input("Enter new/same employee pps number.")
            self.employeeSalary = int(input("Enter new/same employee salary"));
            db.updateEmp(self.employeeName, self.employeeDesignation, self.employeeDob, self.employeePps,
                        self.employeeSalary,self.employeeId)
            print("Record updated successfully in Employee table.!")
        else:
            print("No employee found with that name.!")
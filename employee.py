from db import dataBase as database

class employee:

    def __init__(self):
        self.employeeId = ""
        self.employeeName = ""
        self.employeeDesignation = ""
        self.employeeDob = ""
        self.employeePps = ""
        self.employeeSalary = ""

    def selectAllEmployees(self, cursor):
        cursor.execute('SELECT * FROM dbo.Employee')
        dash = '-' * 180
        print(dash)
        print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Id", "Name", "Designation", "DOB", "PPS","Salary"))
        print(dash)
        for row in cursor:
            print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], row[4],row[5],str(row[6])))
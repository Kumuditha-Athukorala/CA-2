from db import dataBase as database

class incentive:

    def __init__(self):
        self.incentiveId = ""
        self.incentiveAmount = ""
        self.incentiveDate = ""
        self.employeeId = ""
        self.employeeSalary = 0

    def selectAllIncentive(self,cursor):
        days = int(input("Show data upto how many previous days?"))
        cursor.execute('SELECT * FROM dbo.Incentive where incentive_date <=CONVERT (date, GETDATE())   and incentive_date>CONVERT (date, GETDATE()-?)',days)
        dash = '-' * 100

        data = cursor.fetchall()

        if len(data) != 0:
            print(dash)
            print('{:<5s}{:>30s}{:>30s}{:>30s}'.format("Id", "Incentive Amount", "Date", "Employee Id"))
            print(dash)
            for row in data:
                print('{:<5s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), str(row[1]), row[2], row[3]))
        else:
            print("No incentive record present for last %i days"%days)
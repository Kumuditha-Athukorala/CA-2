from db import dataBase as database

class incentive:

    def __init__(self):
        self.incentiveId = ""
        self.incentiveAmount = ""
        self.incentiveDate = ""
        self.employeeId = ""
        self.employeeSalary = 0

    def selectAllIncentive(self,cursor):
        try:
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
        except:
            print("Something went wrong.!! Contact the administrator.!")

    def selectBasedOnName(self, cursor):
        try:
            name = input("Enter name of employee. !")
            args = ['%' + name + '%']

            cursor.execute('SELECT * FROM dbo.Employee where employee_name like ?', args)
            dash = '-' * 180
            data = cursor.fetchall()
            if len(data) != 0:
                    print(dash)
                    print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Id", "Name", "Designation", "DOB", "PPS",
                                                                             "Salary"))
                    print(dash)
                    for row in data:
                        print(
                            '{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], row[4], row[5],str(row[6])))
                    empid=input("Enter employee id from above.!")
                    cursor.execute("SELECT * FROM dbo.Incentive where employee_id=?", empid)
                    data = cursor.fetchall()
                    if len(data) != 0:
                        print(dash)
                        print('{:<5s}{:>30s}{:>30s}{:>30s}'.format("Id", "Incentive Amount", "Date", "Employee Id"))
                        print(dash)
                        for row1 in data:
                            print('{:<5s}{:>30s}{:>30s}{:>30s}'.format(str(row1[0]), str(row1[1]), row1[2], row1[3]))
                    else:
                        print("No incentive found for the employee")

            else:
                    print("No employee found with that name.!")
        except:
            print  ("Something went wrong.!! Contact the administrator.!")

    def addIncentive(self, cursor):
        try:
            name = input("Enter name of employee. !")
            args = ['%' + name + '%']

            cursor.execute('SELECT * FROM dbo.Employee where employee_name like ?', args)
            dash = '-' * 180
            data = cursor.fetchall()
            if len(data) != 0:
                    print(dash)
                    print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Id", "Name", "Designation", "DOB", "PPS",
                                                                             "Salary"))
                    print(dash)
                    for row in data:
                        print(
                            '{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], row[4], row[5], str(row[6])))
                    empid = input("Enter employee id from above.!")

                    db = database()
                    incentive_date = input("Enter incentive date")
                    db.insertIncentive(empid,incentive_date)

            else:
                    print("No employee found with that name.!")
        except:
            print ("Something went wrong.!! Contact the administrator.!")

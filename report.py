import pyodbc
class report:
    def __init__(self):
        self.__inventoryId = ""
        self.__inventoryDate = ""
        self.__inventoryStatus = ""
        self.__manufacturerOrderId = ""
        self.__customerOrderId = ""
        self.__employeeId = ""
        self.__employeeName = ""
        self.__totalSales = ""

    def employeePerformance(self,cursor):

        limit= int(input("Enter limit above which total sales achieved by employees:"))
        cursor.execute("{CALL uspEmployee_Performance (?)}", limit)
        dash = '-' * 100
        print(dash)
        print('{:<5s}{:>30s}{:>60s}'.format("Employee Id", "Name", "Total Sales"))
        print(dash)
        for row in cursor:
            print('{:<5s}{:>30s}{:>60s}'.format(str(row[0]), row[1], str(row[2])))

    def searchBySeats(self, cursor):

        limit = int(input("Enter number of seats in car:"))
        cursor.execute("{CALL uspCarSeats (?)}", limit)
        dash = '-' * 100

        data = cursor.fetchall()

        if len(data) != 0:
            print(dash)
            print('{:<15s}{:>30s}{:>30s}'.format("Model Name", "Model Type", "Model Price", "Year"))
            print(dash)
            for row in data:
                print('{:<15s}{:>30s}{:>30s}'.format(row[1], row[2], str(row[4]), str(row[5])))
        else:
            print("No such car model found")
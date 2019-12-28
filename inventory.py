import pyodbc


class Inventory:
    def __init__(self):
        self.__inventoryId=""
        self.__inventoryDate=""
        self.__inventoryStatus=""
        self.__manufacturerOrderId=""
        self.__customerOrderId=""



    def searchAllInvenrotyRecords(self,cursor):

        cursor.execute('SELECT * FROM dbo.Inventory')
        dash = '-' * 250
        print(dash)
        print('{:<5s}{:>30s}{:>60s}{:>30s}{:>30s}'.format("Inventory Id", "Inventory Date", "Inventory Status", "Manufacturer Order Id", "Customer Order Id"))
        print(dash)
        for row in cursor:
            print('{:<5s}{:>30s}{:>60s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], str(row[3]), str(row[4])))

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


    def addInventoryRecord(self, database, cursor):

        self.__inventoryDate = input("Please Enter the Inventory Date")
        self.__inventoryStatus = input("Please Enter the Inventory Status")
        self.__manufacturerOrderId = input("Please Enter the Manufacturer Order Id")
        self.__customerOrderId = input("Please Enter the Customer Order Id")
        database.insertInventoryrecord(self.__inventoryDate, self.__inventoryStatus, self.__manufacturerOrderId, self.__customerOrderId)
        print("Inventory Record added Successfully")


    def updateInventoryRecord(self, database, cursor):

        inventory = Inventory()
        inventory.searchAllInvenrotyRecords(cursor)

        self.__inventoryId = input("Please Enter the Inventory Id which needs to be updated")
        self.__inventoryDate = input("Please Enter the New or Same Inventory Date")
        self.__inventoryStatus = input("Please Enter the New or Same Inventory Status")
        self.__manufacturerOrderId = input("Please Enter the New or Same Manufacture Order Id")
        self.__customerOrderId = input("Please Enter the New or Same Customer Order Id")
        database.updateInventoryRecord(self.__inventoryId, self.__inventoryDate, self.__inventoryStatus, self.__manufacturerOrderId, self.__customerOrderId)
        print("Inventory Record updated Successfully")



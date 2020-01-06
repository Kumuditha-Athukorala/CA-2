import pyodbc
from validator import Validator
from carmodel import carmodel
from manufacturer_order import ManufacturerOrder
from customer_order import CustomerOrder

validator = Validator()


class Inventory:
    def __init__(self):
        self.__inventoryId=""
        self.__inventoryDate=""
        self.__inventoryStatus=""
        self.__manufacturerOrderId=""
        self.__customerOrderId=""



    def searchAllInvenrotyRecords(self,cursor):
       try:
            cursor.execute('SELECT * FROM dbo.Inventory')
            dash = '-' * 175
            print(dash)
            print('{:<5s}{:>30s}{:>60s}{:>30s}{:>30s}'.format("Inventory Id", "Inventory Date", "Inventory Status", "Manufacturer Order Id", "Customer Order Id"))
            print(dash)
            for row in cursor:
                print('{:<5s}{:>30s}{:>60s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], str(row[3]), str(row[4])))

       except:
           print("Something went wrong.!! Contact the administrator.!")


    def addInventoryRecord(self, database, cursor):
     try:

         manufacturerOrder = ManufacturerOrder()
         manufacturerOrder.searchAllManufactuererOrderRecords(cursor)

         customerOrder = CustomerOrder()
         customerOrder.serachAllCustomerOrders(cursor)

         inventoryDate = input("Please Enter the Inventory Date")
         while not validator.dateValidate(inventoryDate):
             inventoryDate = input("Please Enter the Inventory Date")
         self.__inventoryDate = inventoryDate

         self.__inventoryStatus = input("Please Enter the Inventory Status")

         orderId = input("Please Enter the Manufacturer Order Id")
         while not validator.numberValidate(orderId):
             orderId = input("Please Enter the Manufacturer Order Id")
         self.__manufacturerOrderId = orderId

         self.__customerOrderId = input("Please Enter the Customer Order Id")

         database.insertInventoryrecord(self.__inventoryDate, self.__inventoryStatus, self.__manufacturerOrderId, self.__customerOrderId)
         print("Inventory Record added Successfully")

     except:
         print("Something went wrong.!! Contact the administrator.!")


    def updateInventoryRecord(self, database, cursor):
     try:
            inventory = Inventory()
            inventory.searchAllInvenrotyRecords(cursor)

            inventoryId = input("Please Enter the Inventory Id which needs to be updated")
            while not validator.numberValidate(inventoryId):
                inventoryId = input("Please Enter the Inventory Id which needs to be updated")
            self.__inventoryId = inventoryId

            date = input("Please Enter the New or Same Inventory Date")
            while not validator.dateValidate(date):
                date = input("Please Enter the New or Same Inventory Date")
            self.__inventoryDate = date

            self.__inventoryStatus = input("Please Enter the New or Same Inventory Status")

            manufacturerOrder = ManufacturerOrder()
            manufacturerOrder.searchAllManufactuererOrderRecords(cursor)

            manuOrderId = input("Please Enter the New or Same Manufacture Order Id")
            while not validator.numberValidate(manuOrderId):
                manuOrderId = input("Please Enter the New or Same Manufacture Order Id")
            self.__manufacturerOrderId = manuOrderId

            customerOrder = CustomerOrder()
            customerOrder.serachAllCustomerOrders(cursor)


            self.__customerOrderId = input("Please Enter the New or Same Customer Order Id")

            database.updateInventoryRecord(self.__inventoryId, self.__inventoryDate, self.__inventoryStatus, self.__manufacturerOrderId, self.__customerOrderId)
            print("Inventory Record updated Successfully")
     except:
         print("Something went wrong.!! Contact the administrator.!")


    def viewAvailableCars(self,database,cursor):
      try:
            sql = 'SELECT i.inventory_id, i.inventory_date, i.inventory_status, mo.manufacturer_order_price,cm.car_model_name,' \
                  'cm.car_model_variant,m.manufacturer_name FROM Inventory i ' \
                  'INNER JOIN Manufacturer_Order mo ON i.manufacturer_order_id = mo.manufacturer_order_id ' \
                  'INNER JOIN Car_Model cm ON mo.car_model_id = cm.car_model_id ' \
                  'INNER JOIN Manufacturer m ON cm.manufacturer_id = m.manufacturer_id ' \
                  'WHERE i.inventory_status = \'AVAILABLE\''

            cursor.execute(sql)
            dash = '-' * 200
            print(dash)
            print('{:<5s}{:>30s}{:>60s}{:>30s}{:>30s}{:>30s}'.format("Inventory Id", "Inventory Date", "Inventory Status",
                                                              "Manufacturer Order Price", "Model Name", "Manufacturer Name"))
            print(dash)
            for row in cursor:
                print('{:<5s}{:>30s}{:>60s}{:>30s}{:>36s}{:>28s}'.format(str(row[0]), row[1], row[2], str(row[3]), row[4], row[6]))
      except:
            print("Something went wrong.!! Contact the administrator.!")


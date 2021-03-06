import pyodbc
from validator import Validator
from carmodel import carmodel

validator = Validator()

class ManufacturerOrder:

    def __init__(self):
        self.__manufacturerOrderId=""
        self.__manufacturerOrderDate=""
        self.__manufacturerOrderPrice=""
        self.__carModelId=""


    def searchAllManufactuererOrderRecords(self,cursor):
      try:
            cursor.execute("SELECT * FROM dbo.Manufacturer_Order");
            dash = '-' * 150
            print(dash)
            print('{:<5s}{:>30s}{:>40s}{:>30s}'.format("Order Id", "Manufacturer Order Date", "Manufacturer Order Price", "Car Model Id"))
            print(dash)
            for row in cursor:
                print('{:<5s}{:>30s}{:>40s}{:>30s}'.format(str(row[0]), row[1], str(row[2]), str(row[3])))
      except:
            print("Something went wrong.!! Contact the administrator.!")

    def searchAllManufacturerOrdersWithModelAndManufacturer(self,cursor):
      try:
            sql = "SELECT mo.manufacturer_order_id, mo.manufacturer_order_date, mo.manufacturer_order_price, m.manufacturer_name, " \
                  "cm.car_model_name, cm.car_model_type FROM Manufacturer_Order mo" \
                  " INNER JOIN Car_Model cm ON mo.car_model_id = cm.car_model_id " \
                  "INNER JOIN Manufacturer m ON cm.manufacturer_id = m.manufacturer_id"

            cursor.execute(sql)
            dash = '-' * 175
            print(dash)
            print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>25s}'.format("Order Id", "Manufacturer Order Date", "Manufacturer Order Price",
                                                       "Manufacturer Name", "Model Name", "Type"))
            print(dash)
            for row in cursor:
                print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], str(row[2]), row[3], row[4], row[5]))
      except:
          print ("Something went wrong.!! Contact the administrator.!")

    def addManufacturerOrderRecord(self,database,cursor):
       try:
           orderDate = input("Please Enter the Manufacturer Order Date")
           while not validator.dateValidate(orderDate):
               orderDate = input("Please Enter the Manufacturer Order Date")
           self.__manufacturerOrderDate = orderDate

           orderPrice = input("Please Enter the Manufacturer Order Price")
           while not validator.priceValidate(orderPrice):
               orderPrice = input("Please Enter the Manufacturer Order Price")
           self.__manufacturerOrderPrice = orderPrice

           modelId = input("Please Enter the Car Model Id")
           while not validator.numberValidate(modelId):
               modelId = input("Please Enter the Car Model Id")
           self.__carModelId = modelId

           database.insertManufacturerOrderRecord(self.__manufacturerOrderDate, self.__manufacturerOrderPrice, self.__carModelId)
           print("Manufacturer Order Record added Successfully")

       except:
           print("Something went wrong.!! Contact the administrator.!")


    def updateManufacturerOrderRecord(self,database,cursor):
      try:
       #  manufacturerOrder = ManufacturerOrder()
       # manufacturerOrder.searchAllManufactuererOrderRecords(cursor)
       cursor.execute("SELECT * FROM dbo.Manufacturer_Order");
       dash = '-' * 150
       print(dash)
       print('{:<5s}{:>30s}{:>40s}{:>30s}'.format("Order Id", "Manufacturer Order Date", "Manufacturer Order Price",
                                                  "Car Model Id"))
       print(dash)

       resultSet = cursor.fetchall()

       if (len(resultSet) != 0):
           for row in resultSet:
               print('{:<5s}{:>30s}{:>40s}{:>30s}'.format(str(row[0]), row[1], str(row[2]), str(row[3])))

           orderId = input("Please Enter the Manufacturer Order Id which needs to be updated")
           while not validator.numberValidate(orderId):
                orderId = input("Please Enter the Manufacturer Order Id which needs to be updated")
           self.__manufacturerOrderId = orderId

           orderDate = input("Please Enter the New or Same Manufacturer Order Date")
           while not validator.dateValidate(orderDate):
                orderDate = input("Please Enter the New or Same Manufacturer Order Date")
           self.__manufacturerOrderDate = orderDate

           orderPrice = input("Please Enter the New or Same Manufacturer Order Price")
           while not validator.priceValidate(orderPrice):
                orderPrice = input("Please Enter the New or Same Manufacturer Order Price")
           self.__manufacturerOrderPrice =orderPrice

           modelId = input("Please Enter the New or Same Car Model Id")
           while not validator.numberValidate(modelId):
                modelId = input("Please Enter the New or Same Car Model Id")
           self.__carModelId = modelId

           database.updateManufacturerOrderRecord(self.__manufacturerOrderId, self.__manufacturerOrderDate, self.__manufacturerOrderPrice, self.__carModelId)
           print("Manufacturer Order Record Updated Successfully")

      except:
            print("Something went wrong.!! Contact the administrator.!")


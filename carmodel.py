from db import dataBase as database
from validator import Validator as validator
validator = validator()
class carmodel:

    def __init__(self):
        self.carmodelid = 0
        self.carmodelname = ""
        self.carmodeltype = ""
        self.carmodelprice = 0
        self.camodelyear = 0
        self.mfid=0

    def searchAllCarModel(self, cursor):
        try:
            cursor.execute('SELECT cm.car_model_id,cm.car_model_name,m.manufacturer_name,cm.car_model_price,cm.car_model_type,cm.car_model_year FROM dbo.Car_Model cm inner join  Manufacturer m on cm.manufacturer_id=m.manufacturer_id')
            dash = '-' * 150
            print(dash)
            print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Id", "Car Model Name","Car Manufacturer", "Price" ,"Car Type", "Year"))
            print(dash)
            for row in cursor:
                print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], str(row[3]), str(row[4]),str(row[5])))
        except:
            ("Something went wrong.!! Contact the administrator.!")
    def searchByName(self, cursor):
         try:
            name = input("Enter name of model. !")
            args = ['%' + name + '%']

            cursor.execute('SELECT * FROM dbo.Car_Model where car_model_name like ?', args)
            dash = '-' * 150
            data = cursor.fetchall()

            if len(data) != 0:
                print(dash)
                print(
                    '{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Id", "Car Model Name", "CarType", "Price",
                                                                        "Year"))
                print(dash)
                for row in data:
                    print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1],row[2],
                                                                             str(row[4]), str(row[5])))

            else:
                print("No Car model found with that name.!")
         except:
             ("Something went wrong.!! Contact the administrator.!")


    def searchByMfg(self, cursor):
       try:
            args=input("Enter Manufacturer's name.")
            args = ['%' + args + '%']
            cursor.execute(
                'SELECT cm.car_model_id,cm.car_model_name,m.manufacturer_name,cm.car_model_price,cm.car_model_type,cm.car_model_year FROM dbo.Car_Model cm inner join  Manufacturer m on cm.manufacturer_id=m.manufacturer_id where m.manufacturer_name like ?',args)
            dash = '-' * 150
            print(dash)
            print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Id", "Car Model Name", "Car Manufacturer", "Price",
                                                                     "Car Type", "Year"))
            print(dash)
            for row in cursor:
                print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], str(row[3]),
                                                                         str(row[4]), str(row[5])))
       except:
           ("Something went wrong.!! Contact the administrator.!")

    def searchByType(self,cursor):

        try:
            args = input("Enter Car Type.")
            args = ['%' + args + '%']
            cursor.execute(
                'SELECT cm.car_model_id,cm.car_model_name,m.manufacturer_name,cm.car_model_price,cm.car_model_type,cm.car_model_year FROM dbo.Car_Model cm inner join  Manufacturer m on cm.manufacturer_id=m.manufacturer_id where cm.car_model_type like ?',
                args)
            dash = '-' * 150
            print(dash)
            print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Id", "Car Model Name", "Car Manufacturer", "Price",
                                                                     "Car Type", "Year"))
            print(dash)
            for row in cursor:
                print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], str(row[3]),
                                                                         str(row[4]), str(row[5])))
        except:
            ("Something went wrong.!! Contact the administrator.!")
    def searchByBudget(self, cursor):
       try:
            args = int(input("Enter Customer Budget Limit."))

            cursor.execute(
                'SELECT cm.car_model_id,cm.car_model_name,m.manufacturer_name,cm.car_model_price,cm.car_model_type,cm.car_model_year FROM dbo.Car_Model cm inner join  Manufacturer m on cm.manufacturer_id=m.manufacturer_id where cm.car_model_price<= ?',
                args)
            dash = '-' * 150
            print(dash)
            print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Id", "Car Model Name", "Car Manufacturer", "Price",
                                                                     "Car Type", "Year"))
            print(dash)
            for row in cursor:
                print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], str(row[3]),
                                                                         str(row[4]), str(row[5])))
       except:
           ("Something went wrong.!! Contact the administrator.!")

    def addCarModel(self, cursor):

        try:
            name = input("Enter name of manufacturer. !")
            args = ['%' + name + '%']

            cursor.execute('SELECT * FROM dbo.Manufacturer where manufacturer_name like ?', args)
            dash = '-' * 150
            data = cursor.fetchall()

            if len(data) != 0:
                print(dash)
                print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Id", "Name", "Location", "Email", "Phone-number"))
                print(dash)
                for row in data:
                    print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], row[3], row[4]))
                db = database()
                id = int(input("Enter car id from "))

                name = input("Enter car model name")

                while not validator.nameValidate(name):
                    name = input("Enter car model name")


                type = input("Enter car model type")
                while not validator.nameValidate(type):
                    type = input("Enter car model type")

                price = input("Enter car price")
                while not validator.numberValidate(price):
                    price = input("Enter car price")

                year = input("Enter car year")
                while not validator.numberValidate(year):
                    year = input("Enter car year")

                print("Enter car specification")
                color = input("Enter car color")
                engine = input("Enter engine number")
                fuel = input("Enter fuel type")
                hp = input("Enter horse power")
                zts = input("Enter zero to sixty")
                capacity = input("Enter seating capacity")
                ab = input("Airbags ? Yes or No")

                variant = "<Variant><Color>"+color+"</Color><EngineNo>"+engine+"</EngineNo><Fuel>"+fuel+"</Fuel><Power>"+hp+"</Power><ZeroToSixty>"+zts+"</ZeroToSixty><SeatingCapacity>"+capacity+"</SeatingCapacity><Airbags>"+ab+"</Airbags></Variant>"
                db.addCarModel(id, name, type, price, year, variant)

                print("Car model entered successfully!")

            else:
                print("No manufacturer found with that name.!")
        except:
            ("Something went wrong.!! Contact the administrator.!")






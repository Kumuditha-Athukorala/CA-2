from db import dataBase as database

class carmodel:

    def __init__(self):
        self.carmodelid = 0
        self.carmodelname = ""
        self.carmodeltype = ""
        self.carmodelprice = 0
        self.camodelyear = 0
        self.mfid=0

    def searchAllCarModel(self, cursor):
        cursor.execute('SELECT cm.car_model_id,cm.car_model_name,m.manufacturer_name,cm.car_model_price,cm.car_model_type,cm.car_model_year FROM dbo.Car_Model cm inner join  Manufacturer m on cm.manufacturer_id=m.manufacturer_id')
        dash = '-' * 150
        print(dash)
        print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Id", "Car Model Name","Car Manufacturer", "Price" ,"Car Type", "Year"))
        print(dash)
        for row in cursor:
            print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], str(row[3]), str(row[4]),str(row[5])))

    def searchByName(self, cursor):

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

    def searchByMfg(self, cursor):

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

    def searchByType(self,cursor):

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
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
        print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Id", "Car Model Name","Car Manufactuerer", "Price" ,"Car Type", "Year"))
        print(dash)
        for row in cursor:
            print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], str(row[3]), str(row[4]),str(row[5])))
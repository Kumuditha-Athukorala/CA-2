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
        cursor.execute('SELECT * FROM dbo.Car_Model')
        dash = '-' * 150
        print(dash)
        print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Id", "Name", "Car Type", "Price", "Year"))
        print(dash)
        for row in cursor:
            print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], row[4], row[5]))
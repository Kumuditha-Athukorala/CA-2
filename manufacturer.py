import pyodbc
class manufacturer:

    def __init__(self):
        self.manufacturerId = ""
        self.manufacturerName = ""
        self.manufacturerAddr = ""
        self.manufacturerEmail = ""
        self.manufacturerPhno = ""
    def selectAllManufacturers(self,cursor):

        cursor.execute('SELECT * FROM dbo.Manufacturer')
        dash = '-' * 150
        print(dash)
        print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Id","Name","Location","Email","phonenumber"))
        print(dash)
        for row in cursor:
          #  print(str(row[0])+"      "+row[1]+"          "+row[2]+"            "+row[3]+"                " +row[4])
          #  print("%-15s%s %30s%20s" % (' '.join((str(row[0]), row[1])), row[2], row[3], row[4]))
            print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], row[3],row[4]))
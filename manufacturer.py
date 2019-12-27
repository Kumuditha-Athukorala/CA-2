import pyodbc
class manufacturer:

    def __init__(self):
        self.manufacturerId = ""
        self.manufacturerName = ""
        self.manufacturerAddr = ""
        self.manufacturerEmail = ""
        self.manufacturerPhno = ""

    def selectAllManufacturers (self, cursor):

        cursor.execute('SELECT * FROM dbo.Manufacturer')
        dash = '-' * 150
        print(dash)
        print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}'.format("Id", "Name", "Location", "Email", "phonenumber"))
        print(dash)
        for row in cursor:
            print('{:<5s}{:>30s}{:>30s}{:>30s}{:>30s}'.format(str(row[0]), row[1], row[2], row[3], row[4]))

    def selectBasedOnName(self, cursor):
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
        else:
            print("No manufacturer found with that name.!")

    def addManufacturer(self, cursor):

        self.manufacturerName = input("Enter name of manufacturer.")
        self.manufacturerAddr = input("Enter manufacturer address.")
        self.manufacturerEmail = input("Enter manufacturer email.")
        self.manufacturerPhno = input("Enter manufacturer contact number.")
        cursor.execute('insert into dbo.manufacturer (manufacturer_id,manufacturer_name,manufacturer_address,'
                       'manufacturer_email,manufacturer_phone) values (next value for dbo.SEQ_MANUFACTURER_ID,?,?,?,?) ',self.manufacturerName,
                       self.manufacturerAddr, self.manufacturerEmail, self.manufacturerPhno)
        print(cursor.rowcount, "Record inserted successfully into Manufacturer table")



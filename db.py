import pyodbc

class dataBase:

    def __init__(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=HP\\SQLEXPRESS;'
                              'Database=Over_Drive;'
                              'Trusted_Connection=yes;'
                              )

    def dbConn(self):
           cursor=self.conn.cursor()
           return cursor;


    def insertMf(self, name, addr, eid, phone,id):

        with self.conn as cursor:
            cursor.execute('insert into dbo.manufacturer (manufacturer_id,manufacturer_name,manufacturer_address,'
                       'manufacturer_email,manufacturer_phone) values (next value for dbo.SEQ_MANUFACTURER_ID,?,?,?,?) ',name,
                       addr, eid, phone)

    def updateMf(self, name, addr, eid, phone,id):
        with self.conn as cursor:
            cursor.execute('update dbo.manufacturer set manufacturer_name=?,manufacturer_address=?,'
                           'manufacturer_email=?,manufacturer_phone=? where manufacturer_id=? ',
                           name,
                           addr, eid, phone,id)



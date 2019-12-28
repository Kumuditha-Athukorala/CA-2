import pyodbc

class dataBase:

    def __init__(self):
        print("Inside dbConnect")
        self.conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=LAPTOP-164KM9F1\SQLEXPRESSKUMA;'
                              'Database=Over_Drive;'
                              'Trusted_Connection=yes;')
    def dbConn(self):

        cursor = self.conn.cursor()
        return cursor;


    def insertCustomerRecord(self, name, address, phoneNumber):
        with self.conn as cursor:
            sql = 'INSERT INTO dbo.Customer (customer_id,customer_name,customer_address,customer_phone) ' \
                  'VALUES (CONCAT(\'OVDC\',NEXT VALUE FOR SEQ_CUSTOMER_ID),?,?,?)'
            cursor.execute(sql, name, address, phoneNumber)

    def updateCustomerRecord(self, id,name, address, phoneNumber):
        with self.conn as cursor:
            cursor.execute('UPDATE dbo.Customer SET customer_name=?,customer_address=?,'
                           'customer_phone=? WHERE customer_id=? ',
                           name, address, phoneNumber, id)
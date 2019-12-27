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


    def insertCustomerRecord(self,name, address, phoneNumber):
        with self.conn as cursor:
            cursor.execute('INSERT INTO dbo.Customer (customer_id,customer_name,customer_address,customer_phone)'
                           ' VALUES (CONCAT(\'OVDC\',NEXT VALUE FOR SEQ_CUSTOMER_ID),?,?,?) ',
                           name, address, phoneNumber)

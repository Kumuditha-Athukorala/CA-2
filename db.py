import pyodbc

class dataBase:

    def __init__(self):
        print("Inside dbConnect")
        self.conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=HP\\SQLEXPRESS;'
                              'Database=Over_Drive;'
                              'Trusted_Connection=yes;')
    def dbConn(self):

        cursor = self.conn.cursor()
        return cursor;
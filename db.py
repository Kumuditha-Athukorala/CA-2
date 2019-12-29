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
            sql = 'UPDATE dbo.Customer SET customer_name=?,customer_address=?, ' \
                  'customer_phone=? WHERE customer_id=? ';
            cursor.execute(sql, name, address, phoneNumber, id)

    def insertCustomerOrderRecord(self, orderDate, deliveryDate, sellingPrice, customerId, employeeId):
        with self.conn as cursor:
            sql = 'INSERT INTO dbo.Customer_Order (customer_order_id,customer_order_date,customer_order_delivery_date,' \
                  'customer_order_selling_price,' \
                  'customer_id,employee_id) VALUES (NEXT VALUE FOR SEQ_CUSTOMER_ORDER_ID,?,?,?,?,?)'
            cursor.execute(sql, orderDate, deliveryDate, sellingPrice, customerId, employeeId)

    def updateCustomerOrderRecord(self, orderId, orderDate, deliveryDate, sellingPrice, customerId, employeeId):
        with self.conn as cursor:
            sql = 'UPDATE dbo.Customer_Order SET customer_order_date=?,customer_order_delivery_date=?, ' \
                  'customer_order_selling_price=?, customer_id=?, employee_id=?  WHERE customer_order_id=? ';
            cursor.execute(sql, orderDate, deliveryDate, sellingPrice, customerId, employeeId, orderId)

    def insertInventoryrecord(self, date, status,manufacturerOrder, customerOrder):
        with self.conn as cursor:
            sql = 'INSERT INTO dbo.Inventory (inventory_id, inventory_date, inventory_status,' \
                  'manufacturer_order_id, customer_order_id) VALUES (NEXT VALUE FOR SEQ_INVENTORY_ID,?,?,?,?)'
            cursor.execute(sql, date, status, manufacturerOrder, customerOrder)
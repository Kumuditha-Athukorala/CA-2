import pyodbc

class dataBase:

    def __init__(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=LAPTOP-164KM9F1\SQLEXPRESSKUMA;'
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

    def insertEmp(self, name, desig, dob, pps, salary):
        with self.conn as cursor:
            cursor.execute('insert into dbo.Employee (employee_id,employee_name,employee_designation,'
                           'employee_dob,employee_pps_number,employee_salary) values (concat(\'OVDE\',(next value for dbo.SEQ_EMPLOYEE_ID)),?,?,?,?,?) ',
                           name,
                           desig, dob, pps,salary)

    def updateEmp(self, name, desig, dob, pps,salary,id):
        with self.conn as cursor:
            cursor.execute('update dbo.Employee set employee_name=?,employee_designation=?,'
                           'employee_dob=?,employee_pps_number=?,employee_salary=? where employee_id=? ',
                           name,
                           desig, dob, pps,salary,id)

    def insertIncentive(self, id, date):

        with self.conn as cursor:
            cursor.execute('insert into dbo.Incentive (incentive_id,incentive_date,'
                           'employee_id) values (next value for dbo.SEQ_INCENTIVE_ID,?,?) ',
                           date, id)

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

    def updateInventoryRecord(self, id, date, status,manufacturerOrder, customerOrder):
        with self.conn as cursor:
            sql = 'UPDATE dbo.Inventory SET inventory_date=?,inventory_status=?, ' \
                  'manufacturer_order_id=?, customer_order_id=? WHERE inventory_id=? ';
            cursor.execute(sql, date, status, manufacturerOrder, customerOrder, id)


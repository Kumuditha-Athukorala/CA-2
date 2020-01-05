import pyodbc


class dataBase:

    def __init__(self):
        try:
            self.conn = pyodbc.connect('Driver={SQL Server};'
                             'Server=HP\\SQLEXPRESS;'
                              'Database=Over_Drive;'
                              'Trusted_Connection=yes;'
                              )
        except:
            ("Something went wrong in database connection.!! Contact the administrator.!")

    def dbConn(self):
        try:
           cursor=self.conn.cursor()
           return cursor;
        except:
            ("Something went wrong in database connection.!! Contact the administrator.!")


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

    def insertEmp(self, name, desig, dob, pps, salary,address):
        with self.conn as cursor:
            cursor.execute('insert into dbo.Employee (employee_id,employee_name,employee_designation,'
                           'employee_dob,employee_pps_number,employee_salary,employee_address) values (concat(\'OVDE\',(next value for dbo.SEQ_EMPLOYEE_ID)),?,?,?,?,?,?) ',
                           name,
                           desig, dob, pps,salary,address)

    def updateEmp(self, name, desig, dob, pps,salary,id,add):
        with self.conn as cursor:
            cursor.execute('update dbo.Employee set employee_name=?,employee_designation=?,'
                           'employee_dob=?,employee_pps_number=?,employee_salary=?,employee_address=? where employee_id=? ',
                           name,
                           desig, dob, pps,salary,add,id)

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
                  'customer_phone=? WHERE customer_id=? '
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

        db = dataBase()
        if(db.OR(customerOrder)):
            customerOrder = None

        with self.conn as cursor:
            sql = 'INSERT INTO dbo.Inventory (inventory_id, inventory_date, inventory_status,' \
                  'manufacturer_order_id, customer_order_id) VALUES (NEXT VALUE FOR SEQ_INVENTORY_ID,?,?,?,?)'
            cursor.execute(sql, date, status, manufacturerOrder, customerOrder)

    def OR(self,param):
        if '' == param:
            return True
        elif 'null' == param:
            return True
        elif 'NULL' == param:
            return True
        else:
            return False

    def updateInventoryRecord(self, id, date, status,manufacturerOrder, customerOrder):
        with self.conn as cursor:
            sql = 'UPDATE dbo.Inventory SET inventory_date=?,inventory_status=?, ' \
                  'manufacturer_order_id=?, customer_order_id=? WHERE inventory_id=? ';
            cursor.execute(sql, date, status, manufacturerOrder, customerOrder, id)


    def addCarModel(self, id, name, type, price, year, variant):
        print(variant)
        with self.conn as cursor:
            cursor.execute('insert into dbo.car_model (car_model_id,car_model_name,car_model_type,'
                           'car_model_price,car_model_year,manufacturer_id,car_model_variant) values (next value for dbo.SEQ_CAR_MODEL_ID,?,?,?,?,?,?)',
                           name, type, price, year, id, variant)


    def insertManufacturerOrderRecord(self, date, price, modelId):
        with self.conn as cursor:
            sql = 'INSERT INTO dbo.Manufacturer_Order (manufacturer_order_id, manufacturer_order_date, manufacturer_order_price, car_model_id)' \
                  ' VALUES (NEXT VALUE FOR SEQ_MANUFACTURER_ORDER_ID,?,?,?)'
            cursor.execute(sql, date, price, modelId)


    def updateManufacturerOrderRecord(self,id, date, price, modelId):
        with self.conn as cursor:
            sql = 'UPDATE dbo.Manufacturer_Order SET manufacturer_order_date=?,manufacturer_order_price=?, ' \
                  'car_model_id=? WHERE manufacturer_order_id=? '
            cursor.execute(sql, date, price, modelId, id)



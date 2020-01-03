import pyodbc
from customer import Customer
from employee import employee

class report:
    def __init__(self):
        self.__inventoryId = ""
        self.__inventoryDate = ""
        self.__inventoryStatus = ""
        self.__manufacturerOrderId = ""
        self.__customerOrderId = ""
        self.__employeeId = ""
        self.__employeeName = ""
        self.__totalSales = ""
        self.__customerId=""
        self.__street=""

    def employeePerformance(self,cursor):

        limit= int(input("Enter limit above which total sales achieved by employees:"))
        cursor.execute("{CALL uspEmployee_Performance (?)}", limit)
        dash = '-' * 100
        print(dash)
        print('{:<5s}{:>30s}{:>60s}'.format("Employee Id", "Name", "Total Sales"))
        print(dash)
        for row in cursor:
            print('{:<5s}{:>30s}{:>60s}'.format(str(row[0]), row[1], str(row[2])))

    def searchBySeats(self, cursor):

        limit = int(input("Enter number of seats in car:"))
        cursor.execute("{CALL uspCarSeats (?)}", limit)
        dash = '-' * 100

        data = cursor.fetchall()

        if len(data) != 0:
            print(dash)
            print('{:<15s}{:>30s}{:>30s}'.format("Model Name", "Model Type", "Model Price", "Year"))
            print(dash)
            for row in data:
                print('{:<15s}{:>30s}{:>30s}'.format(row[1], row[2], str(row[4]), str(row[5])))
        else:
            print("No such car model found")


    def getCustomerSpecificOrders(self,cursor):

        customer = Customer()
        customer.searchAllCustomers(cursor)

        self.__customerId = input("Please Enter the Customer Id")

        sql = "EXEC uspCustomer_Order_Details_with_Id ?"
        cursor.execute(sql,self.__customerId)
        dash = '-' * 250
        print(dash)
        print('{:<5s}{:>30s}{:>60s}{:>60s}{:>60s}{:>60s}{:>60s}{:>60s}'.format("Customer Id", "Customer Name",
                        "Address","Phone Number", "Order Id","Order Date", "Delivery Date","Selling Price"))
        print(dash)
        for row in cursor:
            print('{:<5s}{:>30s}{:>60s}{:>60s}{:>60s}{:>60s}{:>60s}{:>60s}'.format(str(row[0]), row[1], row[2] , row[3],
                    str(row[4]), row[5], row[6],str(row[7])))


    def updateEmployeeAddress(self, cursor):

        emp = employee()
        emp.selectAllEmployees(cursor)

        self.__employeeId = input("Please Enter the Employee Id")
        self.__street = input("Please Enter the Same or New Sreet Name")

        cursor.execute("{CALL uspUpdate_Emplyee_Address (?,?)}", self.__employeeId, self.__street)
        cursor.execute("SELECT e.employee_id,e.employee_name,e.employee_address FROM Employee e WHERE e.employee_id = ?",self.__employeeId)
        dash = '-' * 200
        print(dash)
        print('{:<5s}{:>30s}{:>30s}'.format("Employee ID","Employee Name","Employee Address"))
        print(dash)
        for row in cursor:
            print('{:<5s}{:>30s}{:>80s}'.format(str(row[0]), row[1], row[2]))

    def getAvailableCars(self, cursor):

        sql = 'SELECT i.inventory_id, i.inventory_date, i.inventory_status, mo.manufacturer_order_price,cm.car_model_name,' \
              'm.manufacturer_name FROM Inventory i ' \
              'INNER JOIN Manufacturer_Order mo ON i.manufacturer_order_id = mo.manufacturer_order_id ' \
              'INNER JOIN Car_Model cm ON mo.car_model_id = cm.car_model_id ' \
              'INNER JOIN Manufacturer m ON cm.manufacturer_id = m.manufacturer_id ' \
              'WHERE i.inventory_status = \'AVAILABLE\''

        cursor.execute(sql)
        dash = '-' * 200
        print(dash)
        print('{:<5s}{:>30s}{:>60s}{:>30s}{:>30s}{:>30s}'.format("Inventory Id", "Inventory Date", "Inventory Status",
                                                                 "Manufacturer Order Price", "Model Name",
                                                                 "Manufacturer Name"))
        print(dash)
        for row in cursor:
            print('{:<5s}{:>30s}{:>60s}{:>30s}{:>36s}{:>28s}'.format(str(row[0]), row[1], row[2], str(row[3]), row[4], row[5]))


    def getSoldCars(self,cursor):

        sql = 'SELECT i.inventory_id, i.inventory_date, i.inventory_status, mo.manufacturer_order_price,cm.car_model_name,' \
              'm.manufacturer_name FROM Inventory i ' \
              'INNER JOIN Manufacturer_Order mo ON i.manufacturer_order_id = mo.manufacturer_order_id ' \
              'INNER JOIN Car_Model cm ON mo.car_model_id = cm.car_model_id ' \
              'INNER JOIN Manufacturer m ON cm.manufacturer_id = m.manufacturer_id ' \
              'WHERE i.inventory_status = \'SOLD\''

        cursor.execute(sql)
        dash = '-' * 200
        print(dash)
        print('{:<5s}{:>30s}{:>60s}{:>30s}{:>30s}{:>30s}'.format("Inventory Id", "Inventory Date", "Inventory Status",
                                                                 "Manufacturer Order Price", "Model Name",
                                                                 "Manufacturer Name"))
        print(dash)
        for row in cursor:
            print('{:<5s}{:>30s}{:>60s}{:>30s}{:>36s}{:>28s}'.format(str(row[0]), row[1], row[2], str(row[3]), row[4], row[5]))
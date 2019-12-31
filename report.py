import pyodbc
from customer import Customer
from employee import employee

class report:
    def __init__(self):
        self.__inventoryId=""
        self.__inventoryDate=""
        self.__inventoryStatus=""
        self.__manufacturerOrderId=""
        self.__customerOrderId=""
        self.__customerId=""
        self.__employeeId=""
        self.__street=""


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

        cursor.execute("{CALL uspUpdate_Emplyee_Address (?,?)}", self.__customerId, self.__street)
        cursor.execute("SELECT e.employee_id,e.employee_name,e.employee_address FROM Employee e WHERE e.employee_id = ?",self.__employeeId)
        dash = '-' * 250
        print(dash)
        print('{:<5s}{:>30s}{:>60s}'.format("Employee ID","Employee Name","Employee Address"))
        print(dash)
        for row in cursor:
            print('{:<5s}{:>30s}{:>60s}'.format(str(row[0]), row[1], row[2]))
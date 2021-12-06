# Author Name: Bijan Amirzadehasl
# Date: 11/1/2021
# Program Name: Amirzadehasl_ProdWorker.py
# Purpose: Create an Employee class. Create a production worker class that inherits from employee class.
# Prompts the user to fill data for prod worker class and use get methods to display the data

# Employee class
class Employee:
    def __init__(self, employee_name, employee_num):
        self.__employee_name = employee_name
        self.__employee_num = employee_num

    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    def get_employee_name(self):
        return self.__employee_name

    def set_employee_num(self, employee_num):
        self.__employee_num = employee_num

    def get_employee_num(self):
        return self.__employee_num


class ProductionWorker(Employee):
    def __init__(self, employee_name, employee_num, shift_num, pay_rate):
        Employee.__init__(self, employee_name, employee_num)

        self.__shift_num = shift_num

        self.__pay_rate = pay_rate

    def set_shift_num(self, shift_num):
        self.__shift_num = shift_num

    def get_shift_num(self):
        return self.__shift_num

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    def get_pay_rate(self):
        return self.__pay_rate


def main():
    emp_name = input('Enter the Employees name: ')
    emp_num = int(input('Enter the Employees number: '))
    emp_shift = int(input('Enter the Employees shift number (it must be 1 for day shift or 2 for night shift): '))
    while emp_shift != 1 and emp_shift != 2:
        emp_shift = int(input('Please re-enter a value of 1 for day shift or 2 for night shift.'))

    emp_pay = float(input('Enter the Employees pay rate: '))

    pw = ProductionWorker(emp_name, emp_num, emp_shift, emp_pay)

    aShift = ""
    if (pw.get_shift_num() == 1):
        aShift = "Day Shift"
    elif (pw.get_shift_num() == 2):
        aShift = "Night Shift"

    print("{:<19} {:<19} {:<12} {:<12}".format('Employee Name', 'Employee Number', 'Shift', 'Pay Rate'))
    print("{:<19} {:<19} {:<12} {:<12}".format(pw.get_employee_name(), pw.get_employee_num(), aShift, pw.get_pay_rate()))


main()

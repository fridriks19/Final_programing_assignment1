from repo.class_EmployeeRepository import EmployeeRepository

class Employee_service():
    def __init__(self):
        self.__employee_repo = EmployeeRepository()

    def add_employee(self, empl_str):
        self.empl_str = empl_str
        if self.is_valid_employee(self.empl_str):
            self.__employee_repo.add_employee(self.empl_str)

    def is_valid_employee(self, empl_str):
        #ssn
        #gsm
        #nafn  numbers
        #
        return True

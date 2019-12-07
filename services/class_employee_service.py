from repo.class_EmployeeRepository import EmployeeRepository

class Employee_service():
    def __init__(self):
        self.__employee_repo = EmployeeRepository()

    def add_employee(self, empl_str):
        self.empl_str = empl_str
        if self.is_valid_employee(self.empl_str):
            self.__employee_repo.add_employee(self.empl_str)

    def change_employee(self, choice, change, ssn): #Change er breytan og choice er nr á því sem á að breyta 
        self.choice = choice
        self.change = change
        self.ssn = ssn
        if self.is_valid_employee_change(self.choice, self.change):
            empl_change = self.__employee_repo.change_employee(self.choice, self.change, self.ssn)
            return empl_change

    def get_employee(self, ssn):
        self.ssn = ssn
        if self.is_valid_employee(self.ssn):
            empl_info = self.__employee_repo.get_employee(self.ssn)
            return empl_info
        

    def is_valid_employee_change(self, choice, change):
        return True

    def is_valid_employee(self, empl_str):
        #ssn
        #gsm
        #nafn  numbers
        #
        return True

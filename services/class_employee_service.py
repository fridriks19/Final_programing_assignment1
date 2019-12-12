from repo.class_EmployeeRepository import EmployeeRepository
from models.class_employee import Employee

class Employee_service():
    def __init__(self):
        self.__employee_repo = EmployeeRepository()
        self.empl_list = self.__employee_repo.get_allemployees_list()

    def add_employee(self, empl_str):
        self.empl_str = empl_str
        if self.is_valid_employee(self.empl_str):
            self.__employee_repo.add_employee(self.empl_str)
        else:
            return False
            # print("Upplýsingar ekki gildar fyrir starfsmann")
            # print("Passaðu að allar upplýsingar séu rétt skráðar")
            # print("Starfsmaður ekki vistaður")

    def change_employee(self, choice, change, ssn): #"Change" is the variable and "choice" is the number of which thing to change.
        self.choice = choice
        self.change = change
        self.ssn = ssn
        empl_change = self.__employee_repo.write_change_employee(self.choice, self.change, self.ssn)
        return empl_change

    def get_pilots(self):
        """Get a list of all the pilots and print out their SSN, names, roles and ranks"""
        return_str = ""
        empl_list = self.__employee_repo.get_allemployees_list()
        for empl in empl_list:  
            output = Employee(empl)
            if empl[2] == "Pilot":
                return_str += "{}: {}, {}, {} \n".format(output.get_ssn(),output.get_name(),output.get_role(), output.get_rank())
        return return_str
    
    def get_flightattendants(self):
        """Get a list of all the flight attendants and print out their SSN, names, roles and ranks"""
        return_str = ""
        empl_list = self.__employee_repo.get_allemployees_list()
        for empl in empl_list:   
            output = Employee(empl)
            if empl[2] == "Cabincrew":
                return_str += "{}: {}, {}, {} \n".format(output.get_ssn(),output.get_name(),output.get_role(), output.get_rank())
        return return_str

    def get_employee(self, ssn):
        self.ssn = ssn
        empl_list = self.__employee_repo.get_allemployees_list()
        for empl in empl_list:
            if empl[0] == self.ssn:
                return empl
        return False
    
    def get_allemployees(self):
        return self.__employee_repo.get_allemployees()

    def get_allemployees_list(self):
        return self.__employee_repo.get_allemployees_list()

    def is_valid_employee(self, empl_str):
        listed_info = empl_str.split(",")
        is_valid_ssn = False
        is_valid_name = False
        for item in listed_info:
            if listed_info[0].isdigit():
                if len(listed_info[0]) == 10:
                    is_valid_ssn = True
            else:
                is_valid_ssn = False

        for letter in listed_info[1]:
            if letter.isdigit():
                
                return False
            else:
                is_valid_name = True
        if is_valid_ssn == True and is_valid_name == True:
            return True
        else:
            print("Kennitala þarf að innihalda 10 tölustafi!")
            print("Það geta ekki verið tölur í nafni!")
            return False

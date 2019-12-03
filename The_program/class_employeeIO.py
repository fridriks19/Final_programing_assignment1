<<<<<<< HEAD:The_program/klasistarfsmadurIO.py
empl_str = "1103647756,Wilma Horne,Cabincrew,Flight Attendant,N/A,Fellsmúli 25,8998825"
=======
from class_employee import employee
from class_pilot import pilot


empl_str = "111111-4189,Ekki Eggert Orri Hermannsson,Pilot,Main-Pilot,Jumbo999,Funalind,865-8996"
>>>>>>> 8ac353a2232c5c2d80021f7974522c3a8255a294:The_program/class_employeeIO.py

class employeeIO:
    def __init__(self, empl_str):
        self.empl_str = empl_str
    
    def save_employee(self):
        open_file = open("crew2.csv", "a")
        open_file.write(self.empl_str + "\n")
        open_file.close()
        return "Starfsmaður vistaður"

    def load_employee(self):
        open_file = open("crew2.csv", "r")
        open_file_list = []
        for line in open_file:
            line = line.split("\n")
            open_file_list.append(line)
        for employee in open_file_list:
            employee.pop(1)
            employee = ",".join(employee)
            if employee == self.empl_str:
                open_file.close()
                return employee
            return "Starfsmaður fannst ekki"

<<<<<<< HEAD:The_program/klasistarfsmadurIO.py
s1 = StarfsmadurIO(empl_str)
print(s1.load_employee())
=======
S1 = employeeIO(empl_str)
print(S1.load_employee())
>>>>>>> 8ac353a2232c5c2d80021f7974522c3a8255a294:The_program/class_employeeIO.py

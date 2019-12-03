from class_employee import employee
from class_flight_attendant import employee


empl_str = "111111-4189,Ekki Eggert Orri Hermannsson,Pilot,Main-Pilot,Jumbo999,Funalind,865-8996"

class StarfsmadurIO:
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

S1 = StarfsmadurIO(empl_str)
print(S1.load_employee())

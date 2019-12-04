empl_str = "1103647756,Wilma Horne,Cabincrew,Flight Attendant,N/A,Fellsmúli 25,8998825"

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

s1 = employeeIO(empl_str)
print(s1.load_employee())

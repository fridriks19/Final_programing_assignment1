from models.class_employee import Employee


class EmployeeRepository:
    def __init__(self, empl_str =""):
        self.empl_str = empl_str
    
    def add_employee(self, new_empl):
        self.new_empl = new_empl
        open_file = open("./data/crew2.csv", "a")
        open_file.write(self.new_empl + "\n")
        open_file.close()
        return "Starfsmaður vistaður"

    def get_employee(self):
        open_file = open("./data/crew2.csv", "r")
        open_file_list = []
        for line in open_file:
            line = line.strip()
            line = line.split(",")
            open_file_list.append(line)
        for employee in open_file_list:
            if employee[0] == self.empl_str:
                open_file.close()
                return employee
        open_file.close()
        return "Starfsmaður fannst ekki"
    
    def get_allemployees(self):
        return_str  = ""
        open_file = open("./data/crew2.csv", "r")
        open_file_list = []
        for line in open_file:
            line = line.strip()
            line = line.split(",")
            output = Employee(line)  
            open_file_list.append(line)
            return_str +=  "{}: {}, {} \n".format(output.get_ssn(),output.get_name(),output.get_role())
        return return_str

    def change_employee(self, choice, change, name): 
        crew_dictionary = {}
        new_file = ""
        open_file = open("./data/crew2.csv" , "r")
        for line in open_file:
            line = line.split(",")
            crew_dictionary[line[1]] = line    # Make the name the key and the values the rest of line
        
        crew_dictionary[name][choice] = change
        for key in crew_dictionary.keys():  # Go through all the values so we can add them to a new string 
            new_file += ",".join(crew_dictionary[key])  
        open_file = open("./data/crew2.csv", "w")  #We replace the old crew file with the new file 
        open_file.write(new_file)
        open_file.close()
        return "Upplýsingum breytt"
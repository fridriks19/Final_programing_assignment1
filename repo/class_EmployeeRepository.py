from models.class_employee import Employee


class EmployeeRepository:
    def __init__(self, empl_str =""):
        self.empl_str = empl_str
    
    def add_employee(self, new_empl):
        """Appends an incoming string with employee information to the existing employee list"""
        self.new_empl = new_empl
        open_file = open("./data/crew2.csv", "a")
        open_file.write(self.new_empl + "\n")
        open_file.close()
        return "Starfsmaður vistaður"
                
    def get_allemployees(self):
        """Get a list of all the employees and print out there, SSN, names and roles"""
        return_str  = ""
        open_file = open("./data/crew2.csv", "r")
        open_file_list = []
        for line in open_file:
            line = line.strip()
            line = line.split(",")
            output = Employee(line)  
            open_file_list.append(line)
            return_str +=  "{}: {}, {} \n".format(output.get_ssn(),output.get_name(),output.get_role())
        open_file.close()  
        return return_str
    
    def get_allemployees_list(self):
        """Returns a list with all employees from the employee file"""
        open_file = open("./data/crew2.csv", "r")
        empl_list = []
        for line in open_file:
            line = line.strip()
            line = line.split(",")
            empl_list.append(line)
        open_file.close()
        return empl_list[1:]

    def write_change_employee(self, choice, change, ssn): 
        """ Find a employee to change his information by using his/hers SSN"""
        crew_dictionary = {}
        new_file = ""
        open_file = open("./data/crew2.csv" , "r")
        for line in open_file:
            line = line.split(",")
            ssn_key = Employee(line)  
            crew_dictionary[ssn_key.get_ssn()] = line # make the name the key and the values the rest of line
        
        crew_dictionary[ssn][int(choice)+1] = change #Find the specific employee that we are going to change, and change "choice" to "change"
        for key in crew_dictionary.keys():  # go through all the values so we can add them to a new string 
            new_file += ",".join(crew_dictionary[key])  
        open_file = open("./data/crew2.csv", "w")  #We replace the old crew file with the new file 
        open_file.write(new_file)
        open_file.close()
        return "Upplýsingum breytt"

from models.class_employee import Employee


class EmployeeRepository:
    def __init__(self, empl_str =""):
        self.empl_str = empl_str
        self.open_file = open("./data/crew2.csv", "r")
        self.empl_list = []
        for line in self.open_file:
            line = line.strip()
            line = line.split(",")
           # output = Employee(line)  #Svo við getum sótt réttar staðsetningar úr model clasanum 
            self.empl_list.append(line)
        
    
    def add_employee(self, new_empl):
        self.new_empl = new_empl
        open_file = open("./data/crew2.csv", "a")
        open_file.write(self.new_empl + "\n")
        open_file.close()
        return "Starfsmaður vistaður"

    def get_employee(self,fnd_empl_ssn = ""):
        """Find a specific employee by using his/hers SSN""" 

        self.fnd_empl_ssn = fnd_empl_ssn
        open_file = open("./data/crew2.csv", "r")
        open_file_list = []
        for line in open_file:
            line = line.strip()
            line = line.split(",")
            #output = Employee(line)  #Svo við getum sótt réttar staðsetningar úr model clasanum
            open_file_list.append(line)
        for employee in open_file_list[1:]:
            if employee[0] == self.fnd_empl_ssn:
                open_file.close()
                return employee
        return False
                
    def get_pilots(self):
     """Get a list of all the pilots and print out there SSN, names, roles and ranks"""

        return_str  = ""
        open_file = open("./data/crew2.csv", "r")
        open_file_list = []
        for line in open_file:
            line = line.strip()
            line = line.split(",") 
            open_file_list.append(line)  
        for pilot in open_file_list:   
            output = Employee(pilot)
            if pilot[2] == "Pilot":
                return_str += "{}: {}, {}, {} \n".format(output.get_ssn(),output.get_name(),output.get_role(), output.get_rank())
        open_file.close()
        return return_str

    def get_flightattendants(self):
        """Get a list of all the flight attendants and print out there SSN, names, roles and ranks"""

        return_str  = ""
        open_file = open("./data/crew2.csv", "r")
        open_file_list = []
        for line in open_file:
            line = line.strip()
            line = line.split(",") 
            open_file_list.append(line)  
        for pilot in open_file_list:   
            output = Employee(pilot)
            if pilot[2] == "Cabincrew":
                return_str += "{}: {}, {}, {} \n".format(output.get_ssn(),output.get_name(),output.get_role(), output.get_rank())
        open_file.close()
        return return_str

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
        return self.empl_list[1:]

    def change_employee(self, choice, change, ssn): 
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

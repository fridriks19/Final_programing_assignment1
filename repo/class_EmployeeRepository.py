from models.class_employee import Employee
#from models.class_employee import Employee
#from class_pilot import pilot

#empl_str = "111111-4189"
#empl_str = "1111114189","Ekki Eggert Orri Hermannsson","Pilot","Main-Pilot","Jumbo999","Funalind","865-8996"
# fnd_empl_ssn = "1600904199"#1600904199

class EmployeeRepository:
    def __init__(self, empl_str =""):
        self.empl_str = empl_str
        
    
    def add_employee(self, new_empl):
        self.new_empl = new_empl
        open_file = open("./data/crew2.csv", "a")
        open_file.write(self.new_empl + "\n")
        open_file.close()
        return "Starfsmaður vistaður"

    def get_employee(self,fnd_empl_ssn = ""):
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
        else:
            return False
                
    def get_allemployees(self):
        return_str  = ""
        open_file = open("./data/crew2.csv", "r")
        open_file_list = []
        for line in open_file:
            line = line.strip()
            line = line.split(",")
            output = Employee(line)  #Svo við getum sótt réttar staðsetningar úr model clasanum 
            open_file_list.append(line) # ÞARF ÞETTA ??????????
            return_str +=  "{}: {}, {} \n".format(output.get_ssn(),output.get_name(),output.get_role())
            open_file.close()
        return return_str

    def change_employee(self, choice, change, ssn): 
        crew_dictionary = {}
        new_file = ""
        open_file = open("./data/crew2.csv" , "r")
        for line in open_file:
            line = line.split(",")
            ssn_key = Employee(line)  
            crew_dictionary[ssn_key.get_ssn()] = line    # make the name the key and the values the rest of line, gerum 
        
        crew_dictionary[ssn][int(choice)] = change #Finna starfsmanninn sem á að breyta og breyta því sem var valið í choice í change
        for key in crew_dictionary.keys():  # go through all the values so we can add them to a new string 
            new_file += ",".join(crew_dictionary[key])  
        open_file = open("./data/crew2.csv", "w")  #We replace the old crew file with the new file 
        open_file.write(new_file)
        open_file.close()
        return "Upplýsingum breytt"
        

    

# change = "Ananas"  # breytingin
# choice = 5   # hverju á að breyta 
# name = "Ekki Eggert Orri Hermannsson"  

# S1 = EmployeeRepository()
#print(S1.add_employee(empl_str))
# print(S1.get_employee(fnd_empl_ssn))
#print(S1.change_employee(choice, change, name))
#s1 = EmployeeRepository()
#print(s1.get_allemployees())
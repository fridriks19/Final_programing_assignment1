
class Make_change():
    
    def __init__(self, dictionary, choice, name):
        self.__dictionary = dictionary
        self.__choice = choice
        self.__name = name 
        

    def change_crew(self, dictionary, choice, name):
        self.change = self.__choice
        self.placement = ""
   
        if self.__choice == "1":
            self.placement = 2   
            self.attribute = "role"
        elif self.__choice == "2":
            self.placement = 3
            self.attribute = "rank"
        elif self.__choice == "3":
            self.placement = 4
            self.attribute = "liscense"
        elif self.__choice == "4":
            self.placement = 5
            self.attribute = "address" 
        elif self.__choice == "5":
            self.placement = 6
            self.attribute = "phonenumber" 

        self.change = input("Change {}: ".format(self.attribute))
        if self.change != "r":
            self.save = input("Do you whant to self.save the changes?: (y/n)")
            if self.save == "y":
                self.__dictionary[self.__name][self.placement] = self.change
            else:
                return None

    def __str__(self):
        return str(self.__dictionary)

def open_file(filename):
    crew_dictionary = {}
    f = open(filename , "r")
    for line in f:
        line = line.split(",")
        crew_dictionary[line[1]] = line
    return crew_dictionary

user_choice_input = input("Choose bruv: ")
def main():
    filename = "Crew.csv"
    employee_name_input ='Virginia Ho'
    crew_dictionary = open_file(filename)
    change = Make_change(crew_dictionary, user_choice_input, employee_name_input)
    
    print(change)
    # print(crew_dictionary[employee_name_input][0])
    # new_list = change(crew_dictionary, user_choice_input, employee_name_input)
    # print(new_list)
main()

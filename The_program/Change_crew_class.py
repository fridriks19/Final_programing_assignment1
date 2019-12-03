def open_file(filename):
    crew_dictionary = {}
    f = open(filename , "r")
    for line in f:
        line = line.split(",")
        crew_dictionary[line[1]] = line
    return crew_dictionary
        

def change(dictionary, choice, name):
    change = choice
    placement = ""
   
    if choice == "1":
        placement = 2   
        attribute = "role"
    elif choice == "2":
        placement = 3
        attribute = "rank"
    elif choice == "3":
        placement = 4
        attribute = "liscense"
    elif choice == "4":
        placement = 5
        attribute = "address" 
    elif choice == "5":
        placement = 6
        attribute = "phonenumber" 

    change = input("Change {}: ".format(attribute))
    if change != "r":
        save = input("Do you whant to save the changes?: (y/n)")
        if save == "y":
            dictionary[name][placement] = change
            return dictionary
        else:
            return None
        

user_choice_input = input("Choose bruv: ")
def main():
    filename = "Crew.csv"
    crew_dictionary = open_file(filename)

    employee_name_input ='Virginia Ho'
    print(crew_dictionary[employee_name_input][0])
    new_list =change(crew_dictionary, user_choice_input, employee_name_input)
    print(new_list)
main()

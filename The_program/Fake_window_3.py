WITDH = 30
HEADER_MAIN = "NaN AIR"  
HEADER_SUB_A = "Breyta" 
HEADER_SUB_B = "Nýskrá"
HEADER_SUB_C = "Sækja"
BORDER = "*"

#Fastir strengir
QUIT = "'q' - Hætta"
GO_BACK = "'r' - Til baka"
SAVE = "'s' - Vista upplýsingar"
PICK = "Veldu skipun:"
USER_INPUT = ("Valin skipun: ")
#Forsíða 
CHANGE = "'1' - Breyta"
MAKE = "'2' - Nýskrá"
GET = "'3' - Sækja"
#Sub síður
EMPLOYEE = "'1' - Starfmann"
PLACE = "'2' - Áfangastað"
WORK_FLIGHT = "'3' - Vinnuferð"
AIRPLANE = "'4' - Flugvél"
WORK_TIME = "'5' - Vinnustund"
AIRPLANE_TYPE = "'5' - Flugvélategund"
FLIGHT_ATTEND = "'2' - Flugþjónn"
PILOT = "'1' - Flugmaður"

#Input síður#
NAME_INPUT = "Nafn: "
SSN_INPUT  = "Kennitala: "
ADDRESS_INPUT  = "Heimilisfang: "
GSM_INPUT  = "GSM-Sími: "
EMAIL_INPUT  = "Netfang: "
#Áfangastaðir
LAND_INPUT = "Land: "
AIRPORT_INPUT = "Flugvöllur: "
FLIGHT_TIME_INPUT = "Flugtími: "
DISTANCE_INPUT = "Fjarlægð"
CONTACT_INPUT = "Tengiliður"
EMERGENCY_PHONE_INPUT = "Neyðarsími"
user_input = " "


####### þurfum að geta búið til klassa með þessu og kallað á hann í staðinn 
########    - fyrir að hafa kóðan bara hérna 

def open_file(filename):   
    ''' Puts the crew members into a dictionary with values as ssn,name,role,rank,
        licence,address,phonenumber'''
    crew_dictionary = {}
    f = open(filename , "r")
    for line in f:
        line = line.split(",")
        crew_dictionary[line[1]] = line    # make the name the key and the values the rest of line
    return crew_dictionary
    
filename = "Crew.csv"
crew_dictionary = open_file(filename)


def change_crew(dictionary, choice, name):
    ''' Takes the crew member dictionary, the choice that the user inputs to 
        indicate what he whants to change and the name of the crew member the 
        user wanted to change'''
    change = choice
    placement = ""
    if choice == "1":
        placement = 2      # Beacause Role is number 2 in the values in crew_dictionary same goes for the other attributes they are 1 higher
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

    change = input("Change {}: ".format(attribute))   #Change the attribute the user whants
    if change != "r":
        save = input("Do you whant to save the changes?: (y/n): ")
        if save == "y":
            dictionary[name][placement] = change  #Rewrite the old value with the one that the user inputed
            return dictionary
        else:
            return None



#basically sama function og fyrir ofan
def open_dest_file(filename):   
    ''' Puts the destination into a dictionary with the id as key'''
    dest_dictionary = {}
    f = open(filename , "r")
    for line in f:
        line = line.split(",")
        dest_dictionary[line[0]] = line[1]    # make the name the key and the values the rest of line
    return dest_dictionary

filename2 = "Destinations.csv"
destination_dictionary = open_dest_file(filename2)
print(destination_dictionary)

def change_destination(dictionary, choice):
    ''' Takes the dictionary for all destination and the inputed choice 
        so we can change the destination that the user whants to change'''
    




###########################################################################
############################### main menu #################################
###########################################################################

while user_input != "q":
    print(BORDER * WITDH +"\n" + int((WITDH - len(HEADER_MAIN))/2)*" " +  HEADER_MAIN  +   "\n" + BORDER * WITDH )
    print(PICK +"\n" + QUIT+ "\n\n" + CHANGE + "\n" + MAKE + "\n" + GET + "\n")
    user_input = input(USER_INPUT)
    print()


###########################################################################
############################### change sub menu ###########################
###########################################################################
#If the user inputs 1 we go into the CHANGE menu 

    if user_input == "1":
        make_changes = user_input 
        while make_changes != "r":
            print(BORDER * WITDH +"\n" + int((WITDH - len(HEADER_SUB_A))/2)*" " +  HEADER_SUB_A  +   "\n" + BORDER * WITDH )
            print(PICK +"\n"+ QUIT+ " "*5 + GO_BACK +"\n\n" + EMPLOYEE +"\n" + PLACE +"\n" + WORK_FLIGHT +"\n" )
            make_changes = input(USER_INPUT)
            print()

            #If the user input is 1 we want to change the employes attributes 
            if make_changes == "1":
                employee_name_input = input("Nafn Starfsmanns: ")
                while employee_name_input != "r":
                    change_employee = make_changes
                    while change_employee != "r":
                        print(BORDER * WITDH +"\n" + int((WITDH - len(HEADER_SUB_A))/2)*" " +  HEADER_SUB_A  +   "\n" + BORDER * WITDH )
                        print(PICK + "\n" + QUIT + " "*5 + GO_BACK +"\n\n")                
                        print("Nafn: {}".format(crew_dictionary[employee_name_input][1])) 
                        print("Kennitölu: {}".format(crew_dictionary[employee_name_input][0]))
                        print("'1' - Starfsheiti: {}".format(crew_dictionary[employee_name_input][2]))
                        print("'2' - Staða: {}".format(crew_dictionary[employee_name_input][3]))
                        print("'3' - Leyfi: {}".format(crew_dictionary[employee_name_input][4]))
                        print("'4' - Heimilisfang: {}".format(crew_dictionary[employee_name_input][5]))
                        print("'5' - Símanúmer: {}".format(crew_dictionary[employee_name_input][6]))
                        print()
                        change_employee = input(USER_INPUT)   # Input what attribute you whant to change 
                        print()
                        if change_employee != "r":   # Go back if you dont whant to edit what you picked
                            change_crew(crew_dictionary, change_employee, employee_name_input)   

            if make_changes == "2": 
                change_place = make_changes
                counter  = 1
                while change_place != "r":
                    print(BORDER * WITDH +"\n" + int((WITDH - len(HEADER_SUB_A))/2)*" " +  HEADER_SUB_A  +   "\n" + BORDER * WITDH )
                    print(PICK +"\n" + QUIT + " "*5 + GO_BACK +"\n\n")  
                    #loop sem fer í gegnum listan af löndum og prentar þau öll í röð 
                    for key in destination_dictionary:
                        print("'{}' - {}".format(counter, destination_dictionary[key]))   
                        counter += 1
                    print()
                    change_place = input(USER_INPUT)   # Input what attribute you whant to change 
                    print()
                    if change_place != "r":
                        change_destination(destination_dictionary, change_employee)  # for now
                        
            if make_changes == "3":
                change_work_flight
                while change_work_flight != "r":
                    pass


###########################################################################
############################### Make sub menu #############################
###########################################################################
#if the user inputs 2 we go into the MAKE menu


    elif user_input == "2":
        make_user = user_input 
        while make_user != "r":
            print(BORDER * WITDH +"\n" +  int((WITDH - len(HEADER_SUB_B))/2)*" " +  HEADER_SUB_B +   "\n" + BORDER * WITDH )
            print(PICK +"\n" + QUIT+ " "*5 + GO_BACK +"\n\n" + EMPLOYEE +"\n" + PLACE +"\n" + WORK_FLIGHT +"\n" 
                            + AIRPLANE +"\n" + AIRPLANE_TYPE +"\n")
            make_user = input(USER_INPUT)
            print()
            #The result of a choisen input 
            if make_user == "1":
                make_employee = make_user 
                while make_employee  != "r":
                    print(BORDER * WITDH +"\n" +  int((WITDH - len(HEADER_SUB_B))/2)*" " +  HEADER_SUB_B +   "\n" + BORDER * WITDH )
                    print(PICK +"\n" + QUIT+ " "*5 + GO_BACK +"\n\n" + PILOT +"\n" + FLIGHT_ATTEND +"\n")
                    make_employee  = input(USER_INPUT)
                    print()
            elif make_user == "2":
                make_place= make_user 
                while make_place != "r":
                    print(BORDER * WITDH +"\n" +  int((WITDH - len(HEADER_SUB_B))/2)*" " +  HEADER_SUB_B +   "\n" + BORDER * WITDH )
  
                    print(PICK +"\n" +QUIT+ " "*5 + GO_BACK +"\n")
## þarf að búa til sér klasa þar sem við writum í eh skjal sem heldur utan um áfangastaðina 
                    input(LAND_INPUT)
                    input(AIRPORT_INPUT)
                    input(FLIGHT_TIME_INPUT)
                    input(DISTANCE_INPUT )
                    input(CONTACT_INPUT)
                    input(EMERGENCY_PHONE_INPUT)
                    print(SAVE)
                    make_place = input(USER_INPUT)
                    print()
                    if make_place == "s":  # if they save the information
                        print("Upplýsingar vistaðar")
                        make_place = "r"   # so they go back to sub menu automatically

            elif make_user == "3":
                make_work_flight = make_user 
                while make_work_flight != "r":
                    print(BORDER * WITDH +"\n" +  int((WITDH - len(HEADER_SUB_B))/2)*" " +  HEADER_SUB_B +   "\n" + BORDER * WITDH )
                    print(PICK +"\n" + QUIT+ " "*5 + GO_BACK +"\n")
                    make_work_flight  = input(USER_INPUT)
                    print()

            elif make_user == "4":
                make_airplane = make_user 
                while make_airplane  != "r":
                    print(BORDER * WITDH +"\n" +  int((WITDH - len(HEADER_SUB_B))/2)*" " +  HEADER_SUB_B +   "\n" + BORDER * WITDH )
                    print(PICK +"\n" + QUIT+ " "*5 + GO_BACK +"\n")
                    make_airplane  = input(USER_INPUT)
                    print()

            elif make_user == "5":
                make_airplane_type = make_user 
                while make_airplane_type  != "r":
                    print(BORDER * WITDH +"\n" +  int((WITDH - len(HEADER_SUB_B))/2)*" " +  HEADER_SUB_B +   "\n" + BORDER * WITDH )
                    print(PICK +"\n" + QUIT+ " "*5 + GO_BACK +"\n")
                    make_airplane_type  = input(USER_INPUT)
                    print()


###########################################################################
############################### get sub menu ##############################
###########################################################################
#If the user inputs 3 we go into the GET menu


    elif user_input == "3":
        get_user = user_input 
        while get_user != "r":
            print(BORDER * WITDH +"\n" +  int((WITDH - len(HEADER_SUB_C))/2)*" " +  HEADER_SUB_C  +   "\n" + BORDER * WITDH )
  
            print(PICK +"\n")
            print(QUIT+ " "*5 + GO_BACK +"\n")
            print(EMPLOYEE)
            print(PLACE)
            print(WORK_FLIGHT)
            print(AIRPLANE)
            print(WORK_TIME)
            print()
            get_user = input(USER_INPUT)
            print()







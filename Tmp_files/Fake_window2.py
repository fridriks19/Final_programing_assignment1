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

name1 = "Hrannar"
name2 = "kári óla"
ssn = "0303030303"
role = "Pilot"
rank ="Captain"
liscense = "NAkor12"
address = "Apa gata 20"
phonenumber = "666 6666"
user_input = " "


###########################################################################
############################### main menu #################################
###########################################################################


while user_input != "q":
    print(BORDER * WITDH +"\n" + int((WITDH - len(HEADER_MAIN))/2)*" " +  HEADER_MAIN  +   "\n" + BORDER * WITDH )
    print(PICK +"\n")
    print(QUIT+ "\n\n" + CHANGE + "\n" + MAKE + "\n" + GET + "\n")
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
            print(PICK +"\n")
            print(QUIT+ " "*5 + GO_BACK +"\n\n" + EMPLOYEE +"\n" + PLACE +"\n" + WORK_FLIGHT +"\n" ) 
            make_changes = input(USER_INPUT)
            print()

            #If the user input is 1 we want to change the employes attributes 
            if make_changes == "1":
                employe_name_input = input("Nafn Starfsmanns: ")
                change_employe = make_changes
                while change_employe != "r":
                    print(BORDER * WITDH +"\n" + int((WITDH - len(HEADER_SUB_A))/2)*" " +  HEADER_SUB_A  +   "\n" + BORDER * WITDH )
                    print(PICK +"\n")               
                    print("Nafn: {}".format(name1)) 
                    print("Kennitölu: {}".format(ssn))
                    print("'1' - Starfsheiti: {}".format(role))
                    print("'2' - Staða: {}".format(rank))
                    print("'3' - Leyfi: {}".format(liscense))
                    print("'4' - Heimilisfang: {}".format(address))
                    print("'5' - Símanúmer: {}".format(phonenumber))
                    print()
                    change_employe = input(USER_INPUT)
                    print()
    ####!!! Gætum gert eitt fall sem gerir þessa skipun það eru bara nörfnin sem breytast ekkert annað###!!!! 
### Fallið change_classes mydni virka ####
                    if change_employe == "1":    # breytum Starfsheiti ef 1 er valinn
                        change_role = change_employe  
                        while change_role != "r":
                            role = change_role
                            change_role = input("Change role: ")
                        
                            print(SAVE)
                            if change_role == "s":  # if they save the information
                                print("Upplýsingar vistaðar")
                                change_role= "r"   # so they go back to sub menu automatically    
                    if change_employe == "2":
                        change_rank = change_employe
                        while change_rank != "r":
                            rank = change_rank
                            change_rank = input("Change rank: ")
                            print(SAVE)
                            if change_rank == "s":  # if they save the information
                                print("Upplýsingar vistaðar")
                                change_rank= "r"   # so they go back to sub menu automatically                             
                    if change_employe == "3": 
                        change_liscense = change_employe
                        while change_liscense != "r":
                            liscense = change_liscense   #ssave the changes that were made 
                            change_liscense = input("Change liscense: ")                       
                            print(SAVE)
                            if change_liscense == "s":  # if they save the information
                                print("Upplýsingar vistaðar")
                                change_liscense = "r"   # so they go back to sub menu automatically
                    if change_employe == "4": 
                        change_address = change_employe
                        while change_address != "r":
                            address = change_address   
                            change_address = input("Change address: ")                       
                            print(SAVE)
                            if change_address == "s":  
                                print("Upplýsingar vistaðar")
                                change_address = "r"   
                    if change_employe == "5": 
                        change_phonenumber = change_employe
                        while change_phonenumber != "r":
                            phonenumber = change_phonenumber    
                            change_phonenumber = input("Change phonenumber: ")                       
                            print(SAVE)
                            if change_phonenumber == "s": 
                                print("Upplýsingar vistaðar")
                                change_phonenumber = "r"   
                    

            if make_changes == "2": 
                change_place
                while change_place != "r":
                    pass
                    

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
            print(PICK +"\n")
            print(QUIT+ " "*5 + GO_BACK +"\n\n" + EMPLOYEE +"\n" + PLACE +"\n" + WORK_FLIGHT +"\n" + AIRPLANE +"\n" + AIRPLANE_TYPE +"\n")
            make_user = input(USER_INPUT)
            print()
            #The result of a choisen input 
            if make_user == "1":
                make_employee = make_user 
                while make_employee  != "r":
                    print(BORDER * WITDH +"\n" +  int((WITDH - len(HEADER_SUB_B))/2)*" " +  HEADER_SUB_B +   "\n" + BORDER * WITDH )
                    print(PICK +"\n")
                    print(QUIT+ " "*5 + GO_BACK +"\n\n" + PILOT +"\n" + FLIGHT_ATTEND +"\n")
                    make_employee  = input(USER_INPUT)
                    print()
            elif make_user == "2":
                make_place= make_user 
                while make_place != "r":
                    print(BORDER * WITDH +"\n" +  int((WITDH - len(HEADER_SUB_B))/2)*" " +  HEADER_SUB_B +   "\n" + BORDER * WITDH )
  
                    print(PICK +"\n")
                    print(QUIT+ " "*5 + GO_BACK +"\n")
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
                    print(PICK +"\n")
                    print(QUIT+ " "*5 + GO_BACK +"\n")
                    make_work_flight  = input(USER_INPUT)
                    print()

            elif make_user == "4":
                make_airplane = make_user 
                while make_airplane  != "r":
                    print(BORDER * WITDH +"\n" +  int((WITDH - len(HEADER_SUB_B))/2)*" " +  HEADER_SUB_B +   "\n" + BORDER * WITDH )
                    print(PICK +"\n")
                    print(QUIT+ " "*5 + GO_BACK +"\n")
                    make_airplane  = input(USER_INPUT)
                    print()

            elif make_user == "5":
                make_airplane_type = make_user 
                while make_airplane_type  != "r":
                    print(BORDER * WITDH +"\n" +  int((WITDH - len(HEADER_SUB_B))/2)*" " +  HEADER_SUB_B +   "\n" + BORDER * WITDH )
                    print(PICK +"\n")
                    print(QUIT+ " "*5 + GO_BACK +"\n")
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



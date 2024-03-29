from models.class_pilot import pilot
from models.class_flight_attendant import flight_attendant
from services.class_employee_service import Employee_service
from models.class_destination import Destination
from services.class_destination_service import Destination_service
from models.class_employee import Employee
from services.class_voyage_service import Voyage_service
from services.class_aircraft_service import Aircraft_service
from services.class_past_flight_service import Past_flight_service
from services.class_upcoming_flight_service import Upcoming_flight_service
from services.class_voyage_service import Voyage_service
from services.class_worktime_service import Worktime_service

class GetUI():
    def __init__(self):
        self.__get_employee = Employee_service()
        self.__get_destination = Destination_service()
        self.__get_pastflight = Past_flight_service()
        self.__get_upcflight = Upcoming_flight_service()
        self.__get_voyage = Voyage_service()
        #self.__get_worktime = Worktime_service()

        self.WITDH = 50
        self.BORDER = "*"
        self.QUIT = "'q' - Hætta"
        self.GO_BACK = "'r' - Til baka"
        self.PICK = "Veldu skipun:"
        self.USER_INPUT = ("Valin skipun: ")
        # self.get_menu()
         
    ###########################################################################
    ############################### get sub menu ##############################
    ###########################################################################
    def get_menu(self):
        get_input = ""
        while get_input != "r":
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Sækja"))/2)*" " +  "Sækja"  +   "\n" + self.BORDER * self.WITDH )
            print(self.PICK +"\n")
            print(self.GO_BACK +"\n")
            print("'1' - Starfsmann" + "\n" + "'2' - Áfangastað" + "\n" + "'3' - Vinnuferð" + "\n" + "'4' - Vinnutímar starfsmanna" + "\n")
            get_input = input(self.USER_INPUT)
            print()
            if get_input != "r":
                if get_input == "1":
                    self.employee_menu()
                if get_input == "2":
                    self.destination_menu()
                if get_input == "3":
                    self.voyage_menu()
                if get_input == "4":
                    self.worktime_menu()
                else:
                    print("Vinsamlegast veldu eitt af eftirfarandi!")
                    break
            else:
                pass   
            


    def employee_menu(self):
        ''' If the user inputed '1' he gets to the employee menu. Here the user can choose what information he whants to see
            he can choose to see all employees in a list, only the pilots, only the flight attendants or look up a specific employee
            by his ssn number '''
        get_input = ""
        if get_input != "r":
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Sækja starfsmann"))/2)*" " +  "Sækja starfsmann"  +   "\n" + self.BORDER * self.WITDH )
            print(self.PICK +"\n")
            print(self.GO_BACK +"\n")
            print("'1'- Allir starfsmenn")
            print("'2' - Flugmenn")
            print("'3' - Flugþjónn")
            print("'4' - Leita af starfsmanni")
            print()
            get_input = input(self.USER_INPUT)
            while get_input != "1" and get_input != "2" and get_input != "3" and get_input != "4" and get_input != "r":     # We have to make sure that if the user inputs something that is not available there will not be an error
                print("Innsláttarvilla!\nVinsamlegast veldu aftur")
                print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Sækja starfsmann"))/2)*" " +  "Sækja starfsmann"  +   "\n" + self.BORDER * self.WITDH )
                print(self.PICK +"\n")
                print(self.GO_BACK +"\n")
                print("'1'- Allir starfsmenn")
                print("'2' - Flugmenn")
                print("'3' - Flugþjónn")
                print("'4' - Leita af starfsmanni")
                get_input = input(self.USER_INPUT)
                    
            if get_input == "1":
                print(self.__get_employee.get_allemployees())  # Prints all the employees, their ssn, name and role 
                while get_input != "r":
                    print(self.GO_BACK +"\n")
                    get_input = input(self.USER_INPUT)
                else:
                    self.employee_menu()
                    
            if get_input == "2":     #Get only pilots 
                print()
                print(self.__get_employee.get_pilots())
                while get_input != "r":
                    print(self.GO_BACK +"\n")
                    get_input = input(self.USER_INPUT)
                else:
                    self.employee_menu()
             
            if get_input == "3":     #Get flight attendants 
                print()
                print(self.__get_employee.get_flightattendants())
                while get_input != "r":
                    print(self.GO_BACK +"\n")
                    get_input = input(self.USER_INPUT)
                else:
                    self.employee_menu()
            
            if get_input == "4":    # Get one employee by his ssn number and the user inputs the ssn
                print()
                print(self.GO_BACK +"\n") 
                employee_ssn_input = ""
                while employee_ssn_input != "r":
                    employee_ssn_input = input("Kennitala starfsmanns: ")
                    empl_info_lst = self.__get_employee.get_employee(employee_ssn_input)
                    if empl_info_lst != False:     # If empl_info_list returns false then the employee is not in the system/or the ssn was inputed wrong
                        if get_input != "r":
                            info_output = Employee(empl_info_lst)  
                            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Sækja starfsmann"))/2)*" " +  "Sækja starfsmanni"  +   "\n" + self.BORDER * self.WITDH )
                            print(self.PICK +"\n")
                            print(self.GO_BACK +"\n")  
                            print("Kennitala: {}".format(info_output.get_ssn()))        
                            print("Nafn: {}".format(info_output.get_name())) 
                            print("Starfsheiti: {}".format(info_output.get_role()))
                            print("Stöðugildi: {}".format(info_output.get_rank()))
                            print("Leyfi: {}".format(info_output.get_licence()))
                            print("Heimilisfang: {}".format(info_output.get_address()))
                            print("Símanúmer: {}".format(info_output.get_phone()))
                            print()
                            get_input = input(self.USER_INPUT)
                        else:
                            self.employee_menu()
                    else:
                        if employee_ssn_input == "r":
                            self.employee_menu()  
                        print()    
                        print("Starfsmaður ekki til! Vitlaus kennitala.")
                        print()
                  
                
                

    def destination_menu(self):
        ''' The program prints a list of all the available destinations and the user can choose which one he wants to get more information on
            he cannot do anything with the infirmation other then look at it'''
        get_input = ""
        while get_input != "r":
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Sækja áfangastað"))/2)*" " +  "Sækja áfangastað"  +   "\n" + self.BORDER * self.WITDH )
            print(self.PICK +"\n")
            prnt_str, counter = self.__get_destination.get_alldest()  #Prints a list of all the destinations and the counter for how many destinations there are
            print(prnt_str)
            print(self.GO_BACK +"\n")
            get_input = input(self.USER_INPUT)    # User chooses which destination he wants to get more info on 
            if get_input.isdigit() == False:  # if the user doesnt input a number then make him choose again
                if get_input == "r":
                    self.get_menu()
                    break
                else:
                    print("Veldu áfangastað sem er í boði!")
                    self.destination_menu()
                    break
            elif get_input.isdigit() == True and int(get_input) >= 1 and int(get_input) <= int(counter-1):  # the user inputs must be a digit 
                if get_input != "r":
                    print()
                    print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Áfangastaður"))/2)*" " +  "Áfangastaður"  +   "\n" + self.BORDER * self.WITDH )
                    print(self.PICK +"\n")
                    chosen_dest = self.__get_destination.get_dest(get_input) #Takes the users input and sends it to get the destinaton he chose 
                    output = Destination(chosen_dest)
                    print("Áfangastaður: {}".format(output.get_destinationName()))
                    print("Flugvöllur: {}".format(output.get_destinationId()))
                    print("Flugtími: {}".format(output.get_flighttime()))
                    print("Fjarlægð: {}".format(output.get_distance()))
                    print("Tengiliður: {}".format(output.get_contact()))
                    print("Neyðarsímanúmer: {}".format(output.get_phone()))
                    while get_input != "r":
                        print()
                        print(self.GO_BACK +"\n")
                        get_input = input(self.USER_INPUT)
                    if get_input == "r":
                        self.destination_menu()
                        break
                else:
                    self.get_menu()
                    break
                    

    def voyage_menu(self):
        ''' Here the user can choose to se old or new voyages, and in both of those categories he can choose to se a 
            voyage on a specific date or to see all voyages in a certain time window that he chooses'''
        get_input = ""
        while get_input != "r":
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Sækja vinnuferðir"))/2)*" " +  "Sækja vinnuferðir"  +   "\n" + self.BORDER * self.WITDH )
            print(self.PICK +"\n")
            print("'1' - Til að sjá gamlar vinnuferðir")
            print("'2' - Til að sjá áætlaðir vinnuferðir")
            print()
            print(self.GO_BACK+ "\n")
            get_input = input(self.USER_INPUT)
            if get_input != "1" and get_input != "2" and get_input != "r":
                print("Vinsamlegast veldu eitt af eftirfarandi!")
                self.voyage_menu()
            if get_input == "r":
                self.get_menu()
                break
            elif get_input =="1":
                print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Vinnuferð"))/2)*" " +  "Vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
                print(self.PICK +"\n")
                print("'1' - Sjá gamlar vinnuferðir á tímabili")
                print("'2' - Sjá gamlar vinnuferðir á ákveðni dagsetningu")
                print()
                print(self.GO_BACK +"\n")
                old_voyage = input(self.USER_INPUT)
                if old_voyage != "1" and old_voyage != "2" and old_voyage != "r":
                    print("Vinsamlegast veldu eitt af eftirfarandi!")
                elif old_voyage == "1":
                    print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Vinnuferð"))/2)*" " +  "Vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
                    print(self.PICK +"\n")
                    first_date = "Skráðu fyrri dagsetningu tímabilsins"
                    next_date = "Skráðu seinni dagsetning tímabilsins "
                    date1 = self.__get_voyage.get_date_voyage(first_date) # this is a fucntion were the user inputs the dates 
                    date2 = self.__get_voyage.get_date_voyage(next_date)
                    if date1 == False or date2 == False:    # To make sure that the user inputs a date that is available 
                        print()
                        print("Vitlausar dagsetningar!\nSkráðu réttan brottfarartíma!")
                        self.voyage_menu()
                        break
                    else:
                        past_flightss = self.__get_pastflight.get_pastflights(date1,date2)
                        print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Vinnuferð"))/2)*" " +  "Vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
                        print(past_flightss)
                elif old_voyage == "2":
                    print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Vinnuferð"))/2)*" " +  "Vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
                    print(self.PICK +"\n")
                    only_date = "Skráðu dagsetnungu vinnuferða"
                    date = self.__get_voyage.get_date_voyage(only_date)
                    past_flight = self.__get_pastflight.get_pastflight(date)
                    print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Vinnuferð"))/2)*" " +  "Vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
                    print()
                    print(past_flight)
                    print()

            elif get_input =="2":
                print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Vinnuferð"))/2)*" " +  "Vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
                print(self.PICK +"\n")
                print("'1' - Sjá áætlaðar vinnuferðir á tímabili")
                print("'2' - Sjá áætlaðar vinnuferðor á ákveðni dagsetningu")
                print()
                print(self.GO_BACK +"\n")
                upcm_voyage = input(self.USER_INPUT)
                print()
                if upcm_voyage != "1" and upcm_voyage != "2" and upcm_voyage != "r":
                    print("Vinsamlegast veldu eitt af eftirfarandi!")
                elif upcm_voyage == "1":   
                    print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Vinnuferð"))/2)*" " +  "Vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
                    print(self.PICK +"\n")
                    first_date = "Skráðu fyrri dagsetningu tímabilsins"
                    next_date = "Skráðu seinni dagsetning tímabilsins "
                    date1 = self.__get_voyage.get_date_voyage(first_date)
                    date2 = self.__get_voyage.get_date_voyage(next_date)
                    if date1 == False or date2 == False:    
                        print()
                        print("Vitlausar dagsetningar!\nSkráðu réttan brottfarartíma!")
                        self.voyage_menu()
                        break
                    else:
                        upc_flightss = self.__get_upcflight.get_upcomingflights(date1,date2)
                        print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Vinnuferð"))/2)*" " +  "Vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
                        print(upc_flightss)
                elif upcm_voyage == "2":
                    print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Vinnuferð"))/2)*" " +  "Vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
                    print(self.PICK +"\n")
                    only_date = "Skráðu dagsetningu vinnuferða"
                    date = self.__get_voyage.get_date_voyage(only_date)
                    upc_flight = self.__get_upcflight.get_upcomingflight(date)
                    print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Vinnuferð"))/2)*" " +  "Vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
                    print()
                    print(upc_flight)
                    print()
    


    def worktime_menu(self):
        ''' The user can choose to see a list of all the employees that are not / or are working on a specific date the user can 
            also see the work summary for one employee'''
        get_input = ""
        while get_input != "r":
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Sækja vinnutíma"))/2)*" " +  "Sækja vinnutíma"  +   "\n" + self.BORDER * self.WITDH )
            print(self.PICK +"\n")
            print(self.GO_BACK +"\n")
            print("'1' - Sjá lista yfir alla starfsmenn sem eru ekki að vinna ákveðin dag")
            print("'2' - Sjá lista yfir alla starfsmenn sem eru að vinna ákveðin dag")
            print("'3' - Sjá vinnuyfirlit fyrir ákveðins starfsmanns")
            print()
            get_input = input(self.USER_INPUT)
            if get_input != "1" and get_input !="2" and get_input != "3":
                print("Vinsamlegast veldu eitthvert af eftirfarandi!")
            elif get_input == "1":
                print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Sækja vinnutíma"))/2)*" " +  "Sækja vinnutíma"  +   "\n" + self.BORDER * self.WITDH )
                print(self.PICK +"\n")
                prnt_str = ("Skráðu dagsetningu") 
                date = self.__get_voyage.get_date_voyage(prnt_str)  # User chooses the date 
                not_working = Worktime_service(date).not_working_list()
                print()
                print(self.__get_voyage.print_list(not_working))
                
            elif get_input == "2":
                print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Sækja vinnutíma"))/2)*" " +  "Sækja vinnutíma"  +   "\n" + self.BORDER * self.WITDH )
                print(self.PICK +"\n")
                prnt_str = ("Skráðu dagsetningu") 
                date = self.__get_voyage.get_date_voyage(prnt_str)   # User chooses the date 
                working = Worktime_service(date).print_working_list_destination()
                if working == " ":
                    print("Dagsetning ekki til")
                print()
                print(working)
                #print(self.__get_voyage.print_list(working))   # Prints out the list of employees that are working and the destination he is going to on that date 

            elif get_input == "3":
                print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Sækja vinnutíma"))/2)*" " +  "Sækja vinnutíma"  +   "\n" + self.BORDER * self.WITDH )
                print(self.PICK +"\n")
                first_date = "\nSkráðu fyrri dagsetningu tímabilsins"
                next_date = "Skráðu seinni dagsetning tímabilsins "
                date1 = self.__get_voyage.get_date_voyage(first_date)
                date2 = self.__get_voyage.get_date_voyage(next_date)
                print()
                ssn_input = input("\nSkráðu kennitölu starfsmanns: ")
                if ssn_input != "r":
                    empl_info_lst = self.__get_employee.get_employee(ssn_input)
                if empl_info_lst != False:
                    upc_flightss = self.__get_upcflight.get_upcomingflights_list_selected_time(date1,date2)
                    # print(upc_flightss)
                    print(self.__get_upcflight.find_empl_worktime(ssn_input, upc_flightss))
                else:
                    if ssn_input == "r":
                        self.worktime_menu()      
                    print("Starfsmaður ekki til! Vitlaus kennitala.")
                    self.worktime_menu()    
                    break
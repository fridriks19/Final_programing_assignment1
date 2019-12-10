from models.class_pilot import pilot
from models.class_flight_attendant import flight_attendant
from services.class_employee_service import Employee_service
from models.class_destination import Destination
from services.class_destination_service import Destination_service
from models.class_employee import Employee
from services.class_voyage_service import Voyage_service
from services.class_aircraft_service import Aircraft_service

#from services.class_upcoming_flightsIO import Upcoming_flightsIO

class GetUI():
    def __init__(self):
        self.__getemployee = Employee_service()
        self.__getdestination = Destination_service()

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
            print("'1' - Starfmann" + "\n" + "'2' - Áfangastað" + "\n" + "'3' - Vinnuferð" + "\n" + "'4' - Flugvél" + "\n" + "'5' - Flug/vinnutímar" + "\n")
            get_input = input(self.USER_INPUT)
            print()
            if get_input == "1":
                self.employee_menu()
            if get_input == "2":
                self.destination_menu()
            if get_input == "3":
                self.voyage_menu()
            if get_input == "4":
                self.aircraft_menu()
            if get_input == "r":
                get_input = "r"
            else:
                print("Vinsamlegast veldu eitt af eftirfarandi!")
                self.get_menu()


    def employee_menu(self):
        print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Sækja starfsmann"))/2)*" " +  "Sækja starfsmann"  +   "\n" + self.BORDER * self.WITDH )
        print(self.PICK +"\n")
        print(self.GO_BACK +"\n")
        print("'1'- Allir starfsmenn")
        print("'2' - Flugmenn")
        print("'3' - Flugþjónn")
        print("'4' - Leita af starfsmanni")
        get_input = input(self.USER_INPUT)
        while get_input != "1" and get_input != "2" and get_input != "3" and get_input != "4" and get_input != "r":
            print("Innsláttarvilla!\nVinsamlegast veldu '1','2', eða '3'")
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Sækja starfsmann"))/2)*" " +  "Sækja starfsmann"  +   "\n" + self.BORDER * self.WITDH )
            print(self.PICK +"\n")
            print(self.GO_BACK +"\n")
            print("'1'- Allir starfsmenn")
            print("'2' - Flugmenn")
            print("'3' - Flugþjónn")
            print("'4' - Leita af starfsmanni")
            get_input = input(self.USER_INPUT)
            
        if get_input == "1":   # get all employeed 
            print()
            print(self.__getemployee.get_allemployees())
            while get_input != "r":
                print(self.GO_BACK +"\n")
                get_input = input(self.USER_INPUT)

        if get_input == "2":     #Get only pilots 
            print()
            print(self.__getemployee.get_pilots())
            while get_input != "r":
                print(self.GO_BACK +"\n")
                get_input = input(self.USER_INPUT)

        if get_input == "3":     #Get flight attendants 
            print()
            print(self.__getemployee.get_flightattendants())
            while get_input != "r":
                print(self.GO_BACK +"\n")
                get_input = input(self.USER_INPUT)
        
        if get_input == "4":    # Get one employee by his ssn number and the user inputs the ssn
            print()
            print(self.GO_BACK +"\n") 
            employee_ssn_input = input("Kennitala starfsmanns: ")
            while employee_ssn_input != "r":
                empl_info_lst = self.__getemployee.get_employee(employee_ssn_input)
                while empl_info_lst == False:
                    print(self.GO_BACK +"\n") 
                    print("Starfmaður ekki til! Vitlaus kennitala.")
                    employee_ssn_input = input("Kennitala starfsmanns: ")
                    empl_info_lst = self.__getemployee.get_employee(employee_ssn_input)
                    if employee_ssn_input == "r":
                        self.get_menu()  
                if get_input != "r":
                    info_output = Employee(empl_info_lst)  
                    print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Breyta starfsmanni"))/2)*" " +  "Breyta starfsmanni"  +   "\n" + self.BORDER * self.WITDH )
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
                    self.get_menu()
        if get_input =="r":
            self.get_menu()       
            
                

    def destination_menu(self):
        get_input = ""
        while get_input != "r":
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Sækja áfangastað"))/2)*" " +  "Sækja áfangastað"  +   "\n" + self.BORDER * self.WITDH )
            print(self.PICK +"\n")
            print(self.GO_BACK +"\n")
            prnt_str, counter = self.__getdestination.get_alldest()  # prentar út listan af öllum löndunum
            print(prnt_str)
            get_input = input("Veldu áfangastað: ")      # nr á áfangastað 
            if get_input != "r":
                print()
                chosen_dest = self.__getdestination.get_dest(get_input) #tökum þá tölu sem notandi valdi og sendum í DestinationRepo og þar í get_dest fallið 
                output = Destination(chosen_dest)
                print("Áfangastaður: {}".format(output.get_destinationName()))
                print("Flugvöllur: {}".format(output.get_destinationId()))
                print("Flugtími: {}".format(output.get_flighttime()))
                print("Fjarlægð: {}".format(output.get_distance()))
                print("Tengiliður: {}".format(output.get_contact()))
                print("Neyðarsímanúmer: {}".format(output.get_phone()))
                while get_input != "r":
                    print(self.GO_BACK +"\n")
                    get_input = input(self.USER_INPUT)
            else:
                self.get_menu()
                    

    def voyage_menu(self):
        get_input = ""
        while get_input != "r":
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Sækja vinnuferðir"))/2)*" " +  "Sækja vinnuferðir"  +   "\n" + self.BORDER * self.WITDH )
            print(self.PICK +"\n")
            print(self.GO_BACK +"\n")
            print("'1' - Til að sjá gamlar vinnuferðir")
            print("'2' - Til að sjá áætlaðir vinnuferðir")
            get_input = input(self.PICK)
            if get_input != "1" or get_input != "2" or get_input != "r":
                print("Vinsamlegast veldu eitt af eftirfarandi!")
                self.voyage_menu()
            if get_input =="1":
                pass
            if get_input =="2":
                pass
   

    def aircraft_menu(self):
        get_input = ""
        while get_input != "r":
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Sækja flugvélar"))/2)*" " +  "Sækja flugvélar"  +   "\n" + self.BORDER * self.WITDH )
            print(self.PICK +"\n")
            print(self.GO_BACK +"\n")

from repo.class_EmployeeRepository import EmployeeRepository
from repo.class_Aircraft_typeRepository import AircraftRepository
from repo.class_PastFlightsRepository import PastFlightsRepository
from models.class_pilot import pilot
from models.class_flight_attendant import flight_attendant
from services.class_employee_service import Employee_service


#from services.class_upcoming_flightsIO import Upcoming_flightsIO

class MakeUI():
    def __init__(self):
        
        self.__new_employee = Employee_service()
        #self.__new_destination = DestinationRepository()
        self.__new_aircraft = AircraftRepository()
        self.WITDH = 50
        self.BORDER = "*"
        self.QUIT = "'q' - Hætta"
        self.GO_BACK = "'r' - Til baka"
        self.PICK = "Veldu skipun:"
        self.USER_INPUT = ("Valin skipun: ")
    ###########################################################################
    ############################### Make sub menu #############################
    ###########################################################################  
    def make_menu(self):
        make_input = ""
        while make_input != "r":
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá"))/2)*" " +  "Nýskrá"  +   "\n" + self.BORDER * self.WITDH )
            print(self.PICK +"\n")
            print(self.QUIT+ " "*5 + self.GO_BACK +"\n")
            print("'1' - Starfmann" + "\n" + "'2' - Áfangastað" + "\n" + "'3' - Vinnuferð" + "\n" + "'4' - Flugvél" + "\n" + "'5' - Flug/vinnutímar" + "\n")
            make_input = input(self.USER_INPUT).lower()
            print()
            if make_input == "1":
                print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá starfsmann"))/2)*" " +  "Nýskrá starfsmann"  +   "\n" + self.BORDER * self.WITDH )
                print(self.PICK +"\n")
                print ("'1' - Skrá flugmann" + "\n" + "'2' - Skrá flugþjón")   #Gefur valmöguleika um hvort það vilji skrá flugmann eða flugþjón
                make_input = input(self.USER_INPUT).lower()
                ssn = input("Kennitala: ")
                name = input("Nafn: ")
                rank = input("Stöðugildi: ")
                license = input("Réttindi: ")
                address = input("Heimilisfang: ")
                phonenumber = input("GSM-Sími:")
                save_input = input("Viltu vista starfsmanninn \n'1' - Já\n'2' - Nei\n Valin skipun: ")
                if save_input == "1":   
                    if make_input == "1": # If pilot is chosen
                        role =  ""
                        new_list = [ssn,name,role,rank,license,address,phonenumber] #Gerum lista með öllum inputunum og sendum í pilot clasan og síðan öddum við employe-inum í csv fileið
                        new_employee = pilot(new_list)
                        self.__new_employee.add_employee(str(new_employee))
                    if make_input == "2": # If cabincrew is chosen
                        role =  ""
                        new_list = [ssn,name,role,rank,license,address,phonenumber]
                        new_employee = flight_attendant(new_list)
                        print(new_employee)
                        self.__new_employee.add_employee(str(new_employee)) 
                else:
                    make_input = "1"  #Ef það er valið nei við að vista upplýsngar er notandi sendur aftur til baka á nýskrá síðu.
                    
            if make_input == "2":
                print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá áfangastað"))/2)*" " +  "Nýskrá áfangastað"  +   "\n" + self.BORDER * self.WITDH )
                print(self.PICK +"\n")
                destination = input("Áfangastaður: ")
                airportID = input("Flugvöllur: ")
                flight_time = input("Flugtími: ")
                distance = input("Fjarlægð: ")
                contact = input("Tengiliður: ")
                emergency_phone = input("Neyðarsími: ")

                new_list = [destination,airportID,flight_time,distance,contact,emergency_phone]
                new_destination = destination(new_list)
                self.__new_destination.add_destination(new_employee)

            if make_input == "3":
                print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá vinnuferð"))/2)*" " +  "Nýskrá vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
                print(self.PICK +"\n")
                new_string = ""


            if make_input == "4":
                print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá flugvél"))/2)*" " +  "Nýskrá flugvél"  +   "\n" + self.BORDER * self.WITDH )
                print(self.PICK +"\n")

            if make_input == "5":
                print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá flug/vinnutíma"))/2)*" " +  "Nýskrá flug/vinnutíma"  +   "\n" + self.BORDER * self.WITDH )
                print(self.PICK +"\n")
                pass
        else:
            return ""

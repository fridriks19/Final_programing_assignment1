from services.class_EmployeeRepository import EmployeeRepository
from services.class_Aircraft_typeRepository import AircraftRepository
from services.class_PastFlightsRepository import PastFlightsRepository
from models.class_pilot import pilot
from models.class_flight_attendant import flight_attendant


#from services.class_upcoming_flightsIO import Upcoming_flightsIO

class MakeUI():
    def __init__(self):
        self.__new_employee = EmployeeRepository()
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
                print ("'1' - Skrá fugmann" + "\n" + "'2' - Skrá flugþjón")
                make_input = input(self.USER_INPUT).lower()
                #new_list = EmployeeMaker()
                ssn = input("Kennitala: ")
                name = input("Nafn: ")
                rank = input("Stöðugildi: ")
                liscense = input("Réttindi: ")
                address = input("Heimilisfang: ")
                phonenumber = input("GSM-Sími:")

                if make_input == "1":
                    role =  ""
                    new_list = [ssn,name,role,rank,liscense,address,phonenumber]
                    new_employee = pilot(new_list)
                    self.__new_employee.add_employee(str(new_employee))

                if make_input == "2":
                    role =  ""
                    new_list = [ssn,name,role,rank,liscense,address,phonenumber]
                    new_employee = flight_attendant(new_list)
                    new = EmployeeRepository(str(new_employee))
                    print(new.add_employee())

            if make_input == "2":
                print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá áfangastað"))/2)*" " +  "Nýskrá áfangastað"  +   "\n" + self.BORDER * self.WITDH )
                print(self.PICK +"\n")
                new_string = " "

                destination = input("Áfangastaður: ")
                airportID = input("Flugvöllur: ")
                flight_time = input("Flugtími: ")
                distance = input("Fjarlægð: ")
                contact = input("Tengiliður: ")
                emergency_phone = input("Neyðarsími: ")

                new_list = [destination,airportID,flight_time,distance,contact,emergency_phone]
                new_string = ",".join(new_list)
                new_destination = EmployeeRepository(new_string)
                print(new_destination.add_employee())

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

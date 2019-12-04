from services.class_EmployeeRepository import EmployeeRepository
from services.class_Aircraft_typeRepository import AircraftRepository
from services.class_PastFlightsRepository import PastFlightsRepository

#from services.class_upcoming_flightsIO import Upcoming_flightsIO

class MakeUI():
    def __init__(self):
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
                flugmadur_listi = []
                ssn = input("Kennitala: ")
                name = input("Nafn: ")
                role = input("Starfsheiti: ")
                rank = input("Stöðugildi: ")
                liscense = input("Réttindi: ")
                address = input("Heimilisfang: ")
                phonenumber = input("GSM-Sími:")
                new_employee = EmployeeRepository([ssn,name,role,rank,liscense,address,phonenumber])
                print(new_employee.add_employee())
                
    
            if make_input == "2":
                pass
            if make_input == "3":
                pass
            if make_input == "4":
                pass
            if make_input == "5":
                pass
        else:
            return ""

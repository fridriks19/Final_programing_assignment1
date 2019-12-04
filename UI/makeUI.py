from services.class_EmployeeRepository import EmployeeRepository
from services.class_Aircraft_typeRepository import AircraftRepository
<<<<<<< HEAD
from services.class_PastFlightsIO import PastFlightsRepository
=======
<<<<<<< HEAD
from services.class_PastFlightsIO import PastFlightsRepository
=======
from services.class_PastFlightsRepository import PastFlightsRepository
>>>>>>> b26d185051b44da41477e30618ad410286880609
>>>>>>> 708d67af4563841a61faaaf28ae51c9fa4cd5b8a
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

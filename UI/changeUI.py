from services.class_EmployeeRepository import EmployeeRepository
from services.class_Aircraft_typeRepository import AircraftRepository
<<<<<<< HEAD
from services.class_PastFlightsIO import PastFlightsRepository
=======
from services.class_PastFlightsRepository import PastFlightsRepository
>>>>>>> b26d185051b44da41477e30618ad410286880609
#from services.class_upcoming_flightsIO import Upcoming_flightsIO

class ChangeUI():
    def __init__(self ):  
        self.WITDH = 50
        self.BORDER = "*"
        self.QUIT = "'q' - Hætta"
        self.GO_BACK = "'r' - Til baka"
        self.PICK = "Veldu skipun:"
        self.USER_INPUT = ("Valin skipun: ")


    ###########################################################################
    ############################### change sub menu ###########################
    ###########################################################################    
    def change_menu(self):
        change_input = ""  # til að maður geti bakkað um 1 í stað þess að quita bara 
        while change_input != "r":
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Breyta"))/2)*" " +  "Breyta"  +   "\n" + self.BORDER * self.WITDH )
            print(self.PICK +"\n")
            print(self.QUIT+ " "*5 + self.GO_BACK +"\n")
            print("'1' - Starfmann" + "\n" + "'2' - Áfangastað" + "\n" + "'3' - Vinnuferð" + "\n" + "'4' - Flugvél" + "\n" + "'5' - Flug/vinnutímar" + "\n")
            change_input = input(self.USER_INPUT).lower()
            print()
            if change_input == "1":
                pass
            if change_input == "2":
                pass
            if change_input == "3":
                pass
            if change_input == "4":
                pass
            if change_input == "5":
                pass
        else:
            return ""
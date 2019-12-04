from services.class_employeeIO import EmployeeIO
from services.class_aircraft_typeIO import AircraftTypeIO
from services.class_PastFlightsIO import PastFlightsIO
from services.class_upcoming_flightsIO import Upcoming_flightsIO

class ChangeUI():
    def __init__(self ):  
        pass


    ###########################################################################
    ############################### change sub menu ###########################
    ###########################################################################    
    def change_menu(self):
        change_input = ""  # til að maður geti bakkað um 1 í stað þess að quita bara 
        while change_input != "r":
            print(BORDER * WITDH +"\n" + int((WITDH - len("Breyta"))/2)*" " +  "Breyta"  +   "\n" + BORDER * WITDH )
            print(PICK +"\n")
            print(QUIT+ " "*5 + GO_BACK +"\n")
            print("'1' - Starfmann" + "\n" + "'2' - Áfangastað" + "\n" + "'3' - Vinnuferð" + "\n" + "'4' - Flugvél" + "\n" + "'5' - Flug/vinnutímar" + "\n")
            change_input = input(USER_INPUT).lower()
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
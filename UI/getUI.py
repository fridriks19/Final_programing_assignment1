from services.class_employeeIO import EmployeeIO
from services.class_aircraft_typeIO import AircraftTypeIO
from services.class_PastFlightsIO import PastFlightsIO
from services.class_upcoming_flightsIO import Upcoming_flightsIO

class GetUI():
    def __init__(self):
        pass


                
    ###########################################################################
    ############################### get sub menu ##############################
    ###########################################################################
    def get_menu(self):
        get_input = ""
        while get_input != "r":
            print(BORDER * WITDH +"\n" + int((WITDH - len("Sækja"))/2)*" " +  "Sækja"  +   "\n" + BORDER * WITDH )
            print(PICK +"\n")
            print(QUIT+ " "*5 + GO_BACK +"\n")
            print("'1' - Starfmann" + "\n" + "'2' - Áfangastað" + "\n" + "'3' - Vinnuferð" + "\n" + "'4' - Flugvél" + "\n" + "'5' - Flug/vinnutímar" + "\n")
            get_input = input(USER_INPUT)
            print()
            if get_input == "1":
                
            if get_input == "2":
                pass
            if get_input == "3":
                pass
            if get_input == "4":
                pass
            if get_input == "5":
                pass
        else:
            return ""
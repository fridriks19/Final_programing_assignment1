from services.class_employeeIO import EmployeeIO
from services.class_aircraft_typeIO import AircraftTypeIO
from services.class_PastFlightsIO import PastFlightsIO
from services.class_upcoming_flightsIO import Upcoming_flightsIO

class MakeUI():
    def __init__(self):
        pass



    ###########################################################################
    ############################### Make sub menu #############################
    ###########################################################################  
    def make_menu(self):
        make_input = ""
        while make_input != "r":
            print(BORDER * WITDH +"\n" + int((WITDH - len("Nýskrá"))/2)*" " +  "Nýskrá"  +   "\n" + BORDER * WITDH )
            print(PICK +"\n")
            print(QUIT+ " "*5 + GO_BACK +"\n")
            print("'1' - Starfmann" + "\n" + "'2' - Áfangastað" + "\n" + "'3' - Vinnuferð" + "\n" + "'4' - Flugvél" + "\n" + "'5' - Flug/vinnutímar" + "\n")
            make_input = input(USER_INPUT).lower()
            print()
            if make_input == "1":
                pass
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

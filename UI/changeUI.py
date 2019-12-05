from repo.class_EmployeeRepository import EmployeeRepository
from repo.class_Aircraft_typeRepository import AircraftRepository
from repo.class_PastFlightsRepository import PastFlightsRepository
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
            print("'1' - Starfmann" + "\n" + "'2' - Vinnuferð" + "\n" + "'3' - Áfangastað" + "\n")
            change_input = input(self.USER_INPUT).lower()
            print()
            
            if change_input == "1":
                employee_name_input = input("Kennitala starfsmanns: ")
                while employee_name_input != "r":
                   #?? change_employee = change_input
                    while employee_name_input != "r":
                        print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Breyta"))/2)*" " +  "Starfsmaður"  +   "\n" + self.BORDER * self.WITDH )
                        print(self.PICK +"\n")              
                        print("Nafn: {}".format(crew_dictionary[employee_name_input][1])) 
                        print("Kennitölu: {}".format(crew_dictionary[employee_name_input][0]))
                        print("'1' - Starfsheiti: {}".format(crew_dictionary[employee_name_input][2]))
                        print("'2' - Staða: {}".format(crew_dictionary[employee_name_input][3]))
                        print("'3' - Leyfi: {}".format(crew_dictionary[employee_name_input][4]))
                        print("'4' - Heimilisfang: {}".format(crew_dictionary[employee_name_input][5]))
                        print("'5' - Símanúmer: {}".format(crew_dictionary[employee_name_input][6]))
                        print()
                        change_employee = input(USER_INPUT)   # Input what attribute you whant to change 
                        print()
                        if change_employee != "r":   # Go back if you dont whant to edit what you picked
                            change_crew(crew_dictionary, change_employee, employee_name_input)   

                
                pass
            if change_input == "2":
                
                
            if change_input == "3":
               destination_point_input = input("Nafn áfangastaðs: ")
                while destination_point_input != "r":
                    change_destination_point = change_input
                    while destination_point_input != "r":
                        print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Breyta"))/2)*" " +  "Áfangastaður"  +   "\n" + self.BORDER * self.WITDH )
                        print(self.PICK +"\n")     
                        print("'1' - Tengiliður: {}".format(#eithvað tengt class_destination point))
                        print("'2' - Neyðarsími: {}".format(#eitthvað tengt class_destination point))
            
        else:
            return ""
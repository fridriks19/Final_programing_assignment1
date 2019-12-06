from repo.class_EmployeeRepository import EmployeeRepository
from repo.class_Aircraft_typeRepository import AircraftRepository
from repo.class_PastFlightsRepository import PastFlightsRepository
from models.class_employee import Employee
from repo.class_DestinationRepo import DestinationRepo
from services.class_employee_service import Employee_service
#from UI.mainUI import MainUI
#from services.class_upcoming_flightsIO import Upcoming_flightsIO

class ChangeUI():
    def __init__(self):  
        #self.__change_employee = EmployeeRepository()
        self.__change_employee = Employee_service()
        self.__show_dest = DestinationRepo()
        #self.__mainui = MainUI()
        #self.__show_dest = Destination_service()
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
            print(self.GO_BACK +"\n")
            print("'1' - Starfmann" + "\n" + "'2' - Vinnuferð" + "\n" + "'3' - Áfangastað" + "\n")
            change_input = input(self.USER_INPUT).lower()
            print()
 ################################## STARFSMENN VALINN ###########################################################       
            if change_input == "1":
                change_employee_input = ""
                print(self.GO_BACK +"\n") 
                employee_ssn_input = input("Kennitala starfsmanns: ")
                while employee_ssn_input != "r":
                    empl_info_lst = self.__change_employee.get_employee(employee_ssn_input)
                    while empl_info_lst == False:
                        print(self.GO_BACK +"\n") 
                        print("Starfmaður ekki til! Vitlaus kennitala.")
                        employee_ssn_input = input("Kennitala starfsmanns: ")
                        empl_info_lst = self.__change_employee.get_employee(employee_ssn_input)
                        if employee_ssn_input == "r":
                            self.change_menu()  
                    if change_employee_input != "r" :    
                        info_output = Employee(empl_info_lst)  
                        print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Breyta starfsmanni"))/2)*" " +  "Breyta starfsmanni"  +   "\n" + self.BORDER * self.WITDH )
                        print(self.PICK +"\n")
                        print(self.GO_BACK +"\n")  
                        print("Kennitala: {}".format(info_output.get_ssn()))        
                        print("Nafn: {}".format(info_output.get_name())) 
                        print("'1' - Starfsheiti: {}".format(info_output.get_role()))
                        print("'2' - Stöðugildi: {}".format(info_output.get_rank()))
                        print("'3' - Leyfi: {}".format(info_output.get_licence()))
                        print("'4' - Heimilisfang: {}".format(info_output.get_address()))
                        print("'5' - Símanúmer: {}".format(info_output.get_phone()))
                        print()
                        change_employee_input = input(self.USER_INPUT)   # Input what attribute you whant to change 
                        print()
                        if change_employee_input != "r":   # Go back if you dont whant to edit what you picked
                            print(self.GO_BACK +"\n")
                            the_change = input("Skráðu breytingu: ")
                            if the_change != "r":
                                print(self.__change_employee.change_employee(change_employee_input, the_change, employee_ssn_input))
                            else:
                                self.change_menu()   #til að fara til baka úr loopunni 
                        else:
                            self.change_menu()
                    else:
                        self.change_menu()
                else:
                    self.change_menu()
            
################################## VINNUFERÐ VALINN###########################################################
            if change_input == "2":
                pass
                while change_input != "r":
                    print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Breyta vinnuferð"))/2)*" " +  "Breyta vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
                    print(self.PICK +"\n")
                    print(self.GO_BACK +"\n")
                    print("Áfangastaður: {}".format(Voyage()))
                    print("Flugvél: {}".format(Voyage()))
                    print("'2' - Dagsetning og tími: {}".format(Voyage()))
                    print("'4' - Starfsmenn: {}".format(Voyage()))
                    change_input = input(self.USER_INPUT).lower()
################################## VINNUFERÐ VALINN###########################################################               
            if change_input == "3":
                while change_input != "r":
                    print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Breyta áfangastað"))/2)*" " +  "Breyta áfangastað"  +   "\n" + self.BORDER * self.WITDH )
                    print(self.PICK +"\n")
                    print(self.GO_BACK +"\n")
                    print(self.__show_dest.get_alldest())
                    #new_list = [destination,airportID,flight_time,distance,contact,emergency_phone]
                    #new_destination = destination(new_list)
                    #self.__new_destination.add_destination(new_employee)
                    change_input = input("Veldu áfangastað: ")
                    if change_input != "r":
                        print()
                        chosen_dest = self.__show_dest.get_dest_change(change_input) #tökum þá tölu sem notandi valdi og sendum í DestinationRepo og þar í get_dest fallið 
                        print(chosen_dest)
                        change_input = input(self.USER_INPUT).lower() # 1 eða 2 
                        
                else:
                    self.change_menu()
                #print("Áfangastaður ekki vistaður")
           
        #else:
        #    self.__mainui.main_menu()
  
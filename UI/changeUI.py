from repo.class_EmployeeRepository import EmployeeRepository
from repo.class_Aircraft_typeRepository import AircraftRepository
from repo.class_FlightRepository import FlightRepository
from models.class_employee import Employee
from repo.class_DestinationRepo import DestinationRepo
from services.class_employee_service import Employee_service
from models.class_destination import Destination
from services.class_destination_service import Destination_service
from services.class_voyage_service import Voyage_service
#from UI.mainUI import MainUI
#from services.class_upcoming_flightsIO import Upcoming_flightsIO

class ChangeUI():
    def __init__(self):  
        #self.__change_employee = EmployeeRepository()
        self.__change_employee = Employee_service()
        #self.__change_dest = DestinationRepo()
        self.__change_dest = Destination_service()
        self.__change_voyage = Voyage_service()
        #self.__mainui = MainUI()
        self.WITDH = 50
        self.BORDER = "*"
        self.QUIT = "'q' - Hætta"
        self.GO_BACK = "'r' - Til baka"
        self.PICK = "Veldu skipun:"
        self.USER_INPUT = ("Valin skipun: ")
        # self.change_menu()


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
            if change_input == "1":
                self.employee_menu()
            if change_input == "2":
                self.voyage_menu()
            if change_input == "3":
                self.destination_menu()
            if change_input == "r":
                change_input = "r"
            else:
                print("Vinsamlegast veldu eitt af eftir farandi möguleikum")
                
            

 ################################## STARFSMENN VALINN ###########################################################       
    def employee_menu(self):
        change_employee_input = ""
        print(self.GO_BACK +"\n") 
        employee_ssn_input = input("Kennitala starfsmanns: ")
        if employee_ssn_input != "r":
            empl_info_lst = self.__change_employee.get_employee(employee_ssn_input)
            if empl_info_lst != False:
                while change_employee_input != "r" :
                    empl_info_lst = self.__change_employee.get_employee(employee_ssn_input)    
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
                    if change_employee_input != "1" and change_employee_input != "2" and change_employee_input != "3" and change_employee_input != "4" and change_employee_input != "5" :
                        pass
                    else:
                                                # Go back if you dont whant to edit what you picked
                        print(self.GO_BACK +"\n")
                        the_change = input("Skráðu breytingu: ")
                        if the_change != "r":
                            save_input = ""
                            if save_input != "1" and save_input != "2": # Ef hvorki 2 né 1 er sleginn inn þá er aftur spurt um input 
                                print("\nViltu vista starfsmanninn \n'1' - Já: \n'2' - Nei: ")
                                save_input = input(str(self.USER_INPUT))
                                print()
                            if save_input == "1":  
                                print(self.__change_employee.change_employee(change_employee_input, the_change, employee_ssn_input))
                            else:
                                pass
                else:
                    print("Skipun ekki til. Vinsmlegast reyndu aftur!")
                    self.employee_menu()
            # else:
            #     self.change_menu()
            else:
                if employee_ssn_input == "r":
                    self.change_menu()      
                print("Starfmaður ekki til! Vitlaus kennitala.")
                self.employee_menu()    
                       
################################## VINNUFERÐ VALINN###########################################################
    def voyage_menu(self):
        pass
    #     while change_input != "r":
    #         print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Breyta vinnuferð"))/2)*" " +  "Breyta vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
    #         print(self.PICK +"\n")
    #         print(self.GO_BACK +"\n")
    #         print("Áfangastaður: {}".format(self.__change_voyage()))
    #         print("Flugvél: {}".format(self.__change_voyage()))
    #         print("'2' - Dagsetning og tími: {}".format(self.__change_voyage()))
    #         print("'4' - Starfsmenn: {}".format(self.__change_voyage()))
    #         change_input = input(self.USER_INPUT).lower()
################################## Áfangastað VALINN###########################################################               
    def destination_menu(self):
    
        print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Breyta áfangastað"))/2)*" " +  "Breyta áfangastað"  +   "\n" + self.BORDER * self.WITDH )
        print(self.PICK +"\n")
        prnt_str, counter = self.__change_dest.get_alldest()   # prentar út listan af öllum löndunum
        print(prnt_str)
        print(self.GO_BACK +"\n")
        change_input = input("Veldu áfangastað: ")      # nr á áfangastað 
        if change_input != "r":
            print()
            chosen_dest = self.__change_dest.get_dest(change_input) #tökum þá tölu sem notandi valdi og sendum í DestinationRepo og þar í get_dest fallið 
            output = Destination(chosen_dest)
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Breyta áfangastað"))/2)*" " +  "Breyta áfangastað"  +   "\n" + self.BORDER * self.WITDH )
            print(self.PICK +"\n")
            print(self.GO_BACK +"\n")
            print("Áfangastaður: {}".format(output.get_destinationName()))
            print("Flugvöllur: {}".format(output.get_destinationId()))
            print("Flugtími: {}".format(output.get_flighttime()))
            print("Fjarlægð: {}".format(output.get_distance()))
            print("'1' - Tengiliður: {}".format(output.get_contact()))
            print("'2' - Neyðarsímanúmer: {}".format(output.get_phone()))
            print()
            change_input = input(self.USER_INPUT).lower() # 1 eða 2  til að velja hvað á að breyta     
            print()
            if change_input == "1" or change_input == "2":  # contact
                the_change = input("Skráðu breytingu: ") 
                if the_change != "r":
                    save_input = ""
                    if save_input != "1" and save_input != "2": # Ef hvorki 2 né 1 er sleginn inn þá er aftur spurt um input 
                        print("\nViltu vista áfangastað \n'1' - Já: \n'2' - Nei: ")
                        save_input = input(str(self.USER_INPUT))
                        print()
                    if save_input == "1":
                        #print("Áfangastaður vistaður ")
                        print(self.__change_dest.change_dest(change_input, the_change, chosen_dest[0]))   # geri chosen dest til að taka bara nafnið á áfangastaðnum og senda inn í clasan
                                
                    else:
                        print("Áfangastaður ekki vistaður ")
                        self.destination_menu()
                else:
                    self.destination_menu()  
        else:
            self.destination_menu()
from repo.class_EmployeeRepository import EmployeeRepository
from repo.class_Aircraft_typeRepository import AircraftRepository
from repo.class_PastFlightsRepository import PastFlightsRepository
from models.class_employee import Employee
#from services.class_upcoming_flightsIO import Upcoming_flightsIO

class ChangeUI():
    def __init__(self):  
        self.__change_employee = EmployeeRepository()
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
                if employee_ssn_input != "r":
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
                        print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Breyta"))/2)*" " +  "Starfsmaður"  +   "\n" + self.BORDER * self.WITDH )
                        print(self.PICK +"\n")
                        print(self.GO_BACK +"\n")  
                        print("Kennitala: {}".format(info_output.get_ssn()))        
                        print("Nafn: {}".format(info_output.get_name())) 
                        print("'2' - Starfsheiti: {}".format(info_output.get_role()))
                        print("'3' - Stöðugildi: {}".format(info_output.get_rank()))
                        print("'4' - Leyfi: {}".format(info_output.get_licence()))
                        print("'5' - Heimilisfang: {}".format(info_output.get_address()))
                        print("'6' - Símanúmer: {}".format(info_output.get_phone()))
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
                    print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá vinnuferð"))/2)*" " +  "Nýskrá vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
                    print(self.PICK +"\n")
                    print(self.GO_BACK +"\n")
                    print("Áfangastaður: {}".format(Voyage()))
                    print("Flugvél: {}".format(Voyage()))
                    print("'2' - Dagsetning og tími: {}".format(Voyage()))
                    print("'4' - Starfsmenn: {}".format(Voyage()))
                    make_input = input(self.USER_INPUT).lower()
################################## VINNUFERÐ VALINN###########################################################               
            if change_input == "3":
                pass
            else:
                return "" 

    # ###########################################################################
    # ############################### change sub menu ###########################
    # ###########################################################################    
    # def change_menu(self):
    #     change_input = ""  # til að maður geti bakkað um 1 í stað þess að quita bara 
    #     while change_input != "r":
    #         print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Breyta"))/2)*" " +  "Breyta"  +   "\n" + self.BORDER * self.WITDH )
    #         print(self.PICK +"\n")
    #         print(self.QUIT+ " "*5 + self.GO_BACK +"\n")
    #         print("'1' - Starfmann" + "\n" + "'2' - Vinnuferð" + "\n" + "'3' - Áfangastað" + "\n")
    #         change_input = input(self.USER_INPUT).lower()
    #         print()
        
    #         if change_input == "1":
    #             pass
    #             employee_name_input = input("Kennitala starfsmanns: ")
    #             while employee_name_input != "r":
    #                #?? change_employee = change_input
    #                 while employee_name_input != "r":
    #                     print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Breyta"))/2)*" " +  "Starfsmaður"  +   "\n" + self.BORDER * self.WITDH )
    #                     print(self.PICK +"\n")              
    #                     print("Nafn: {}".format(crew_dictionary[employee_name_input][1])) 
    #                     print("Kennitölu: {}".format(crew_dictionary[employee_name_input][0]))
    #                     print("'1' - Starfsheiti: {}".format(crew_dictionary[employee_name_input][2]))
    #                     print("'2' - Staða: {}".format(crew_dictionary[employee_name_input][3]))
    #                     print("'3' - Leyfi: {}".format(crew_dictionary[employee_name_input][4]))
    #                     print("'4' - Heimilisfang: {}".format(crew_dictionary[employee_name_input][5]))
    #                     print("'5' - Símanúmer: {}".format(crew_dictionary[employee_name_input][6]))
    #                     print()
    #                     change_employee = input(USER_INPUT)   # Input what attribute you whant to change 
    #                     print()
    #                     if change_employee != "r":   # Go back if you dont whant to edit what you picked
    #                         change_crew(crew_dictionary, change_employee, employee_name_input)   
            

    #         if change_input == "2":
    #             pass
                
    #         if change_input == "3":
    #             pass
    #             destination_point_input = input("Nafn áfangastaðs: ")
    #             while destination_point_input != "r":
    #                 change_destination_point = change_input
    #                 while destination_point_input != "r":
    #                     print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Breyta"))/2)*" " +  "Áfangastaður"  +   "\n" + self.BORDER * self.WITDH )
    #                     print(self.PICK +"\n")     
    #                     print("'1' - Tengiliður: {}".format(#eithvað tengt class_destination point))
    #                     print("'2' - Neyðarsími: {}".format(#eitthvað tengt class_destination point))
            
    #         else:
    #             return None
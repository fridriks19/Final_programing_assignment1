
from models.class_employee import Employee
from services.class_employee_service import Employee_service
from models.class_destination import Destination
from services.class_destination_service import Destination_service
from services.class_voyage_service import Voyage_service
from services.class_upcoming_flight_service import Upcoming_flight_service
from services.class_voyage_crew_service import Voyage_crew_service

class ChangeUI():
    def __init__(self):  
        self.__change_employee = Employee_service()
        self.__change_dest = Destination_service()
        self.__change_voyage = Voyage_service()
        self.__get_upcflight = Upcoming_flight_service()
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
                        print("Vinsamlegast veldu það sem þú vilt breyta!")
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
            else:
                if employee_ssn_input == "r":
                    self.change_menu()      
                print("Starfmaður ekki til! Vitlaus kennitala.")
                self.employee_menu()    
                       
################################## VINNUFERÐ VALINN###########################################################
    def voyage_menu(self):
        change_input = ""
        while change_input != "r":
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Breyta vinnuferð"))/2)*" " +  "Breyta vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
            print(self.PICK +"\n")
            print(self.GO_BACK)
            print("'Enter' - Til að velja dagsetningu.")
            print()
            change_input = input("Viltu velja dagsetningu?")
            if change_input == "r":
                self.change_menu()
            a_prnt_str = "Veldu dagsetningu vinnuferðar sem þú vilt breyta"
            date = self.get_date_voyage(a_prnt_str)   # Fáum til baka dagsettningu á því formi sem við viljum svo hægt sé að leita af réttri ferð í csv skránni
            change_flight = self.__get_upcflight.get_upcomingflight(date)
            if change_flight == "Flug fannst ekki":
                print(change_flight)
            else:
                date1, date2 = self.__get_upcflight.get_upcoming_voyage(date)
                while change_input != "r":
                    print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Breyta vinnuferð"))/2)*" " +  "Breyta vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
                    print(self.PICK +"\n")
                    print(change_flight)
                    print()
                    print("Starfsmenn vinnuferðar")
                    print("'1' - Flugstjóri: {}".format(date1[6]))
                    print("'2' - Aðstoðarflugmaður:  {}".format(date1[7]))
                    print("'3' - Yfirflugþjónn: {}".format(date1[8]))
                    print("'4' - Flugþjónn 1: {}".format(date1[9]))
                    print("'5' - Flugþjónn 2: {}".format(date1[10]))
                    print(self.GO_BACK + "\n")
                    change_input = input(self.USER_INPUT).lower()
                    if change_input != "1" and change_input != "2" and change_input != "3" and change_input != "4" and change_input != "5": 
                        if change_input == "r":
                            self.voyage_menu()
                        else:
                            print("Vinsamlegast veldu starfsmann til að breyta/skrá í vinnuferð!") 
                            pass      
                    else: 
                        if change_input == "1":
                            print("Breyta/skrá  yfirflugmanni.")
                            capt_list = Voyage_crew_service(date1[3],date1[5]).get_captain()
                            if capt_list == []:
                                print("Engir lausir flugstjórar fyrir þessa vél, vinsamlegast veldu aðra vél")
                                pass
                            else:
                                print(self.__change_voyage.prnt_str(capt_list))
                                change_input = input(self.PICK)
                                print()
                                while change_input.isdigit() == False or int(change_input) > len(change_input) or int(change_input) < 1:
                                    print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Breyta vinnuferð"))/2)*" " +  "Breyta vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
                                    print(self.PICK +"\n")
                                    print("Veldu flugstjóra úr listanum!")
                                    print(self.__change_voyage.prnt_str(capt_list))
                                    change_input = input(self.PICK)
                                else:
                                    save_input = ""
                                    change_input = int(change_input)
                                    if save_input != "1" and save_input != "2":
                                        print(self.GO_BACK +"\n")
                                        print("Viltu vista flugstjóran? \n'1' - Já: \n'2' - Nei: ")
                                        save_input = input(str(self.USER_INPUT))
                                        print()
                                    if save_input == "1":
                                        change_input = int(change_input)-1
                                        date1[6] = capt_list[change_input][0]
                                        date2[6] = capt_list[change_input][0]
                                        print("Flugstjóri vistaður")
                                        print()
                                    else:
                                        empl_pick = "r"
                                        print("Flugstjóri ekki vistaður")

                        if change_input == "2":
                            print("Breyta/skrá  aðstoðarflugmanni.")
                            _list = Voyage_crew_service(date1[3],date1[5]).get_captain()
                            pass

                        if change_input == "3":
                            print("Breyta/skrá  yfirflugþjóni.")
                            pass

                        if change_input == "4":
                            print("Breyta/skrá flugþjóni 1.")
                            pass

                        if change_input == "5":
                            print("Breyta/skrá  flugjóni 2.")
                            pass

                



################################## Áfangastað VALINN###########################################################               


    def destination_menu(self):
        change_input = ""
        while change_input != "r":
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Breyta áfangastað"))/2)*" " +  "Breyta áfangastað"  +   "\n" + self.BORDER * self.WITDH )
            print(self.PICK +"\n")
            prnt_str, counter = self.__change_dest.get_alldest()   # prentar út listan af öllum löndunum
            print(prnt_str)
            print(self.GO_BACK +"\n")
            change_input = input("Valin skipun: ")      # nr á áfangastað 
            if change_input.isdigit() == False:  # if the user doesnt input a number then send him back
                if change_input == "r":
                    # self.change_menu()
                    change_input = "r"
                else:
                    print("Veldu áfangastað sem er í boði!")
                    self.destination_menu()
            elif change_input.isdigit() == True or int(change_input) >= 1 or int(change_input) <= int(counter):
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
                if change_input != "1" and change_input != "2":  # contact
                    pass
                else:
                    print(self.GO_BACK +"\n")
                    the_change = input("Skráðu breytingu: ") 
                    if the_change != "r":
                        save_input = ""
                        if save_input != "1" and save_input != "2": # Ef hvorki 2 né 1 er sleginn inn þá er aftur spurt um input 
                            print("\nViltu vista áfangastað \n'1' - Já: \n'2' - Nei: ")
                            save_input = input(str(self.USER_INPUT))
                            print()
                        if save_input == "1":
                            print("Áfangastaður vistaður ")
                            print(self.__change_dest.change_dest(change_input, the_change, chosen_dest[0]))   # geri chosen dest til að taka bara nafnið á áfangastaðnum og senda inn í clasan
                        else:
                            print("Áfangastaður ekki vistaður ")
                            pass
                    else:
                        print("Skipun ekki til. Vinsmlegast reyndu aftur!")
                        self.destination_menu()
            








    def get_date_voyage(self, prnt_str):
        print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Breyta vinnuferð"))/2)*" " +  "Breyta vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
        print(self.PICK +"\n")
        self.prnt_str = prnt_str
        print(prnt_str)   
        print()
        year = input("Sláðu inn ár: ")      #Input a year 
        while year.isdigit() == False:     # if its not a number then let them try again
            print("Vinsamlegast skráðu ár!")
            year = input("Sláðu inn ár: ")
        month = input("Sláðu inn númer mánaðar")
        while month.isdigit() == False:
            print("Vinsamlegast skráðu númer mánaðar!")
            month = input("Sláðu inn númer mánaðar: ")
        day = input("Sláðu inn dagsetningu: ")
        while day.isdigit() == False:
            print("Vinsamlegast skráðu dagsettningu!")
            day = input("Sláðu inn dagsettningu: ")
        hour = input("Sláðu inn klukkustund brottfarar: ")
        while hour.isdigit() == False:
            print("Vinsamlegast skráðu klukkutíma!")
            hour = input("Sláðu inn klukkustund brottfarar: ")
        mint = input("Sláðu inn mínútu brottfarar: ")
        while mint.isdigit() == False:
            print("Vinsamlegast skráðu mínútur!")
            mint = input("Sláðu inn mínútu brottfarar: ")
        user_chosen_date = [year,month,day,hour,mint,0]
        date = self.__get_upcflight.add_date(user_chosen_date)  # The date gets set to the right format in add_date
        return date
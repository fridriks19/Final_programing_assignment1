from models.class_pilot import pilot
from models.class_flight_attendant import flight_attendant
from services.class_employee_service import Employee_service
from models.class_destination import Destination
from services.class_destination_service import Destination_service
from services.class_aircraft_service import Aircraft_service
from services.class_voyage_service import Voyage_service
from services.class_voyage_crew_service import Voyage_crew_service
from services.class_aircraft_service import Aircraft_service
from models.class_voyage import Voyage
import datetime

#from services.class_upcoming_flightsIO import Upcoming_flightsIO

class MakeUIupd():
    def __init__(self):
        self.__new_employee = Employee_service()
        self.__new_destination = Destination_service()
        self.__new_aircraft = Aircraft_service()
        self.__new_voyage = Voyage_service()
        self.WITDH = 50
        self.BORDER = "*"
        self.QUIT = "'q' - Hætta"
        self.GO_BACK = "'r' - Til baka"
        self.PICK = "Veldu skipun:"
        self.USER_INPUT = ("Valin skipun: ")
        #self.make_menu()
    ###########################################################################
    ############################### Make sub menu #############################
    ###########################################################################  
    def make_menu(self):
        make_input = ""
        while make_input != "r":
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá"))/2)*" " +  "Nýskrá"  +   "\n" + self.BORDER * self.WITDH )
            print(self.PICK +"\n")
            print(self.GO_BACK +"\n")
            print("'1' - Starfsmann" + "\n" + "'2' - Áfangastað" + "\n" + "'3' - Vinnuferð" + "\n" ) 
            make_input = input(self.USER_INPUT).lower()
            print()
            if make_input != "r":
                if make_input == "1":
                    self.employee_menu()
                if make_input == "2":
                    self.destination_menu()
                if make_input == "3":
                    self.voyage_menu()
                # if make_input == "4":
                #     self.aircraft_menu()
                else:
                    print("Vinsamlegast veldu einn af eftifarandi valmöguleikum!")
            break
###################STARFSMAÐUR VALIN ################################################################################################################  
    def employee_menu(self):
        ''' The user can make a new employee which will either be a pilot or an flight attendant, and 
            the employee has to have a ssn,name,rank,liscence,address,phonenumber'''
        print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá starfsmann"))/2)*" " +  "Nýskrá starfsmann"  +   "\n" + self.BORDER * self.WITDH )
        print(self.PICK +"\n")
        print(self.GO_BACK +"\n")
        print ("'1' - Skrá flugmann" + "\n" + "'2' - Skrá flugþjón")  
        print()
        make_input = input(self.USER_INPUT).lower()
        if make_input == "r":
            self.make_menu()
        else:   
            while make_input != "1" and make_input != "2": 
                make_input = input(self.USER_INPUT).lower()
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá starfsmann"))/2)*" " +  "Nýskrá starfsmann"  +   "\n" + self.BORDER * self.WITDH ) 
            print(self.PICK +"\n")
            # new_list = EmployeeMaker()
            ssn = input("Kennitala: ")
            name = input("Nafn: ")
            rank = input("Stöðugildi: ")
            liscense = input("Réttindi: ")
            address = input("Heimilisfang: ")
            phonenumber = input("GSM-Sími: ")

            save_input = ""
            while save_input != "1" and save_input != "2": 
                print("\nViltu vista starfsmanninn \n'1' - Já \n'2' - Nei ")
                save_input = input(str(self.USER_INPUT))
                print()
            if save_input == "1":   #if the user chooses pilot
                if make_input == "1": 
                    role =  ""
                    new_list = [ssn,name,role,rank,liscense,address,phonenumber] 
                    new_employee = pilot(new_list)
                    self.__new_employee.add_employee(str(new_employee))
  
                elif make_input == "2": # if the user chooses flight attendant
                    role =  ""
                    new_list = [ssn,name,role,rank,liscense,address,phonenumber]
                    new_employee = flight_attendant(new_list)
                    self.__new_employee.add_employee(str(new_employee))

            else:
                print("Starfsmaður ekki vistaður")
                self.employee_menu() 
        
###################ÁFANGASTAÐUR VALIN ################################################################################################                  
    def destination_menu(self):
        ''' The user gets to "make" add a new destination to the system, and the destination must have 
            a destination name, flight time, distance to the destiation from KEF, contact and emergency phone number'''
        print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá áfangastað"))/2)*" " +  "Nýskrá áfangastað"  +   "\n" + self.BORDER * self.WITDH )
        print(self.PICK +"\n")
        print(self.GO_BACK +"\n")
        
        airportID = input("Flugvöllur: ")
        if airportID == "r":
            self.make_menu()
        else:    
            destination = input("Áfangastaður: ")
            flight_time = input("Flugtími: ")
            distance = input("Fjarlægð: ")
            contact = input("Tengiliður: ")
            emergency_phone = input("Neyðarsími: ")
            save_input = ""
            if save_input != "1" and save_input != "2": 
                print("\nViltu vista áfangastað \n'1' - Já: \n'2' - Nei: ")
                save_input = input(str(self.USER_INPUT))
                print()
            if save_input == "1":
                new_list = [airportID,destination,flight_time,distance,contact,emergency_phone]
                new_destination = Destination(new_list)
                self.__new_destination.add_destination(str(new_destination))
            else:
                print("Áfangastaður ekki vistaður")
                self.destination_menu()
                

###################VINNUFERÐ VALIN ################################################################################################################  
    def voyage_menu(self):
        ''' This is were the user can make a voyage. When making a voyage the user must first choose a destination, then he can
            choose a departing date, after that he can choose a aircraft and the system will shoe him if they are available or not, 
            then the user can add employees if he whants but he can also add them laiter, then finally he can choose to save the 
            voyage or not. '''
        self.chosen_destination = ""
        self.depart_voyage_info = ["flightnum1","KEF",2,3,4,5,"","","",""," "]   # We use "" to represent no employees
        self.arriv_voyage_info = ["flightnum2",1,"KEF",3,4,5,"","","",""," "]   #We know every single voyage starts at KEF and ends at KEF 
        make_input = ""
        while make_input != "r":
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá vinnuferð"))/2)*" " +  "Nýskrá vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
            print(self.PICK +"\n")
            print(self.GO_BACK +"\n")
            print("'1' - Áfangastaður")
            print("'2' - Dagsetning og tími")
            print("'3' - Flugvél")
            print("'4' - Starfsmenn")
            print("'5' - Vista vinnuferðina, án eða með starfsmönnum")
            print()
            make_input = input(self.USER_INPUT).lower()
            if make_input == "1":
                self.voyage_destination()
            if make_input == "2":
                self.voyage_date()
            if make_input == "3":
                self.voyage_aircraft()
            if make_input == "4":
                self.voyage_employees()
            if make_input == "5":
                self.save_voyage()
            if make_input == "r":
                self.make_menu()
                break
            if make_input != "1" or make_input != "2" or make_input != "3" or make_input != "4" or make_input != "r":
                print("Vinsamlegast veldu eitt af eftifarandi valmöguleikum!")

    def voyage_destination(self):
        ''' Choose the destination from a list of all the destinations in the systmen '''
        dest_input = ""
        print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá vinnuferð"))/2)*" " +  "Nýskrá vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
        print(self.PICK +"\n")
        print("Veldu áfangastað: ")
        all_dest_str, dest_counter = self.__new_destination.get_alldest()  #Prints a list of all the destinations
        print(all_dest_str)
        dest_input = input(self.USER_INPUT)
        if dest_input.isdigit() == False:  # if the user doesnt input a number then send him back
            if dest_input =="r":
                pass
            else:
                print("Veldu áfangastað sem er í boði")
                self.voyage_destination()
        elif int(dest_input) >= 1 and int(dest_input) <= int(dest_counter):   # or int(dest_input) == "r"
            print()
            user_chosen_dest = self.__new_destination.get_dest(dest_input)
            print("Áfangastaður: {}\nFlugvöllur: {}\nFlugtími: {}\nFjarlægð: {}\nTengiliður: {}\nNeyðarsímanúmer: {}".format(user_chosen_dest[1],user_chosen_dest[0], user_chosen_dest[2],user_chosen_dest[3],user_chosen_dest[4],user_chosen_dest[5]))
            save_input = ""
            if save_input != "1" and save_input != "2": 
                print("\nViltu velja þennan áfangastað \n'1' - Já \n'2' - Nei ")
                save_input = input(str(self.USER_INPUT))
                print()
            if save_input == "1":
                self.chosen_destination = self.__new_destination.get_dest(dest_input)  #LYR  self.chosen_destination[0]
                self.chosen_destination = self.chosen_destination[0] # We only need the destination ID
                self.chosen_destination

    def voyage_date(self):
        ''' Choose a departing date for the voyage and '''
        if self.chosen_destination =="":  # To make sure that there is a chosend destination to find out all the dates and times 
            print("Veldu fyrst áfangarstað")
        else:
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá dags/tíma vinnuferðar"))/2)*" " +  "Nýskrá dags/tíma vinnuferðar"  +   "\n" + self.BORDER * self.WITDH )
            print(self.PICK + "\n")
            print("Skráðu dagsetningu vinnuferðar: ")
            print()
            year = input("Sláðu inn ár: ")      #Input aa year 
            while year.isdigit() == False:     # if its not a number then let them try again
                print("Vinsamlegast skráðu ár!")
                year = input("Sláðu inn ár: ")
            month = input("Sláðu inn númer mánaðar: ")
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

            print()
            user_chosen_date = [year,month,day,hour,mint,0]
            self.depart_date = self.__new_voyage.add_date(user_chosen_date)   
            if self.depart_date != False:        # We check if the date is in a valid format and is in the future
                self.arrival_date = self.__new_voyage.get_arrival_time(self.chosen_destination,self.depart_date)  #date 2
                self.return_depart = self.__new_voyage.get_return_flight_time(self.chosen_destination, self.arrival_date)  #date3
                self.return_arrival = self.__new_voyage.get_arrival_time(self.chosen_destination,self.return_depart)  #date4
                print("Brottfarartími frá Íslandi:", datetime.datetime.strptime(self.depart_date, "%Y-%m-%dT%H:%M:%S"))
                print("Lendingartími á áfangarstað:",datetime.datetime.strptime(self.arrival_date, "%Y-%m-%dT%H:%M:%S"))
                print("Brottfarartími frá áfangarstað:",datetime.datetime.strptime(self.return_depart, "%Y-%m-%dT%H:%M:%S"))
                print("Lendingartími á Íslandi:",datetime.datetime.strptime(self.return_arrival,"%Y-%m-%dT%H:%M:%S"))
                print()
                save_input = ""

                if save_input != "1" and save_input != "2":
                    print(self.GO_BACK +"\n")
                    print("Viltu vista dagsetningar \n'1' - Já \n'2' - Nei ")
                    save_input = input(str(self.USER_INPUT))
                    print()
                if save_input == "1":   # If the user wants to save then all the dates are saved in two lists one for departing and other for arriving
                    self.depart_voyage_info[2] = self.chosen_destination 
                    self.depart_voyage_info[3] = self.depart_date
                    self.depart_voyage_info[4] = self.arrival_date
                    self.arriv_voyage_info[1] = self.chosen_destination
                    self.arriv_voyage_info[3] = self.return_depart
                    self.arriv_voyage_info[4] = self.return_arrival
                if save_input == "2":
                    self.voyage_date()  # send back
                    
            else:
                print("Ógild dagsettning vinsamlegast reyndu aftur.")

    def voyage_aircraft(self):
        ''' Choose a aircraft from the "all aircraft list " and in the list it says which aircrafts are free and which are not'''
        if self.arriv_voyage_info[4] == 4:
            print("Skráðu fyrst dagsetningu brottfarar.")
        else:
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá flugvél vinnuferðar"))/2)*" " +  "Nýskrá flugvél vinnuferðar"  +   "\n" + self.BORDER * self.WITDH )
            print(self.PICK +"\n")
            print(self.__new_voyage.print_avail_aircraft(self.depart_date,self.return_arrival))
            print(self.GO_BACK +"\n")
            air_choice = input("Veldu nafn flugvélar: ") 
            while air_choice != "r":
                valid_or_not = self.__new_voyage.is_valid_aircraft(air_choice,self.depart_date,self.return_arrival)    # checks if the aircraft you chose is in use or not
                if valid_or_not == True:    # if ture then the aircraft is not in use at this date
                    save_input = ""
                    if save_input != "1" and save_input != "2": 
                        print(self.GO_BACK +"\n")
                        print("Viltu vista flugvél? \n'1' - Já \n'2' - Nei ")
                        save_input = input(str(self.USER_INPUT))
                        print()
                        if save_input =="1":
                            self.depart_voyage_info[5] = air_choice
                            self.arriv_voyage_info[5] = air_choice
                            print("Flugvél vistuð.")
                            air_choice = "r"  # To go back automatically

                        else:
                            print("Flugvél ekki vistuð")
                            air_choice = "r"
                            
                else:
                    print("Vinsamlegast veldu lausa flugvél úr listanum!")
                    air_choice = "r"

    def voyage_employees(self):
        if self.chosen_destination =="":  # To make sure that there is a chosend destination to find out all the dates and times 
            print("Veldu fyrst áfangarstað!")
        if self.arriv_voyage_info[4] == 4:
            print("Skráðu fyrst dagsetningu brottfarar!")
        if self.arriv_voyage_info[5] == 5:
            print("Skráðu fyrst flugvél vinnuferðar!")
        else:
            empl_pick =""
            while empl_pick != "r":
                print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá starfsmenn vinnuferðar"))/2)*" " +  "Nýskrá starfsmenn vinnuferðar"  +   "\n" + self.BORDER * self.WITDH )
                print(self.PICK +"\n")
                print("'1' - Veldu flugstjóra")
                print("'2' - Veldu aðstoðarflugmann")
                print("'3' - Veldu yfir flugþjón")
                print("'4' - Veldu flugþjón 2")
                print("'5' - Veldu flugþjón 3")
                print()
                print(self.GO_BACK + "\n")
                #We use the datetime to get rid of the T so we can send a normal date to the service
                empl_pick = input(self.USER_INPUT)
                print()
                if empl_pick == "1":
                    capt_list = Voyage_crew_service(self.depart_voyage_info[3],self.depart_voyage_info[5]).get_captain()  # Send the departure date and the aircraft choice to get the pilots that are available on that date and have a liscence on that plane 
                    if capt_list == []:
                        print("Engir lausir flugstjórar fyrir þessa vél, vinsamlegast veldu aðra vél")
                        pass
                    else: 
                        print(self.__new_voyage.prnt_str(capt_list))    #Prints a list of all available captains that are free and have licence on this aircraft
                        empl_pick = input(self.PICK) 
                        print()
                        while empl_pick.isdigit() == False or int(empl_pick) > len(capt_list) or int(empl_pick) < 1:  # the inputed integer has to be in the capt list range
                            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá starfsmenn vinnuferðar"))/2)*" " +  "Nýskrá starfsmenn vinnuferðar"  +   "\n" + self.BORDER * self.WITDH )
                            print(self.PICK +"\n")
                            print("Veldu flugstjóra úr listanum!")
                            print(self.__new_voyage.prnt_str(capt_list))
                            empl_pick = input(self.PICK) 

                        else: 
                            save_input = ""
                            empl_pick =int(empl_pick)
                            if save_input != "1" and save_input != "2": 
                                print(self.GO_BACK +"\n")
                                print("Viltu vista flugstjóran? \n'1' - Já \n'2' - Nei ")
                                save_input = input(str(self.USER_INPUT))
                                print()
                                if save_input =="1":
                                    empl_pick = int(empl_pick)-1  #-1 because in lists we count from 0 and up 
                                    self.depart_voyage_info[6] = capt_list[empl_pick][0]
                                    self.arriv_voyage_info[6] = capt_list[empl_pick][0]
                                    print("Flugstjóri vistaður")
                                    print()
                                else:
                                    empl_pick = "r"
                                    print("Flugstjóri ekki vistaður")

                if empl_pick == "2":  # Copilot
                    copilot_list = Voyage_crew_service(self.depart_voyage_info[3],self.depart_voyage_info[5]).get_copilot()
                    if copilot_list == []:
                        print("Engir lausir aðstoðarflugmenn fyrir þessa vél, vinsamlegast veldu aðra vél")
                        pass
                    else:
                        print(self.__new_voyage.prnt_str(copilot_list))
                        empl_pick = input(self.PICK) 
                        print()
                        while empl_pick.isdigit() == False or int(empl_pick) > len(copilot_list) or int(empl_pick) < 1:  # the inputed integer has to be in the capt list range
                            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá starfsmenn vinnuferðar"))/2)*" " +  "Nýskrá starfsmenn vinnuferðar"  +   "\n" + self.BORDER * self.WITDH )
                            print(self.PICK +"\n")
                            print("Veldu aðstoðarflugmann úr listanum!")
                            print(self.__new_voyage.prnt_str(copilot_list))
                            empl_pick = input(self.PICK) 

                        else: 
                            save_input = ""
                            empl_pick =int(empl_pick)
                            if save_input != "1" and save_input != "2": 
                                print(self.GO_BACK +"\n")
                                print("Viltu vista aðstoðarflugmann? \n'1' - Já \n'2' - Nei ")
                                save_input = input(str(self.USER_INPUT))
                                print()
                                if save_input =="1":
                                    empl_pick = int(empl_pick)-1  
                                    self.depart_voyage_info[7] = copilot_list[empl_pick][0]
                                    self.arriv_voyage_info[7] = copilot_list[empl_pick][0]
                                    print("Aðstoðarflugmaður vistaður")
                                    print()
                                else:
                                    empl_pick = "r"
                                    print("Aðstoðarflugmaður ekki vistaður")

                if empl_pick == "3":
                    flight_service_m_list = Voyage_crew_service(self.depart_voyage_info[3],self.depart_voyage_info[5]).get_fsm()
                    if flight_service_m_list == []:
                        print("Engir lausir yfirflugþjónar fyrir þetta flug, vinsamlegast velud aðra dagsettningu ")
                        pass
                    else:
                        print(self.__new_voyage.prnt_str(flight_service_m_list))
                        empl_pick = input(self.PICK) 
                        print()
                        while empl_pick.isdigit() == False or int(empl_pick) > len(flight_service_m_list) or int(empl_pick) < 1:  # the inputed integer has to be in the capt list range
                            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá starfsmenn vinnuferðar"))/2)*" " +  "Nýskrá starfsmenn vinnuferðar"  +   "\n" + self.BORDER * self.WITDH )
                            print(self.PICK +"\n")
                            print("Veldu yfirflugþjón úr listanum!")
                            print(self.__new_voyage.prnt_str(flight_service_m_list))
                            empl_pick = input(self.PICK) 

                        else: 
                            save_input = ""
                            empl_pick =int(empl_pick)
                            if save_input != "1" and save_input != "2": # Ef hvorki 2 né 1 er sleginn inn þá er aftur spurt um input 
                                print(self.GO_BACK +"\n")
                                print("Viltu vista yfirflugþjóninn? \n'1' - Já \n'2' - Nei ")
                                save_input = input(str(self.USER_INPUT))
                                print()
                                if save_input =="1":
                                    empl_pick = int(empl_pick)-1  # þar sem staðsetningar í lista telja frá 0 og upp ekki 1 og upp
                                    self.depart_voyage_info[8] = flight_service_m_list[empl_pick][0]
                                    self.arriv_voyage_info[8] = flight_service_m_list[empl_pick][0]
                                    print("Yfirflugþjónn vistaður")
                                    print()
                                else:
                                    empl_pick = "r"
                                    print("Yfirflugþjón ekki vistaður")

                if empl_pick == "4":
                    flight_attendant_list = Voyage_crew_service(self.depart_voyage_info[3],self.depart_voyage_info[5]).get_fa()
                    if flight_attendant_list == []:
                        print("Engir lausir flugþjónar fyrir fyrir þetta flug, vinsamlegast velud aðra dagsettningu")
                        pass
                    else:
                        print(self.__new_voyage.prnt_str(flight_attendant_list))
                        empl_pick = input(self.PICK) 
                        print()
                        while empl_pick.isdigit() == False or int(empl_pick) > len(flight_attendant_list) or int(empl_pick) < 1:  # the inputed integer has to be in the capt list range
                            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá starfsmenn vinnuferðar"))/2)*" " +  "Nýskrá starfsmenn vinnuferðar"  +   "\n" + self.BORDER * self.WITDH )
                            print(self.PICK +"\n")
                            print("Veldu yfirflugþjón úr listanum!")
                            print(self.__new_voyage.prnt_str(flight_attendant_list))
                            empl_pick = input(self.PICK) 

                        else: 
                            save_input = ""
                            empl_pick =int(empl_pick)
                            if save_input != "1" and save_input != "2": # Ef hvorki 2 né 1 er sleginn inn þá er aftur spurt um input 
                                print(self.GO_BACK +"\n")
                                print("Viltu vista yfirflugþjóninn? \n'1' - Já \n'2' - Nei ")
                                save_input = input(str(self.USER_INPUT))
                                print()
                                if save_input =="1":
                                    empl_pick = int(empl_pick)-1  # þar sem staðsetningar í lista telja frá 0 og upp ekki 1 og upp
                                    self.depart_voyage_info[9] = flight_attendant_list[empl_pick][0]
                                    self.arriv_voyage_info[9] = flight_attendant_list[empl_pick][0]
                                    print("Yfirflugþjónn vistaður")
                                    print()
                                else:
                                    empl_pick = "r"
                                    print("Yfirflugþjón ekki vistaður")
                if empl_pick == "5":
                    flight_attendant_list = Voyage_crew_service(self.depart_voyage_info[3],self.depart_voyage_info[5]).get_fa()
                    if flight_attendant_list == []:
                        print("Engir lausir aðstoðarflugmenn fyrir fyrir þetta flug, vinsamlegast velud aðra dagsettningu")
                        pass
                    else:
                        print(self.__new_voyage.prnt_str(flight_attendant_list))
                        empl_pick = input(self.PICK) 
                        print()
                        while empl_pick.isdigit() == False or int(empl_pick) > len(flight_attendant_list) or int(empl_pick) < 1:  # the inputed integer has to be in the capt list range
                            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá starfsmenn vinnuferðar"))/2)*" " +  "Nýskrá starfsmenn vinnuferðar"  +   "\n" + self.BORDER * self.WITDH )
                            print(self.PICK +"\n")
                            print("Veldu yfirflugþjón úr listanum!")
                            print(self.__new_voyage.prnt_str(flight_attendant_list))
                            empl_pick = input(self.PICK) 

                        else: 
                            save_input = ""
                            empl_pick =int(empl_pick)
                            if save_input != "1" and save_input != "2": # Ef hvorki 2 né 1 er sleginn inn þá er aftur spurt um input 
                                print(self.GO_BACK +"\n")
                                print("Viltu vista yfirflugþjóninn? \n'1' - Já: \n'2' - Nei: ")
                                save_input = input(str(self.USER_INPUT))
                                print()
                                if save_input =="1":
                                    empl_pick = int(empl_pick)-1  # þar sem staðsetningar í lista telja frá 0 og upp ekki 1 og upp
                                    self.depart_voyage_info[10] = flight_attendant_list[empl_pick][0]
                                    self.arriv_voyage_info[10] = flight_attendant_list[empl_pick][0]
                                    print("Yfirflugþjónn vistaður")
                                    print()
                                else:
                                    empl_pick = "r"
                                    print("Yfirflugþjón ekki vistaður")    

    def save_voyage(self):
        #First the user has to pick a destination, date and aricraft so that he can save the voyage 
        if self.arriv_voyage_info[5] == 5:
            print("Skráðu fyrst flugvél vinnuferðar!")   
        elif self.arriv_voyage_info[4] == 4:
            print("Skráðu fyrst dagsetningu brottfarar!")
        elif self.chosen_destination =="":  # To make sure that there is a chosend destination to find out all the dates and times 
            print("Veldu fyrst áfangarstað!")
        else:
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá starfsmenn vinnuferðar"))/2)*" " +  "Nýskrá starfsmenn vinnuferðar"  +   "\n" + self.BORDER * self.WITDH )
            print(self.PICK +"\n")
            print("Viltu vista vinnuferð með eftirfarandi upplýsingum?")
            print()
            print("Brottfarartími frá Íslandi: {}".format(self.depart_voyage_info[1]))
            print("Lendingartími á áfangarstað: {}".format(self.depart_voyage_info[2]))
            print("Brottfarartími frá áfangarstað: {}".format(self.arriv_voyage_info[3]))
            print("Lendingartími á Íslandi: {}".format(self.arriv_voyage_info[4]))
            print("Flugvél: {}".format(self.depart_voyage_info[5]))
            print("Flugstjóri: {}".format(self.depart_voyage_info[6]))
            print("Aðstoðarflugmaður: {}".format(self.depart_voyage_info[7]))
            print("Yfir flugþjónn: {}".format(self.depart_voyage_info[8]))
            print("Flugþjónn: {}".format(self.depart_voyage_info[9]))
            print("Flugþjónn 3: {}".format(self.depart_voyage_info[10]))
            print()
            save_input = ""
            if save_input != "1" and save_input != "2": # Ef hvorki 2 né 1 er sleginn inn þá er aftur spurt um input 
                print(self.GO_BACK +"\n")
                print("Viltu vista Vinnuferð \n'1' - Já \n'2' - Nei ")
                save_input = input(str(self.USER_INPUT))
                print()
                if save_input =="1":
                    flight_nums = self.__new_voyage.add_flight_nums(self.depart_voyage_info[2]) # adds flight numbers to the voyage
                    self.depart_voyage_info[0] = flight_nums[0]
                    self.arriv_voyage_info[0] = flight_nums[1]
                    the_voyage_str = Voyage(self.depart_voyage_info, self.arriv_voyage_info) #turn the lists into to strings 
                    self.__new_voyage.add_voyage(str(the_voyage_str))
                
                else:
                    print("Vinnuferð ekki vistuð.")
                    self.voyage_menu()

            
###################################################################################################################################  

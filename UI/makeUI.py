from models.class_pilot import pilot
from models.class_flight_attendant import flight_attendant
from services.class_employee_service import Employee_service
from repo.class_voyageRepo import VoyageRepo
from models.class_destination import Destination
from services.class_destination_service import Destination_service
from services.class_aircraft_service import Aircraft_service
from services.class_voyage_service import Voyage_service
import datetime

#from services.class_upcoming_flightsIO import Upcoming_flightsIO

class MakeUI():
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
    ###########################################################################
    ############################### Make sub menu #############################
    ###########################################################################  
    def make_menu(self):
        make_input = ""
        while make_input != "r":
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá"))/2)*" " +  "Nýskrá"  +   "\n" + self.BORDER * self.WITDH )
            print(self.PICK +"\n")
            print(self.GO_BACK +"\n")
            print("'1' - Starfmann" + "\n" + "'2' - Áfangastað" + "\n" + "'3' - Vinnuferð" + "\n" + "'4' - Flugvél" + "\n")
            make_input = input(self.USER_INPUT).lower()
            print()
###################STARFSMAÐUR VALIN ################################################################################################################  
            if make_input == "1":
                    print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá starfsmann"))/2)*" " +  "Nýskrá starfsmann"  +   "\n" + self.BORDER * self.WITDH )
                    print(self.PICK +"\n")
                    print(self.GO_BACK +"\n")
                    print ("'1' - Skrá flugmann" + "\n" + "'2' - Skrá flugþjón")   #Gefur valmöguleika um hvort það vilji skrá flugmann eða flugþjón
                    make_input = input(self.USER_INPUT).lower()
                    while make_input != "1" and make_input != "2":  # Svo það sé einungis hægt að velja 1 eða 2 til að halda áfram
                        make_input = input(self.USER_INPUT).lower()
                        

                    print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá starfsmann"))/2)*" " +  "Nýskrá starfsmann"  +   "\n" + self.BORDER * self.WITDH ) 
                    print(self.PICK +"\n")
                    # new_list = EmployeeMaker()
                    ssn = input("Kennitala: ")
                    name = input("Nafn: ")
                    rank = input("Stöðugildi: ")
                    liscense = input("Réttindi: ")
                    address = input("Heimilisfang: ")
                    phonenumber = input("GSM-Sími:")

                    save_input = ""
                    if save_input != "1" and save_input != "2": # Ef hvorki 2 né 1 er sleginn inn þá er aftur spurt um input 
                        print("\nViltu vista starfsmanninn \n'1' - Já: \n'2' - Nei: ")
                        save_input = input(str(self.USER_INPUT))
                        print()
                    if save_input == "1":   
                        if make_input == "1": #Ef það er valið flugmann
                            print("Starfsmaður vistaður")
                            role =  ""
                            new_list = [ssn,name,role,rank,liscense,address,phonenumber] #Gerum lista með öllum inputunum og sendum í pilot clasan og síðan öddum við employe-inum í csv fileið
                            new_employee = pilot(new_list)
                            self.__new_employee.add_employee(str(new_employee))
                        elif make_input == "2": #Ef það er valið flugþjón
                            print("Starfsmaður vistaður")
                            role =  ""
                            new_list = [ssn,name,role,rank,liscense,address,phonenumber]
                            new_employee = flight_attendant(new_list)
                            self.__new_employee.add_employee(str(new_employee))
                    else:
                        print("Starfsmaður ekki vistaður")
                        make_input = "1"  #Ef það er valið nei við að vista upplýsngar er notandi sendur aftur til baka á nýskrá síðu.
                
 ###################ÁFANGASTAÐUR VALIN ################################################################################################                  
            elif make_input == "2":
                print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá áfangastað"))/2)*" " +  "Nýskrá áfangastað"  +   "\n" + self.BORDER * self.WITDH )
                print(self.PICK +"\n")
                print(self.GO_BACK +"\n")
                airportID = input("Flugvöllur: ")
                destination = input("Áfangastaður: ")
                flight_time = input("Flugtími: ")
                distance = input("Fjarlægð: ")
                contact = input("Tengiliður: ")
                emergency_phone = input("Neyðarsími: ")
                save_input = ""
                if save_input != "1" and save_input != "2": # Ef hvorki 2 né 1 er sleginn inn þá er aftur spurt um input 
                    print("\nViltu vista áfangastað \n'1' - Já: \n'2' - Nei: ")
                    save_input = input(str(self.USER_INPUT))
                    print()
                if save_input == "1":
                    new_list = [destination,airportID,flight_time,distance,contact,emergency_phone]
                    new_destination = Destination(new_list)
                    print(new_destination)
                    self.__new_destination.add_destination(str(new_destination))
                else:
                    print("Áfangastaður ekki vistaður")

###################VINNUFERÐ VALIN ################################################################################################################  
            elif make_input == "3":
                chosen_destination = ""
                depart_voyage_info = [0,"KEF",2,3,4,5,"","","","",""]   # Höfum autt("") fyrir starfsmenn svo hægt sé að fylla inn í seinna 
                arriv_voyage_info = [0,1,"KEF",3,4,5,"","","","",""]
                while make_input != "r":
                    print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá vinnuferð"))/2)*" " +  "Nýskrá vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
                    print(self.PICK +"\n")
                    print(self.GO_BACK +"\n")
                    print("'1' - Áfangastaður")
                    print("'2' - Dagsetning og tími")
                    print("'3' - Flugvél")
                    print("'4' - Starfsmenn")
                    print(chosen_destination)
                    make_input = input(self.USER_INPUT).lower()
                    if make_input == "1":  # Arriving at 
                        print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá vinnuferð"))/2)*" " +  "Nýskrá vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
                        print(self.PICK +"\n")
                        print("Veldu áfangastað: ")
                        self.__new_destination.get_alldest()  # prentum út öll löndin svo user getur valið áfangastað
                        make_input = input("Veldu áfangastað: ")
                        print()
                        user_chosen_dest = self.__new_destination.get_dest(make_input) # Sendum valið frá user í get_dest til að láta destinationið í listan sem heldur utan um allar upplýsingar um vinnuferð
                        print("Áfangastaður: {}\nFlugvöllur: {}\nFlugtími: {}\nFjarlægð: {}\nTengiliður: {}\nNeyðarsímanúmer: {}".format(user_chosen_dest[1],user_chosen_dest[0], user_chosen_dest[2],user_chosen_dest[3],user_chosen_dest[4],user_chosen_dest[5]))
                        save_input = ""
                        if save_input != "1" and save_input != "2": # Ef hvorki 2 né 1 er sleginn inn þá er aftur spurt um input 
                            print("\nViltu velja þennan áfangastað \n'1' - Já: \n'2' - Nei: ")
                            save_input = input(str(self.USER_INPUT))
                            print()
                        if save_input == "1":
                            chosen_destination = self.__new_destination.get_dest(make_input)  #LYR  chosen_destination[0]
                            chosen_destination = chosen_destination[0] # We only need the destination ID
                            print(chosen_destination)
                    elif make_input == "2": # DATE/TIME
                        if chosen_destination =="":  # To make sure that there is a chosend destination to find out all the dates and times 
                            print("Veldu fyrst áfangarstað")
                        else:
                            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá dags/tíma vinnuferðar"))/2)*" " +  "Nýskrá dags/tíma vinnuferðar"  +   "\n" + self.BORDER * self.WITDH )
                            print("Skráðu dagsetningu vinnuferðar: ")
                            print()
                            year = input("Sláðu inn ár: ")      #Input aa year 
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

                            print()
                            user_chosen_date = [year,month,day,hour,mint,0]
                            depart_date = self.__new_voyage.add_date(user_chosen_date)   # dat1
                            if depart_date != False:
                                arrival_date = self.__new_voyage.get_arrival_time(chosen_destination,depart_date)  #date 2
                                return_depart = self.__new_voyage.get_return_flight_time(chosen_destination, arrival_date)  #date3
                                return_arrival = self.__new_voyage.get_arrival_time(chosen_destination,return_depart)  #date4
                                print("Brottfarartími frá Íslandi:", datetime.datetime.strptime(depart_date, "%Y-%m-%dT%H:%M:%S"))
                                print("Lendingartími á áfangarstað:",datetime.datetime.strptime(arrival_date, "%Y-%m-%dT%H:%M:%S"))
                                print("Brottfarartími frá áfangarstað:",datetime.datetime.strptime(return_depart, "%Y-%m-%dT%H:%M:%S"))
                                print("Lendingartími á Íslandi:", datetime.datetime.strptime(return_arrival, "%Y-%m-%dT%H:%M:%S"))
                                save_input = ""
                                if save_input != "1" and save_input != "2": # Ef hvorki 2 né 1 er sleginn inn þá er aftur spurt um input 
                                    print(self.GO_BACK +"\n")
                                    print("\nViltu vista dagsetningar \n'1' - Já: \n'2' - Nei: ")
                                    save_input = input(str(self.USER_INPUT))
                                    print()
                                if save_input == "1":   # ef .að er saveað þá fyllum við í listana með viðeigandi upplýsingum 
                                    depart_voyage_info[2] = chosen_destination 
                                    depart_voyage_info[3] = depart_date
                                    depart_voyage_info[4] = arrival_date
                                    arriv_voyage_info[1] = chosen_destination
                                    arriv_voyage_info[3] = return_depart
                                    arriv_voyage_info[4] = return_arrival
                                else:
                                    make_input =="3"   # senda til baka 

                            else:
                                print("Ógild dagsettning vinsamlegast reyndu aftur.")

                    elif make_input == "3":
                        print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá flugvél vinnuferðar"))/2)*" " +  "Nýskrá flugvél vinnuferðar"  +   "\n" + self.BORDER * self.WITDH )
                        print(self.PICK +"\n")
                        print(self.__new_voyage.print_avail_aircraft(depart_date,return_arrival))
                        print("Veldu nafn flugvélar")
                        aircraft_choice = input("TF-:")  # aafs   AAA
                        


                    elif make_input =="4":
                        print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá starfsmenn vinnuferðar"))/2)*" " +  "Nýskrá starfsmenn vinnuferðar"  +   "\n" + self.BORDER * self.WITDH )
                        print(self.PICK +"\n")


###################FLUGVÉL VALIN ################################################################################################################  
            elif make_input == "4":
                print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá flugvél"))/2)*" " +  "Nýskrá flugvél"  +   "\n" + self.BORDER * self.WITDH )
                print(self.PICK +"\n")
                print(self.GO_BACK +"\n")
                print("Veldu tegund")
                print("'1' - NAFokkerF100")
                print("'2' - NABAE146")
                print("'3' - NAFokkerF28")
                make_input 

                Planetypeid = input("Nafn: ")
                manufacturer = input("Framleiðandi: ")
                model = input("Tegund: ")
                capacity = input("Fjöldi farþegasæta: ")

                
###################FLUG OG VINNUTÍMAR VALIN ################################################################################################################  

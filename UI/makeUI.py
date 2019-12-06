from repo.class_EmployeeRepository import EmployeeRepository
from repo.class_Aircraft_typeRepository import AircraftRepository
from repo.class_PastFlightsRepository import PastFlightsRepository
from models.class_pilot import pilot
from models.class_flight_attendant import flight_attendant
from services.class_employee_service import Employee_service
from repo.class_DestinationRepo import DestinationRepo
from repo.class_voyageRepo import VoyageRepo


#from services.class_upcoming_flightsIO import Upcoming_flightsIO

class MakeUI():
    def __init__(self):
        
        self.__new_employee = Employee_service()
        self.__show_dest = DestinationRepo()
        self.__new_voyage = VoyageRepo()
        #self.__new_destination = DestinationRepository()
        self.__new_aircraft = AircraftRepository()
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
            print("'1' - Starfmann" + "\n" + "'2' - Áfangastað" + "\n" + "'3' - Vinnuferð" + "\n" + "'4' - Flugvél" + "\n" + "'5' - Flug/vinnutímar" + "\n")
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
                        print("Viltu vista starfsmanninn \n'1' - Já: \n'2' - Nei: ")
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
                destination = input("Áfangastaður: ")
                airportID = input("Flugvöllur: ")
                flight_time = input("Flugtími: ")
                distance = input("Fjarlægð: ")
                contact = input("Tengiliður: ")
                emergency_phone = input("Neyðarsími: ")

###################VINNUFERÐ VALIN ################
            if make_input == "3":
                print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá vinnuferð"))/2)*" " +  "Nýskrá vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
                print(self.PICK +"\n")
                voyage_list = []
                print("'1' - Áfangastaður")
                date_time = "'2' - Dagsetning og tími"
                airplane = "'3' - Flugvél"
                employee = "'4' - Starfsmenn"
                make_input = input(self.USER_INPUT).lower()
                if make_input == "1":
                    save_input = ""
                if save_input != "1" and save_input != "2": # Ef hvorki 2 né 1 er sleginn inn þá er aftur spurt um input 
                    save_input = input(str("Viltu vista vinnuferð? \n'1' - Já: \n'2' - Nei: "))
                if save_input == "1":
                    new_list = [destination,airportID,flight_time,distance,contact,emergency_phone]
                    new_destination = destination(new_list)
                    self.__new_destination.add_destination(new_employee)
                else:
                    print("Áfangastaður ekki vistaður")

###################VINNUFERÐ VALIN ################################################################################################################  
            elif make_input == "3":
                while make_input != "r":
                    print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá vinnuferð"))/2)*" " +  "Nýskrá vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
                    print(self.PICK +"\n")
                    print(self.GO_BACK +"\n")
                    print("'1' - Áfangastaður")
                    print("'2' - Dagsetning og tími")
                    print("'3' - Flugvél")
                    print("'4' - Starfsmenn")
                    make_input = input(self.USER_INPUT).lower()

                    if make_input == "1":  # Arriving at 
                        print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá vinnuferð"))/2)*" " +  "Nýskrá vinnuferð"  +   "\n" + self.BORDER * self.WITDH )
                        print(self.PICK +"\n")
                        print("Veldu áfangastað: ")
                        self.__show_dest.get_alldest()  # prentum út öll löndin svo user getur valið áfangastað
                        make_input = input("Veldu áfangastað: ")
                        print()
                        chosen_dest = self.__show_dest.get_dest(make_input) # Sendum valið frá user í get_dest til að láta destinationið í listan sem heldur utan um allar upplýsingar um vinnuferð
                        print(chosen_dest)

                    elif make_input == "2": # DATE/TIME
                        print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá dags/tíma vinnuferðar"))/2)*" " +  "Nýskrá dags/tíma vinnuferðar"  +   "\n" + self.BORDER * self.WITDH )
                        print(self.PICK +"\n")
                    
                    elif make_input == "3":
                        print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá flugvél vinnuferðar"))/2)*" " +  "Nýskrá flugvél vinnuferðar"  +   "\n" + self.BORDER * self.WITDH )
                        print(self.PICK +"\n")
                    
                    elif make_input =="4":
                        print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá starfsmenn vinnuferðar"))/2)*" " +  "Nýskrá starfsmenn vinnuferðar"  +   "\n" + self.BORDER * self.WITDH )
                        print(self.PICK +"\n")


###################FLUGVÉL VALIN ################################################################################################################  
            elif make_input == "4":
                print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá flugvél"))/2)*" " +  "Nýskrá flugvél"  +   "\n" + self.BORDER * self.WITDH )
                print(self.PICK +"\n")
###################FLUG OG VINNUTÍMAR VALIN ################################################################################################################  
            elif make_input == "5":
                print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Nýskrá flug/vinnutíma"))/2)*" " +  "Nýskrá flug/vinnutíma"  +   "\n" + self.BORDER * self.WITDH )
                print(self.PICK +"\n")
                pass
        else:
            return ""

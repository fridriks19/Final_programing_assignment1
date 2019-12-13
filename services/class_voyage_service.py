from models.class_flight import Flight
from repo.class_FlightRepository import FlightRepository
from services.class_upcoming_flight_service import Upcoming_flight_service
from services.class_destination_service import Destination_service
from services.class_aircraft_service import Aircraft_service
import datetime

class Voyage_service:

    def __init__(self):
        self.flights = FlightRepository()
        self.dest_list = Destination_service().get_all_dest_list()
        self.upcflights = Upcoming_flight_service()

    def add_date(self, date_list):
        '''Returns input date as a valid datetime string'''
        self.date_list = date_list
        year = int(self.date_list[0])
        month = int(self.date_list[1])
        day = int(self.date_list[2])
        hours = int(self.date_list[3])
        mins = int(self.date_list[4])
        secs = int(self.date_list[5])
        try:
            date = datetime.datetime(year,month,day,hours,mins,secs)
        except ValueError:
            return False
        if Voyage_service().is_valid_date(date):
           return date.strftime("%Y-%m-%dT%H:%M:%S")
        else:
            return False
    
    def is_valid_date(self, date):
        '''Checks if date is not set after today so 
            you can't make a voyage that departs after today'''
        self.date = date
        if self.date >= date.today():
            return True
        else:
            return False

    def add_voyage(self, voyage_str):
        '''Sends the voyage string to the Upcoming Flight Repository'''
        self.voyage_str = voyage_str
        # Checks for valid input before sending to the repository
        if self.is_valid_voyage(voyage_str):
            self.flights.add_upcomingflight(voyage_str)

    def get_voyage(self, voyage_dep, voyage_arr):
        '''Finds a voyage and returns a formatted string with info for a selected voyage'''
        self.voyage_dep = voyage_dep
        self.voyage_arr = voyage_arr
        voyage_list = self.flights.get_upcomingflights()
        selected_voyage_list = []
        for flight in voyage_list:
            # Gets both flights for the selected voyage
            next_flight = voyage_list.index(flight) + 1
            if flight[3] == self.voyage_dep:
                if voyage_list[next_flight][3] == self.voyage_arr:
                    selected_voyage_list.append(flight)
                    selected_voyage_list.append(voyage_list[next_flight])
        printable_selected_voyage_list = Voyage_service().print_voyage(selected_voyage_list)
        return printable_selected_voyage_list
    
    def is_valid_aircraft(self, chosen_aircr, date1, date2):
        '''Checks if aircraft is available for selected dates'''
        self.chosen_aircr = chosen_aircr
        self.date1 = date1
        self.date2 = date2
        aircraft_list = Aircraft_service().get_aircrafts()
        available_aircrafts = Voyage_service().get_avail_aircraft(date1, date2)
        for aircraft in aircraft_list:
            if self.chosen_aircr == aircraft[0]:
                for aircrafts in available_aircrafts:
                    if aircrafts[0] == chosen_aircr and aircrafts[1] == "Laus":
                        return True
        else:
            return False

    
    def print_voyage(self, selected_voyage_list):
        '''Returns a formatted string with information for a selected voyage'''
        self.selected_voyage_list = selected_voyage_list
        prnt_str = ""
        self.flight = Flight(self.selected_voyage_list[0])
        # String with all the info for a selected voyage
        prnt_str += "\tFlug út\nFlugnúmer: \t {}\nBrottfarastaður: {}\nÁfangastaður: \t {}\nBrottfaratími:   {}\
            \nLendingartími:   {}\nFlugvél:\t {}\nFlugmenn:\t {}\n\t\t {}\nFlugþjónar:\t {}\n\t\t {}\n\t\t {}\n".format\
            (self.flight.get_flightNumber(), self.flight.get_departingFrom(), self.flight.get_arrivingAt(), \
            self.flight.get_departure(), self.flight.get_arrival(), self.flight.get_aircraftID(), self.flight.get_captain(), \
            self.flight.get_copilot(), self.flight.get_fsm(), self.flight.get_fa1(), self.flight.get_fa2())
        self.flight = Flight(self.selected_voyage_list[1])
        prnt_str += "\n\tFlug heim\nFlugnúmer: \t {}\nBrottfarastaður: {}\nÁfangastaður: \t {}\nBrottfaratími:   {}\
            \nLendingartími:   {}\nFlugvél:\t {}\nFlugmenn:\t {}\n\t\t {}\nFlugþjónar:\t {}\n\t\t {}\n\t\t {}\n".format\
            (self.flight.get_flightNumber(), self.flight.get_departingFrom(), self.flight.get_arrivingAt(), \
            self.flight.get_departure(), self.flight.get_arrival(), self.flight.get_aircraftID(), self.flight.get_captain(), \
            self.flight.get_copilot(), self.flight.get_fsm(), self.flight.get_fa1(), self.flight.get_fa2())
        return prnt_str

    def get_all_voyages(self):
        '''Returns a string with information for all upcoming flights'''
        return self.flights.get_upcomingflights()

    def add_flight_nums(self, destination):
        '''Adds a flight number to both departing and arriving flight when making a new voyage'''
        self.destination = destination
        destination_list = Destination_service().get_all_dest_list()
        for dest in destination_list:
            if dest[0] == self.destination:
                dest_num = destination_list.index(dest) + 1
        flights_list = self.flights.get_upcomingflights()
        flights_list = flights_list[::-1]
        for flight in flights_list:
            if flight[1] == self.destination:
                current_flight_num = flight[0]
                break
            else:
                current_flight_num = "NOTAVAIL"
        current_flight_num = list(current_flight_num)
        if current_flight_num[2] == "0":
            if current_flight_num[3] == str(dest_num):
                current_flight_num[-1] = int(current_flight_num[-1]) + 1
                next_flight = current_flight_num[:]
                current_flight_num[-1] = str(current_flight_num[-1])
                next_flight[-1] = int(next_flight[-1]) + 1
                next_flight[-1] = str(next_flight[-1])
                current_flight_num = "".join(current_flight_num)
                next_flight = "".join(next_flight)
                both_flight_nums = [current_flight_num, next_flight]
                return both_flight_nums
        else:
            current_flight_num = "NA0"+str(dest_num)+"0"
            next_flight = "NA0"+str(dest_num)+"1"
            both_flight_nums = [current_flight_num, next_flight]
        return both_flight_nums
    
    def get_avail_aircraft(self, date1, date2):
        '''Gets a list for all aircrafts and returns a list with info 
        about each aircraft and if its available'''
        self.date1 = date1
        self.date2 = date2
        self.date1 = self.date1.split("T")
        self.date2 = self.date2.split("T")
        avail_list = []
        aircraft_list = Aircraft_service().get_aircrafts()
        upc_flights_list = FlightRepository().get_upcomingflights()
        for aircraft in aircraft_list:
            for flight in upc_flights_list:
                if aircraft[0] in flight:
                    # Split the time string on "T" so we can use only the date, not time
                    flight[3] = flight[3].split("T")
                    flight[4] = flight[4].split("T")
                    # If an aircraft has a flight on these dates the aircraft gets marked "Upptekið"
                    if self.date1[0] == flight[3][0] or self.date2[0] == flight[4][0]:
                        if [aircraft[0], "Upptekin"] not in avail_list:
                            not_avail_pairing = [aircraft[0], "Upptekin"]
                            avail_list.append(not_avail_pairing)
            else:
                avail_pairing = [aircraft[0], "Laus"]
                if [aircraft[0], "Upptekin"] not in avail_list:
                    avail_list.append(avail_pairing)
        return avail_list

    def print_avail_aircraft(self, date1, date2):
        '''Returns a formatted string with information about the availability for each aircraft'''
        self.date1 = date1
        self.date2 = date2
        prnt_str = ""
        avail_aircrafts = Voyage_service().get_avail_aircraft(self.date1, self.date2)
        for pairs in avail_aircrafts:
            prnt_str += "{} - {}\n".format(pairs[0], pairs[1])
        return prnt_str
                    
    def get_arrival_time(self, destination, input_date):
        '''Calculates arrival time for flight depending on the lenght of the flight'''
        self.destination = destination
        self.input_date = input_date
        for dest in self.dest_list:
            if dest[0] == self.destination:
                flighttime = dest[2]
        # Convert string to datetime for calculations
        datetime_input_date = datetime.datetime.strptime(self.input_date, "%Y-%m-%dT%H:%M:%S")
        flighttime = flighttime.split(":")
        # Input 0,0,0,0 in timedelta to get the right format for output
        datetime_flighttime = datetime.timedelta(0,0,0,0,int(flighttime[1]), int(flighttime[0]))
        arrival_time = datetime_flighttime + datetime_input_date
        return arrival_time.strftime("%Y-%m-%dT%H:%M:%S")
    
    def get_return_flight_time(self, destination, arrival_time):
        '''Calculates a return flight for voyage by adding an hour delay at the destination'''
        self.destination = destination
        self.arrival_time = arrival_time
        hour_delay = datetime.timedelta(hours=1)
        datetime_arrival_time = datetime.datetime.strptime(str(self.arrival_time), "%Y-%m-%dT%H:%M:%S")
        # Add one hour to time to get the return flight time, since theres always an hour delay
        return_flight_time = datetime_arrival_time + hour_delay
        return return_flight_time.strftime("%Y-%m-%dT%H:%M:%S")
        
    def is_valid_voyage(self, voyage_str):
        '''Unfinished feature. Stay tuned for v.1.0012'''
        return True


    def prnt_str(self,empl_list):
        '''Returns a formatted string with employee information 
        and a number which is used to select that employee'''
        print_str = ""
        counter = 1
        for employee in empl_list:
            print_str +=  "'{}' - Kt: {}, {}.\n".format(counter, employee[0], employee[1])
            counter += 1
        return print_str
    
    def print_list(self,empl_list):
        '''Returns a formatted string with the SSN for each employee in the incoming list'''
        prnt_str = ""
        for employee in empl_list:
            if len(employee) == 2:   # The list will be of length 2 if it has the destination in it. 
                prnt_str += "Kennitala starfsmanns: {}, áfangastaður vinnuferðar: {}\n".format(employee[0],employee[1])
            else:    # else the employee list is a part of not working list and we don't print the destination 
                prnt_str += "Kennitala starfsmanns: {}\n".format(employee[0])
        return str(prnt_str)

    def get_date_voyage(self, prnt_str):
        '''Gets date from user with a number of inputs,
        where each input checks if the user inputs only digits'''
        self.prnt_str = prnt_str
        print()
        print(prnt_str)   
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
        user_chosen_date = [year,month,day,hour,mint,0]
        date = self.upcflights.add_date(user_chosen_date)
        return date
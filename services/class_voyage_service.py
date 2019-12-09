from repo.class_voyageRepo import VoyageRepo
from models.class_flight import Flight
from repo.class_FlightRepository import FlightRepository
from services.class_aircraft_service import Aircraft_service
from services.class_upcoming_flight_service import Upcoming_flight_service
from repo.class_Aircraft_typeRepository import AircraftRepository
from repo.class_DestinationRepo import DestinationRepo
import datetime

class Voyage_service:

    def __init__(self):
        self.voyage_repo = VoyageRepo()
        self.flight_repo = FlightRepository()
        self.dest_list = DestinationRepo().get_all_dest_list()

    def add_date(self, date_list):
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
        self.date = date
        if self.date >= date.today():
            return True
        else:
            return False

    def get_aircraft(self):
        aircraft_list = AircraftRepository().get_all_aircraft_types()
        aircraft_info_list = []
        for aircraft in aircraft_list[1:]:
            pair_list = []
            pair_list = [aircraft[0], aircraft[1]]
            aircraft_info_list.append(pair_list)
        return aircraft_info_list


    def add_voyage(self, voyage_str):
        self.voyage_str = voyage_str
        # Checks for valid input before sending to the repository
        if self.is_valid_voyage(voyage_str):
            self.voyage_repo.add_voyage(voyage_str)

    def get_voyage(self, voyage_dep, voyage_arr):
        self.voyage_dep = voyage_dep
        self.voyage_arr = voyage_arr
        voyage_list = self.voyage_repo.get_voyage_list()
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

    
    def print_voyage(self, selected_voyage_list):
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
        return self.voyage_repo.get_voyage_list()

    # def add_flight_num(self, destination):
    #     flights_list = self.flight_repo.get_upcomingflights()
    #     current_flight_num = flights_list[-1][0]
    #     current_flight_num = current_flight_num.split("A")
        
    #     for dest in self.dest_list:
    #         if dest[0] == destination:
    #     counter = int(current_flight_num[1]) + 1
    #     printed_flight_num = "NA{0:0=3d}".format(counter)
    #     return printed_flight_num
    
    def get_avail_aircraft(self, date1, date2):
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
                            avail_pairing = [aircraft[0], "Upptekin"]
                            avail_list.append(avail_pairing)
            else:
                not_avail_pairing = [aircraft[0], "Laus"]
                avail_list.append(not_avail_pairing)
        return avail_list

    def print_avail_aircraft(self, date1, date2):
        self.date1 = date1
        self.date2 = date2
        prnt_str = ""
        avail_aircrafts = Voyage_service().get_avail_aircraft(self.date1, self.date2)
        for pairs in avail_aicrafts:
            prnt_str += "{} - {}".format(avail_aircrafts[0], avail_aircrafts[1])
        return prnt_str
                    
    def get_arrival_time(self, destination, input_date):
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
        self.destination = destination
        self.arrival_time = arrival_time
        hour_delay = datetime.timedelta(hours=1)
        datetime_arrival_time = datetime.datetime.strptime(str(self.arrival_time), "%Y-%m-%dT%H:%M:%S")
        # Add one hour to time to get the return flight time, since theres always an hour delay
        return_flight_time = datetime_arrival_time + hour_delay
        return return_flight_time.strftime("%Y-%m-%dT%H:%M:%S")
        
    def is_valid_voyage(self, voyage_str):
        return True

print(Voyage_service.print_avail_aircraft("2019-11-28T00:00:00", "2019-11-18T03:00:00"))

from class_voyageRepo import VoyageRepo
from class_flight import Flight
from class_FlightRepository import FlightRepository
from class_aircraft_service import Aircraft_service
from class_upcoming_flight_service import Upcoming_flight_service
import datetime

class Voyage_service:

    def __init__(self):
        self.voyage_repo = VoyageRepo()
        self.flight_repo = FlightRepository()

    def add_voyage(self, voyage_str):
        self.voyage_str = voyage_str
        if self.is_valid_voyage(voyage_str):
            self.voyage_repo.add_voyage(voyage_str)

    def get_voyage(self, voyage_dep, voyage_arr):
        self.voyage_dep = voyage_dep
        self.voyage_arr = voyage_arr
        voyage_list = self.voyage_repo.get_voyage_list()
        selected_voyage_list = []
        for flight in voyage_list:
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

    def add_flight_num(self):
        flights_list = self.flight_repo.get_upcomingflights()
        current_flight_num = flights_list[-1][0]
        current_flight_num = current_flight_num.split("A")
        counter = int(current_flight_num[1]) + 1
        printed_flight_num = "NA{0:0=3d}".format(counter)
        return printed_flight_num
    
    # def get_avail_aircraft(self, date1, date2):
    #     self.date1 = date1
    #     self.date2 = date2
    #     dt_str1 = datetime.datetime.strptime(self.date1, "%Y-%m-%dT%H:%M:%S")
    #     dt_str2 = datetime.datetime.strptime(self.date2, "%Y-%m-%dT%H:%M:%S")
    #     margin = dt_str2 - dt_str1
    #     print(margin)
    #     margin_date = datetime.timedelta(days = 1)
    #     avail_list = []
    #     aircraft_list = Aircraft_service().get_aircrafts()
    #     upc_flights_list = FlightRepository().get_upcomingflights()
    #     for aircraft in aircraft_list:
    #         for flight in upc_flights_list:
    #             if aircraft[0] in flight:
    #                 if self.date1 == flight[3] or self.date2 == flight[4]:
    #                     avail_pairing = [aircraft[0], "Upptekin"]
    #                     avail_list.append(avail_pairing)
    #                     break
    #         else:
    #             not_avail_pairing = [aircraft[0], "Laus"]
    #             avail_list.append(not_avail_pairing)
    #     return avail_list
                    

    def is_valid_voyage(self, voyage_str):
        return True

print(Voyage_service().get_avail_aircraft("2019-12-26T09:27:00", "2019-12-26T12:27:00"))
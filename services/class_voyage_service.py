from repo.class_voyageRepo import VoyageRepo
from model.class_flight import Flight

class Voyage_service:

    def __init__(self):
        self.voyage_repo = VoyageRepo()

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


    def is_valid_voyage(self, voyage_str):
        return True

from repo.class_Aircraft_typeRepository import AircraftRepository
from models.class_aircraft import Aircraft
from services.class_voyage_service import Voyage_service

class Aircraft_service():
    def __init__(self):
        self.__aircraftrepo = AircraftRepository()

    def get_aircraft(self):
        pass

    def get_aircrafts(self):
        aircraft_list = []
        open_file = open("./data/Aircraft.csv", "r")
        for line in open_file:
            line = line.strip().split(",")
            aircraft_list.append(line)
        return aircraft_list[1:]


    def add_aircraft(self, air_str = ""):
        self.air_str = air_str
        aircraft = self.__aircraftrepo.add_aircraft_type(self.air_str)
        return aircraft


    def is_valid_aircraft(self, chosen_aircr, date1, date2):
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

    def find_air_id(self, aircraft_name):
        aircraft_str = ""
        open_file = open("./data/Aircraft.csv", "r")
        for line in open_file:
            if aircraft_name in line:
                aircraft_str = line[0]                
        return aircraft_str[1]

        
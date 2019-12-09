from repo.class_Aircraft_typeRepository import AircraftRepository
from models.class_aircraft import Aircraft

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
        if self.is_valid_aircraft(self.air_str):
            aircraft = self.__aircraftrepo.add_aircraft_type(self.air_str)
            return aircraft
    
    def is_valid_aircraft(self, air_str):
        return True 

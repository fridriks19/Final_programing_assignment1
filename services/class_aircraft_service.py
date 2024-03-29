from repo.class_Aircraft_typeRepository import AircraftRepository
from models.class_aircraft import Aircraft

class Aircraft_service():
    def __init__(self):
        self.__aircraftrepo = AircraftRepository()

    def get_aircrafts(self):
        '''Gets a list with all aircrafts'''
        aircraft_list = self.__aircraftrepo.get_all_aircraft_types()
        return aircraft_list[1:]


    def add_aircraft(self, air_str = ""):
        """Add an aircraft to the aircraft repository"""

        self.air_str = air_str
        aircraft = self.__aircraftrepo.add_aircraft_type(self.air_str)
        return aircraft


    def get_aircraft(self):
        '''Gets a list with all aircrafts, but only limited info'''
        aircraft_list = AircraftRepository().get_all_aircraft_types()
        aircraft_info_list = []
        for aircraft in aircraft_list[1:]:
            pair_list = []
            pair_list = [aircraft[0], aircraft[1]]
            aircraft_info_list.append(pair_list)
        return aircraft_info_list

    def find_air_id(self, aircraft_name):
        """Finds the id for the aircraft"""

        aircraft_str = ""
        self.aircraft_name = aircraft_name
        aircraft_list = Aircraft_service().get_aircrafts()
        for aircraft in aircraft_list:
            if aircraft_name in aircraft:
                aircraft_str = str(aircraft[1])                
        return aircraft_str

        
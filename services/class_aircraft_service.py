from repo.class_Aircraft_typeRepository import AircraftRepository

class Aircraft_service():
    def __init__(self):
        self.__aircraftrepo = AircraftRepository()

    def get_aircraft(self):
        pass

    def add_aircraft(self, air_str = ""):
        self.air_str = air_str
        if self.is_valid_aircraft(self.air_str):
            aircraft = self.__aircraftrepo.add_aircraft_type(self.air_str)
            return aircraft
    
    def is_valid_aircraft(self, air_str):
        return True 

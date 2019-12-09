class Aircraft():
    def __init__(self, aircraft_info_list):
        self.aircraft_info_list = aircraft_info_list
        self.__aircraftId = self.aircraft_info_list[0]
        self.__planeTypeId = self.aircraft_info_list[1]
    
    def __str__(self):
        return "{}".format(self.aircraft_info_list)
    
    def get_airctaftId(self):
        return self.__aircraftId

    def get_planeTypeId(self):
        return self.__planeTypeId

        
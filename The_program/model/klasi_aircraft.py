class Aircraft():
    def __init__(self, aircraft_info_list):
        self.aircraft_info_list = aircraft_info_list
        self.aircraftId = self.aircraft_info_list[0]
        self.planeTypeId = self.aircraft_info_list[1]
    
    def __str__(self):
        return "{}".format(self.aircraft_info_list)
"""flightNumber, departingFrom, arrivingAt, departure, arrival, aircraftID, captain, copilot, fsm, fa1, fa2"""
class Flight():
    def __init__(self, flight_info_list=""):
        self.flight_info_list = flight_info_list
        self.__flightNumber = self.flight_info_list[0]
        self.__departingFrom = self.flight_info_list[1]
        self.__arrivingAt = self.flight_info_list[2]
        self.__departure = self.flight_info_list[3]
        self.__arrival = self.flight_info_list[4]
        self.__aircraftID = self.flight_info_list[5]
        self.__captain = self.flight_info_list[6]
        self.__copilot = self.flight_info_list[7]
        self.__fsm = self.flight_info_list[8]
        self.__fa1 = self.flight_info_list[9]
        self.__fa2 = self.flight_info_list[10]

    def __str__(self):
        prnt_str = ""
        for item in self.flight_info_list:
            if self.flight_info_list.index(item) == 10:
                prnt_str += item
            else:
                prnt_str += item + ","
        return prnt_str

    def get_flightNumber(self):
        return self.__flightNumber
    
    def get_departingFrom(self):
        return self.__departingFrom
    
    def get_arrivingAt(self):
        return self.__arrivingAt
    
    def get_departure(self):
        return self.__departure

    def get_arrival(self):
        return self.__arrival

    def get_aircraftID(self):
        return self.__aircraftID
    
    def get_captain(self):
        return self.__captain
    
    def get_copilot(self):
        return self.__copilot
    
    def get_fsm(self):
        return self.__fsm
    
    def get_fa1(self):
        return self.__fa1
    
    def get_fa2(self):
        return self.__fa2
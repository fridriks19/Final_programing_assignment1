#flightNumber,departingFrom,arrivingAt,departure,arrival,aircraftID,captain,copilot,fsm,fa1,fa2
class past_flights():
    def __init__(self, flight_info_list):
        self.flight_info_list = flight_info_list
        self.flightNumber = self.flight_info_list[0]
        self.departingFrom = self.flight_info_list[1]
        self.arrivingAt = self.flight_info_list[2]
        self.departure = self.flight_info_list[3]
        self.arrival = self.flight_info_list[4]
        self.aircraftID = self.flight_info_list[5]
        self.captain = self.flight_info_list[6]
        self.copilot = self.flight_info_list[7]
        self.fsm = self.flight_info_list[8]
        self.fa1 = self.flight_info_list[9]
        self.fa2 = self.flight_info_list[10]
        
    def __str__(self):
        return "{}".format(self.flight_info_list)
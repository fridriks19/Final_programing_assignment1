
class Upcoming_flights():
    """flightNumber, departingFrom, arrivingAt, departure, arrival"""
    def __init__(self, upcoming_flights_info_list):
        self.upcoming_flights_info_list = upcoming_flights_info_list
        self.__flightNumber = self.upcoming_flights_info_list[0]
        self.__departingFrom = self.upcoming_flights_info_list[1]
        self.__arrivingAt = self.upcoming_flights_info_list[2]
        self.__departureTime = self.upcoming_flights_info_list[3]
        self.__arrivalTime = self.upcoming_flights_info_list[4]
    
    def __inti__(self):
        return "{}".format(self.upcoming_flights_info_list)

    def return_details(self):  # make a set with all the details 
        ''' Returns the order details in a dictionary'''
        return {"Flight numbers": self.__flightNumber,
                "Departing from": self.__departingFrom,
                "Arriving at": self.__arrivingAt,
                "Departure time": self.__departureTime,
                "Arrival time": self.__arrivalTime }
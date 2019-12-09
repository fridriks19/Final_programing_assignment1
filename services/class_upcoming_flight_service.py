import datetime
from repo.class_FlightRepository import *

class Upcoming_flight_service:

    def __init__(self):
        self.flights = FlightRepository()
        self.upcoming_list = self.flights.get_upcomingflights()

    def get_all_upcomingflights(self):
        return none
    
    def get_upcomingflights(self, date_1, date_2):
        self.date_1 = date_1
        self.date_2 = date_2
        pf_list = []
        prnt_str = ""
        # Changes the string to a valid datetime format
        dt_str1 = datetime.datetime.strptime(self.date_1, "%Y-%m-%dT%H:%M:%S")
        dt_str2 = datetime.datetime.strptime(self.date_2, "%Y-%m-%dT%H:%M:%S")
        # Sort the list by date
        sorted_list = sorted(self.upcoming_list, key=lambda date: date[3]) 
        for flight in sorted_list:
            # Checks if flight is within set date parameters
            if datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S") >= dt_str1 and datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S") <= dt_str2:
                pf_list.append(flight)
        for flight in pf_list:
            flight_time = datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S")
            prnt_str += "Flug: {}\nFrá: {}\nTil: {}\nDags: {}\n\n".format(flight[0], flight[1], flight[2], flight_time)
        return prnt_str
    
    def get_upcomingflight(self, upc_date):
        self.upc_date = upc_date
        for flight in self.upcoming_list:
            if flight[3] == self.upc_date:
                # Checks if flight is within set date parameters
                flight_time = datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S")
                prnt_str = "Flug: {}\nFrá:  {}\nTil:  {}\nDags: {}".format(flight[0], flight[1], flight[2], flight_time)
                return prnt_str
        return "Flug fannst ekki"

#print(Upcoming_flight_service().get_upcomingflight("2019-12-26T09:27:00"))
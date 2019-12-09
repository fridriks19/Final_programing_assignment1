import datetime
from class_FlightRepository import *

class Past_flight_service:

    def __init__(self):
        self.flights = FlightRepository()
        self.past_list = self.flights.get_pastflights()
    
    def get_pastflights(self, date_1, date_2):
        self.date_1 = date_1
        self.date_2 = date_2
        pf_list = []
        prnt_str = ""
        # Changes the string to a valid datetime format
        dt_str1 = datetime.datetime.strptime(self.date_1, "%Y-%m-%dT%H:%M:%S")
        dt_str2 = datetime.datetime.strptime(self.date_2, "%Y-%m-%dT%H:%M:%S")
        # Sort the list by date
        sorted_list = sorted(self.past_list, key=lambda date: date[3]) 
        for flight in sorted_list:
            # Checks if flight is within set date parameters
            if datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S") >= dt_str1 and datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S") <= dt_str2:
                pf_list.append(flight)
        for flight in pf_list:
            flight_time = datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S")
            prnt_str += "Flug: {}\nFrá: {}\nTil: {}\nDags: {}\n\n".format(flight[0], flight[1], flight[2], flight_time)
        return prnt_str
    
    def get_pastflight(self, past_date):
        self.past_date = past_date
        for flight in self.past_list:
            if flight[3] == self.past_date:
                # Checks if flight is within set date parameters
                flight_time = datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S")
                prnt_str = "Flug: {}\nFrá:  {}\nTil:  {}\nDags: {}".format(flight[0], flight[1], flight[2], flight_time)
                return prnt_str
        return "Flug fannst ekki"

print(Past_flight_service().get_pastflight("2019-11-28T06:25:00"))
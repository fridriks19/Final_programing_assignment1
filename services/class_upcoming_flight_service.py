import datetime
from repo.class_FlightRepository import *

class Upcoming_flight_service:

    def __init__(self):
        self.flights = FlightRepository()
        self.upcoming_list = self.flights.get_upcomingflights()

    def get_all_upcomingflights(self):
        return none

    def add_upc_flight(self, flight_str):
        self.flight_str = flight_str
        return FlightRepository().add_upcomingflight(self.flight_str)
    
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
    
    def get_upcomingflights_list(self):
        return FlightRepository().get_upcomingflights()

    def get_upcomingflight(self, upc_date):
        self.upc_date = upc_date
        for flight in self.upcoming_list:
            if flight[3] == self.upc_date:
                # Checks if flight is within set date parameters
                flight_time = datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S")
                prnt_str = "Flug: {}\nFrá:  {}\nTil:  {}\nDags: {}".format(flight[0], flight[1], flight[2], flight_time)
                return prnt_str
        return "Flug fannst ekki"
    
    def get_upcoming_voyage(self, upc_date):
        self.upc_date = upc_date
        for flight in self.upcoming_list:
            if flight[3] == self.upc_date:
                flight1 = flight
                flight2_index = self.upcoming_list.index(flight)
                flight2 = self.upcoming_list[flight2_index+1]
        return flight1, flight2

    def change_upcoming_voyage(self, original_upc_flight, upd_upc_flight):
        self.upc_date = upc_date
        upc_voyages = Upcoming_flight_service().get_upcomingflights_list()
        for flight in upc_voyages:
            if flight == str(original_upc_flight[0])
            flight_index = upc_voyages.index(flight)
            upc_voyages[flight_index + 1] = str(upd_upc_flight[1])
            flight = str(upd_upc_flight[0])
        FlightRepository().save_changed_upc_flights(upc_voyages)
        return "Breytingar Vistaðar"



    def add_date(self, date_list):
        self.date_list = date_list
        year = int(self.date_list[0])
        month = int(self.date_list[1])
        day = int(self.date_list[2])
        hours = int(self.date_list[3])
        mins = int(self.date_list[4])
        secs = int(self.date_list[5])
        try:
            date = datetime.datetime(year,month,day,hours,mins,secs)
        except ValueError:
            return False
        if Upcoming_flight_service().is_valid_date(date):
           return date.strftime("%Y-%m-%dT%H:%M:%S")
        else:
            return False

    def is_valid_date(self, date):
        return True

#print(Upcoming_flight_service().get_upcomingflight("2019-12-26T09:27:00"))
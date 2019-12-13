import datetime
from repo.class_FlightRepository import *

class Upcoming_flight_service:

    def __init__(self):
        self.flights = FlightRepository()
        self.upcoming_list = self.flights.get_upcomingflights()

    def get_all_upcomingflights(self):
        return None

    def add_upc_flight(self, flight_str):
        '''Sends the incoming flight string to the Flight Repository where it gets added
            to the csv file'''
        self.flight_str = flight_str
        return FlightRepository().add_upcomingflight(self.flight_str)
    
    def get_upcomingflights(self, date_1, date_2):
        '''Returns all upcoming flights within set date parameters in a formatted string'''
        self.date_1 = date_1
        self.date_2 = date_2
        upcoming_list = self.flights.get_upcomingflights()
        pf_list = []
        prnt_str = ""
        # Changes the string to a valid datetime format
        dt_str1 = datetime.datetime.strptime(self.date_1, "%Y-%m-%dT%H:%M:%S")
        dt_str2 = datetime.datetime.strptime(self.date_2, "%Y-%m-%dT%H:%M:%S")
        # Sort the list by date
        sorted_list = sorted(upcoming_list, key=lambda date: date[3])
        sorted_list = sorted_list
        for flight in sorted_list:
            # Checks if flight is within set date parameters
            if datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S") >= dt_str1 and datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S") <= dt_str2:
                pf_list.append(flight)
        for flight in pf_list:
            flight_time = datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S")
            prnt_str += "Flug: {}\nFrá: {}\nTil: {}\nDags: {}\nFlugstjóri: {}\nAðstoðarflugmaður: {}\nYfirflugþjónn: {}\nFlugþjónn 1: {}\nFlugþjónn 2: {}\n\n".format(flight[0], flight[1], flight[2], flight_time, flight[6], flight [7], flight[8], flight[9], flight[10])
        return prnt_str

    def get_upcomingflights_list_selected_time(self, date1, date2):
        '''Returns a list with all upcoming flight within set date parameters'''
        self.date1 = date1
        self.date2 = date2
        uf_list = []
        prnt_str = ""
        # Changes the string to a valid datetime format
        dt_str1 = datetime.datetime.strptime(self.date1, "%Y-%m-%dT%H:%M:%S")
        dt_str2 = datetime.datetime.strptime(self.date2, "%Y-%m-%dT%H:%M:%S")
        # Sort the list by date
        sorted_list = sorted(self.upcoming_list, key=lambda date: date[3]) 
        for flight in sorted_list:
            # Checks if flight is within set date parameters
            if datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S") >= dt_str1 and datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S") <= dt_str2:
                uf_list.append(flight)
        return uf_list
    
    def find_empl_worktime(self, ssn, flight_list):
        '''Returns info in a formatted string about an upcoming flight that has the 
            selected employee as a member of the crew'''
        self.ssn = str(ssn)
        self.flight_list = flight_list
        empl_flight_list = []
        prnt_str = ""
        for flight in self.flight_list:
            for item in flight:
                if self.ssn == str(item):
                    empl_flight_list.append(flight)
        for flight in empl_flight_list:
            flight_time = datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S")
            prnt_str += "Flug: {}\nFrá: {}\nTil: {}\nDags: {}\nFlugstjóri: {}\nAðstoðarflugmaður: {}\nYfirflugþjónn: {}\nFlugþjónn 1: {}\nFlugþjónn 2: {}\n\n".format(flight[0], flight[1], flight[2], flight_time, flight[6], flight [7], flight[8], flight[9], flight[10])
        return prnt_str
    
    def get_upcomingflights_list(self):
        '''Gets all upcoming flights in  a simple list with the flights as element lists'''
        return FlightRepository().get_upcomingflights()

    def get_upcomingflight(self, upc_date):
        '''Gets an upcoming flight that matches the input date and returns it as a formatted string'''
        self.upc_date = upc_date
        upc_list = self.flights.get_upcomingflights()
        for flight in upc_list:
        #for flight in self.upcoming_list:
            if flight[3] == self.upc_date:
                # Checks if flight is within set date parameters
                flight_time = datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S")
                prnt_str = "Flug: {}\nFrá: {}\nTil: {}\nDags: {}\nFlugstjóri: {}\nAðstoðarflugmaður: {}\nYfirflugþjónn: {}\nFlugþjónn 1: {}\nFlugþjónn 2: {}\n\n".format(flight[0], flight[1], flight[2], flight_time, flight[6], flight [7], flight[8], flight[9], flight[10])
                return prnt_str
        return "Flug fannst ekki"
    
    def get_upcomingflight_list(self, upc_date):
        '''Gets an upcoming flight that matches the input date and returns it as a formatted string'''
        self.upc_date = upc_date
        upc_list = self.flights.get_upcomingflights()
        for flight in upc_list:
        #for flight in self.upcoming_list:
            if flight[3] == self.upc_date:
                return flight
        return "Flug fannst ekki"
    
    def get_upcoming_voyage(self, upc_date):
        '''Gets an upcoming flight and returns it along with the next flight'''
        self.upc_date = upc_date
        upc_list = self.flights.get_upcomingflights()
        #for flight in self.upcoming_list:
        for flight in upc_list:
            if flight[3] == upc_date:
                flight1 = flight
                flight2_index = upc_list.index(flight)
                flight2 = upc_list[flight2_index+1]
        return flight1, flight2

    def change_upcoming_voyage(self, upc_flight1, upc_flight2):
        '''Fetches the upcoming flights list and replaces the upcoming flights that match
            the date of the two upc_flight lists'''
        self.upc_flight1 = upc_flight1
        self.upc_flight2 = upc_flight2
        upc_voyages = FlightRepository().get_upcomingflights()
        new_upc_voyages = []
        for flight in upc_voyages:
            if flight[0] == upc_flight1[0]:
                flight = self.upc_flight1
                new_upc_voyages.append(flight)
            elif flight[0] == upc_flight2[0]:
                flight = self.upc_flight2
                new_upc_voyages.append(flight)
            else:
                new_upc_voyages.append(flight)
        FlightRepository().save_changed_upc_flights(new_upc_voyages)
        return "Breytingar Vistaðar"



    def add_date(self, date_list):
        '''Gets input from user and converts it to a valid datetime string'''
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
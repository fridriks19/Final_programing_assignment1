#from models.class_flight import Flight
import datetime


class FlightRepository():
    def __init__(self, flight_str, flight_str2=""):
        self.flight_str = flight_str
        self.flight_str2 = flight_str2
        self.upcoming_list = []
        self.past_list = []
        self.open_upcoming = open("./data/UpcomingFlights.csv", "r")
        for line in self.open_upcoming:
            line = line.strip()
            line = line.split(",")
            self.upcoming_list.append(line)
        self.open_past = open("./data/PastFlights2.csv", "r")
        for line in self.open_past:
            line = line.strip()
            line = line.split(",")
            self.past_list.append(line)

    
    def get_upcomingflight(self):
        for flight in self.upcoming_list:
            if flight[3] == self.flight_str:
                # Checks if flight is within set date parameters
                flight_time = datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S")
                self.open_upcoming.close()
                prnt_str = "Flug: {}\nFrá: {}\nTil: {}\nDags: {}".format(flight[0], flight[1], flight[2], flight_time)
                return prnt_str
        self.open_upcoming.close()
        return "Flug fannst ekki"
    
    def get_upcomingflights_ot(self):
        prnt_str = ""
        pf_list = []
        # Changes the string to a valid datetime format
        dt_str1 = datetime.datetime.strptime(self.flight_str, "%Y-%m-%dT%H:%M:%S")
        dt_str2 = datetime.datetime.strptime(self.flight_str2, "%Y-%m-%dT%H:%M:%S")
        # Get rid of "header" in csv file before sorting the list
        self.upcoming_list.pop(0)
        # Sort the list by date
        sorted_list = sorted(self.upcoming_list, key=lambda date: date[3]) 
        for flight in sorted_list:
            # Checks if flight is within set date parameters
            if datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S") >= dt_str1 and datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S") <= dt_str2:
                pf_list.append(flight)
        for flight in pf_list:
            flight_time = datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S")
            prnt_str += "Flug: {}\nFrá: {}\nTil: {}\nDags: {}\n\n".format(flight[0], flight[1], flight[2], flight_time)
        self.upcoming_list.close()
        return prnt_str


    def get_pastflight(self):
        for flight in self.past_list:
            if flight[3] == self.flight_str:
                flight_time = datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S")
                self.open_past.close()
                prnt_str = "Flug: {}\nFrá: {}\nTil: {}\nDags: {}".format(flight[0], flight[1], flight[2], flight_time)
                return prnt_str
        self.open_past.close()
        return "Flug fannst ekki"
    
    def get_pastflights_ot(self):
        pf_list = []
        prnt_str = ""
        # Changes the string to a valid datetime format
        dt_str1 = datetime.datetime.strptime(self.flight_str, "%Y-%m-%dT%H:%M:%S")
        dt_str2 = datetime.datetime.strptime(self.flight_str2, "%Y-%m-%dT%H:%M:%S")
        # Get rid of "header" in csv file before sorting the list
        self.past_list.pop(0)
        # Sort the list by date
        sorted_list = sorted((self.past_list), key=lambda date: date[3]) 
        for flight in sorted_list:
            # Checks if flight is within set date parameters
            if datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S") >= dt_str1 and datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S") <= dt_str2:
                pf_list.append(flight)
        for flight in pf_list:
            flight_time = datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S")
            prnt_str += "Flug: {}\nFrá: {}\nTil: {}\nDags: {}\n\n".format(flight[0], flight[1], flight[2], flight_time)
        self.open_past.close()
        return prnt_str

f1 = FlightRepository("2019-11-04T05:32:00", "2019-11-14T05:18:00")
print(f1.get_pastflights_ot())
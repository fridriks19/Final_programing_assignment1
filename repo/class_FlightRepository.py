#from models.class_flight import Flight
import datetime


class FlightRepository():
    def __init__(self, flight_str, flight_str2=""):
        self.flight_str = flight_str
        self.flight_str2 = flight_str2
    
    def get_upcomingflight(self):
        open_file = open("./data/UpcomingFlights.csv", "r")
        open_file_list = []
        for line in open_file:
            line = line.strip()
            line = line.split(",")
            open_file_list.append(line)
        for flight in open_file_list:
            if flight[3] == self.flight_str:
                # Checks if flight is within set date parameters
                flight_time = datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S")
                open_file.close()
                prnt_str = "Flug: {}\nFrá: {}\nTil: {}\nDags: {}".format(flight[0], flight[1], flight[2], flight_time)
                return prnt_str
        open_file.close()
        return "Flug fannst ekki"
    
    def get_upcomingflights_ot(self):
        open_file = open("./data/UpcomingFlights.csv", "r")
        open_file_list = []
        pf_list = []
        for line in open_file:
            line = line.strip()
            line = line.split(",")
            open_file_list.append(line)
        # Changes the string to a valid datetime format
        dt_str1 = datetime.datetime.strptime(self.flight_str, "%Y-%m-%dT%H:%M:%S")
        dt_str2 = datetime.datetime.strptime(self.flight_str2, "%Y-%m-%dT%H:%M:%S")
        # Get rid of "header" in csv file before sorting the list
        open_file_list.pop(0)
        # Sort the list by date
        sorted_list = sorted(open_file_list, key=lambda date: date[3]) 
        for flight in sorted_list:
            # Checks if flight is within set date parameters
            if datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S") >= dt_str1 and datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S") <= dt_str2:
                pf_list.append(flight)
        for flight in pf_list:
            flight_time = datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S")
            prnt_str += "Flug: {}\nFrá: {}\nTil: {}\nDags: {}\n\n".format(flight[0], flight[1], flight[2], flight_time)
        return prnt_str


    def get_pastflight(self):
        open_file = open("./data/PastFlights2.csv", "r")
        open_file_list = []
        for line in open_file:
            line = line.strip()
            line = line.split(",")
            open_file_list.append(line)
        for flight in open_file_list:
            if flight[3] == self.flight_str:
                flight_time = datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S")
                open_file.close()
                prnt_str = "Flug: {}\nFrá: {}\nTil: {}\nDags: {}".format(flight[0], flight[1], flight[2], flight_time)
                return prnt_str
        open_file.close()
        return "Flug fannst ekki"
    
    def get_pastflights_ot(self):
        open_file = open("./data/PastFlights2.csv", "r")
        open_file_list = []
        pf_list = []
        prnt_str = ""
        for line in open_file:
            line = line.strip()
            line = line.split(",")
            open_file_list.append(line)
        # Changes the string to a valid datetime format
        dt_str1 = datetime.datetime.strptime(self.flight_str, "%Y-%m-%dT%H:%M:%S")
        dt_str2 = datetime.datetime.strptime(self.flight_str2, "%Y-%m-%dT%H:%M:%S")
        # Get rid of "header" in csv file before sorting the list
        open_file_list.pop(0)
        # Sort the list by date
        sorted_list = sorted(open_file_list, key=lambda date: date[3]) 
        for flight in sorted_list:
            # Checks if flight is within set date parameters
            if datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S") >= dt_str1 and datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S") <= dt_str2:
                pf_list.append(flight)
        for flight in pf_list:
            flight_time = datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S")
            prnt_str += "Flug: {}\nFrá: {}\nTil: {}\nDags: {}\n\n".format(flight[0], flight[1], flight[2], flight_time)
        return prnt_str

f1 = FlightRepository("2019-11-02T06:21:00")
print(f1.get_pastflight())

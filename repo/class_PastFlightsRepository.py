#from models.class_past_flights import Past_flights
import datetime


class PastFlightsRepository():
    def __init__(self, past_str, past_str2=0):
        self.past_str = past_str
        self.past_str2 = past_str2
    
    def get_pastflights(self):
        open_file = open("./data/PastFlights2.csv", "r")
        open_file_list = []
        for line in open_file:
            line = line.strip()
            line = line.split(",")
            open_file_list.append(line)
        for flight in open_file_list:
            if flight[3] == self.past_str:
                open_file.close()
                return flight
        open_file.close()
        return "Flug fannst ekki"
    
    def get_pastflights_overtime(self):
        open_file = open("./data/PastFlights2.csv", "r")
        open_file_list = []
        for line in open_file:
            line = line.strip()
            line = line.split(",")
            open_file_list.append(line)
        # Changes the string to a valid datetime format
        dt_str1 = datetime.datetime.strptime(self.past_str, "%Y-%m-%dT%H:%M:%S")
        dt_str2 = datetime.datetime.strptime(self.past_str2, "%Y-%m-%dT%H:%M:%S")
        for flight in open_file_list[1:]:
            # Checks if flight is within set date parameters
            if datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S") >= dt_str1 and datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S") <= dt_str2:
                print(flight[3])

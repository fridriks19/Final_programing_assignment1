import datetime


class FlightRepository():
    def __init__(self):
        self.flight_list = []
    
    def get_upcomingflights(self):
        self.open_upcoming = open("./data/UpcomingFlights.csv", "r")
        for line in self.open_upcoming:
            line = line.strip()
            line = line.split(",")
            self.flight_list.append(line)
        self.open_upcoming.close()
        return self.flight_list[1:]
    
    def get_pastflights(self):
        self.open_past = open("./data/PastFlights2.csv", "r")
        for line in self.open_past:
            line = line.strip()
            line = line.split(",")
            self.flight_list.append(line)
        self.open_past.close()
        return self.flight_list[1:]

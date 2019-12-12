import datetime


class FlightRepository():
    def __init__(self):
        self.flight_list = []
        self.open_file()
    
    def open_file(self):
        self.flight_list = []
        open_file = open("./data/UpcomingFlights.csv", "r")
        for line in open_file:
            line = line.strip().split(",")
            self.flight_list.append(line)
        open_file.close()

    def get_upcomingflights(self):
        self.open_upcoming = open("./data/UpcomingFlights.csv", "r")
        for line in self.open_upcoming:
            line = line.strip()
            line = line.split(",")
            self.flight_list.append(line)
        self.open_upcoming.close()
        return self.flight_list[1:]
    
    def get_upcomingflights_plusheader(self):
        self.open_upcoming = open("./data/UpcomingFlights.csv", "r")
        for line in self.open_upcoming:
            line = line.strip()
            line = line.split(",")
            self.flight_list.append(line)
        self.open_upcoming.close()
        return self.flight_list
    
    def add_upcomingflight(self, flight_str):
        self.flight_str = flight_str
        open_file = open("./data/UpcomingFlights.csv", "a")
        open_file.write(self.flight_str + "\n")
        open_file.close()
        return "Vinnuferð vistuð"

    
    def get_pastflights(self):
        self.open_past = open("./data/PastFlights.csv", "r")
        for line in self.open_past:
            line = line.strip()
            line = line.split(",")
            self.flight_list.append(line)
        self.open_past.close()
        return self.flight_list[1:]
    
    def save_changed_upc_flights(self, new_upc_list):
        self.new_upc_list = new_upc_list
        self.writable_upc = open("./data/UpcomingFlights.csv", "w")
        for flight in new_upc_list:
            flight = ",".join(flight)
            self.writable_upc.write(flight)
            self.writable_upc.write("\n")
        self.writable_upc.close()


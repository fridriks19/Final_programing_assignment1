from models.class_upcoming_flights import Upcoming_flights
# import dateutil.parser
# date = "2019-11-08T06:35:00"
# parsedDate = dateutil.parser.parse(date)
# print(parsedDate.second)

class Upcoming_flightsIO():
    def __init__(self):
        self.__upcoming_flights = Upcoming_flights()


    def add_upcoming_flights(self):
        pass


    def get_upcoming_flights(self):
        open_file = open("UpcomingFlights2.csv", "r")
        for line in open_file:
            line = line.split(",")
            print(line)

    def change_upcoming_flights(self):
        pass
    
U = Upcoming_flightsIO()
U.get_upcoming_flights()

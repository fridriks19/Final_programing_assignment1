from models.class_flight import Flight

class Voyage(Flight):

    def __init__(self, departing_flight_list, arriving_flight):
        self.departing_flight_list = departing_flight_list
        self.arriving_flight_list = arriving_flight_list
        self.departing_flight = Flight(self.departing_flight_list)
        self.arriving_flight = Flight(self.arriving_flight_list)

    def __str__(self):
        return "{}\n{}".format(self.departing_flight, self.arriving_flight)

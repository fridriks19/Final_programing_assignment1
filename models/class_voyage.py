class Voyage:

    def __init__(self,departing_flight, arriving_flight):
        self.departing_flight = departing_flight
        self.arriving_flight = arriving_flight

    def __str__(self):
        return "{}\n{}".format(self.departing_flight, self.arriving_flight)

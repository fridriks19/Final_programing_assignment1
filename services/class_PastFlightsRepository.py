#from models.class_past_flights import Past_flights

past_str = "2019-11-02T06:21:00"

class PastFlightsRepository():
    def __init__(self, past_str):
        self.past_str = past_str
    
    def get_PastFlights(self):
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

F1 = PastFlightsRepository(past_str)
print(F1.get_PastFlights())

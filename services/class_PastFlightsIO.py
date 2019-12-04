from models.class_past_flights import Past_flights

past_str = "NA5614,KEF,LYR,2019-11-02T06:21:00,2019-11-02T10:21:00,TF-TYQ,3009907461,2410876598,1600904199,3002688722,0505942924"

class PastFlightsIO():
    def __init__(self, past_str):
        self.past_str = past_str
    
    def load_PastFlights(self):
        open_file = open("PastFlights2.csv", "r")
        open_file_list = []
        for line in open_file:
            line = line.split("\n")
            line.pop(1)
            open_file_list.append(line)
        for flight in open_file_list:
            flight  = ",".join(flight)
            #print(flight)
            if flight == self.past_str:
                open_file.close()
                return flight

F1 = PastFlightsIO(past_str)
print(F1.load_PastFlights())

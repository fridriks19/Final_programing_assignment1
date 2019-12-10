
class VoyageRepo():
    
    def __init__(self, voyage_str=""):
        self.voyage_str = voyage_str
    
    def add_voyage(self, new_voyage):
        self.new_voyage = new_voyage
        open_file = open("./data/UpcomingFlights.csv", "a")
        open_file.write(self.new_voyage + "\n")
        open_file.close()
        return "Vinnuferð vistuð"
    
    def get_upc_voyage_list(self):
        voyage_list = []
        open_file = open("./data/UpcomingFlights.csv", "r")
        for line in open_file:
            line = line.strip()
            line = line.split(",")
            voyage_list.append(line)
        open_file.close()
        return voyage_list[1:]
    
    def get_past_voyage_list(self):
        voyage_list = []
        open_file = open("./data/PastFlights.csv", "r")
        for line in open_file:
            line = line.strip()
            line = line.split(",")
            voyage_list.append(line)
        open_file.close()
        return voyage_list[1:]

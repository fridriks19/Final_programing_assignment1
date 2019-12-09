from models.class_aircraft import Aircraft

class AircraftRepository:
    def __init__(self, aircr_type_str =""):
        self.aircr_type_str = aircr_type_str
    
    def add_aircraft_type(self,add_airc_str):
        self.add_airc_str = add_airc_str
        open_file = open("./data/AircraftType.csv", "a")
        open_file.write(self.add_airc_str + "\n")
        open_file.close()
        return "Flugvél vistuð"

    def get_aircraft_type(self):
        open_file = open("./data/Aircraft.csv", "r")
        open_file_list = []
        for line in open_file:
            line = line.strip()
            line = line.split(",")
            open_file_list.append(line)
        for aircraft_type in open_file_list:
            if aircraft_type[0] == self.aircr_type_str:
                open_file.close()
                return aircraft_type
        open_file.close()
        return "Flugvél fannst ekki"
    
    def get_all_aircraft_types(self):
        open_file = open("./data/Aircraft.csv", "r")
        open_file_list = []
        for line in open_file:
            line = line.strip()
            line = line.split(",")
            open_file_list.append(line)
        return open_file_list
        
    def get_aircrafts(self):
        aircraft_list = []
        open_file = open("./data/Aircraft.csv", "r")
        for line in open_file:
            line = line.strip().split(",")
            aircraft_list.append(line)
        return aircraft_list[1:]

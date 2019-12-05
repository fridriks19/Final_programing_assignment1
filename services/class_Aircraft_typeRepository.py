from models.class_aircraft import Aircraft

class AircraftRepository:

    def __init__(self, aircr_type_str):
        self.aircr_type_str = aircr_type_str
    
    def add_aircraft_type(self):
        open_file = open("./data/AircraftType.csv", "a")
        open_file.write(self.aircr_type_str + "\n")
        open_file.close()
        return "Flugvél vistuð"

    def get_aircraft_type(self):
        open_file = open("./data/AircraftType.csv", "r")
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
        open_file = open("./data/AircraftType.csv", "r")
        open_file_list = []
        for line in open_file:
            line = line.strip()
            line = line.split(",")
            open_file_list.append(line)
        prnt_str = ""
        for aircraft in open_file_list[1:]:
            aircraft = Aircraft(aircraft)
            prnt_str += "{}\n".format(aircraft.get_airctaftId())
        open_file.close()
        return prnt_str


a1 = AircraftRepository("")
#print(a1.save_aircraft_type())
print(a1.get_all_aircraft_types())
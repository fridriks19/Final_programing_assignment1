
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
            #aircraft_type = ",".join(aircraft_type)
            if aircraft_type[0] == self.aircr_type_str:
                open_file.close()
                return aircraft_type
        open_file.close()
        return "Flugvél fannst ekki"

a1 = AircraftRepository("NAFokker100")
#print(a1.save_aircraft_type())
print(a1.get_aircraft_type())
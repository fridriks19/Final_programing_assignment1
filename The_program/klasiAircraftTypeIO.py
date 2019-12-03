class AircraftTypeIO:

    def __init__(self, aircr_type_str):
        self.aircr_type_str = aircr_type_str
    
    def save_aircraft_type(self):
        open_file = open("AircraftType.csv", "a")
        open_file.write(self.aircr_type_str + "\n")
        open_file.close()
        return "Flugvél vistuð"

    def load_aircraft_type(self):
        open_file = open("AircraftType.csv", "r")
        open_file_list = []
        for line in open_file:
            line = line.split("\n")
            open_file_list.append(line)
        for aircraft_type in open_file_list:
            aircraft_type.pop(1)
            aircraft_type = ",".join(aircraft_type)
            print(aircraft_type)
            if aircraft_type == self.aircr_type_str:
                open_file.close()
                return aircraft_type
            else:
                open_file.close()
                return "Flugvél fannst ekki"

a1 = AircraftTypeIO("NEFokker99999,Fokk,F150,200,28574,64234,61.6,11000,35.53,8.50,28.08")
#print(a1.save_aircraft_type())
print(a1.load_aircraft_type())
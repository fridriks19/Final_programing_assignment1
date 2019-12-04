
class AircraftRepository:

    def __init__(self, aircr_type_str):
        self.aircr_type_str = aircr_type_str
    
<<<<<<< HEAD:services/class_aircraft_typeIO.py
    def save_aircraft_type(self):
        open_file = open("./data/AircraftType.csv", "a")
=======
    def add_aircraft_type(self):
        open_file = open("AircraftType.csv", "a")
>>>>>>> 47cb4bf5d5b904d31281cddcbfecb2f7c1b2d063:services/class_Aircraft_typeRepository.py
        open_file.write(self.aircr_type_str + "\n")
        open_file.close()
        return "Flugvél vistuð"

<<<<<<< HEAD:services/class_aircraft_typeIO.py
    def load_aircraft_type(self):
        open_file = open("./data/AircraftType.csv", "r")
=======
    def get_aircraft_type(self):
        open_file = open("AircraftType.csv", "r")
>>>>>>> 47cb4bf5d5b904d31281cddcbfecb2f7c1b2d063:services/class_Aircraft_typeRepository.py
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
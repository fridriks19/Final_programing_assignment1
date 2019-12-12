from models.class_destination import Destination

class DestinationRepo(Destination):
    """Data about Destinations, you can also change the info about the emergency contact"""

    def __init__(self, dest_str=""):
        self.dest_str = dest_str
        self.dest_list = [] 
        self.open_file()
        
    def open_file(self):
        self.dest_list = []
        open_file = open("./data/Destination2.csv", "r")
        for line in open_file:
            line = line.strip().split(",")
            self.dest_list.append(line)
        open_file.close()

    def add_dest(self, dest_str):
        """Add an destination to our destinations list"""

        self.dest_str = dest_str
        open_file = open("./data/Destination2.csv", "a")
        open_file.write(self.dest_str + "\n")
        open_file.close()
        return "Áfangastaður vistaður"

    def get_alldest(self):
        """Get all destinations from our destinations list"""

        prnt_str = ""
        counter = 1
        dest_dict = {}
        for line in self.dest_list[1:]:
            output = Destination(line)
            dest_dict[output.get_destinationId()] = output.get_destinationName()
        for key in dest_dict:
            prnt_str += ("'{}' - {} \n".format(counter, dest_dict[key]))   
            counter += 1
        return prnt_str, counter
    
    def get_all_dest_list(self):
        return self.dest_list[1:]

    def get_dest(self, user_input):
        self.user_input = int(user_input)
        self.open_file()
        chosen_dest = self.dest_list[self.user_input]
        return chosen_dest
  
    def change_dest(self, choice, change, dest):
        '''Get a list of all the destinations, so you can change the "contact" and his "emergency number"'''

        dest_dictionary = {}
        new_file = ""
        open_file_change = open("./data/Destination2.csv" , "r")
        for line in open_file_change:
            line = line.split(",")
            id_key = Destination(line)  
            dest_dictionary[id_key.get_destinationId()] = line
        open_file_change.close()
        dest_dictionary[dest][int(choice)+3] = change # Your choice will become change. The "+3" is because the first option is nut number 1, but it is 3 above.
        for key in dest_dictionary.keys():  #Go through all the values so we can add them to a new string 
            new_file += ",".join(dest_dictionary[key])  
        open_file_change = open("./data/Destination2.csv", "w")  #We replace the old crew file with the new file 
        open_file_change.write(new_file)
        open_file_change.close()
        self.open_file()
        return "Upplýsingum breytt"



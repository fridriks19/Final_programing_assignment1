from models.class_destination import Destination

class DestinationRepo(Destination):
    def __init__(self, dest_str=""):
        self.dest_str = dest_str
        self.dest_list = [] 
        open_file = open("./data/Destinations.csv", "r")
        for line in open_file:
            line = line.strip().split(",")
            self.dest_list.append(line)
        
    def get_alldest(self):
        prnt_str = ""
        counter = 1
        dest_dict = {}
        for line in self.dest_list[1:]:
            output = Destination(line)
            dest_dict[output.get_destinationId()] = output.get_destinationName()
        for key in dest_dict:
            prnt_str += ("'{}' - {}\n".format(counter, dest_dict[key]))   
            counter += 1
        print(str(prnt_str))

    def get_dest(self, user_input):  #Gets the destination and id 
        self.user_input = int(user_input)
        #print(self.dest_list)
        chosen_dest = self.dest_list[self.user_input]
        return "Áfangastaður: {}\nFlugvöllur: {}\nFlugtími: {}\nFjarlægð: {}\nTengiliður: {}\nNeyðarsímanúmer: {}".format(chosen_dest[1],chosen_dest[0], chosen_dest[2],chosen_dest[3],chosen_dest[4],chosen_dest[5])

    def get_dest_change(self, user_input):  #only diffrence is that we whant to show what to input to chose. 
        self.user_input = int(user_input)
        #print(self.dest_list)
        chosen_dest = self.dest_list[self.user_input]
        return "Áfangastaður: {}\nFlugvöllur: {}\nFlugtími: {}\nFjarlægð: {}\n'1' - Tengiliður: {}\n'2' - Neyðarsímanúmer: {}".format(chosen_dest[1],chosen_dest[0], chosen_dest[2],chosen_dest[3],chosen_dest[4],chosen_dest[5])

    


   
        


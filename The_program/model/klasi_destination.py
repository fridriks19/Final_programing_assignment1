class Destination():
    def __init__(self, destination_info_list):
        self.destination_info_list = destination_info_list
        self.destinationID = self.destination_info_list[0]
        self.destinationName = self.destination_info_list[1]
    
    def __str__(self):
        return "{}".format(self.destination_info_list)
class Destination():
    def __init__(self, destination_info_list):
        self.destination_info_list = destination_info_list
        self.__destinationId = self.destination_info_list[0]
        self.__destinationName = self.destination_info_list[1]
    
    def __str__(self):
        return "{}".format(self.destination_info_list)
    
    def get_destinationId(self):
        return self.__destinationId

    def get_destinationName(self):
        return self.__destinationName
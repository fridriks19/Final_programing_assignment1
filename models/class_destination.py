class Destination():  """xid,destination,flighttime,distance,contact,emergencyphonenumber"""
    def __init__(self, destination_info_list):
        self.destination_info_list = destination_info_list
        self.__destinationId = self.destination_info_list[0]
        self.__destinationName = self.destination_info_list[1]
        self.__flighttime = self.destination_info_list[2]
        self.__distance = self.destination_info_list[3]
        self.__contact = self.destination_info_list[4]
        self.__phone = self.destination_info_list[5]

    def __str__(self):
        prnt_str = ",".join(self.destination_info_list)
        return prnt_str
    
    def get_destinationId(self):
        return self.__destinationId

    def get_destinationName(self):
        return self.__destinationName
    
    def get_contact(self):
        return self.__contact

    def get_phone(self):
        return self.__phone

    def get_distance(self):
        return self.__distance
    
    def get_flighttime(self):
        return self.__flighttime
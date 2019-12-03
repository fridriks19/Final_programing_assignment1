class Airplane:
    """Aiplane has planeTypeId,planeType,model,capacity,emptyWeight,maxTakeoffWeight,
        unitThrust,serviceCeiling,length,height,wingspan"""

    def __init__(self, airplane_info_list):
        self.airplane_info_list = airplane_info_list
        self.__planeTypeId = self.airplane_info_list[0]
        self.__planeType = self.airplane_info_list[1]
        self.__model = self.airplane_info_list[2]
        self.__capacity = self.airplane_info_list[3]
        self.__emptyWeight = self.airplane_info_list[4]
        self.__maxTakeoffWeight = self.airplane_info_list[5]
        self.__unitThrust = self.airplane_info_list[6]
        self.__serviceCeiling = self.airplane_info_list[7]
        self.__length = self.airplane_info_list[8]
        self.__height = self.airplane_info_list[9]
        self.__wingspan = self.airplane_info_list[10]


    def __str__(self):
        prnt_str = ""
        for i in self.airplane_info_list:
            if airplane_info_list.index(i) == 10:
                prnt_str += i
            else:
                prnt_str += i + ","
        return prnt_str
        return "{}".format(self.airplane_info_list)

    def get_planeTypeId(self):
        return self.__planeTypeId
    
    def get_planetype(self):
        return self.__planeType








                                                            

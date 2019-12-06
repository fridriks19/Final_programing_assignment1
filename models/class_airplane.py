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
            if self.airplane_info_list.index(i) == 10:
                prnt_str += i
            else:
                prnt_str += i + ","
        return prnt_str
        #return "{}".format(self.airplane_info_list)

    def get_planeTypeId(self):
        return self.__planeTypeId
    
    def get_planetype(self):
        return self.__planeType

    def get_model(self):
        return self.__model

    def get_capacity(self):
        return self.__capacity

    def get_emptyWeight(self):
        return self.__emptyWeight
    
    def get_maxTakeoffWeight(self):
        return self.__maxTakeoffWeight

    def get_unitThrust(self):
        return self.__unitThrust
    
    def get_serviceCeiling(self):
        return self.__serviceCeiling

    def get_length(self):
        return self.__length

    def get_height(self):
        return self.__height

    def get_wingspan(self):
        return self.__wingspan
        






                                                            

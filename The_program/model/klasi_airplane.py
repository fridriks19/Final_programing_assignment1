class Airplane:
    """Aiplane has planeTypeId,planeType,model,capacity,emptyWeight,maxTakeoffWeight,
        unitThrust,serviceCeiling,length,height,wingspan"""

    def __init__(self, airplane_info_list):
        self.airplane_info_list = airplane_info_list
        self.planeTypeId = self.airplane_info_list[0]
        self.planeType = self.airplane_info_list[1]
        self.model = self.airplane_info_list[2]
        self.capacity = self.airplane_info_list[3]
        self.emptyWeight = self.airplane_info_list[4]
        self.maxTakeoffWeight = self.airplane_info_list[5]
        self.unitThrust = self.airplane_info_list[6]
        self.serviceCeiling = self.airplane_info_list[7]
        self.length = self.airplane_info_list[8]
        self.height = self.airplane_info_list[9]
        self.wingspan = self.airplane_info_list[10]


    def __str__(self):
        prnt_str = ""
        for i in self.airplane_info_list:
            if airplane_info_list.index(i) == 10:
                prnt_str += i
            else:
                prnt_str += i + ","
        return prnt_str
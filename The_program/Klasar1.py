#planeTypeId,planeType,model,capacity,emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan


class Airplane: 
    """Aiplane has planeTypeId,planeType,model,capacity,emptyWeight,maxTakeoffWeight
    unitThrust,serviceCeiling,length,height,wingspan"""

    def __init__ (self, planeTypeID, planetype, model, capacity, emptyweight, 
            maxTakeoffweight, unitThrust, serviceCeiling, length, height, wingspan):
      
        self.__planeTypeID = planeTypeID
        self.__planetype = planetype
        self.__model = model 
        self.__capacity = capacity
        self.__emptyweight = emptyweight
        self.__maxTakeoffweight = maxTakeoffweight
        self.__unitThrust = unitThrust
        self.__serviceCeiling = serviceCeiling
        self.__length = length
        self.__height = height
        self.__wingspan = wingspan

    def __str__(self):
        pass
#planeTypeId,planeType,model,capacity,emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan


class Airplane: 
    """Aiplane has planeTypeId,planeType,model,capacity,emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan"""

    def __init__ (self, planeTypeID, planetype, model, capacity, emptyweight, 
            maxTakeoffweight, unitThrust, serviceCeiling, length, height, wingspan):
      
        self.planeTypeID = planeTypeID
        self.planetype = planetype
        self.model = model 
        self.capacity = capacity
        self.emptyweight = emptyweight
        self.maxTakeoffweight = maxTakeoffweight
        self.unitThrust = unitThrust
        self.serviceCeiling = serviceCeiling
        self.length = length
        self.height = height
        self.wingspan = wingspan

    def __str__(self):
        pass
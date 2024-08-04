from vehicles import VehicleType

class ParkingSlot:
    __id = None
    __type = None
    __occupied = None
    __vehicle = None

    def __init__(self, slotId) -> None:
        self.__id = slotId
        self.__type = ""
        self.__occupied = False
        
        self.__setType()
    
    def __setType(self):
        number = int(self.__id.split('_')[-1])
        if(number==1):
            self.__type = VehicleType.TRUCK
        elif(number==2 or number==3):
            self.__type = VehicleType.BIKE
        else:
            self.__type = VehicleType.CAR
    
    def getType(self):
        return self.__type
    
    def __setOccupancy(self, occupancy):
        self.__occupied = occupancy
    
    def getOccupancy(self):
        return self.__occupied
    
    def getId(self):
        return self.__id
    
    def __setVehicle(self, vehicle):
        self.__vehicle = vehicle
    
    def getVehicle(self):
        return self.__vehicle

    def park(self, vehicle):
        if vehicle.getType()!=self.getType():
            raise Exception("vehicle-lot type mismatch")
        if self.getOccupancy()==True:
            raise Exception("Slot not empty")
        
        self.__setVehicle(vehicle)
        self.__setOccupancy(True)
        return self.getId()
    
    def unpark(self, id):
        if id!=self.getId():
            raise Exception("wrong lot")
        
        vehicle = self.getVehicle()
        self.__setVehicle(None)
        self.__setOccupancy(False)

        return vehicle
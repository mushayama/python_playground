from parking_slot import ParkingSlot
from vehicles import VehicleType, Bike

class ParkingFloor:
    __id = None
    __slots = None
    __totalTruckSlots = None
    __totalBikeSlots = None
    __totalCarSlots = None
    __occupiedTruckSlots = None
    __occupiedBikeSlots = None
    __occupiedCarSlots = None

    def __init__(self, floorId, numberOfSlots) -> None:
        self.__id = floorId
        self.__slots = []
        self.__totalTruckSlots = 0
        self.__totalBikeSlots = 0
        self.__totalCarSlots = 0
        self.__occupiedTruckSlots = 0
        self.__occupiedBikeSlots = 0
        self.__occupiedCarSlots = 0

        self.addSlots(numberOfSlots)
    
    def addSlots(self, numberOfSlots):
        slotsSoFar = len(self.__slots)
        for i in range(1, numberOfSlots+1):
            self.__slots.append(ParkingSlot(self.__id+'_'+str(slotsSoFar+i)))
        
        self.__setTotalSlots();

    def __setTotalSlots(self):
        totalSlots = len(self.__slots)
        
        if totalSlots>0:
            self.__totalTruckSlots = 1
            if totalSlots==2:
                self.__totalBikeSlots = 1
            elif totalSlots>=3:
                self.__totalBikeSlots = 2
                self.__totalCarSlots = totalSlots-3
    
    def getTotalSlots(self):
        return len(self.__slots)
    
    def getTotalTruckSlots(self):
        return self.__totalTruckSlots
    
    def getTotalBikeSlots(self):
        return self.__totalBikeSlots
    
    def getTotalCarSlots(self):
        return self.__totalCarSlots
    
    def getOccupiedTruckSlots(self):
        return self.__occupiedTruckSlots
    
    def getOccupiedBikeSlots(self):
        return self.__occupiedBikeSlots
    
    def getOccupiedCarSlots(self):
        return self.__occupiedCarSlots
    
    def adjustOccupiedSlots(self, type, change=1):
        if type == VehicleType.TRUCK:
            self.__occupiedTruckSlots+=change
        elif type == VehicleType.BIKE:
            self.__occupiedBikeSlots+=change
        else:
            self.__occupiedCarSlots+=change
    
    def getFreeSlotCount(self, type):
        if type == VehicleType.TRUCK:
            return self.getTotalTruckSlots()-self.getOccupiedTruckSlots()
        elif type == VehicleType.BIKE:
            return self.getTotalBikeSlots()-self.getOccupiedBikeSlots()
        elif type == VehicleType.CAR:
            return self.getTotalCarSlots()-self.getOccupiedCarSlots()
        else:
            raise Exception("Invalid vehicle type")
    
    def displayFreeCount(self, type):
        floorNumber = int(self.__id.split('_')[-1])
        print(f"No. of free slots for {type.name} on Floor {floorNumber}: {self.getFreeSlotCount(type)}")

    def getSlotIdsByOccupancy(self, type, occupied=False):
        slotIds = ""
        if type == VehicleType.TRUCK:
            if self.getTotalTruckSlots() != 0 and self.__slots[0].getOccupancy()==occupied:
                slotIds = slotIds + " 1"
        elif type == VehicleType.BIKE:
            for i in range(self.getTotalBikeSlots()):
                if self.__slots[1+i].getOccupancy()==occupied:
                    slotIds = slotIds + " " + str(2+i)
        elif type == VehicleType.CAR:
            for i in range(self.getTotalCarSlots()):
                if self.__slots[3+i].getOccupancy()==occupied:
                    slotIds = slotIds + " " + str(4+i)
        else:
            raise Exception("Inavlid vehicle type")
        return slotIds
    
    def displaySlots(self, type, occupied=False):
        floorNumber = int(self.__id.split('_')[-1])
        print(f"Free slots for {type.name} on Floor {floorNumber}:{self.getSlotIdsByOccupancy(type, occupied)}")
    
    def park(self, vehicle):
        if self.getFreeSlotCount(vehicle.getType())==0:
            raise Exception("no free slot")
        
        ticket = ""
        for i in range(self.getTotalSlots()):
            if vehicle.getType()==self.__slots[i].getType() and self.__slots[i].getOccupancy()==False:
                ticket = self.__slots[i].park(vehicle)
                self.adjustOccupiedSlots(vehicle.getType())
                break
        return ticket
    
    def unpark(self, ticket):
        slotId = int(ticket.split('_')[-1])
        if slotId>self.getTotalSlots():
            return "Invalid Ticket from floor"
        vehicle = self.__slots[slotId-1].unpark(ticket)
        self.adjustOccupiedSlots(vehicle.getType(),-1)
        return vehicle



    

    

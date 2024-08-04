from parking_floor import ParkingFloor
from vehicles import VehicleType

class ParkingLot:
    __id = None
    __floors = None
    __noOfTruckSlots = None
    __noOfBikeSlots = None
    __noOfCarSlots = None
    __occupiedTruckSlots = None
    __occupiedBikeSlots = None
    __occupiedCarSlots = None

    def __init__(self, id, floors, slotsPerFloor) -> None:
        self.__id = id
        self.__floors = []
        self.__noOfTruckSlots = 0;
        self.__noOfBikeSlots = 0;
        self.__noOfCarSlots = 0;
        self.__occupiedTruckSlots = 0;
        self.__occupiedBikeSlots = 0;
        self.__occupiedCarSlots = 0;
        
        self.addFloors(floors,slotsPerFloor)

    def addFloors(self, numberOfNewFloors, slotsPerFloor=0):
        floorsSoFar = len(self.__floors)
        for i in range(1, numberOfNewFloors+1):
            self.__floors.append(ParkingFloor(self.__id+'_'+str(floorsSoFar+i), slotsPerFloor))
            self.__noOfTruckSlots+= self.__floors[floorsSoFar+i-1].getTotalTruckSlots()
            self.__noOfBikeSlots+= self.__floors[floorsSoFar+i-1].getTotalBikeSlots()
            self.__noOfCarSlots+= self.__floors[floorsSoFar+i-1].getTotalCarSlots()

    def addSlotsToFloor(self, floorNumber, numberOfSlots=1):
        prevNoOfTruckSlots =  self.__floors[floorNumber-1].getTotalTruckSlots()
        prevNoOfBikeSlots =  self.__floors[floorNumber-1].getTotalBikeSlots()
        prevNoOfCarSlots =  self.__floors[floorNumber-1].getTotalCarSlots()

        self.floors[floorNumber-1].addSlots(numberOfSlots)

        self.__noOfTruckSlots+= self.__floors[floorNumber-1].getTotalTruckSlots() - prevNoOfTruckSlots
        self.__noOfBikeSlots+= self.__floors[floorNumber-1].getTotalBikeSlots() - prevNoOfBikeSlots
        self.__noOfCarSlots+= self.__floors[floorNumber-1].getTotalCarSlots() - prevNoOfCarSlots

    def display(self, displayType, vehicleType):
        if displayType=="free_count":
            for floor in range(len(self.__floors)):
                self.__floors[floor].displayFreeCount(vehicleType)
        elif displayType=="free_slots":
            for floor in range(len(self.__floors)):
                self.__floors[floor].displaySlots(vehicleType)
        elif displayType=="occupied_slots":
            for floor in range(len(self.__floors)):
                self.__floors[floor].displaySlots(vehicleType, True)
        else:
            raise Exception("Invalid display type")
    
    def checkAvailability(self, vehicleType):
        if vehicleType==VehicleType.TRUCK and self.__noOfTruckSlots==self.__occupiedTruckSlots:
            return False
        if vehicleType==VehicleType.BIKE and self.__noOfBikeSlots==self.__occupiedBikeSlots:
            return False
        if vehicleType==VehicleType.CAR and self.__noOfCarSlots==self.__occupiedCarSlots:
            return False
        return True
    
    def park(self, vehicle):
        if self.checkAvailability(vehicle.getType())==False:
            return "Parking Lot Full"
        
        ticket=""
        for floor in range(len(self.__floors)):
            if self.__floors[floor].getFreeSlotCount(vehicle.getType())!=0:
                ticket = self.__floors[floor].park(vehicle)
                if vehicle.getType()==VehicleType.TRUCK:
                    self.__occupiedTruckSlots+=1
                elif vehicle.getType()==VehicleType.BIKE:
                    self.__occupiedBikeSlots+=1
                else:
                    self.__occupiedCarSlots+=1
                break
        return ticket
    
    def unpark(self, ticket):
        if len(ticket.split('_'))!=3 or ticket.split('_')[0]!=self.__id or int(ticket.split('_')[1])>len(self.__floors):
            return "Invalid Ticket from lot"
        floorNo = int(ticket.split('_')[1])
        vehicle = self.__floors[floorNo-1].unpark(ticket)
        if vehicle.getType()==VehicleType.TRUCK:
            self.__occupiedTruckSlots-=1
        elif vehicle.getType()==VehicleType.BIKE:
            self.__occupiedBikeSlots-=1
        else:
            self.__occupiedCarSlots-=1
        return vehicle
    
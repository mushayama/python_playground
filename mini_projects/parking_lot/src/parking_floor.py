from .parking_slot import ParkingSlot
from .vehicles import VehicleType, Vehicle
from .display_board import DisplayBoard, DisplayType
from typing import Optional

class ParkingFloor:
    __floorId: str = None
    __parkingSlots: dict[VehicleType,list[ParkingSlot]] = None
    __noOfFreeSlots: dict[VehicleType, int] = None
    __displayBoard: DisplayBoard = None

    def __init__(self, floorId: str, numberOfSlots: int) -> None:
        self.__floorId = floorId
        self.__parkingSlots = {}
        self.__noOfFreeSlots = {}
        for type in VehicleType:
            self.__parkingSlots[type]=[]
            self.__noOfFreeSlots[type]=0

        self.__addSlots(numberOfSlots)

        self.__displayBoard: DisplayBoard = DisplayBoard()
    
    def __addSlots(self, numberOfSlots: int) -> None:
        for slotId in range(1, numberOfSlots+1):
            newSlot = ParkingSlot(self.__floorId+'_'+str(slotId))
            self.__parkingSlots[newSlot.getSlotType()].append(newSlot)
        
        self.__setNoOfFreeSlots();

    def __setNoOfFreeSlots(self) -> None:
        for type in VehicleType:
            self.__noOfFreeSlots[type] = len(self.__parkingSlots[type])
    
    def getNoOfFreeSlots(self, slotType: VehicleType) -> int:
        return self.__noOfFreeSlots[slotType]
    
    def getFloorId(self) -> str:
        return self.__floorId
    
    def display(self, displayType: DisplayType, slotType: VehicleType) -> None:
        self.__displayBoard.displayMessage(self.getFloorId().split('_')[1], self.__parkingSlots[slotType], self.__noOfFreeSlots[slotType], displayType, slotType)
    
    def park(self, vehicle: Vehicle) -> Optional[str]:
        for slot in self.__parkingSlots[vehicle.getVehicleType()]:
            if slot.getIsSlotFree():
                ticket = slot.park(vehicle)
                if ticket!=None:
                    self.__noOfFreeSlots[vehicle.getVehicleType()]-=1;
                return ticket
    
    def unpark(self, ticket: str) -> Optional[Vehicle]:
        for type in VehicleType:
            for slot in self.__parkingSlots[type]:
                if slot.getSlotId()==ticket:
                    vehicle = slot.unpark(ticket)
                    if vehicle!=None:
                        self.__noOfFreeSlots[type]+=1
                    return vehicle
        print("Invalid ticket")
        return None

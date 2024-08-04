from vehicles import VehicleType, Vehicle
from typing import Optional

class ParkingSlot:
    __slotId: str = None
    __slotType: VehicleType = None
    __isSlotFree: bool = None
    __vehicle: Optional[Vehicle] = None

    def __init__(self, slotId: str) -> None:
        self.__slotId = slotId
        self.__slotType = None
        self.__isSlotFree = True
        
        self.__setSlotType()
    
    def __setSlotType(self) -> None:
        number = int(self.__slotId.split('_')[-1])
        if(number==1):
            self.__slotType = VehicleType.TRUCK
        elif(number==2 or number==3):
            self.__slotType = VehicleType.BIKE
        else:
            self.__slotType = VehicleType.CAR
    
    def getSlotType(self) -> VehicleType:
        return self.__slotType
    
    def getSlotId(self) -> str:
        return self.__slotId
    
    def __setIsSlotFree(self, isSlotFree: bool) -> None:
        self.__isSlotFree = isSlotFree
    
    def getIsSlotFree(self) -> bool:
        return self.__isSlotFree
    
    def __setVehicle(self, vehicle: Vehicle) -> None:
        self.__vehicle = vehicle
    
    def getVehicle(self) -> Optional[Vehicle]:
        return self.__vehicle

    def park(self, vehicle: Vehicle) -> Optional[str]:
        if vehicle.getVehicleType()!=self.getSlotType():
            print("vehicle-lot type mismatch")
            return None
        if self.getIsSlotFree()==False:
            print("Slot not empty")
            return None
        
        self.__setVehicle(vehicle)
        self.__setIsSlotFree(False)
        return self.getSlotId()
    
    def unpark(self, ticket: str) -> Optional[Vehicle]:
        if ticket!=self.getSlotId():
            print("Wrong slot")
            return None
        if self.getVehicle()==None:
            print("No Vehicle found")
            return None
        
        vehicle = self.getVehicle()
        self.__setVehicle(None)
        self.__setIsSlotFree(True)

        return vehicle
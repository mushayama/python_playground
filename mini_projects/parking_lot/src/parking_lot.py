from .parking_floor import ParkingFloor
from .vehicles import VehicleType, Vehicle
from .display_board import DisplayType
from typing import Optional

class ParkingLot:
    __lotId: str = None
    __parkingFloors: list[ParkingFloor] = None

    def __init__(self, lotId: str, floors: int, slotsPerFloor: int) -> None:
        self.__lotId = lotId
        self.__parkingFloors = []
        
        self.__addFloors(floors,slotsPerFloor)
        print(f"Created parking lot with {floors} floors and {slotsPerFloor} slots per floor")

    def __addFloors(self, numberOfNewFloors: int, slotsPerFloor: int) -> None:
        for i in range(1, numberOfNewFloors+1):
            self.__parkingFloors.append(ParkingFloor(self.__lotId+'_'+str(i), slotsPerFloor))

    def display(self, displayType: DisplayType, vehicleType: VehicleType) -> None:
        for floor in self.__parkingFloors:
            floor.display(displayType, vehicleType)
    
    def park(self, vehicle: Vehicle) -> Optional[str]:
        for floor in self.__parkingFloors:
            if floor.getNoOfFreeSlots(vehicle.getVehicleType())!=0:
                ticket = floor.park(vehicle)
                return ticket
        print("Parking Lot Full")
        return None
    
    def unpark(self, ticket: str) -> Optional[Vehicle]:
        if len(ticket.split('_'))!=3 or ticket.split('_')[0]!=self.__lotId or int(ticket.split('_')[1])>len(self.__parkingFloors):
            return "Invalid Ticket"
        
        floorNo = int(ticket.split('_')[1])
        vehicle = self.__parkingFloors[floorNo-1].unpark(ticket)
        return vehicle
    
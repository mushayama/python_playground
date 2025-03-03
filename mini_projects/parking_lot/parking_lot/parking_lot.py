from .parking_floor import ParkingFloor
from .vehicles import VehicleType, Vehicle
from .display_board import DisplayType
from typing import Optional

class ParkingLot:
    __lot_id: str = None
    __parking_floors: list[ParkingFloor] = None

    def __init__(self, lot_id: str, floors: int, slots_per_floor: int) -> None:
        self.__lot_id = lot_id
        self.__parking_floors = []

        self.__add_floors(floors, slots_per_floor)
        print(f"Created parking lot with {floors} floors and {slots_per_floor} slots per floor")

    def __add_floors(self, number_of_new_floors: int, slots_per_floor: int) -> None:
        for i in range(1, number_of_new_floors+1):
            self.__parking_floors.append(ParkingFloor(self.__lot_id+'_'+str(i), slots_per_floor))

    def display(self, display_type: DisplayType, vehicle_type: VehicleType) -> None:
        for floor in self.__parking_floors:
            floor.display(display_type, vehicle_type)

    def park(self, vehicle: Vehicle) -> Optional[str]:
        for floor in self.__parking_floors:
            if floor.get_no_of_free_slots(vehicle.get_vehicle_type())!=0:
                ticket = floor.park(vehicle)
                return ticket
        print("Parking Lot Full")
        return None

    def unpark(self, ticket: str) -> Optional[Vehicle]:
        if len(ticket.split('_'))!=3 or ticket.split('_')[0]!=self.__lot_id or int(ticket.split('_')[1])>len(self.__parking_floors):
            return "Invalid Ticket"

        floor_no = int(ticket.split('_')[1])
        vehicle = self.__parking_floors[floor_no-1].unpark(ticket)
        return vehicle

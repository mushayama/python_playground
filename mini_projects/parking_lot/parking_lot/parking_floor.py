from .parking_slot import ParkingSlot
from .vehicles import VehicleType, Vehicle
from .display_board import DisplayBoard, DisplayType
from typing import Optional

class ParkingFloor:
    __floor_id: str = None
    __parking_slots: dict[VehicleType,list[ParkingSlot]] = None
    __no_of_free_slots: dict[VehicleType, int] = None
    __display_board: DisplayBoard = None

    def __init__(self, floor_id: str, number_of_slots: int) -> None:
        self.__floor_id = floor_id
        self.__parking_slots = {}
        self.__no_of_free_slots = {}
        for type in VehicleType:
            self.__parking_slots[type]=[]
            self.__no_of_free_slots[type]=0

        self.__add_slots(number_of_slots)

        self.__display_board: DisplayBoard = DisplayBoard()

    def __add_slots(self, number_of_slots: int) -> None:
        for slot_id in range(1, number_of_slots+1):
            new_slot = ParkingSlot(self.__floor_id+'_'+str(slot_id))
            self.__parking_slots[new_slot.get_slot_type()].append(new_slot)

        self.__set_no_of_free_slots();

    def __set_no_of_free_slots(self) -> None:
        for type in VehicleType:
            self.__no_of_free_slots[type] = len(self.__parking_slots[type])

    def get_no_of_free_slots(self, slot_type: VehicleType) -> int:
        return self.__no_of_free_slots[slot_type]

    def get_floor_id(self) -> str:
        return self.__floor_id

    def display(self, display_type: DisplayType, slot_type: VehicleType) -> None:
        self.__display_board.display_message(self.get_floor_id().split('_')[1], self.__parking_slots[slot_type], self.__no_of_free_slots[slot_type], display_type, slot_type)

    def park(self, vehicle: Vehicle) -> Optional[str]:
        for slot in self.__parking_slots[vehicle.get_vehicle_type()]:
            if slot.get_is_slot_free():
                ticket = slot.park(vehicle)
                if ticket!=None:
                    self.__no_of_free_slots[vehicle.get_vehicle_type()]-=1;
                return ticket

    def unpark(self, ticket: str) -> Optional[Vehicle]:
        for type in VehicleType:
            for slot in self.__parking_slots[type]:
                if slot.get_slot_id()==ticket:
                    vehicle = slot.unpark(ticket)
                    if vehicle!=None:
                        self.__no_of_free_slots[type]+=1
                    return vehicle
        print("Invalid ticket")
        return None

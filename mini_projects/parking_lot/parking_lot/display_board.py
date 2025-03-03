from .vehicles import VehicleType
from .parking_slot import ParkingSlot
from typing import Literal

DisplayType = Literal["free_count", "free_slots", "occupied_slots"]

class DisplayBoard:
    def display_message(self, floor_id: str, parking_slots: list[ParkingSlot], no_of_free_slots: int, display_type: DisplayType, slot_type: VehicleType) -> None:
        if display_type == "free_count":
            self.__display_count(slot_type, floor_id, no_of_free_slots)
        elif display_type == "free_slots":
            self.__display_slots(slot_type, floor_id, parking_slots, True)
        else:
            self.__display_slots(slot_type, floor_id, parking_slots, False)

    def __display_count(self, slot_type: VehicleType, floor_no: str, no_of_free_slots: int) -> None:
        print(f"No. of free slots for {slot_type.value} on Floor {floor_no}: {no_of_free_slots}")

    def __display_slots(self, slot_type: VehicleType, floor_no: str, parking_slots: list[ParkingSlot], free_slots: bool) -> None:
        slots_to_show = ""
        for slot in parking_slots:
            if slot.get_is_slot_free()==free_slots:
                slots_to_show=slots_to_show+","+slot.get_slot_id().split('_')[-1]
        free_string = "Free" if free_slots else "Occupied"
        print(f"{free_string} slots for {slot_type.value} on Floor {floor_no}: {slots_to_show[1:]}")

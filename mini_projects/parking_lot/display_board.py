from vehicles import VehicleType
from parking_slot import ParkingSlot
from typing import Literal

DisplayType = Literal["free_count", "free_slots", "occupied_slots"]

class DisplayBoard:
    def displayMessage(self, floorId: str, parkingSlots: list[ParkingSlot], noOfFreeSlots: int, display_type: DisplayType, slotType: VehicleType) -> None:
        if display_type == "free_count":
            self.displayCount(slotType, floorId, noOfFreeSlots)
        elif display_type == "free_slots":
            self.displaySlots(slotType, floorId, parkingSlots, True)
        else:
            self.displaySlots(slotType, floorId, parkingSlots, False)
    
    def displayCount(self, slotType: VehicleType, floorNo: str, noOfFreeSlots: int) -> None:
        print(f"No. of free slots for {slotType.value} on Floor {floorNo}: {noOfFreeSlots}")

    def displaySlots(self, slotType: VehicleType, floorNo: str, parkingSlots: list[ParkingSlot], freeSlots: bool) -> None:
        slotsToShow = ""
        for slot in parkingSlots:
            if slot.getIsSlotFree()==freeSlots:
                slotsToShow=slotsToShow+","+slot.getSlotId().split('_')[-1]
        freeString = "Free" if freeSlots else "Occupied"
        print(f"{freeString} slots for {slotType.value} on Floor {floorNo}: {slotsToShow[1:]}")


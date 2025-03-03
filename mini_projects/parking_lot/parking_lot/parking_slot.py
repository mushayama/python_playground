from .vehicles import VehicleType, Vehicle
from typing import Optional

class ParkingSlot:
    __slot_id: str = None
    __slot_type: VehicleType = None
    __is_slot_free: bool = None
    __vehicle: Optional[Vehicle] = None

    def __init__(self, slot_id: str) -> None:
        self.__slot_id = slot_id
        self.__slot_type = None
        self.__is_slot_free = True

        self.__set_slot_type()

    def __set_slot_type(self) -> None:
        number = int(self.__slot_id.split('_')[-1])
        if(number==1):
            self.__slot_type = VehicleType.TRUCK
        elif(number==2 or number==3):
            self.__slot_type = VehicleType.BIKE
        else:
            self.__slot_type = VehicleType.CAR

    def get_slot_type(self) -> VehicleType:
        return self.__slot_type

    def get_slot_id(self) -> str:
        return self.__slot_id

    def __set_is_slot_free(self, is_slot_free: bool) -> None:
        self.__is_slot_free = is_slot_free

    def get_is_slot_free(self) -> bool:
        return self.__is_slot_free

    def __set_vehicle(self, vehicle: Vehicle) -> None:
        self.__vehicle = vehicle

    def get_vehicle(self) -> Optional[Vehicle]:
        return self.__vehicle

    def park(self, vehicle: Vehicle) -> Optional[str]:
        if vehicle.get_vehicle_type()!=self.get_slot_type():
            print("vehicle-lot type mismatch")
            return None
        if self.get_is_slot_free()==False:
            print("Slot not empty")
            return None

        self.__set_vehicle(vehicle)
        self.__set_is_slot_free(False)
        return self.get_slot_id()

    def unpark(self, ticket: str) -> Optional[Vehicle]:
        if ticket!=self.get_slot_id():
            print("Wrong slot")
            return None
        if self.get_vehicle()==None:
            print("No Vehicle found")
            return None

        vehicle = self.get_vehicle()
        self.__set_vehicle(None)
        self.__set_is_slot_free(True)

        return vehicle
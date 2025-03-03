from enum import Enum

class VehicleType(Enum):
    TRUCK = "TRUCK"
    BIKE = "BIKE"
    CAR = "CAR"

class Vehicle:
    __vehicle_reg_no: str = None
    __vehicle_color: str = None
    __vehicle_type: VehicleType = None

    def __init__(self, vehicle_reg_no: str, vehicle_color: str, vehicle_type: VehicleType) -> None:
        self.__vehicle_reg_no = vehicle_reg_no
        self.__vehicle_color = vehicle_color
        self.__vehicle_type = vehicle_type

    def get_vehicle_reg_no(self):
        return self.__vehicle_reg_no

    def get_vehicle_color(self):
        return self.__vehicle_color

    def get_vehicle_type(self):
        return self.__vehicle_type

class Truck(Vehicle):
    def __init__(self, vehicle_reg_no: str, vehicle_color: str) -> None:
        super().__init__(vehicle_reg_no, vehicle_color, VehicleType.TRUCK)

class Bike(Vehicle):
    def __init__(self, vehicle_reg_no: str, vehicle_color: str) -> None:
        super().__init__(vehicle_reg_no, vehicle_color, VehicleType.BIKE)

class Car(Vehicle):
    def __init__(self, vehicle_reg_no: str, vehicle_color: str) -> None:
        super().__init__(vehicle_reg_no, vehicle_color, VehicleType.CAR)
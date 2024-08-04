from enum import Enum

class VehicleType(Enum):
    TRUCK = "TRUCK"
    BIKE = "BIKE"
    CAR = "CAR"

class Vehicle:
    __vehicleRegNo: str = None
    __vehicleColor: str = None
    __vehicleType: VehicleType = None

    def __init__(self, vehicleRegNo: str, vehicleColor: str, vehicleType: VehicleType) -> None:
        self.__vehicleRegNo = vehicleRegNo
        self.__vehicleColor = vehicleColor
        self.__vehicleType = vehicleType
    
    def getVehicleRegNo(self):
        return self.__vehicleRegNo

    def getVehicleColor(self):
        return self.__vehicleColor
    
    def getVehicleType(self):
        return self.__vehicleType

class Truck(Vehicle):
    def __init__(self, vehicleRegNo: str, vehicleColor: str) -> None:
        super().__init__(vehicleRegNo, vehicleColor, VehicleType.TRUCK)

class Bike(Vehicle):
    def __init__(self, vehicleRegNo: str, vehicleColor: str) -> None:
        super().__init__(vehicleRegNo, vehicleColor, VehicleType.BIKE)

class Car(Vehicle):
    def __init__(self, vehicleRegNo: str, vehicleColor: str) -> None:
        super().__init__(vehicleRegNo, vehicleColor, VehicleType.CAR)
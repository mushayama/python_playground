from enum import Enum

class VehicleType(Enum):
    TRUCK = 1
    BIKE = 2
    CAR = 3

class Vehicle:
    __registrationNo = None
    __color = None
    __type = None

    def __init__(self, registrationNo, color, type) -> None:
        self.__registrationNo = registrationNo
        self.__color = color
        self.__type = type
    
    def getRegistrationNo(self):
        return self.__registrationNo

    def getColor(self):
        return self.__color
    
    def getType(self):
        return self.__type

class Truck(Vehicle):
    def __init__(self, registrationNo, color) -> None:
        super().__init__(registrationNo, color, VehicleType.TRUCK)

class Bike(Vehicle):
    def __init__(self, registrationNo, color) -> None:
        super().__init__(registrationNo, color, VehicleType.BIKE)

class Car(Vehicle):
    def __init__(self, registrationNo, color) -> None:
        super().__init__(registrationNo, color, VehicleType.CAR)
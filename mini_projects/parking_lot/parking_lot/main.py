from .parking_lot import ParkingLot
from .vehicles import Vehicle, VehicleType
from .display_board import DisplayType
from typing import Optional, get_args

def display_commands():
    print("You can enter one of the following commands at a time:")
    print("create_parking_lot <parking_lot_id> <no_of_floors> <no_of_slots_per_floor>")
    print("park_vehicle <vehicle_type> <reg_no> <color>")
    print("unpark_vehicle <ticket_id>")
    print("display <display_type> <vehicle_type>")
    print("\tPossible display_type: free_count, free_slots, occupied_slots")
    print("exit")
    print()

def create_parking_lot(args: list[str]) -> Optional[ParkingLot]:
    if(len(args)!=4 or int(args[2])>100 or int(args[2])<0 or int(args[3])>100 or int(args[3])<0):
        print("Invalid Command")
        return None

    return ParkingLot(args[1], int(args[2]), int(args[3]))

def park_vehicle(parkingLot: Optional[ParkingLot], args) -> None:
    if parkingLot==None:
        print("Create a parking lot first")
        return

    if len(args)!=4 or not(args[1] in VehicleType._value2member_map_):
        print("Invalid Input")
        return

    _, vehicleType, regNo, color = args

    vehicle=Vehicle(regNo, color, VehicleType(vehicleType))

    if vehicle!=None:
        ticket = parkingLot.park(vehicle)

        if ticket !=None:
            print(f"Parked Vehicle. Ticket ID: {ticket}")

def unpark_vehicle(parkingLot: Optional[ParkingLot], args) -> None:
    if parkingLot==None:
        print("Create a parking lot first")
        return

    if len(args)!=2:
        print("Invalid Input")
        return

    vehicle = parkingLot.unpark(args[1])
    if vehicle!=None:
        print(f"Unparked vehicle with Registration Number: {vehicle.get_vehicle_reg_no()} and color {vehicle.get_vehicle_color()}")

def display(parkingLot: Optional[ParkingLot], args: list[str]) -> None:
    if parkingLot==None:
        print("Create a parking lot first")
        return

    if len(args)!=3 or not(args[1] in get_args(DisplayType)) or not(args[2] in VehicleType._value2member_map_):
        print("invalid Input")
        return

    vehicleType = VehicleType(args[2])

    parkingLot.display(args[1], vehicleType)

def main() -> None:
    print("Welcome to our parking lot system")
    display_commands()

    parkingLot=None

    while(True):
        command = input("Enter your command: ")

        commandAttributes = command.split()
        if command=="exit":
            break
        elif commandAttributes[0]=="create_parking_lot":
            parkingLot = create_parking_lot(commandAttributes)
        elif commandAttributes[0]=="park_vehicle":
            park_vehicle(parkingLot, commandAttributes)
        elif commandAttributes[0]=="unpark_vehicle":
            unpark_vehicle(parkingLot, commandAttributes)
        elif commandAttributes[0]=="display":
            display(parkingLot, commandAttributes)
        elif command=="C":
            display_commands()
        else:
            print("Invalid Input")

        print("Enter C to display commands again")
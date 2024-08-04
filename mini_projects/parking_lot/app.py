from parking_lot import ParkingLot
from vehicles import Car, Bike, Truck, VehicleType

def displayCommands():
    print("You can enter one of the following commands at a time:")
    print("create_parking_lot <parking_lot_id> <no_of_floors> <no_of_slots_per_floor>")
    print("park_vehicle <vehicle_type> <reg_no> <color>")
    print("unpark_vehicle <ticket_id>")
    print("display <display_type> <vehicle_type>")
    print("\tPossible display_type: free_count, free_slots, occupied_slots")
    print("exit")
    print()

def createParkingLot(command):
    attributes = command.split()
    if(len(attributes)!=4 or int(attributes[2])>100 or int(attributes[2])<0 or int(attributes[3])>100 or int(attributes[3])<0):
        print("Invalid Command")
        return None
    
    return ParkingLot(attributes[1], int(attributes[2]), int(attributes[3]))

def parkVehicle(parkingLot, command):
    if parkingLot==None:
        print("Create a parking lot first")
        return
    attributes = command.split()
    if len(attributes)!=4 or not(attributes[1]=="CAR" or attributes[1]=="BIKE" or attributes[1]=="TRUCK"):
        print("Invalid Input")
        return
    _, vehicleType, regNo, color = command.split()
    vehicle=None
    if attributes[1]=="CAR":
        vehicle=Car(regNo, color)
    elif attributes[1]=="BIKE":
        vehicle = Bike(regNo, color)
    else:
        vehicle = Truck(regNo, color)
    
    if vehicle!=None:
        ticket = parkingLot.park(vehicle)

        if ticket == "Parking Lot Full":
            print(ticket)
        else:
            print(f"Parked Vehicle. Ticket ID: {ticket}")

def unparkVehicle(parkingLot, command):
    if parkingLot==None:
        print("Create a parking lot first")
        return
    attributes = command.split()

    if len(attributes)!=2:
        print("Invalid Input")
        return
    
    print(attributes[1])
    vehicle = parkingLot.unpark(attributes[1])
    print(vehicle)
    # print(f"Unparked vehicle with Registration Number: {vehicle.getResgistrationNo()} and color {vehicle.getColor()}")

def display(parkingLot, command):
    if parkingLot==None:
        print("Create a parking lot first")
        return
    attributes = command.split()

    if len(attributes)!=3 or not(attributes[1]=="free_count" or attributes[1]=="free_slots" or attributes[1]=="occupied_slots"):
        print("invalid Input")
        return
    
    vehicleType = None
    if attributes[2]=="CAR":
        vehicleType = VehicleType.CAR
    elif attributes[2]=="TRUCK":
        vehicleType = VehicleType.TRUCK
    elif attributes[2]=="BIKE":
        vehicleType = VehicleType.BIKE
    
    parkingLot.display(attributes[1], vehicleType)

def __main__():
    print("Welcome to our parking lot system")
    displayCommands()

    parkingLot=None

    while(True):
        command = input("Enter your command: ")

        commandType= command.split()[0]
        if command=="exit":
            break
        elif commandType=="create_parking_lot":
            parkingLot = createParkingLot(command)
        elif commandType=="park_vehicle":
            parkVehicle(parkingLot, command)
        elif commandType=="unpark_vehicle":
            unparkVehicle(parkingLot, command)
        elif commandType=="display":
            display(parkingLot, command)
        elif commandType=="C":
            displayCommands()
        else:
            print("Invalid Input")
        
        print("Enter C to display commands again")

__main__()

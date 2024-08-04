import unittest
from ..parking_lot import ParkingLot
from ..parking_floor import ParkingFloor
from ..parking_slot import ParkingSlot
from ..vehicles import Truck, Car, Bike, VehicleType

class TestParkingLot(unittest.TestCase):
    def testParkingSlot(self):
        self.assertEqual(ParkingSlot("Lot1234_2_1").getType(), VehicleType.TRUCK)
        self.assertEqual(ParkingSlot("Lot1234_2_2").getType(), VehicleType.BIKE)
        self.assertEqual(ParkingSlot("Lot1234_2_3").getType(), VehicleType.BIKE)
        self.assertEqual(ParkingSlot("Lot1234_2_4").getType(), VehicleType.CAR)
        self.assertEqual(ParkingSlot("Lot1234_2_5").getType(), VehicleType.CAR)
    
    def testParkingSlotParking(self):
        parkingSlot = ParkingSlot("Lot1234_2_1")

        self.assertEqual(parkingSlot.getOccupancy(), False)

        truck = Truck("up21/bleah/ble", "blue")

        ticket = parkingSlot.park(truck)
        self.assertEqual(parkingSlot.getOccupancy(), True)
        self.assertEqual(parkingSlot.getId(), ticket)
        self.assertEqual(ticket, "Lot1234_2_1")
        self.assertEqual(parkingSlot.getVehicle(), truck)

        vehicle = parkingSlot.unpark(ticket)
        self.assertEqual(parkingSlot.getOccupancy(), False)
        self.assertEqual(parkingSlot.getVehicle(), None)
        self.assertEqual(vehicle, truck)

    # def testParkingLotCreation(self):
    #     parkingLot = ParkingLot("Lot1234", 4, 5)
        
    #     self.assertEqual(parkingLot.id, "Lot1234")
    #     self.assertEqual(len(parkingLot.floors), 4)
    #     for floor in range(len(parkingLot.floors)):
    #         self.assertEqual(parkingLot.floors[floor].id,parkingLot.id+"_"+str(floor+1))
    #         self.assertEqual(len(parkingLot.floors[floor].slots),5)
    #         for slot in range(len(parkingLot.floors[floor].slots)):
    #             self.assertEqual(parkingLot.floors[floor].slots[slot].id, parkingLot.floors[floor].id+'_'+str(slot+1))
        
    
    # def testParkingLotAddFloor(self):
    #     parkingLot = ParkingLot("Lot1234", 4, 5)
    #     parkingLot.addFloors(2)
    #     self.assertEqual(len(parkingLot.floors), 6)
    
    # def testParkingLotAddSlotsToFloor(self):
    #     parkingLot = ParkingLot("Lot1234", 4, 5)
    #     parkingLot.addSlotsToFloor(3, 3)
    #     self.assertEqual(len(parkingLot.floors[2].slots),8)

if __name__ == '__main__':
    unittest.main()
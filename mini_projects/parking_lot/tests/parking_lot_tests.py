import unittest
import unittest.mock
import builtins
import contextlib, io
from ..src.parking_lot import ParkingLot
from ..src.parking_floor import ParkingFloor
from ..src.parking_slot import ParkingSlot
from ..src.vehicles import Vehicle, VehicleType
from ..src.display_board import DisplayBoard, DisplayType

'''
Run command:
python3 -m unittest mini_projects/parking_lot/tests/parking_lot_tests.py
from appropriate directory ofc
'''

class TestParkingLot(unittest.TestCase):
    def testParkingSlot(self):
        self.assertEqual(ParkingSlot("Lot1234_2_1").getSlotType(), VehicleType.TRUCK)
        self.assertEqual(ParkingSlot("Lot1234_2_2").getSlotType(), VehicleType.BIKE)
        self.assertEqual(ParkingSlot("Lot1234_2_3").getSlotType(), VehicleType.BIKE)
        self.assertEqual(ParkingSlot("Lot1234_2_4").getSlotType(), VehicleType.CAR)
        self.assertEqual(ParkingSlot("Lot1234_2_5").getSlotType(), VehicleType.CAR)
    
    def testParkingSlotParking(self):
        parkingSlot = ParkingSlot("Lot1234_2_1")

        self.assertEqual(parkingSlot.getIsSlotFree(), True)

        truck = Vehicle("up21/bleah/ble", "blue", VehicleType.TRUCK)

        ticket = parkingSlot.park(truck)
        self.assertEqual(parkingSlot.getIsSlotFree(), False)
        self.assertEqual(parkingSlot.getSlotId(), ticket)
        self.assertEqual(ticket, "Lot1234_2_1")
        self.assertEqual(parkingSlot.getVehicle(), truck)

        vehicle = parkingSlot.unpark(ticket)
        self.assertEqual(parkingSlot.getIsSlotFree(), True)
        self.assertEqual(parkingSlot.getVehicle(), None)
        self.assertEqual(vehicle, truck)
    
    def testParkingFloor(self):
        parkingFloor = ParkingFloor("Lot1234_2", 5)

        self.assertEqual(parkingFloor.getFloorId(), "Lot1234_2")
        self.assertEqual(parkingFloor.getNoOfFreeSlots(VehicleType.TRUCK),1)
        self.assertEqual(parkingFloor.getNoOfFreeSlots(VehicleType.BIKE),2)
        self.assertEqual(parkingFloor.getNoOfFreeSlots(VehicleType.CAR),2)
    
    def testParkingFloorParking(self):
        parkingFloor = ParkingFloor("Lot1234_2", 5)

        bike = Vehicle("up21/bleah/ble", "blue", VehicleType.BIKE)

        bikeSlotCount = parkingFloor.getNoOfFreeSlots(VehicleType.BIKE)
        ticket = parkingFloor.park(bike)
        self.assertEqual(ticket, "Lot1234_2_2")
        self.assertEqual(bikeSlotCount-1, parkingFloor.getNoOfFreeSlots(VehicleType.BIKE))

        mock = unittest.mock.Mock()
        mock.side_effect = print
        print_original = print
        builtins.print = mock
        
        str_io = io.StringIO()
        with contextlib.redirect_stdout(str_io):
            parkingFloor.unpark("gibberish_1_1")
        output = str_io.getvalue()

        assert print.called
        assert output.startswith("Invalid ticket")
        builtins.print = print_original

        vehicle = parkingFloor.unpark(ticket)
        self.assertEqual(bikeSlotCount, parkingFloor.getNoOfFreeSlots(VehicleType.BIKE))
        self.assertEqual(vehicle, bike)
    
    def testParkingLotParking(self):
        parkingLot = ParkingLot("lot1234", 1, 5)

        car1 = Vehicle("up21/bleh/blah", "white", VehicleType.CAR)
        ticket1 = parkingLot.park(car1)

        self.assertEqual(ticket1, "lot1234_1_4")

        parkingLot.park(Vehicle("zxcv/bnm", "red", VehicleType.CAR))

        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            parkingLot.park(Vehicle("qwert", "black", VehicleType.CAR))
            self.assertEqual(
                mock_stdout.getvalue(),
                'Parking Lot Full\n'  # It's important to remember about '\n'
            )
        
        self.assertEqual(parkingLot.unpark("gibberish"), "Invalid Ticket")

        vehicle = parkingLot.unpark(ticket1)
        self.assertEqual(vehicle, car1)

    def testParkingLotDisplay(self):
        displayBoard = DisplayBoard()

        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            displayBoard.displayMessage("0",[],2,"free_count",VehicleType.CAR)
            self.assertEqual(
                mock_stdout.getvalue(),
                'No. of free slots for CAR on Floor 0: 2\n'  # It's important to remember about '\n'
            )
        
        slot1 = ParkingSlot("lot1234_1_4")
        slot2 = ParkingSlot("lot1234_1_5")

        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            displayBoard.displayMessage("0",[slot1, slot2],0,"free_slots",VehicleType.CAR)
            self.assertEqual(
                mock_stdout.getvalue(),
                'Free slots for CAR on Floor 0: 4,5\n'  # It's important to remember about '\n'
            )
        
        slot1.park(Vehicle("qwerty", "color", VehicleType.CAR))
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            displayBoard.displayMessage("0",[slot1, slot2],0,"occupied_slots",VehicleType.CAR)
            self.assertEqual(
                mock_stdout.getvalue(),
                'Occupied slots for CAR on Floor 0: 4\n'  # It's important to remember about '\n'
            )


if __name__ == '__main__':
    unittest.main()
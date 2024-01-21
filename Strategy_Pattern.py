#Strategy Pattern
from abc import ABC, abstractmethod

class DriveStrategy(ABC):
    @abstractmethod
    def drive(self):
        pass

class NormalDriveStrategy(DriveStrategy):
    def drive(self):
        print('Normal Drive Capability')

class SportsDriveStrategy(DriveStrategy):
    def drive(self):
        print('Sports Drive Capability')

class Vehicle:
    def __init__(self, driveObj: DriveStrategy):
        self.driveObject = driveObj
    def drive(self):
        self.driveObject.drive()

class SportsVehicle(Vehicle):
    def __init__(self):
        super().__init__(SportsDriveStrategy())


class NormalVehicle(Vehicle):
    def __init__(self):
        super().__init__(NormalDriveStrategy())

class OffRoadVehicle(Vehicle):
    def __init__(self):
        super().__init__(SportsDriveStrategy())

OffRoadVehicle().drive()

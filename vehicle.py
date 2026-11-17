from abc import ABC

class Vehicle(ABC):

    speed = {
        'car': 60,
        'bike': 30,
        'cng': 20,
    }
    def __init__(self, license_plate, vehicle_type, rate) -> None:
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type
        self.rate = rate

class Car(Vehicle):
    def __init__(self, license_plate, vehicle_type, rate) -> None:
        super().__init__(license_plate, vehicle_type, rate)

class Bike(Vehicle):
    def __init__(self, license_plate, vehicle_type, rate) -> None:
        super().__init__(license_plate, vehicle_type, rate)

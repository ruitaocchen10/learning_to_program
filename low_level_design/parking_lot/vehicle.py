from enum import Enum

class VehicleType(Enum):
    motorcycle = "motorcycle"
    car = "car"
    truck = "truck"

class Vehicle:
    def __init__(self, v_type: VehicleType):
        self.v_type = v_type
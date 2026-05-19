from enum import Enum

class VehicleType(Enum):
    motorcycle = "motorcycle"
    car = "car"
    truck = "truck"

class Vehicle:
    def __init__(self, name: str, v_type: VehicleType):
        self.name = name
        self.v_type = v_type

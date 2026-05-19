from enum import Enum
from vehicle import Vehicle
from typing import Optional

class SpotType(Enum):
    small = "small"
    medium = "medium"
    large = "large"

class ParkingSpot:
    def __init__ (self, name, spot_type: str, state: Optional[Vehicle] = None):
        self.name = name
        self.type = SpotType(spot_type)
        self.state = state

    def printSpot(self):
        return self.name, self.type, self.state
    


        
        
    


from parking_spot import ParkingSpot
from vehicle import Vehicle

class ParkingLot:
    def __init__(self, sm_spots: int = 20, md_spots: int = 50, lg_spots: int = 30):
        self.sm_spots = [ ParkingSpot((f"S{num}"), "small", None) for num in range(sm_spots) ]
        self.md_spots = [ ParkingSpot((f"M{num}"), "medium", None) for num in range(md_spots) ]
        self.lg_spots = [ ParkingSpot((f"L{num}"), "large", None) for num in range(lg_spots) ]
        
        self.lots = [ self.sm_spots, self.md_spots, self.lg_spots ]

    def get_spots(self):
        return self.lots
    
    def lot_full(self):
        for lot in self.lots:
            for spot in lot:
                if spot.state is None:
                    return False
        
        return True
    
    def s_lot_full(self):
        for spot in self.sm_spots:
            if spot.state is None:
                return False
        
        return True
    
    def m_lot_full(self):
        for spot in self.md_spots:
            if spot.state is None:
                return False
        
        return True

    def l_lot_full(self): 
        for spot in self.lg_spots:
            if spot.state is None:
                return False
        
        return True
    
    def evaluateVehicle(self, vehicle: Vehicle):
        if self.lot_full():
            return -1
        
        if vehicle.v_type == "motorcycle":
            if self.s_lot_full():
                return -1
            
            for spot in self.sm_spots:
                if spot.state is None:
                    spot.state = vehicle
                    return 1

        elif vehicle.v_type == "car":
            if self.m_lot_full():
                return -1
            
            elif self.s_lot_full():
                return -1
            
            for spot in self.md_spots:
                if spot.state is None:
                    spot.state = vehicle
                    return 1

            for spot in self.s_spots:
                if spot.state is None:
                    spot.state = vehicle
                    return 1
                
        elif vehicle.v_type == "truck":
            if self.l_lot_full():
                return -1
            
            elif self.m_lot_full():
                return -1
            
            elif self.s_lot_full():
                return -1
            
            for spot in self.lg_spots:
                if spot.state is None:
                    spot.state = vehicle
                    return 1
            
            for spot in self.md_spots:
                if spot.state is None:
                    spot.state = vehicle
                    return 1

            for spot in self.s_spots:
                if spot.state is None:
                    spot.state = vehicle
                    return 1
                

    def exitVehicle(self, vehicle: Vehicle):
        for lot in self.lots:
            for spot in lot:
                if spot.state is vehicle:
                    spot.state = None
                    return 1
        
        else:
            return -1


lot = ParkingLot()
coopy_car = Vehicle("Coopy", "car")
ruitao_car = Vehicle("Ruitao", "car")
jazzy_truck = Vehicle("Jazzy", "truck")
joe_motorcycle = Vehicle("Joe", "motorcycle")
lot.evaluateVehicle(ruitao_car)
lot.evaluateVehicle(coopy_car)
lot.evaluateVehicle(jazzy_truck)
lot.evaluateVehicle(joe_motorcycle)
lot.exitVehicle(coopy_car)
spots = lot.get_spots()
for lot in spots:
    for spot in lot:
        print(spot.printSpot())

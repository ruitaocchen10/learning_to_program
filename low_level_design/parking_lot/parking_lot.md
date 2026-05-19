# Requirements

1. Create a parking spot system that tracks parking spots, supports (motorcycles, cars, and trucks), allows vehicles to park and leave.
2. 100 parking spots: 20 small, 50 medium, 30 large
3. Motorcycle fits anywhere, car fits medium or large, trucks only large
4. System assigns optimal available slot
5. Reject vehicles if there are no spots for that specific vehicle, or if the lot is full
   Out of scope: UI representation, Automatic Tester

# Entities

Parking Lot (Parking Manager)
Parking Spots
Vehicles - Cars - Motorcycles - Trucks

# Class Design

Parking Lot: - Initializes 100 empty spots with the correct type distribution - Accepts vehicles if: - There is a spot available for the type of vehicle - Rejects vehicles if: - Lot is full - There are no spots available for that type of vehicle - Type of vehicle doesn't match - Assigns vehicles to Parking Spots

Parking Spot: - Empty or not - If full, type of vehicle - Spot type: large, medium, or small

Vehicle: - Car, Truck, Motorcycle

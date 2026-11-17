from datetime import datetime
from vehicle import Car , Bike 

class Ridesharing:
    def __init__(self , company_name) -> None:
        self.company_name = company_name
        self.rides = []
        self.drivers = []
        self.riders = []

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)


    def __str__(self):
        return f"Company : {self.company_name} with :  {len(self.riders)} riders and {len(self.drivers)} drivers."


class Ride:
    def __init__(self, rider ,start_location, end_location , vehicle) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.vehicle = vehicle


      #  self.vehicle = None
        self.driver = None
        self.rider = rider
        self.start_time = None
        self.end_time = None
        self.estimated_fare = self.calculate_fare(vehicle.vehicle_type)


    def set_driver(self, driver):
        self.driver = driver


    def start_ride(self):
        self.start_time = datetime.now()


    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare


    #Total fare calculation
    def calculate_fare(self , vehicle):
        print(vehicle)
        distance = 10  # Example distance in km
        fare_per_km = {
            'car': 10,  # Example fare per km for car
            'bike': 5,   # Example fare per km for bike
            'cng': 7   # Example fare per km for cng
        }
        return distance*fare_per_km.get(vehicle.lower(), 0)  # Default fare is 0 if vehicle type is not recognized

    

    def __repr__(self):
        return f"Ride details : Started {self.start_location} to {self.end_location}"    


class RideRequest:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location


class RideMatching:
    def __init__(self, drivers) -> None:
        self.available_drivers = drivers

    def find_driver(self, rider_request , vehicle_type):
        # Implement logic to find the nearest available driver based on rider's location
        if len(self.available_drivers) > 0:
            print("Looking for available driver...") 
            driver = self.available_drivers[0]  # For simplicity, just pick the first available driver
          #  ride = Ride(rider_request.rider.current_location, rider_request.end_location)

            if vehicle_type == 'car':
                vehicle = Car("ABC123", "car", 10)  # Example car object
            elif vehicle_type == 'bike':
                vehicle = Bike("XYZ789", "bike", 5)  # Example bike object

            ride = Ride(rider_request.rider,rider_request.rider.current_location, rider_request.end_location, vehicle)
            
            #ride.vehicle = vehicle

            driver.accept_ride(ride)
            return  ride   
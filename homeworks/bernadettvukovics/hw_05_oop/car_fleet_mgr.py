class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0  # Initial mileage
        self.fuel_level = 100  # Initial fuel level in percentage

    # Method to drive the car, reduces fuel and increases mileage
    def drive(self, km):
        # Check if there's enough fuel to drive the desired distance
        fuel_needed = km * 0.1
        if self.fuel_level >= fuel_needed:
            self.mileage += km
            self.fuel_level -= fuel_needed
            print(f"{self.brand} {self.model} drove {km} km.")
        else:
            # Calculate the maximum distance that can be driven with the current fuel level
            max_drivable_distance = self.fuel_level / 0.1
            self.mileage += max_drivable_distance
            self.fuel_level = 0
            print(f"{self.brand} {self.model} drove {max_drivable_distance} km, but ran out of fuel.")

    # Method to refuel the car
    def refuel(self, amount):
        if self.fuel_level + amount <= 100:
            self.fuel_level += amount
            print(f"{self.brand} {self.model} refueled by {amount}%. Current fuel level: {self.fuel_level}%.")
        else:
            self.fuel_level = 100
            print(f"{self.brand} {self.model} is now fully refueled.")

    # Display car details
    def get_car_info(self):
        return f"{self.brand} {self.model} ({self.year}) - Mileage: {self.mileage} km, Fuel: {self.fuel_level}%"


# Define the Fleet class to manage a collection of Car objects
class Fleet:
    def __init__(self):
        self.cars = []

    # Add a car to the fleet
    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.brand} {car.model} added to the fleet.")

    # Remove a car from the fleet
    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} {car.model} removed from the fleet.")
        else:
            print(f"{car.brand} {car.model} not found in the fleet.")

    # Get the total mileage of all cars in the fleet
    def get_total_mileage(self):
        total_mileage = sum(car.mileage for car in self.cars)
        return f"Total fleet mileage: {total_mileage} km"

    # Display the details of all cars in the fleet
    def display_fleet_info(self):
        if not self.cars:
            print("No cars in the fleet.")
        else:
            for car in self.cars:
                print(car.get_car_info())


# Create a fleet and some car objects
fleet = Fleet()

# Creating some car objects
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Ford", "Focus", 2019)
car3 = Car("BMW", "X5", 2021)

# Add cars to the fleet
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

# Drive some cars
car1.drive(50)
car2.drive(30)
car3.drive(100)

# Refuel some cars
car1.refuel(20)
car2.refuel(15)

# Display fleet info
fleet.display_fleet_info()

# Display total mileage of the fleet
print(fleet.get_total_mileage())
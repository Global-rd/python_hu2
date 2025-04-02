# Homework 05 - Object Oriented Programming
import logging

# The 4 steps of logging setup:

# 1. Create handlers - where the logs will go
file_handler = logging.FileHandler("car_fleet.log")
stream_handler = logging.StreamHandler()

# 2. Define the formatter - how the logs will look
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# 3. Assigning the formatter to each handler
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# 4. Creating logger and assign the handlers to it
logger = logging.getLogger("car_fleet_manager")
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


# Create a car class with specific attributes and methods
class Car:
    """
    A class representing a car with basic attributes like brand and morel and year.
    And with basic functionalities like driving and refueling.
    """

    brand: str
    model: str
    year: int
    mileage: float
    fuel_level: float

    # Initializing a new Car instance
    def __init__(self, car_brand: str, car_model: str, car_year: int):
        """
        Initialize a new Car instance.
        """
        self.brand = car_brand
        self.model = car_model
        self.year = car_year
        self.mileage = 0.0
        self.fuel_level = 100.0
        logger.info(f"Created new car: {self.brand}{self.model} ({self.year})")

    # Implement drive() method
    def drive(self, kilometers: float) -> float:
        """
        Simulating car driving for a given km distance
        """
        logger.info(
            f"Attempting to drive {kilometers} km with {self.brand}{self.model}"
        )

        # Calculate how far can the car go with our current fuel level
        max_possible_km = self.fuel_level / 0.1

        # Determine actual distance driven
        actual_km = min(kilometers, max_possible_km)

        # Updating the mileage and fuel level
        self.mileage += actual_km
        self.fuel_level -= actual_km * 0.1

        if actual_km < kilometers:
            logger.warning(
                f"Not enough fuel to drive {kilometers} km. We could only drive {actual_km} km."
            )
        else:
            logger.info(f"Successfully drove {actual_km} km.")

        logger.debug(
            f"Updated mileage: {self.mileage} km, fuel level: {self.fuel_level}%"
        )

        return actual_km

    # Implement refuel() method
    def refuel(self, percentage_points_to_add: float) -> float:
        """
        Refuel the car by a specified amount in percentage points
        """
        logger.info(
            f"Adding {percentage_points_to_add}% fuel to {self.brand}{self.model}"
        )

        # How much fuel can be added? It should not exceed 100%
        max_refill = 100 - self.fuel_level
        actual_refill = min(
            percentage_points_to_add, max_refill
        )  # we are working with percentages, not absolute units like "Litre" so the refuel will be adding percentages to the tank not actual litres. Otherwise I would introduce a tank_capacity attribute to the Car class

        # update fuel level
        self.fuel_level += actual_refill

        if actual_refill < percentage_points_to_add:
            logger.info(
                f"Could only add {actual_refill}% fuel (tank capacity reached)."
            )
        else:
            logger.info(f"Successfully added {actual_refill}% fuel.")

        logger.debug(f"Updated fuel level: {self.fuel_level}%")

        return actual_refill


# Implement a Fleet class with management functionalities


class Fleet:
    """
    A class representing a fleet
    """

    def __init__(self):
        self.cars = []  # initialize the fleet with empty list of cars
        logger.info("New fleet has been created")

    def add_car(self, car: Car) -> None:
        """
        Add a car to the fleet.
        """
        self.cars.append(car)  # add car object to the fleet
        logger.info("Added Car to the fleet")
        logger.debug(f"Fleet now has {len(self.cars)} cars")

    def remove_car(self, car: Car) -> bool:
        """
        Remove a car from the fleet.
        """
        if car in self.cars:
            self.cars.remove(car)
            logger.info(f"Removed Car from the fleet")
            logger.debug(f"Fleet now has {len(self.cars)} cars")
            return True
        logger.warning(f"Failed to remove car: Car not found in fleet")
        return False

    def total_mileage(self) -> float:
        """
        Calculate the total mileage of all the cars in the fleet.
        """
        total = 0.0
        for car in self.cars:
            total += car.mileage
        logger.debug(f"Calculated total fleet mileage: {total} km")
        return total


def print_fleet_status(fleet: Fleet) -> None:
    logger.debug("Printing fleet status")

    print(f"Total cars in fleet: {len(fleet.cars)}")
    print(f"Total fleet mileage: {fleet.total_mileage()} km")

    print("\nDetails of the cars in our fleet:")
    for i, car in enumerate(fleet.cars, 1):
        print(f"Car {i}: {car.brand} {car.model} ({car.year})")
        print(f"  Mileage: {car.mileage} km")
        print(f"  Fuel level: {car.fuel_level} %")


def main():
    logger.info("Starting car fleet management application")

    # create a fleet
    my_fleet = Fleet()

    # create cars
    cars = [
        Car("Toyota", "Auris", 2006),
        Car("Jeep", "Grand Cherokee", 1996),
        Car("Volkswagen", "Passat", 2001),
        Car("Toyota", "Auris", 2006),  # we will have two of the same in the fleet
    ]

    # Add the cars to the fleet
    logger.info("Adding cars to the fleet")
    for car in cars:
        my_fleet.add_car(car)

    print("Our Initial fleet:")
    print_fleet_status(my_fleet)

    # Let's drive the cars
    logger.info("Starting to drive")
    print("\nDriving the cars! Yay!")
    km_driven = cars[0].drive(100)
    print(f"We drove {km_driven} km in the {cars[0].brand} {cars[0].model}")

    km_driven = cars[1].drive(200)
    print(f"We drove {km_driven} km in the {cars[1].brand} {cars[1].model}")

    km_driven = cars[2].drive(300)
    print(f"We drove {km_driven} km in the {cars[2].brand} {cars[2].model}")

    km_driven = cars[3].drive(400)
    print(f"We drove {km_driven} km in the other {cars[3].brand} {cars[3].model}")

    print("\nFleet status after driving:")
    print_fleet_status(my_fleet)

    # Now let's tank the cars
    logger.info("Refueling cars")
    print(f"\nRefueling the {cars[2].brand} {cars[2].model}...")
    fuel_added = cars[2].refuel(30)
    print(f"Added {fuel_added}% fuel to the {cars[2].brand} {cars[2].model}")

    # Let's try to drive more than the fuel limit allows us to
    logger.info("Testing fuel limit scenario")
    print(f"\nTrying to drive 10000 km in the {cars[2].brand} {cars[2].model}...")
    km_driven = cars[2].drive(10000)
    print(f"Could only drive {km_driven} km due to fuel limitations")

    print("\nOur Fleet's status after the stuff that we did:")
    print_fleet_status(my_fleet)

    # Let's remove a car
    logger.info("Removing a car from the fleet")
    print(f"Removing one of the Toyota Auris cars")
    if my_fleet.remove_car(cars[0]):
        print("Successfully removed the car")
        print(
            "Note: the cars are not unique, in case there are multiple ones, we only removed one"
        )

    print("\nOur final fleet status")
    print_fleet_status(my_fleet)

    logger.info("Car fleet management application completed")


if __name__ == "__main__":
    main()

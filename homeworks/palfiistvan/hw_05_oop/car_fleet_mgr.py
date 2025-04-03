class InvalidAmountError(Exception):
    """
    Custom exception for invalid amount on (km) and (refuel).
    """
    pass

class Car:
    def __init__(self, brand:str, model:str, year:int):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100
    
    def drive(self, km):
        if km <= 0:
            raise InvalidAmountError("The value of km cannot be zero or negative!")
        fuel_usage = km * 0.1
        if fuel_usage <= self.fuel_level:
            self.mileage += km
            self.fuel_level -= fuel_usage
            print(f"{self.brand} {self.model} ({self.year}) {km} kmdriven. Odometer: {self.mileage}, fuel: {self.fuel_level:.2f}%")
        else:
            max_driveable_km = self.fuel_level / 0.1
            print(f"Not enough fuel for {km} The maximum you can drive: {max_driveable_km} km.")
            self.mileage += max_driveable_km
            self.fuel_level = 0
            print(f"{self.brand} {self.model} ({self.year}) only {max_driveable_km} km could go.")

    def refuel(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Refueling rate cannot be zero or negative!")
        new_fuel_level = self.fuel_level + amount
        if new_fuel_level > 100:
            self.fuel_level = 100
            print(f"{self.brand} {self.model} ({self.year}) full tank.")
        else:
            self.fuel_level = new_fuel_level
            print(f"{self.brand} {self.model} ({self.year}) {amount} was refueled with. Current fuel: {self.fuel_level}%.")
        
    def get_status(self):
        return f"{self.brand} {self.model} ({self.year}) - kilometers/hour: {self.mileage} km, fuel: {self.fuel_level}%"
        
class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.brand} {car.model} ({car.year}) added to the fleet.")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} {car.model} ({car.year}) removed from fleet.")
        else:
            print(f"{car.brand} {car.model} ({car.year}) not in fleet.")

    def total_mileage(self):
        total_km = sum(car.mileage for car in self.cars)
        print(f"Total fleet kilometers: {total_km} km")
        return total_km

    def display_fleet_status(self):
        if not self.cars:
            print("Fleet is empty.")
        for car in self.cars:
            print(car.get_status())

if __name__ == "__main__":
    # Make cars
    car1 = Car("Mitsubishi", "Galant", 1992)
    car2 = Car("Opel", "Astra", 2015)
    car3 = Car("Volkswagen", "Golf", 2015)

    # Make Fleet
    fleet = Fleet()

    # cars add fleet
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)

    # drive & fill
    car1.drive(55)
    car2.drive(350)
    car3.refuel(-12)

    # fleet sataus
    fleet.display_fleet_status()

    # summa kilometer
    fleet.total_mileage()

    # remove a car
    fleet.remove_car(car3)

    # new status
    fleet.display_fleet_status()
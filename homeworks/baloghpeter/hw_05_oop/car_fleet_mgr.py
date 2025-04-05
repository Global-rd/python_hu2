class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, distance):
        max_distance = self.fuel_level * 10 
        if distance > max_distance:
            distance = max_distance
        self.mileage += distance
        self.fuel_level -= distance * 0.1
        self.fuel_level = max(self.fuel_level, 0)
        print(f"{self.brand} {self.model} drove {distance} km. Mileage: {self.mileage} km, Fuel level: {self.fuel_level:.1f}%")

    def refuel(self, amount):
        self.fuel_level += amount
        if self.fuel_level > 100:
            self.fuel_level = 100
        print(f"{self.brand} {self.model} refueled. Fuel level: {self.fuel_level:.1f}%")

class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.brand} {car.model} added to the fleet.")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} {car.model} removed from the fleet.")
        else:
            print("Car not found in fleet.")

    def total_mileage(self):
        return sum(car.mileage for car in self.cars)

    def display_fleet(self):
        print("Fleet status:")
        for car in self.cars:
            print(f"{car.brand} {car.model} ({car.year}) - Mileage: {car.mileage} km, Fuel: {car.fuel_level:.1f}%")
        print(f"Total fleet mileage: {self.total_mileage()} km")

car1 = Car("Volksawagen", "Passat", 2020)
car2 = Car("Audi", "A4", 2018)
car3 = Car("Mercedes-Benz", "S320", 2022)

fleet = Fleet()
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

car1.drive(150)
car2.drive(50)
car3.refuel(20)
car1.refuel(30)

fleet.display_fleet()

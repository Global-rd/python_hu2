class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, kilometers):
        if kilometers < 0:
            raise ValueError("A megtett kilométerek nem lehetnek negatívak!")
        fuel_needed = kilometers * 0.1
        if self.fuel_level >= fuel_needed:
            self.mileage += kilometers
            self.fuel_level -= fuel_needed
            return True
        else:
            return False

    def refuel(self, amount):
        if amount > 0:
            self.fuel_level = min(self.fuel_level + amount, 100)
            return True
        else:
            return False

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) has {self.mileage} km in it and the fuel status is: {self.fuel_level}%"

class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, car):
        self.cars.remove(car)

    def total_mileage(self):
        return sum(car.mileage for car in self.cars)

    def check_car_in_fleet(self, car):
        if car not in self.cars:
            raise ValueError(f"{car.brand} {car.model} is not in the fleet")

    def __str__(self):
        fleet_info = "Fleet Information:\n"
        for car in self.cars:
            fleet_info += str(car) + "\n"
        fleet_info += f"Total Mileage: {self.total_mileage()}"
        return fleet_info

car1 = Car("Opel", "Astra", 2004)
car2 = Car("Peugeot", "206", 2005)
car3 = Car("Mitsubishi", "Outlander", 2024)

fleet = Fleet()
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

try:
    fleet.check_car_in_fleet(car1)  
    car1.drive(90)
    
    fleet.check_car_in_fleet(car2)
    car2.drive(74)

    fleet.check_car_in_fleet(car3)
    car3.drive(54)

    car1.refuel(22)
    car2.refuel(32)

    print(fleet)  
except ValueError as error:
    print(f"{error}")

print(fleet)
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, km):
        needed_fuel = km * 0.1
        if needed_fuel > self.fuel_level:
            km = self.fuel_level / 0.1
            self.fuel_level = 0
            self.mileage += km
        else:
            self.fuel_level -= needed_fuel
            self.mileage += km

    def refuel(self, amount):
        self.fuel_level += amount
        if self.fuel_level > 100:
            self.fuel_level = 100

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} - {self.mileage:.1f} km, Fuel: {self.fuel_level:.1f}%"

class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)

    def total_mileage(self):
        total = 0
        for car in self.cars:
            total += car.mileage
        return total

if __name__ == "__main__":
    car1 = Car("Suzuki", "Samurai", 1985)
    car2 = Car("Nissan", "Juke", 2010)
    car3 = Car("Ford", "Ranger", 2018)
    car4 = Car("Suzuki", "S-Cross", 2022)

    fleet = Fleet()

    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)
    fleet.add_car(car4)

    car1.drive(15)
    car2.drive(100)
    car3.refuel(30)
    car3.drive(50)
    car4.drive(0)

    print(car1)
    print(car2)
    print(car3)
    print(car4)

    print("The total mileage of the fleet:", fleet.total_mileage(), "km")
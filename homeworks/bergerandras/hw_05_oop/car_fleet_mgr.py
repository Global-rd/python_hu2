class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, distance):

        fuel_used = distance * 0.1
        if distance < 0:
            print("Distance cannot be negative")
        elif self.fuel_level >= fuel_used:
            self.mileage += distance
            self.fuel_level -= fuel_used
            print(f"{self.brand} {self.model} drove {distance} KM, fuel is on {self.fuel_level}")
        else:
            self.mileage += self.fuel_level / 0.1
            self.fuel_level = 0
            print(f"{self.brand} {self.model} ran out of fuel and drove {self.mileage} KM")

    def refuel(self, amount):
        if amount + self.fuel_level <= 100 and amount >= 0:
            self.fuel_level += amount
            print(f"{self.brand} {self.model} refualed by {amount}%")
        elif amount < 0:
            print("Fuel cannot be negative")
        else:
            self.fuel_level = 100
            print(f"{self.brand} {self.model} is on max fuel ({self.fuel_level}%)")

class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.brand} {car.model} added to the fleet")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} {car.model} removed from the fleet")
        else:
            print(f"{car.brand} {car.model} not in the fleet")
            
    def total_mileage(self):
        return f"The total mileage is: {sum(car.mileage for car in self.cars)}"

car1 = Car("Nissan", "Navara", 2016)
car2 = Car("Infiniti", "QX70", 2014)
car3 = Car("Hyundai", "Ioniq 5", 2021)

fleet = Fleet()

fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

fleet.remove_car(car3)

car1.drive(50)
car2.drive(260)

car1.refuel(4)
car2.refuel(150)

print(fleet.total_mileage())
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, kilometers):
        fuel_consumption = kilometers * 0.1
        if fuel_consumption <= self.fuel_level:
            self.mileage += kilometers
            self.fuel_level -= fuel_consumption
            print(f"{self.brand} {self.model} {kilometers} km-t vezetett.")
        else:
            max_drive = int(self.fuel_level / 0.1)
            self.mileage += max_drive
            self.fuel_level = 0
            print(f"{self.brand} {self.model} csak {max_drive} km-t tudott menni, mert kifogyott az üzemanyag.")

    def refuel(self, fuel):
        self.fuel_level = min(100, self.fuel_level + fuel)
        print(f"{self.brand} {self.model} {fuel} liter üzemanyagot tankolt.")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}), km: {self.mileage}, üzemanyag: {self.fuel_level:.2f}%"

class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.brand} {car.model} hozzáadva a flottához.")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} {car.model} eltávolítva a flottából.")
        else:
            print(f"{car.brand} {car.model} nincs a flottában.")

    def total_mileage(self):
        total = sum(car.mileage for car in self.cars)
        return total

# Példa használat
fleet = Fleet()

car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2019)
car3 = Car("Ford", "Mustang", 2021)

fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

car1.drive(500)
car2.drive(200)
car3.drive(1000)

car1.refuel(30)
car2.refuel(10)

print("\nAutók állapota:")
for car in fleet.cars:
    print(car)

print(f"\nFlotta összes futott kilométere: {fleet.total_mileage()} km")

fleet.remove_car(car2)

print("\nAutók állapota eltávolítás után:")
for car in fleet.cars:
    print(car)

print(f"\nFlotta összes futott kilométere eltávolítás után: {fleet.total_mileage()} km")
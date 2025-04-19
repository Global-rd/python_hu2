class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100.0  # %

    def drive(self, distance):
        required_fuel = distance * 0.1
        if self.fuel_level >= required_fuel:
            self.mileage += distance
            self.fuel_level -= required_fuel
            print(f"{self.brand} {self.model} megtett {distance} km-t.")
        else:
            max_distance = self.fuel_level / 0.1
            self.mileage += max_distance
            self.fuel_level = 0
            print(f"{self.brand} {self.model} csak {max_distance:.1f} km-t tudott megtenni, mert kifogyott az üzemanyag.")

    def refuel(self, amount):
        if amount < 0:
            print("Hiba: az érték negatív!")
            return
        self.fuel_level += amount
        if self.fuel_level > 100:
            self.fuel_level = 100
        print(f"{self.brand} {self.model} tankolva lett. Jelenlegi üzemanyagszint: {self.fuel_level:.1f}%")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - {self.mileage} km, {self.fuel_level:.1f}% üzemanyag"


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
            print("Nincs ilyen autó a flottában.")

    def total_mileage(self):
        return sum(car.mileage for car in self.cars)

    def show_fleet(self):
        print("\nFlotta állapota:")
        for car in self.cars:
            print(car)
        print(f"Összesített kilométeróra állás: {self.total_mileage()} km")


# Példányosítás, műveletek
car1 = Car("Porsche", "911 GT3 RS", 2023)
car2 = Car("Ford", "Mustang GT", 2018)
car3 = Car("Audi", "RS6", 2023)

fleet = Fleet()
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

car1.drive(100)
car2.drive(300)
car3.drive(700)

car1.refuel(20)
car2.refuel(50)
car3.refuel(30)

fleet.show_fleet()
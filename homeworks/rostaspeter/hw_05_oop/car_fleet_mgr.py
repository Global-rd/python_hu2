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
            print(f"{self.brand} {self.model}: Nincs elég üzemanyag {distance} km megtételéhez!")
            distance = max_distance
        self.mileage += distance
        self.fuel_level -= distance * 0.1
        print(f"{self.brand} {self.model} megtett {distance} km-t. Kilométeróra állás: {self.mileage} km, üzemanyag: {self.fuel_level:.1f}%")

    def refuel(self, amount):
        if self.fuel_level + amount > 100:
            self.fuel_level = 100
        else:
            self.fuel_level += amount
        print(f"{self.brand} {self.model} feltankolva. Az üzemanyag: {self.fuel_level}%")

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} - {self.mileage} km, {self.fuel_level:.1f}% üzemanyag"

class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"Autó hozzáadva! [{car}]")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Autó eltávolítva!  [{car}]")
        else:
            print("Autó nem található.")

    def total_mileage(self):
        return sum(car.mileage for car in self.cars)


if __name__ == "__main__":
    car1 = Car("Ford", "Mustang", 2020)
    car2 = Car("BMW", "M5", 2018)
    car3 = Car("BMW", "I4", 2024)
    car4 = Car("Lamborgini", "Urus", 2019)
    car5 = Car("Porsche", "911", 2024)

    fleet = Fleet()

    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)
    fleet.add_car(car4)
    fleet.add_car(car5)

    car1.drive(75)
    car2.drive(83)
    car3.refuel(2)
    car3.drive(23)
    car4.drive(42)
    car5.refuel(20)
    car5.drive(50)

    print("\nFlotta:")
    print(fleet)
    print(f"Összes kilométer: {fleet.total_mileage()}")

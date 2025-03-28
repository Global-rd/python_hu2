#Hibaüzenetek

class InvalidMileError(Exception): #Mile exception for invalid amount of mile.
    pass

class InvalidFuelError(Exception): #Fuel quantity exception for invalid amount of fuel.
    pass

"""
Készíts egy Car osztályt, amely rendelkezik a következő tulajdonságokkal:
    ● Márka (brand)
    ● Modell (model)
    ● Gyártási év (year)
    ● Kilométeróra állása (mileage), induló értéke 0.
    ● Üzemanyag-szint (fuel_level), induló értéke 100 (százalékban).

Az osztály tartalmazza a következő metódusokat:
    ● Egy konstruktor, amely beállítja a fenti attribútumokat.
    ● Egy drive() metódus, amely adott számú kilométerrel növeli a
        kilométeróra állását, és csökkenti az üzemanyag-szintet (tételezzük fel,
        hogy 0.1% üzemanyag fogy megtett kilométerenként). A drive()
        metódus csak annyit km-et engedjen vezetni, amennyire elegendő
        üzemanyag van.
    ● Egy refuel() metódus, amely feltölti az üzemanyag-szintet egy adott
        mennyiséggel. Figyelj a limitekre.
"""

class Car:
    def __init__(self, brand: str, model: str, year: int, mileage = 0, fuel_level: float = 100.0):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level
    
    def __str__(self):
        return (f'{self.brand} {self.model} ({self.year})')

    def drive(self, mile:float):
        if self.fuel_level >= 0.1 * mile:
            self.mileage += mile
            self.fuel_level -= mile * 0.1
        else:
            raise InvalidMileError(f"{self}: Nincs ennyi km-re üzemanyag az autóban.")

    def refuel(self, refuel_quantity: float):
        if refuel_quantity <= 0:
            raise InvalidFuelError('Nem lehet negatív szám.')
        elif self.fuel_level + refuel_quantity <= 100:
            self.fuel_level += refuel_quantity
            print(f'{self}: Sikeresen tankoltál {refuel_quantity}% üzemanyagot. A tankban {self.fuel_level}% üzemanyag van.')

        else:
            refuel_quantity = 100 - self.fuel_level
            self.fuel_level = 100
            print(f'{self}: Csak {refuel_quantity}% üzemanyagot tudtál tankolni. A tank {self.fuel_level}%-on van.')

"""Készíts egy Fleet osztályt, amely kezeli a Car objektumokat:
    ● Az osztály rendelkezzen egy listával, amelyben az autók találhatóak.
    ● Tartalmazzon metódusokat Car objektumok hozzáadására és
        eltávolítására a flottába/flottából.
    ● Tartalmazzon egy metódust, amely összesíti a flotta összes autójának
        összes kilométerét.
    ● Hozz létre néhány Car objektumot, add hozzá őket a flottához, hajts
    végre néhány műveletet (vezetés, tankolás), jelenítsd meg az autók
    állapotát és a flotta összesítő adatait."""

class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car: Car):
        self.cars.append(car)
        print(f'Sikeresen hozzáadtad a {car} autót a flottához.')

    def remove_car(self, car: Car):
        if car in self.cars:
            self.cars.remove(car)
            print(f'Törölve a flottából: {car}')
        else:
            print(f'A {car} autó nem található a flottában.')
    
    def total_mileage(self):
        return sum(car.mileage for car in self.cars)

    def show_fleet(self):
        print("Flotta állapota:")
        for car in self.cars:
            print(f" ● {car} - mileage: {car.mileage} - fuel level: {car.fuel_level}")
        print(f"Összesített kilométeróra állás: {self.total_mileage()} km")
        
"""● Hozz létre néhány Car objektumot, add hozzá őket a flottához, hajts
    végre néhány műveletet (vezetés, tankolás), jelenítsd meg az autók
    állapotát és a flotta összesítő adatait."""

car1 = Car("Toyota", "Yaris", 2015, 1200.0, 12)
car2 = Car("Ford", "Focus", 2023, fuel_level = 98)
car3 = Car("Suzuki", "Swift", 2022, 125, 50)
car4 = Car("BYD", "Xiong", 2025, fuel_level = 100)

fleet = Fleet()
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)
fleet.add_car(car4)

car1.drive(100)
car2.drive(50)
car3.drive(14)
car4.drive(105)

car1.refuel(50)
car2.refuel(98)
car3.refuel(15)

fleet.show_fleet()

fleet.remove_car(car1)

fleet.show_fleet()

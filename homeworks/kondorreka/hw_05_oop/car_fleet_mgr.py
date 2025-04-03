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
        if mile < 0:
            raise InvalidMileError(f"A megtett kilométer nem lehet negatív szám.")
        elif self.fuel_level >= 0.1 * mile:
            self.mileage += mile
            self.fuel_level -= mile * 0.1
            print(f"{self}: {mile} km-t vezettél.\n"
                f"    A km óra jelenlegi állása: {self.mileage}. Az üzemanyag szint: {self.fuel_level}%\n")
        else:
            raise InvalidMileError(f"Nincs ennyi km-re üzemanyag az autóban.\n"
                                       f"   Az üzemanyag szinted: {self.fuel_level}%, ami csak {self.fuel_level / 0.1} km-re elegendő.\n")

    def refuel(self, refuel_quantity: float):
        if refuel_quantity <= 0:
            raise InvalidFuelError(f'A tankolás értéke nem lehet negatív vagy 0.\n'
                                    f'   Jelenlegi üzemanyagszint: {self.fuel_level}%\n')
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
print("-----------------------------------------")

fleet = Fleet()
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)
fleet.add_car(car4)
print("-----------------------------------------")

for car, mile in [
    (car1, -200),
    (car1, 200),
    (car1, 100),
    (car2, 50),
    (car3, 14),
    (car4, 105)
]:
    try:
        car.drive(mile)
    except InvalidMileError as ime:
        print(f"{car}: Hibás üzemanyagszint paraméter: {ime}")

print("-----------------------------------------")

for car, refuel_quantity in [
    (car1, -50),
    (car2, 0),
    (car1, 50),
    (car2, 98),
    (car3, 15),
    (car4, 30)
]:
    try:
        car.refuel(refuel_quantity)
    except InvalidFuelError as ife:
        print(f"{car}: Hibás üzemanyagszint paraméter: {ife}")
    
print("-----------------------------------------")

fleet.show_fleet()
print("-----------------------------------------")

fleet.remove_car(car1)
print("-----------------------------------------")

fleet.show_fleet()

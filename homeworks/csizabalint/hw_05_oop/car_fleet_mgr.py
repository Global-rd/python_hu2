"""
Hozz létre egy új mappát a neveddel ellátott mappán belül “hw_05_oop” néven. A következő feladatokhoz tartozó .py file-okat ide mentsd el.
Feladat 1:
Hozz létre egy car_fleet_mgr.py nevű file-t, és kódold le a következő feladat megoldását:

Készíts egy Car osztályt, amely rendelkezik a következő tulajdonságokkal:
● Márka (brand)
● Modell (model)
● Gyártási év (year)
● Kilométeróra állása (mileage), induló értéke 0.
● Üzemanyag-szint (fuel_level), induló értéke 100 (százalékban).

Az osztály tartalmazza a következő metódusokat:
● Egy konstruktor, amely beállítja a fenti attribútumokat.
● Egy drive() metódus, amely adott számú kilométerrel növeli a kilométeróra állását, és csökkenti az üzemanyag-szintet (tételezzük fel, hogy 0.1% üzemanyag fogy megtett kilométerenként). A drive() metódus csak annyit km-et engedjen vezetni, amennyire elegendő üzemanyag van.
● Egy refuel() metódus, amely feltölti az üzemanyag-szintet egy adott mennyiséggel. Figyelj a limitekre.

Készíts egy Fleet osztályt, amely kezeli a Car objektumokat:
● Az osztály rendelkezzen egy listával, amelyben az autók találhatóak.
● Tartalmazzon metódusokat Car objektumok hozzáadására és eltávolítására a flottába/flottából.
● Tartalmazzon egy metódust, amely összesíti a flotta összes autójának összes kilométerét.
● Hozz létre néhány Car objektumot, add hozzá őket a flottához, hajts végre néhány műveletet (vezetés, tankolás), jelenítsd meg az autók állapotát és a flotta összesítő adatait.
"""

class InvalidAmountError(Exception):
    """
    Custom exception for invalid input values like negative km or fuel amounts.
    """
    pass

class Car:
    def __init__(self, brand: str, model: str, year: int):
        """
        Initialize the Car object with brand, model, year, mileage and fuel level.
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0  # Initial mileage is set to 0
        self.fuel_level = 100  # Initial fuel level is 100%

    def drive(self, km: int):
        """
        Simulate driving the car for a given number of kilometers.
        If there's enough fuel, mileage increases and fuel decreases.
        """
        if km <= 0:
            raise InvalidAmountError("Kilometers must be positive values!")
        
        fuel_usage = km * 0.1  # Each km consumes 0.1% of fuel
        if fuel_usage <= self.fuel_level:
            self.mileage += km
            self.fuel_level -= fuel_usage
            print(f"{self.brand} {self.model} ({self.year}) drove {km} km. Current mileage: {self.mileage} km, Fuel: {self.fuel_level:.2f}%")
        else:
            max_possible_km = self.fuel_level / 0.1  # Max km that can be driven with the available fuel
            self.mileage += max_possible_km
            self.fuel_level = 0  # Fuel becomes 0 after driving the max possible distance
            print(f"Not enough fuel for {km} km. Maximum possible distance with current fuel: {max_possible_km} km.")

    def refuel(self, amount: int):
        """
        Refuel the car. The fuel level is capped at 100%.
        """
        if amount <= 0:
            raise InvalidAmountError("Refuel amount must be positive!")
        
        new_fuel_level = self.fuel_level + amount
        if new_fuel_level > 100:
            self.fuel_level = 100
            print(f"{self.brand} {self.model} ({self.year}) refueled to full tank.")
        else:
            self.fuel_level = new_fuel_level
            print(f"{self.brand} {self.model} ({self.year}) refueled by {amount}%. Current fuel level: {self.fuel_level}%.")
        
    def get_status(self):
        """
        Return the current status of the car (mileage and fuel level).
        """
        return f"{self.brand} {self.model} ({self.year}) - Mileage: {self.mileage} km, Fuel: {self.fuel_level}%"
        
class Fleet:
    def __init__(self):
        """
        Initialize the Fleet object with an empty list of cars.
        """
        self.cars = []

    def add_car(self, car: Car):
        """
        Add a car to the fleet.
        """
        self.cars.append(car)
        print(f"{car.brand} {car.model} ({car.year}) has been added to the fleet.")

    def remove_car(self, car: Car):
        """
        Remove a car from the fleet.
        """
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} {car.model} ({car.year}) has been removed from the fleet.")
        else:
            print(f"{car.brand} {car.model} ({car.year}) is not in the fleet.")

    def total_mileage(self):
        """
        Return the total mileage of all cars in the fleet.
        """
        total_km = sum(car.mileage for car in self.cars)
        print(f"Total fleet mileage: {total_km} km")
        return total_km

    def display_fleet_status(self):
        """
        Display the status of all cars in the fleet.
        """
        if not self.cars:
            print("The fleet is empty.")
        else:
            for car in self.cars:
                print(car.get_status())

if __name__ == "__main__":
    # Create some cars with different brands, models, and years
    car1 = Car("Toyota", "Corolla", 2010)
    car2 = Car("Ford", "Focus", 2018)
    car3 = Car("BMW", "320i", 2020)

    # Create a fleet
    fleet = Fleet()

    # Add cars to the fleet
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)

    # Drive and refuel the cars
    car1.drive(55)
    car2.drive(350)
    try:
        car3.refuel(-12)  # Invalid refuel amount (negative)
    except InvalidAmountError as e:
        print(f"Error: {e}")

    # Display fleet status
    fleet.display_fleet_status()

    # Show total mileage
    fleet.total_mileage()

    # Remove a car from the fleet
    fleet.remove_car(car3)

    # Display updated fleet status
    fleet.display_fleet_status()

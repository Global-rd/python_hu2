# Car osztály 
class Car:
    def __init__(self, brand, model, year):
        # Alapértelmezett attribútumok beállítása
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0  # Kezdeti kilométeróra állás
        self.fuel_level = 100  # Kezdeti üzemanyagszint (százalékban)

    def drive(self, distance):
        # Mennyi kilométert tud megtenni a jelenlegi üzemanyaggal
        max_distance = self.fuel_level / 0.1  # 0.1% üzemanyag/km
        actual_distance = min(distance, max_distance)  # Ennyit tud ténylegesen megtenni
        self.mileage += actual_distance  # Növeljük a megtett kilométereket
        self.fuel_level -= actual_distance * 0.1  # Csökkentjük az üzemanyagot
        print(f"{self.brand} {self.model} {actual_distance} km-t ment. Aktuális óraállás: {self.mileage} km, üzemanyagszint: {self.fuel_level:.2f}%")

    def refuel(self, amount):
        #  A hozzáadott mennyiség nem negatív-e?
        if amount < 0:
            print("Negatív mennyiséggel nem lehet tankolni.")
            return
        # Üzemanyagszint frissítése max 100%-ig
        self.fuel_level = min(100.0, self.fuel_level + amount)
        print(f"{self.brand} {self.model} tankolva lett. Jelenlegi üzemanyagszint: {self.fuel_level:.2f}%")

    def __str__(self):
        
        return f"{self.year} {self.brand} {self.model} - Óraállás: {self.mileage} km, Üzemanyag: {self.fuel_level:.2f}%"


# Autók listájának kezelése
class Fleet:
    def __init__(self):
        self.cars = []  # A autókat tartalmazó lista

    def add_car(self, car):
        self.cars.append(car)
        print(f"Autó hozzáadva: {car}")

    def remove_car(self, car):
        # Autó eltávolítása
        if car in self.cars:
            self.cars.remove(car)
            print(f"Autó eltávolítva: {car}")
        else:
            print("Az autó nem található a flottában.")

    def total_mileage(self):
        # Összes megtett kilométer
        return sum(car.mileage for car in self.cars)

    def show_fleet_status(self):
        
        for car in self.cars:
            print(car)
        print(f"A teljes megtett táv: {self.total_mileage()} km")



if __name__ == "__main__":
  
    car1 = Car("Toyota", "Corolla", 2015)
    car2 = Car("Ford", "Focus", 2018)
    car3 = Car("Tesla", "Model 3", 2020)

    # Autók hozzáadása
    fleet = Fleet()
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)

    
    car1.drive(200)       # Toyota
    car2.drive(300)       # Ford 
    car2.refuel(10)       # Ford tankolás
    car3.drive(950)       # Tesla 
    car3.refuel(30)       # Tesla 

    # Állapot kiírás
    fleet.show_fleet_status()

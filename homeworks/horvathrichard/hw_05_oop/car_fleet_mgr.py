
#a flotta autóinak "gyártója"
class Car:

    #a drive metódus által levezetett kilométerek hozzáadása minden kocsi esetében(!)
    sum_mileage = []
    
    #konstruktor az attribútumok beállításaira
    def __init__(self, brand:str, model:str, year:int, mileage=float(0), fuel_level=float(100)):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level

    #adott számú kilométerrel növeli a kilométeróra állását, és csökkenti az üzemanyag-szintet(százalékban) -> 0.1/km
    def drive (self, mileage):
        self.mileage += mileage
        consume = float(mileage * 0.1)
        if self.fuel_level > 0:
            self.fuel_level -= consume
            return self.fuel_level
        print(f"{mileage} km was driven by {self.model}.\n---Odometer reading: {self.mileage}---\nThe car consumed {consume}l fuel.\n---Fuel level: {self.fuel_level}%---")
        if self.fuel_level < 50:
            print(f"Your fuel level is under it's half!")
        elif self.fuel_level <25:
            print(f"--------Warning!--------\nYour fuel level is on low: {self.fuel_level}!")
    

    #feltölti az üzemanyag-szintet egy adott mennyiséggel
    def refuel (self, fuel_load):
        if self.fuel_level < 100 and self.fuel_level + fuel_load < 100:
            self.fuel_level += fuel_load
            print(f"{self.model} was loaded with {fuel_load}L of fuel successfully!\n---It's fuel level is on {self.fuel_level}%---")


#a flotta
class Fleet:

    #konstruktor az attribútumok beállításaira (mint például a könyvtár --> Lesson10,composition.py)
    def __init__ (self, name:str):
        self.name = name
        self.cars = []

    #kocsi hozzáadása a flottához
    def add_car (self, car:Car):
        self.cars.append(car)

    #kocsi törlése a flottából
    def remove_car (self, model:str):
        for car in self.cars:
            if car.model == model:
                self.cars.remove(car)
                return
        print(f"Model not found: {model}")

    #az egész flotta megtett kilométere összesítve
    def fleet_mileage (self,):
        pass




#a flotta autóinak "gyártója"
class Car:

    #a drive metódus által levezetett kilométerek hozzáadása minden kocsi esetében(!)
    sum_mileage = 0
    
    #konstruktor az attribútumok beállításaira
    def __init__(self, brand:str, model:str, year:int, mileage=float(0.00), fuel_level=float(100.00)):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level

    #a létrehozott autó felhasználóbarát nevesítése
    def __str__(self):
        return(f"{self.brand} {self.model}, {self.year}")

    #adott számú kilométerrel növeli a kilométeróra állását, és csökkenti az üzemanyag-szintet(százalékban) -> 0.1/km
    def drive (self, mileage=float):
        consume = float(mileage * 0.1)
        if self.fuel_level - consume > 0:
            Car.sum_mileage += mileage
            self.mileage += mileage
            self.fuel_level -= consume
            print(f"{mileage} km was driven by the {self.model}.\n---Odometer reading: {self.mileage}---\nThe car consumed {consume:.2f}l fuel.\n---Fuel level: {self.fuel_level:.2f}%---")
            if self.fuel_level <25:
                print(f"--------Warning!--------\nYour fuel level is on low: {self.fuel_level:.2f}!")
            elif self.fuel_level < 50:
                print(f"Your fuel level is under it's half!")
        else:
            print(f"You can not travel {mileage}km with {self.fuel_level:.2f}L fuel!\nTime to refuel!")
        
    

    #feltölti az üzemanyag-szintet egy adott mennyiséggel
    def refuel (self, fuel_load):
        if self.fuel_level + fuel_load < 100:
            self.fuel_level += fuel_load
            print(f"{self.model} was loaded with {fuel_load}L of fuel successfully!\n---It's fuel level is on {self.fuel_level}%---")
        else:
            print(f"You can not overload your fuel tank!")

    #az egész flotta által megtett kilométerek kiíratása
    @classmethod
    def get_sum_mileage(cls):
        return cls.sum_mileage

"""
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
"""
car1 = Car("Porsche","GT",1996,0)
print(car1)
print(car1.mileage)
print(car1.fuel_level)
print("-----")
car1.drive(33.8)
print("-----")
print(car1.fuel_level)
car1.drive(500)
car1.drive(400)
car1.drive(400)
car1.refuel(99)
print(Car.get_sum_mileage())
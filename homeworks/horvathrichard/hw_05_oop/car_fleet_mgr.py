
#a flotta autóinak "gyártója"
class Car:
    
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


#a flotta
class Fleet:

    #összes futott km
    sum_mileage = 0

    #konstruktor az attribútumok beállításaira (mint például a könyvtár --> Lesson10,composition.py)
    def __init__ (self, name:str):
        self.name = name
        self.cars = []

    def list_cars(self):
        print(f"Aviable cars in {self.name}:")
        for car in self.cars:
            print(car)

    #kocsi hozzáadása a flottához
    def add_car (self, car:Car):
        self.cars.append(car)
        print(f"{car} car model added to the fleet successfully.")

    #kocsi törlése a flottából
    def remove_car (self, model:str):
        for car in self.cars:
            if car.model == model:
                self.cars.remove(car)
                print(f"{car} car model was deleted from the fleet successfully.")
            else:
                print(f"Model not found: {model}")

    #az összes autó kilométereit összegzi
    def update_fleet_mileage(self):
        total_mileage = 0
        for car in self.cars:
            total_mileage += car.mileage
        Fleet.sum_mileage = total_mileage
        print(f"Total mileage of the fleet: {Fleet.sum_mileage} km.")

        

car1 = Car("Porsche","GT",1996,)
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
print("-------------------------------------")
flotta1 = Fleet("Ételfutár Profi Flotta ÉPF")
flotta1.add_car(car1)
print(flotta1.name)
flotta1.list_cars()
flotta1.update_fleet_mileage()

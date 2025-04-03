
class RangeError(Exception): 
    pass


class Car:
    def __init__(self, brand:str, model:str, year:int):
        self.brand=brand
        self.model=model
        self.year=year
        self.mileage:int=0
        self.fuel_level:float=100.0
        

    def __str__(self):
        return (f"{self.brand} {self.model} ({self.year})")

        

    def drive(self, mile:int):
        range==int(self.fuel_level)*10
        
        if mile > range:   
            raise RangeError(f"you can only go {range} km with your current fuel level")
        else: 
            self.mileage += mile
            self.fuel_level -=mile*0.1
            print(f"{self}: {mile} km-was covered.\n")
       
    def refuel(self, fuel):
        if fuel + self.fuel_level <= 100 and fuel >= 0:
            self.fuel_level += fuel
            print(f"{self.brand} {self.model} refueled by {fuel}%")
        elif fuel < 0:
            print("Fuel cannot be negative")
        else:
            self.fuel_level = 100
            print(f"{self.brand} {self.model} is on max fuel ({self.fuel_level}%)")


class Fleet:
    def __init__(self):
        self.cars=[]


    def add_car(self, car):
        self.cars.append(car)
        print(f"A {car} car was added to the fleet")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} {car.model} removed from the fleet")
        else:
            print(f"{car.brand} {car.model} not in the fleet")


    def total_mileage(self):
        return sum(car.mileage for car in self.cars)

    def fleet_info(self):
        print("Fleet details:")
        for car in self.cars:
            print(f" {car} - mileage: {car.mileage} - fuel level: {car.fuel_level}")
            print(f"Total mileage of the fleet: {self.total_mileage()} km") 

car1 = Car("Honda", "Civic", 2011)
car2 = Car("Suzuki", "Vitara", 2019)
car3 = Car("Hyundai", "Ioniq", 2022)

fleet = Fleet()

fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

fleet.remove_car(car1)

car1.drive(30)
car2.drive(200)

car1.refuel(9)
car2.refuel(120)

print(fleet.total_mileage())

            
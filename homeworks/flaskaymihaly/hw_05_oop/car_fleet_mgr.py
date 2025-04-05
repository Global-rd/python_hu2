

class ValueError(Exception): 
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
        if mile <= 0:
            raise ValueError("mile must be positive values!")
        
         
        
        fuel_usage = mile * 0.1  
        if fuel_usage <= self.fuel_level:
            self.mileage += mile
            self.fuel_level -= fuel_usage
            print(f"{self.brand} {self.model} ({self.year}) drove {mile} km-s. Current mileage: {self.mileage} km, Fuel: {self.fuel_level:.2f}%")
        else:
            limit=int(self.fuel_level)*10  
            self.mileage +=limit
            self.fuel_level = 0  
            print(f"Not enough fuel for {mile} miles. Maximum possible distance with current fuel: {limit} km-s.")



       
    def refuel(self, fuel):
        if fuel < 0:
            raise ValueError("Fuel cannot be negative")
        elif self.fuel_level + fuel > 100:
            self.fuel_level = 100
            print(f"{self.brand} {self.model} refueled to full (100%)")
        else:
            self.fuel_level += fuel
            print(f"{self.brand} {self.model} refueled by {fuel}%")



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

            
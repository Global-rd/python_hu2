

class Car:

    sum_mileage = []
    
    def __iniit__(self, brand:str, model:str, year:int, mileage:float, fuel_level:float)_
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level


    def drive (self, mileage, fuel_level):
        pass

    def refuel (self, fuel_level):
        pass



class Fleet:

    def __init__ (self, name:str):
        self.name = name
        self.cars = []

    def add_car (self, car:Car):
        self.cars.append(car)

    def remove_car (self, model:str):
        for car in self.cars:
            if car.model == model:
                self.cars.remove(car)
                return
        print(f"Model not found: {model}")

    def fleet_mileage (self,):
        pass



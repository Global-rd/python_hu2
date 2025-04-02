class Car:
    def __init__(self,brand : str , model : str , creation_date : int):
        self.brand = brand
        self.model = model
        self.creation_date = creation_date
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, distance : int):

        if distance < 0:
            raise Exception("You cannot drive negative kilometers!")
        if self.fuel_level*10 - distance > 0:
            self.fuel_level -= distance/10
            self.mileage += distance
            print(f"The {self.brand} {self.model} successfully drove {distance} kilometers.")

        else:
            self.mileage += self.fuel_level*10
            print(f"The {self.brand} {self.model} ran out of fuel and could only drive {self.fuel_level*10} kilometers.")
            self.fuel_level = 0
        
    def refuel(self, refill : int):
        if refill < 0:
            raise Exception("You cannot refuel negative amounts!")
        if self.fuel_level+refill > 100:
            print(f"The fuel tank of the {self.brand} {self.model} has been refilled to full, with {self.fuel_level+refill-100} fuel left.")
            self.fuel_level = 100
        else:
            self.fuel_level += refill
            print(f"The fuel tank of the {self.brand} {self.model} has been successfully refilled, now its at {self.fuel_level} %.")
        
    def car_info(self):
        return(f"{self.brand} {self.model} - Creation Date: {self.creation_date} - Fuel Tank: {self.fuel_level}% - Mileage: {self.mileage} kilometers")


class Fleet:
    def __init__(self):
        self.cars = []
    
    def add_car(self, car : Car):
        self.cars.append(car)
        print(f"The new {car.brand} {car.model} has been successfully added to the fleet.")

    def remove_car(self, car : Car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"The new {car} has been successfully removed from the fleet.")
    
    def overall_mileage(self):
        print(f"\nThe cars in the fleet share a combined sum of {sum(car.mileage for car in self.cars)} kilometers driven.\n")
    
    def fleet_info(self):
        if self.cars == []:
            print("\nThere are no cars in the fleet!\n")
        else:
            print("- Fleet Info: -")
            for car in self.cars:
                print(car.car_info())


fleet=Fleet()

car1=Car("Audi","A6",2020)
car2=Car("BMW","XM",2017)
car3=Car("Honda","Civic",2018)
car4=Car("Nissan","Z",2016)
car5=Car("Toyota","RAV-4",2022)

fleet.overall_mileage()
fleet.fleet_info()

fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)
fleet.add_car(car4)
fleet.add_car(car5)

car1.drive(200)
car2.drive(1100)
car2.refuel(40)
car2.drive(100)
car4.drive(500)
print(car2.car_info())

car5.drive(200)
car5.refuel(200)

fleet.overall_mileage()
fleet.fleet_info()
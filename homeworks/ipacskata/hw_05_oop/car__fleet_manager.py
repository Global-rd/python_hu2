class Car:
  
    def __init__(self, brand:str, modell:str, year:int, mileage:int = 0, fuel_level: float =100):


        self.brand = brand
        self.modell = modell
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level



    
    
    
    def drive(self):
        mileage = int(input("How far did you drive in km?"))    
   
        required_fuel = mileage * 0.1 
        if self.fuel_level < required_fuel:
            print("Not enough fuel to drive that far!")
            return 
    
        self.mileage += mileage
        self.fuel_level -= required_fuel
    
        print(f"The car was driven {mileage} km and the fuel level is now {self.fuel_level}%")

  


  
    def refuel_car(self):
        amount = float(input("How much did you refuel the car with?"))
        if self.fuel_level + amount > 100:
            print ("You trying to put too much fuel!")
            return
        self.fuel_level += amount
        print(f"Fuel level is now {self.fuel_level:}%.")

class Fleet:

    def __init__(self):
        self.cars = []

    def add_car(self, car:Car):
        self.cars.append(car)

    def remove_car (self, car:Car):
        self.cars.remove(car)  

    def all_mileage(self):
        total = 0

        for car in self.cars:

             total += car.mileage

        print(f"Total mileage of the fleet: {total} km")

   

    def car_list(self):
       
        for car in self.cars:
            print(f"{car.brand} {car.modell} ({car.year}) - {car.mileage} km, fuel: {car.fuel_level}%")

my_car = Car("Toyota", "Corolla", 2020, mileage=150, fuel_level=25)
my_car.refuel_car()
fleet = Fleet()
fleet.add_car(my_car)

car2 = Car("Ford", "Focus", 2018, mileage=120000, fuel_level=60)
fleet.add_car(car2)

fleet.car_list()
fleet.all_mileage()

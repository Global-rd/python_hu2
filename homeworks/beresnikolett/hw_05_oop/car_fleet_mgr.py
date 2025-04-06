class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_level = 100 #Fuel level in percentage
        self.mileage = 0

    def drive(self, distance: float):
        if distance <= 0:
            raise ValueError("Cannot drive a non-positive distance.")
        fuel_for_drive = distance * 0.1  # 0.1% üzemanyag
        max_distance = self.fuel_level / 0.1
        if fuel_for_drive > self.fuel_level:
            print(f"Not enough fuel to drive {distance} km. You can only drive {max_distance:.1f} km.")
            distance = max_distance
            fuel_for_drive = self.fuel_level
        else:    
            self.mileage += distance
            self.fuel_level -= fuel_for_drive
            print(f"The {self.brand} {self.model} has driven {distance} kilometers. Current fuel level: {self.fuel_level}%.")
    
    def refuel(self, amount: float):
        if amount <= 0:
             raise ValueError("The amount of fuel to be added must be positive.")
        elif self.fuel_level + amount > 100:
            self.fuel_level = 100
            print(f"The {self.brand} {self.model}'s fuel tank is full, no need for more fuel. Current fuel level: {self.fuel_level}%.")
        else:
            self.fuel_level += amount
            print(f"The {self.brand} {self.model} has been refueled with {amount}%. Current fuel level: {self.fuel_level}%.")
        
    def __str__(self):
        return f"{self.year} {self.brand} {self.model} - {self.mileage} kilometers driven, {self.fuel_level}% of fuel left."
    
    def __len__(self):
        return len(self.brand) + len(self.model) + len(str(self.year)) + len(str(self.milage)) + len(str(self.fuel_level))
    
class Fleet(Car):
    def __init__(self):
        self.cars = []
      
    def __str__(self):
        print(f"Fleet contains {len(self.cars)} cars.")
    
    def list_of_cars(self):
        for cars in self.cars:
            print(f"{cars.brand} {cars.model}")
        print(f"Fleet contains {len(self.cars)} cars.")
        
    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.brand} {car.model} has been added to the fleet.")
    
    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} {car.model} has been removed from the fleet.")
        else:
            print(f"{car.brand} {car.model} is not in the fleet.")
        
    def fleet_total_mileage(self):
        total_mileage = sum(car.mileage for car in self.cars)
        print(f"The total mileage of the fleet is {total_mileage} kilometers.")
    
    def fleet_status(self):
        status = []
        for car in self.cars:
            status.append(f"{car.brand} {car.model}: {car.mileage} kilometers driven, {car.fuel_level}% of fuel left.")
        return "\n".join(status) and print(f"Fleet status:\n{status}")
    
car_1 = Car("Toyota", "Corolla", 2020)
car_1.drive(500)
car_1.refuel(20)
car_2 = Car("Honda", "Civic", 2019)
car_2.drive(150)
car_2.refuel(5)
car_3 = Car("Ford", "Focus", 2021)
car_3.refuel(40)
car_3.drive(1500)
car_3.refuel(5)

fleet_1 = Fleet()
fleet_1.add_car(car_1)
fleet_1.add_car(car_2)
fleet_1.add_car(car_3)

fleet_1.list_of_cars()

fleet_1.fleet_total_mileage()
fleet_1.fleet_status()

fleet_1.remove_car(car_2)












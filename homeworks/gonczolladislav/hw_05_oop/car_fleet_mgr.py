class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100.0

    def drive(self, kilometers):
        if kilometers < 0:
            raise ValueError("Distance must be a positive number.")
        
        fuel_consumption = kilometers * 0.1
        if fuel_consumption <= self.fuel_level:
            self.mileage += kilometers
            self.fuel_level -= fuel_consumption
            print(f"{self.brand} {self.model} distance {kilometers} km.")
        else:
            max_drive = int(self.fuel_level / 0.1)
            self.mileage += max_drive
            self.fuel_level = 0
            print(f"{self.brand} {self.model} distance is {max_drive} km, fuel tank is empty.")

    def refuel(self, fuel):
        if fuel < 0:
            raise ValueError("Fuel amount must be a positive number.")  

        self.fuel_level = min(100, self.fuel_level + fuel)
        print(f"{self.brand} {self.model} refuel {fuel} liters of fuel.")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}): Km: {self.mileage}, Fuel level: {self.fuel_level:.1f}%"


class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.brand} {car.model} added to fleet.")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} {car.model} removed from fleet.")
        else:
            print(f"{car.brand} {car.model} not found on fleet.")

    def total_mileage(self):
        total = sum(car.mileage for car in self.cars)
        return total

    def __str__(self):
        fleet_status = "\nFleet state:\n"
        for car in self.cars:
            fleet_status += str(car) + "\n"
        fleet_status += f"All drived distance in km: {self.total_mileage()}"
        return fleet_status


car1 = Car("Renault", "Megane", 2020)
car2 = Car("Volkswagen", "Passat", 2021)
car3 = Car("Audi", "Q3 Sportback", 2025)
car4 = Car("Cupra", "Terramar", 2025)

fleet = Fleet()
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)
fleet.add_car(car4)

car1.drive(500)
car2.drive(300)
car3.drive(1100)
car4.drive(600)

car1.refuel(30)
car2.refuel(20)
car4.refuel(15)

print(fleet)

fleet.remove_car(car3)

print("\nFleet after car removal:\n")
print(fleet)
#Car class

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    #drive
    def drive(self, distance):
        if distance < 0: 
            raise ValueError("Distance cannot be negative.")
        if self.fuel_level <= 0:
            print("Fuel tank is empty. Please refuel.")
            return
        if distance > self.max_distance():
            print(f"Cannot drive {distance} km. Maximum distance is {self.max_distance()} km.")
            return
        fuel_needed = distance * 0.1
        if fuel_needed <= self.fuel_level:
            self.mileage += distance
            self.fuel_level -= fuel_needed
        else:
            print(f"Not enough fuel to drive {distance} km. Please refuel.")

    #refuel
    def refuel(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative.")  
        if self.fuel_level + amount > 100:
            self.fuel_level = 100
        else:
            self.fuel_level += amount

    # calculate maximum distance
    def max_distance(self):
        return self.fuel_level / 0.1

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - Mileage: {self.mileage} km, Fuel Level: {self.fuel_level}%"

# Fleet class
class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, car):
        if car in self.cars: 
            self.cars.remove(car)
            print(f"{car} has been successfully removed from the fleet.")
        else:   
            print(f"{car} not found in the fleet.")

    def total_mileage(self):
        return sum(car.mileage for car in self.cars)

    def __str__(self):
        return "\n".join(str(car) for car in self.cars)

# car types, 
if __name__ == "__main__":
    car1 = Car("Ford", "Mustang", 2006)
    car2 = Car("Trabant", "601", 1985)
    car3 = Car("Polski", "Fiat 650E", 1988)

    fleet = Fleet()
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)

    car1.drive(100)
    car2.drive(50) 
    car3.drive(330)
    car3.refuel(23)

    print("Car's details:")
    print(fleet)

    print("\nFleet's total mileage:")
    print(fleet.total_mileage())

    print("\nMaximum distance each car can drive:")
    for car in fleet.cars:
        print(f"{car.brand} {car.model}: {car.max_distance():.2f} km")
# Autó osztály

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100  

    def drive(self, distance):
        if distance < 0:
            raise ValueError("Distance cannot be negative.")
           
        fueling = distance * 0.1  

        if self.fuel_level >= fueling:
            self.mileage += distance
            self.fuel_level -= fueling
            print(f"{self.brand} {self.model} went {distance} kilometers.")
        else:
            max_distance = self.fuel_level / 0.1
            self.mileage += max_distance
            self.fuel_level = 0
            print(f"{self.brand} {self.model} could only went {max_distance:.0f} km because it ran out of fuel.")

    def refuel(self, amount):
        if amount < 0:
            raise ValueError("The amount cannot be negative.")
        self.fuel_level += amount
        if self.fuel_level > 100:
            self.fuel_level = 100
        print(f"{self.brand} {self.model} has been refueled. Fuel level: {self.fuel_level:.0f}%")

    def show_info(self):
        print(f"{self.brand} {self.model} ({self.year}) - {self.mileage:.0f} km, {self.fuel_level:.0f}% fuel level")


#Fleet
class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.brand} {car.model} added to the fleet.")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} {car.model} deleted from the fleet.")

    def total_mileage(self):
        total = 0
        for car in self.cars:
            total += car.mileage
        return total

    def show_all_cars(self):
        for car in self.cars:
            car.show_info()


if __name__ == "__main__":
    car1 = Car("Nissan", "Juke", 2017)
    car2 = Car("BMW", "X7", 2020)
    car3 = Car("KIA", "Picanto", 2018)

    fleet = Fleet()
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)


    car1.drive(250)      
    car2.drive(600)     
    car3.drive(1400)      

    car2.refuel(50)      
    car3.refuel(70)      

    print("\nCars:")
    fleet.show_all_cars()

    print("\nTotal kilometer driven:", fleet.total_mileage())





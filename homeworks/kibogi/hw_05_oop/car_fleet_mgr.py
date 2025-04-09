

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, distance):
        
        max_distance = self.fuel_level / 0.1
        if distance > max_distance:
           
           print(f"ÜZEMANYAG HIBA: {self.brand} {self.model} {self.year}\n - Tervezett távolság: {distance}\n - Maximum megtehető távolság: {max_distance}")
           distance = max_distance

        self.mileage += distance
        self.fuel_level -= distance * 0.1
        print(f"Utazási információ\n - Autó: {self.brand} {self.model} {self.year}\n - Megtett kilóméter: {distance}\n - Üzemanyag szint: {self.fuel_level}%")

          

    def refuel(self, amount):
        if self.fuel_level + amount > 100:
            self.fuel_level = 100
            print(f"TÚLTANKOLÁS - HIBA: {self.brand} {self.model} {self.year}")

        elif self.fuel_level + amount == 100:
            self.fuel_level = 100
            print(f"PONT TELE TANKOLÁS: {self.brand} {self.model} {self.year}\n - Tankolási mennyiség: {amount}% \n - Végső üzemanyag szint: {self.fuel_level}%")

        else:
            self.fuel_level += amount
            print(f"ALUL TANKOLÁS: {self.brand} {self.model} {self.year}\n - Tankolási mennyiség: {amount}% \n - Végső üzemanyag szint: {self.fuel_level}%")

    def get_car_info(self):
        return f"{self.brand} {self.model} {self.year}, Kilométeróra: {self.mileage} km, Üzemanyag szint: {self.fuel_level}%"

class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"Megvétel: {car.brand} {car.model} {car.year}")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Eladás: {car.brand} {car.model} {car.year}")
        #else:
            #print(f"Hiba: {car.brand} {car.model} {car.year} nem létezik a flottában!")
    
    def count_cars(self):
        return len(self.cars)
    
    def total_mileage(self):
        total = sum(car.mileage for car in self.cars)
        return total

    def get_fleet_info(self):
        for car in self.cars:
            print(car.get_car_info())
    
    

# ----------------------- BOGI FLOTTA FUTTATÁSA -------------------------

car1 = Car("Toyota", "Paseo", 1996)
car2 = Car("Mazda", "RX8", 2004)
car3 = Car("Honda", "Civic 2.2 iDTEC", 2013)
car4 = Car("Honda", "Civic Type R FK8", "2019")
car5 = Car("Honda", "HRV", "2020") 


fleet = Fleet()

print("\nAutóvásárlás:")
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

print("\nAutóvásárlás összegzése:")
fleet.get_fleet_info()
print(f"\nAutók száma a flottában: {fleet.count_cars()}")
print(f"\nA flotta összes kilométere: {fleet.total_mileage()}")

print("---")

print("\nUtazás - első kör:")
car1.drive(180)
car2.drive(263)
car3.drive(222)

print("\nTankolási szünet:")
car1.refuel(50)
car2.refuel(26.3)
car3.refuel(20)


print("\nAutók állapota az első kör után:")
fleet.get_fleet_info()
print(f"\nA flotta összes kilométere: {fleet.total_mileage()} km")

print("---")

print("\nUtazás - második kör:")
car1.drive(1500)
car2.drive(111)
car3.drive(245)

print("\nTankolási szünet:")
car1.refuel(40)
car2.refuel(70)
car3.refuel(25)

print("\nAutók állapota az második kör után:")
fleet.get_fleet_info()
print(f"\nA flotta összes kilométere: {fleet.total_mileage()}")

print("---")

print("\nAutóeladás:")
fleet.remove_car(car1)
fleet.remove_car(car2)

print(f"\nAutók száma a flottában: {fleet.count_cars()}")
fleet.get_fleet_info()

print("---")

print("\nAutóvásárlás:")
fleet.add_car(car4)
fleet.add_car(car5)

print("\nJelenlegi flotta:")
fleet.get_fleet_info()
print(f"\nAutók száma a flottában: {fleet.count_cars()}")
print(f"\nA flotta összes kilométere: {fleet.total_mileage()}")

print("---")

print("\nUtazás - harmadik kör:")
car3.drive(188)
car4.drive(273)   
car5.drive(210)  

print("\nTankolási szünet:")
car3.refuel(15)
car4.refuel(25)
car5.refuel(10)

print("\nAutók állapota az harmadik kör után:")
fleet.get_fleet_info()
print(f"\nA flotta összes kilométere: {fleet.total_mileage()}")

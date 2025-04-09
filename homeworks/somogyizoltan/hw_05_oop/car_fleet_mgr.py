"""
Hozz létre egy car_fleet_mgr.py nevű file-t, és kódold le a következő feladat
megoldását:
Készíts egy Car osztályt, amely rendelkezik a következő tulajdonságokkal:
● Márka (brand)
● Modell (model)
● Gyártási év (year)
● Kilométeróra állása (mileage), induló értéke 0.
● Üzemanyag-szint (fuel_level), induló értéke 100 (százalékban).
Az osztály tartalmazza a következő metódusokat:
● Egy konstruktor, amely beállítja a fenti attribútumokat.
● Egy drive() metódus, amely adott számú kilométerrel növeli a
kilométeróra állását, és csökkenti az üzemanyag-szintet (tételezzük fel,
hogy 0.1% üzemanyag fogy megtett kilométerenként). A drive()
metódus csak annyit km-et engedjen vezetni, amennyire elegendő
üzemanyag van.
● Egy refuel() metódus, amely feltölti az üzemanyag-szintet egy adott
mennyiséggel. Figyelj a limitekre.
Készíts egy Fleet osztályt, amely kezeli a Car objektumokat:
● Az osztály rendelkezzen egy listával, amelyben az autók találhatóak.
● Tartalmazzon metódusokat Car objektumok hozzáadására és
eltávolítására a flottába/flottából.
● Tartalmazzon egy metódust, amely összesíti a flotta összes autójának
összes kilométerét.
● Hozz létre néhány Car objektumot, add hozzá őket a flottához, hajts
végre néhány műveletet (vezetés, tankolás), jelenítsd meg az autók
állapotát és a flotta összesítő adatait."
"""
# Hibaüzenet miatt

class NegativeUserInput(Exception):
    pass

#  Létrehozni a Car osztályt, amit kibővítettem egy új paraméterrel ami a rendszám, hogy könnyeben lehessen egy adott autóra hivatkozni 
class Car:
    def __init__(self, c_registered_num:str, c_brand: str, c_model: str, c_year: int, c_mileage:int=0, c_fuel_level:float=100.0):
        self.registered_num = c_registered_num
        self.brand = c_brand
        self.model = c_model
        self.year = c_year
        self.mileage = c_mileage
        self.fuel_level = c_fuel_level
        

    def __str__(self):    
        return f"{self.brand} {self.model} - registration year: {self.year} - registered number: {self.registered_num} - km: {self.mileage} - fuel: {self.fuel_level}"
    
    def drive(self, running_km:int):
        
        if running_km < 0:
            raise NegativeUserInput("Km must be a positive number!") 
        
        else:
            if self.fuel_level >= 0.1*running_km:
                self.mileage += running_km
                self.fuel_level -= 0.1*running_km
                print(f"{self} car mileage is added to car.")
            else:
                print(f"{self} in car is not enought fuel!")
    

    def refuel(self, fuel_level):

        if fuel_level < 0:
            raise NegativeUserInput("Fuel level must be a positive number!")  
        
        else:
            if self.fuel_level + fuel_level <= 100:
                self.fuel_level += fuel_level
                print(f"{self} - car have a {self.fuel_level} fuel")
            else:
                self.fuel_level = 100.0
                print(f"{self} - car have a full fuel")    

        

class Fleet:
    def __init__(self):
        self.list_of_cars = []

    def add_car(self, one_car:Car):
        self.list_of_cars.append(one_car)

    def remove_car(self, one_car:Car):
        self.list_of_cars.remove(one_car)

    def print_car_list(self):
         print("Cars in fleet list:")
         total_mile = 0

         for car in self.list_of_cars:
             print(car)
             total_mile += car.mileage
         
         print(f"Total mileage: {total_mile} km")    


    def find_car(self, reg_num):
        for car in self.list_of_cars:
            if car.registered_num == reg_num:
                return car
        return None      # Ha nem találta meg a rendszám alapján         

# Fő menü kiíratása, amit ciklusban fogok hívni - ez olyan lesz, mint a 4. feladatnál, csak aktualizáltam - lehet, hogy írni kellene erre egy saját modult...
def display_menu():
    print("Fleet Manager! Please enter your choice!")
    print("1. Add New Car")
    print("2. Remove One Car")
    print("3. Input km for One Car")
    print("4. Refuel for One Car")
    print("5. View all Car from fleet")
    print("6. Exit")



#  Kezdjük a programot
    
car = Car("XXX", "YYYY", "ZZZ", 2020)

fleet = Fleet()

# Main loop az menü kiíratására és az adatok bekérésehez
while True:
    display_menu()

    user_choice = int(input("Your choice is: "))

    if user_choice in range(1, 7):

        if user_choice == 1:       #   Add new car to list
            print("Please enter the car!")
            reg_num = input(f"Registered number: ")
            brand = input(f"Brand: ")
            model = input(f"Model: ")
            year = int(input(f"Date of 1. registration: "))

            if fleet.find_car(reg_num) == None:
                car = Car(reg_num, brand, model, year)
                fleet.add_car(car)
                print(f"{car} is added to list!")
            else:                
                print(f"{reg_num} - this registered number is in the list!")
            
        elif user_choice == 2:      #   Remove car from the list
            print("Please enter the car!")
            reg_num = input(f"Registered number: ")

            car = fleet.find_car(reg_num)
            if car == None:
                print(f"{reg_num} - this registered number isn't the list!")                
            else:
                fleet.remove_car(car)
                print(f"{car.registered_num} is removed from list!")
            
        elif user_choice == 3:       #   Add km to the car
            print("Please enter the car!")
            reg_num = input(f"Registered number: ")
            reg_mile = int(input(f"Add km: "))
            
            car = fleet.find_car(reg_num)
            if car == None:
                print(f"{reg_num} - this registered number isn't the list!")                
            else:
                car.drive(reg_mile)

        elif user_choice == 4:       #   Refuel gas to the car
            print("Please enter the car!")
            reg_num = input(f"Registered number: ")
            fuel_plus = int(input(f"Add fuel level (max 100): "))

            car = fleet.find_car(reg_num)
            if car == None:
                print(f"{reg_num} - this registered number isn't the list!")                
            else:
                car.refuel(fuel_plus)

        elif user_choice == 5:
            fleet.print_car_list()            
        else:
            break 

    else:
        print(f"Wrong number >>{user_choice}<<! Please try again!")

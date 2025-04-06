

class Car:
    def __init__(self, brand:str, model:str, license_plate_number: str, year:int, km: int = 0, fuel_level: int = 100):  # a year-nek is str a hintje?
        self.brand = brand
        self.model = model
        self.license_plate_number = license_plate_number  # JAVÍTÁS: rendszám
        self.year = year
        self.km = km
        self.fuel_level = fuel_level


    def drive(self, distance):
        
        if distance < 0:
            raise ValueError("Distance cannot be negative number!")  # JAVÍTÁS: gondolom itt is ValueErrort kell adni     
        
        fuel_consumption = distance / 10  # 1 km-enként 0,1% 
       
        if self.fuel_level > 0:  # feltétel, különben nem tud vezetni
            if self.fuel_level >= fuel_consumption:
                self.km -= distance
                self.fuel_level -= fuel_consumption
                print(f"Distance made: {distance}, Fuel: {self.fuel_level}%")
            else:
                print("Not enough fuel in the tank!")
        else:
            print("No fuel in the tank!")

    def refuel(self, refuel_level):

        if refuel_level <= 0:
            raise ValueError("Refuel level must be greater than 0%!")  # JAVÍTÁS: ValueError
        elif refuel_level > 100:
            raise ValueError("Fuel level cannot be greater than 100%!") # JAVÍTÁS: ValueError - gondolom akkor már erre is így kellene
        elif refuel_level <= self.fuel_level:
            print("You have enough fuel!")
        else:
            fuel_difference = refuel_level -self.fuel_level
            self.fuel_level += (refuel_level - self.fuel_level)
            self.km += fuel_difference * 10
            print(f"Fuel level: {self.fuel_level}%")
        print(f"Maximum distance left: {self.fuel_level * 10} km")
    
    def __str__(self):
        return f"License plate number: {self.brand} {self.model}, {self.license_plate_number}, {self.year}, {self.km}km, fuel: {self.fuel_level}%"


class Fleet:

    def __init__(self):
        self.fleet = []

    def add_car(self, car: Car):  # hivatkozom a Car osztályra
        self.fleet.append(car)  # JAVÍTÁS: autó hozzáadása
        print(f"Car added to the fleet.")
    
    def remove_car(self, license_plate_number: str):  # JAVÍTÁS: rendszám alapján törlök
        car_to_remove = None
        for car in self.fleet:
            if car.license_plate_number == license_plate_number:
                car_to_remove = car
                break

        if car_to_remove:
            self.fleet.remove(car_to_remove)
            print(f"Car with license plate {license_plate_number} deleted from fleet")
        else:
            print(f"Car with license plate {license_plate_number} is not present in fleet")
    
    def total_km(self):
        return sum(car.km for car in self.fleet)
    
    def print_fleet(self):  # enélkül nem engedett hozzáadni új autót, de nem teljesen értem
        print("List of fleet:")
        for car in self.fleet:
            print(car)
# LOGIKA:

my_fleet = Fleet()

while True:

    my_fleet.print_fleet()  # itt kiiratom a dictionary-my_fleet.print_fleet()t

    activity_list_fleet_level = {
        1: "add car",
        2: "remove car",
        3: "select car",  
        4: "finish",  # kilépjen a loopból
    }

    # listázom az opciókat

    for activities_fleet_level in activity_list_fleet_level:
        print(f"{activities_fleet_level}: {activity_list_fleet_level[activities_fleet_level]}")
    select_activity_fleet_level = int(input("Select activity! Add number of option! "))

    if select_activity_fleet_level == 1:
              
        #Bekérem az új autó adatait
        print("Enter car data!")
        brand = input("Brand: ")
        model = input("Model: ")
        license_plate_number = input("License plate number: ")  # JAVÍTÁS: rendszám bekérése
        year = int(input("Year: "))
        fuel_level = int(input("Fuel_level in %: "))  # erre nem írtam most validációs feltételt, ahogy a car osztályban van
        km = int(fuel_level * 10)

        new_car = Car(brand, model, license_plate_number, year, km, fuel_level)

        my_fleet.add_car(new_car)

    elif select_activity_fleet_level == 2:
        
        license_plate_number = input("Enter license plate number of car to remove: ")  # model alapján törlök
        my_fleet.remove_car(license_plate_number)  # az előbb definiált model megadott értéke alapján törlöm az autót a listából

    elif select_activity_fleet_level == 3:
        
        license_plate_number = input("Enter car's license plate number to select: ")  # JAVÍTÁS: listaként kell kezelni
                
        for car in my_fleet.fleet:
            if car.license_plate_number == license_plate_number:
                selected_car = car
                break
        
        if selected_car:  # JAVÍTÁS: enélkül ha nincs talált egyezés a listában, akkor is elindul a loop
            while True:
                activity_list_car_level = {
                    1: "drive",
                    2: "refuel vehicle",
                    3: "finish",  # kilépjen a loopból
                }

                # listázom az opciókat

                for activities_car_level in activity_list_car_level:
                    print(f"{activities_car_level}: {activity_list_car_level[activities_car_level]}")
                select_activity_car_level = int(input("Select activity! Add number of option! "))

                if select_activity_car_level == 1:
                    if car.fuel_level == 0:
                        print(f"You must refill the fuel tank!")
                        continue  # vissza a loop elejére
                    else:
                        distance = int(input("Distance you drove in km: "))
                        if distance > selected_car.fuel_level * 10: # maximum távolság
                            print(f"Maximum distance with your fuel level is {selected_car.fuel_level * 10} km. Enter valid distance!")
                            continue
                        else:
                            selected_car.drive(distance)  # car objektum drive metódusa distance paraméterrel

                elif select_activity_car_level == 2:
                    refuel_level = int(input("Please add the level of refuelling in %: "))
                    if refuel_level <= selected_car.fuel_level:  # nem lehet kisebb, mint ami van
                        print(f"You have enough fuel!")
                        continue
                    elif refuel_level > 100:  # nem lehet nagyobb, mint 100%
                        print (f"The maximum fuel level can be 100%!")
                        continue
                    else:
                        selected_car.refuel(refuel_level)
                
                elif select_activity_car_level == 3:
                    print("You parked the car.")
                    print(f"Fuel: {car.fuel_level}%")
                    print(f"Maximum distance left: {car.fuel_level * 10} km")
                    print(f"What would you like to do?")
                    break
                else:
                    print("Choose a valid option!")
                    continue

        else:
            print("Car not found!")

    elif select_activity_fleet_level == 4:
        break
    else:
        print("Choose a valid option!")
        continue
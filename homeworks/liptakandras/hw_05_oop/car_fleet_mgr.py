

class Car:
    def __init__(self, brand:str, model:str, year:int, km: int = 0, fuel_level: int = 100):  # a year-nek is str a hintje?
        self.brand = brand
        self.model = model
        self.year = year
        self.km = km
        self.fuel_level = fuel_level

    def drive(self, distance):
              
        fuel_consumption = distance / 10  # 1 km-enként 0,1% 
       
        if self.fuel_level > 0:  # feltétel, különben nem tud vezetni
            if self.fuel_level >= fuel_consumption:
                self.km += distance
                self.fuel_level -= fuel_consumption
                print(f"Distance made: {distance}, Fuel: {self.fuel_level}%")
            else:
                print("Not enough fuel in the tank!")
        else:
            print("No fuel in the tank!")

    def refuel(self, refuel_level):

        if refuel_level <= 0:
            print(f"Refuel level must be greater than 0%!")
        elif refuel_level > 100:
            print(f"Fuel level cannot be greater than 100%!")
        elif refuel_level <= self.fuel_level:
            print("You have enough fuel!")
        else:
            self.fuel_level += (refuel_level - self.fuel_level)
            print(f"Fuel level: {self.fuel_level}%")
        print(f"Maximum distance left: {self.fuel_level * 10} km")

class Cars:

    def __init__(self):
        self.cars = {}  # dictionary a brand, model, year, km, fuel level miatt

    def add_car(self, car: Car):  # hivatkozom a Car osztályra
        self.cars[car.model] = {  # minden autó egy dictionary, tehát dictionary a listában
            "brand": car.brand,
            "model": car.model,
            "year": car.year,
            "km": car.km,
            "fuel_level": car.fuel_level,
        }
        print(f"Car added to the list of cars.")
    
    def remove_car(self, model: str):
        if model in self.cars:
            del self.cars[model]
        else:
            print("This car is not on the list of cars!")
    
    def total_km(self):
        return sum(car["km"] for car in self.cars.values())
    
    def print_cars(self):  # enélkül nem engedett hozzáadni új autót, de nem teljesen értem
        print("List of cars:")
        for model, car_data in self.cars.items():
            print(f"{car_data['brand']} {car_data['model']}, {car_data['year']}, {car_data['km']}km, fuel: {car_data['fuel_level']}%")

# LOGIKA:

my_cars = Cars()

while True:

    my_cars.print_cars()  # itt kiiratom a dictionary-t

    activity_list_cars_level = {
        1: "add car",
        2: "remove car",
        3: "select car",  
        4: "finish",  # kilépjen a loopból
    }

    # listázom az opciókat

    for activities_cars_level in activity_list_cars_level:
        print(f"{activities_cars_level}: {activity_list_cars_level[activities_cars_level]}")
    select_activity_cars_level = int(input("Select activity! Add number of option! "))

    if select_activity_cars_level == 1:
              
        #Bekérem az új autó adatait
        print("Enter car data!")
        brand = input("Brand: ")
        model = input("Model: ")
        year = int(input("Year: "))
        fuel_level = int(input("Fuel_level in %: "))  # erre nem írtam most validációs feltételt, ahogy a car osztályban van
        km = int(fuel_level * 10)

        new_car = Car(brand, model, year, km, fuel_level)

        my_cars.add_car(new_car)

    elif select_activity_cars_level == 2:
        
        model = input("Enter model of car to remove: ")  # model alapján törlök
        my_cars.remove_car(model)  # az előbb definiált model megadott értéke alapján törlöm az autót a listából

    elif select_activity_cars_level == 3:
        
        model = input("Enter model to select: ")  # model alapján választhat autót
        if model in my_cars.cars:  # autóválasztás feltétele, hogy már létezik a listában
            selected_car = my_cars.cars[model]
            car = Car(selected_car["brand"], selected_car["model"], selected_car["year"], selected_car["km"], selected_car["fuel_level"])
        
        
            # KIVÁLASZTOTT AUTÓ KM ÉS FOGYASZTÁS VÁLTOZÁSA

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
                        if distance > car.fuel_level * 10: # maximum távolság
                            print(f"Maximum distance with your fuel level is {car.fuel_level * 10} km. Enter valid distance!")
                            continue
                        else:
                            car.drive(distance)  # car objektum drive metódusa distance paraméterrel
                            my_cars.cars[car.model]["km"] = car.km  # visszaírom a listába
                            my_cars.cars[car.model]["fuel_level"] = car.fuel_level  # visszaírom a listába

                elif select_activity_car_level == 2:
                    refuel_level = int(input("Please add the level of refuelling in %: "))
                    if refuel_level <= car.fuel_level:  # nem lehet kisebb, mint ami van
                        print(f"You have enough fuel!")
                        continue
                    elif refuel_level > 100:  # nem lehet nagyobb, mint 100%
                        print (f"The maximum fuel level can be 100%!")
                        continue
                    else:
                        car.refuel(refuel_level)
                        my_cars.cars[car.model]["fuel_level"] = car.fuel_level  # visszaírom a listába
                        my_cars.cars[car.model]["km"] = int(car.fuel_level * 10)  # visszaírom a listába
                
                elif select_activity_car_level == 3:
                    print("You parked the car.")
                    print(f"Fuel: {car.fuel_level}%")
                    print(f"Maximum distance left: {car.fuel_level * 10} km")
                    print(f"What would you like to do?")
                    break
                else:
                    print("Choose a valid option!")
                    continue

    elif select_activity_cars_level == 4:
        pass
    else:
        print("Choose a valid option!")
        continue

    my_cars.print_cars()
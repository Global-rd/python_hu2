#real life example: egy gépezet ami játékokat gyárt

#van egy kezelőfeülülete, amin be tudjuk állítani a következőket:
#- játék típus (pl: barbie, matchbox)
#- játék színe
#ezután a gép legyártja a játékot

#class: maga a gépezet, ami tudja hogyan kell megcsinálni a megadott paraméterek alapján a játékot, van hozzá egy  leírása
#__init__(): a gép kezelőfelülete, amivel interaktálunk amikor létre akarjuk hozni a játékot, itt egy gombnyomás hoz létre új játékot
#instance(példány): az osztály egy példánya, vagyis a gép által létrehozott játék
#instance variable: a tulajdonság, ami jellemzi a gép által létrehozott játékot (attribute: sárga szín, barbi típus)
#class variable: egy olyan változó ami kizárólag a gépet jellemzi, például hány játékot gyártott le eddig
#instance method: olyan metódus ami a példányokat (játékok) használja/módosítja, pl egy move() metódus
#class method: egy olyan metódus ami az osztály változóit használja/módosítja pl egy get_toy_count() metódus
#static method: nincs hozzáférése sem az osztályhoz, sem a példányhoz, de logikailag ide tartozik, pl: használhatja e a gyerek x éves korban a játékot ()


class Toy:

    toy_count = 0

    def __init__(self, t_type, t_color):
        self.toy_type = t_type
        self.toy_color = t_color
        Toy.toy_count +=1

    def play(self): #instance method
        print(f"Currently playing with {self.toy_color} {self.toy_type}")

    def move(self, distance, direction):
        print(f"{self.toy_color} {self.toy_type} moved {distance} meters to {direction}")

    @classmethod #decorator
    def get_toy_count(cls):
        return cls.toy_count
    
    @staticmethod
    def is_toy_safe_for_age(toy_type, age):

        if toy_type == "matchbox" and age < 3:
            return False
        return True


toy_matchbox = Toy(t_type="matchbox", t_color="yellow")
print(toy_matchbox)
print(toy_matchbox.toy_type)
print(toy_matchbox.toy_color)
toy_matchbox.toy_color = "green"
print(toy_matchbox.toy_type)
print(toy_matchbox.toy_color)

toy_matchbox.play()

toy_barbie = Toy(t_type="barbie", t_color="pink")
toy_barbie.play()

print(f"toy count: {Toy.get_toy_count()}")

print(Toy.is_toy_safe_for_age(toy_matchbox.toy_type, 3))

toy_matchbox.move(10, "left")

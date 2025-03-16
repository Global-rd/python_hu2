#mire jók a function-ök?
#kód újrahasznosítása
#a rendezettség fokozása
# "separation of concerns" - különböző feladatok különböző function-ökre bontása
# szabályok amiket érdemes betartani:
# DRY: Don't Repeat Yourself! -> repetitív logika absztrakciója function-ökkel
# Single Responsibility Principle -> egy function egy feladatért legyen felelős
# Kerüljük el a mutable object-eket default argumentekként!

# bad example:
name_1 = "Alice"
name_2 = "Bob"
name_3 = "Jim"

print(f"Hello {name_1}, welcome home!")
print(f"Hello {name_2}, welcome home!")
print(f"Hello {name_3}, welcome home!")

#good example:
print("-----------------------")

def greet_user(name):
    print(f"Hello {name}, welcome on board!")

greet_user(name_1)
greet_user(name_2)
greet_user(name_3)

print("---------------------")
# for loop
names = ["Alice", "Bob", "Jim"]
for name in names:
    greet_user(name)



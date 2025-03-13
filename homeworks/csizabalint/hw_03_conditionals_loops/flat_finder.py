"""
Feladat:
Nagyon szereti New York-ot és San Fransisco-t, bármelyik városban kivenne egy lakást, ha az albérlet ára kevesebb mint 4000 USD havonta.
Gyűlöli Washington-t, és semmi pénzért nem lakna ott
Annyira imádja Chicago-t, hogy még a pénz sem akadály, bármit megadna azért hogy ott lakhasson
Ha bármilyen más helyről van szó, 3000 USD vagy ez alatti havi lakbér ellenében költözne oda.
"""

#Input City
city = input("Which city do you want to live in? ")
budget = int(input("What is your budget for the rent in USD? "))

#Conditions
if city == "Chicago":
    print(f"You can afford it, go to Chicago!")

elif city in["New York", "San Fransisco"] and budget < 4000:
        print(f"Your {budget} USD budget is enough, you can move to {city}!")
    
elif city == "Washington":
    print("There is no money in the world that would make you move to Washington!")

elif budget <= 3000:
    print(f"Your {budget} USD budget is enough, you can move to {city}!")
    
else:
    print(f"Your {budget} USD budget is not enough, you can't move to {city}!")
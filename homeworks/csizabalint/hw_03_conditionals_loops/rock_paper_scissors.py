"""
Feladat 2: while és for loop használata
Hozz létre egy rock_paper_scissors.py nevű file-t, és kódold le a következő feladat megoldását:

Írj egy python programot ami levezényli a kő-papír-olló játékot két játékos között. 
A program kérje be, hogy hány kört akarnak játszani a játékosok.
Figyelj oda, hogy olyan számot kell megadnia a felhasználónak ami mellett nem tudnak döntetlent játszani!
Ha nem ilyen számot ad meg, írj ki hibaüzenetet és addig kérd be újra a körök számát amíg páratlan számot nem ad meg.
Ezután a program felváltva kérje be az első és második játékos válaszát, ami kizárólag a következő stringek
valamelyike lehet: "rock", "paper", "scissors". Ellenkező esetben kezeld úgy a hibát ahogy a körök számánál.
Tárold a nyertesek pontjait, és minden kör végén növeld az aktuális játékos pontszámát.
A végén printeld ki ki nyert, és hány ponttal.
"""

print("Let's play Rock-Paper-Scissors!")

while True:
    rounds = int(input("How many rounds would you like to play? It should be an odd number: "))
    if rounds % 2 == 1:
        break
    print("The number must be odd.")
   
   
points = {"Player 1": 0, "Player 2": 0}
options = ["rock", "paper", "scissors"]

for round_num in range(rounds):
    print(f"\nRound {round_num + 1}:")
    
    while True:
        p1 = input("Player 1's choice: ")
        while p1 not in options:
            print("Please choose between rock, paper, scissors.")
            p1 = input("Player 1's choice: ")
        
        p2 = input("Player 2's choice: ")
        while p2 not in options:
            print("Please choose between rock, paper, scissors.")
            p2 = input("Player 2's choice: ")
        
        if p1 != p2:
            break
        print("Draw! Please choose again.")
    
    if (p1, p2) in [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]:
        print("Player 1 wins this round!")
        points["Player 1"] += 1
    else:
        print("Player 2 wins this round!")
        points["Player 2"] += 1

if points["Player 1"] > points["Player 2"]:
    winner = "Player 1"
else:
    winner = "Player 2"

print(f"\nGame Over! {winner} won with: {points['Player 1']} - {points['Player 2']}")
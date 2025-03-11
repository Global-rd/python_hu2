"""
Írj egy python programot ami levezényli a kő-papír-olló játékot két játékos között. A
program kérje be, hogy hány kört akarnak játszani a játékosok. Figyelj oda, hogy
olyan számot kell megadnia a felhasználónak ami mellett nem tudnak döntetlent
játszani! Ha nem ilyen számot ad meg, írj ki hibaüzenetet és addig kérd be újra a
körök számát amíg páratlan számot nem ad meg. Ezután a program felváltva kérje
be az első és második játékos válaszát, ami kizárólag a következő stringek
valamelyik lehet: "rock", "paper", "scissors". Ellenkező esetben kezeld úgy a hibát
ahogy a körök számánál. Tárold a nyertesek pontjait, és minden kör végén növeld
az aktuális játékos pontszámát. A végén printeld ki ki nyert, és hány ponttal.

Egy kicsit megbolondítottam....
player_01 a számítógép lesz a random generátor segítségével..
Tudom, hogy ezt még nem tanultuk, de remélem ezzel játszani is lehet...
"""

import random

# Változók, alap érték megadás
max_round = 0
input_list = ["rock", "paper", "scissors"]
player_01_points = 0
player_02_points = 0

player_01_choise = ""
player_02_choise = ""

# Bekérni a maximum tippelési számot

while True:
    max_round = int(input("Add meg mennyi játékot szeretnél játszani: "))
    if max_round % 2 == 1:
        break
    else:
        print("HIBA! Páratlan számot kell megadnod!")

# Fő ciklus, amíg le nem csökken nullára
while max_round > 0:
    
    # Itt választom ki, hogy a számítógép mit választ...
    pc_choise = random.randint(0, 2)
    
    player_01_choise = input_list[pc_choise]

    while True:
        player_02_choise = input(f"Add meg a második játékos tippjét ebből a listából {input_list}:")
        if player_02_choise in input_list:
            break
        else:
            print("HIBA! Nem a megengedett tippet írtad! Add meg még egyszer!")
    
    # Tesztelni a beadott tippeket
    if player_01_choise == player_02_choise:
        # Azonos tipp, nem csökkentem a ciklus számlálót
        print("Azonos mindkét tipp! Próbáld meg még egyszer!")
    else:
        # Nem azonos tipp, itt csökken a körök számlálója
        max_round -= 1

        # Megnézni, hogy ki nyert
        if player_01_choise == "rock" and player_02_choise == "paper":
            print("ebben a körben a 2-es nyert")
            player_02_points += 1
        elif player_01_choise == "rock" and player_02_choise == "scissors":    
            print("ebben a körben az 1-es nyert")
            player_01_points += 1
        elif player_01_choise == "paper" and player_02_choise == "scissors":    
            print("ebben a körben a 2-es nyert")
            player_02_points += 1
        elif  player_01_choise == "paper" and player_02_choise == "rock":       
            print("ebben a körben az 1-es nyert")
            player_01_points += 1
        elif player_01_choise == "scissors" and player_02_choise == "rock":       
            print("ebben a körben a 2-es nyert")
            player_02_points += 1
        else:
            print("ebben a körben az 1-es nyert")
            player_01_points += 1  

# Kiírni a végeredményt
if player_01_points > player_02_points:
    print(f"A számítógép győzött {player_01_points} : {player_02_points} arányban!" )
else:
    print(f"A második játékos győzött {player_02_points} : {player_01_points} arányban!" )    
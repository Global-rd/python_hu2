rounds = 0

while rounds % 2 != 1:

    rounds = int(input ("Hány kört szeretnél játszani?"))

    if rounds % 2 != 1:
        print (f"Hiba, a megadott körök száma {rounds}, ami páros szám. Kérlek adj meg egy páratlan számot")
    else:
        print ("Kezdödhet a játék!")

        

choices = ["rock", "paper", "scissors"]
point_player_1 = 0
point_player_2 = 0
round_count = 0

while round_count < rounds:

    choice_player_1 = input ("Játékos 1, mi a választásod?")

    if choice_player_1 not in choices:
        print (f"Hiba, a választásod {choice_player_1}, ami nem elfogadott. Választásod csak rock, paper, scissors lehet.")

    choice_player_2 = input ("Játékos 2, mi a választásod?")

    if choice_player_2 not in choices:
        print (f"Hiba, a választásod {choice_player_2}, ami nem elfogadott. Választásod csak rock, paper, scissors lehet.")

    if choice_player_1 == choice_player_2:
        round_count +=1
        print(f"Döntetlen! Körök száma {round_count}")

    elif (choice_player_1 == "rock" and choice_player_2 == "scissors") or (choice_player_1 == "paper" and choice_player_2 == "rock") or (choice_player_1 == "scissors" and choice_player_2 == "paper"):
        point_player_1 +=1 
        round_count +=1
        print(f"Az első játékos nyert!. Pontja: {point_player_1}. Körök száma {round_count}")
    else:
        point_player_2 +=1 
        round_count +=1
        print(f"A második játékos nyert! Pontja: {point_player_2}. Körök száma {round_count}")
    

if point_player_1 == point_player_2:
    print("A játéknak vége, az eredmény dDöntetlen!")

elif (point_player_1 > point_player_2) :
    print(f"A játéknak vége, Játékos 1 nyert {point_player_1} az {point_player_2}-hez.!")

else: 
    print(f"A játéknak vége, Játékos 2 nyert {point_player_2} az {point_player_1}-hez.!")
           
rounds = int(input("Add meg, hogy hány kört szeretnétek játszani: "))
first_player_score = 0
second_player_score = 0
while rounds%2 == 0:
    rounds=int(input("Kérlek add meg újra, hogy hány kört szeretnétek játszani (csakis páratlan szám lehet): "))

for i in range(rounds):

    while True:

        while True:
            first_player_input=input("Első játékos, add meg, hogy mit lépsz: ")
            if first_player_input in ("rock","paper","scissors"):
                break
    
        while True:
            second_player_input=input("Második játékos, add meg, hogy mit lépsz: ")
            if second_player_input in ("rock","paper","scissors"):
                break

        if first_player_input == second_player_input:
            print(f"\n Ez a kör döntetlen volt! Próbáljuk meg újra! \n")
        elif (first_player_input == "rock" and second_player_input == "scissors") or (first_player_input == "paper" and second_player_input == "rock") or (first_player_input == "scissors" and second_player_input == "paper"):
            first_player_score += 1
            print(f"\n Ezt a kört az Első Játékos nyerte! Most {first_player_score} pontja van!\n")
            break
        else:
            second_player_score += 1
            print(f"\n Ezt a kört a Második Játékos nyerte! Most {second_player_score} pontja van!\n")
            break
    

if first_player_score > second_player_score:
    print(f"\n Az Első Játékos nyerte ezt a meccset! \n Az Első Játékosnak {first_player_score} pontja volt, míg a Második Játékosnak {second_player_score} pontja volt. \n")
else:
    print(f"\n A Második Játékost nyerte ezt a meccset! \n Az Első Játékosnak {first_player_score} pontja volt, míg a Második Játékosnak {second_player_score} pontja volt. \n")
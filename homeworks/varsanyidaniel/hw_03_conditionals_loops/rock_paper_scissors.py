def vs (f,s,player_1_score,player_2_score):
    if f == "rock" and s == "scissors":
        print("Ezt a kört az Első Játékos nyerte!")
        return player_1_score + 1
    elif f == "scissors" and s == "paper":
        print("Ezt a kört az Első Játékos nyerte!")
        return player_1_score + 1
    elif f == "paper" and s == "rock":
        print("Ezt a kört az Első Játékos nyerte!")
        return player_1_score + 1
    elif f == s:
        print("Ez a kört döntetlen volt!")
    else:
        print("Ezt a kört a Második Játékos nyerte!")
        return player_2_score + 1



rounds = int(input("Add meg, hogy hány kört szeretnétek játszani: "))
first_player_score = 0
second_player_score = 0
while rounds%2 == 0:
    rounds=int(input("Kérlek add meg újra, hogy hány kört szeretnétek játszani (csakis páratlan szám lehet): "))

for i in range(rounds):

    while True:
        first_player_input("Első játékos, add meg, hogy mit lépsz: ")
        if first_player_input in ("rock","paper","scissors"):
                break
    
    while True:
        second_player_input("Második játékos, add meg, hogy mit lépsz: ")
        if second_player_input in ("rock","paper","scissors"):
            break

vs(first_player,second_player,first_player_score,second_player_score)

if first_player_score > second_player_score:
    print("Az Első Játékos nyerte ezt a meccset!")
elif first_player_score < second_player_score:
    print("A Második Játékost nyerte ezt a meccset!")
else:
    print("A meccs döntetlen volt!")
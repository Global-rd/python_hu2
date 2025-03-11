# körök számának bekérése, hiba vissza adása ha a szám páros
rounds = int(input("How many rounds do you want to play?"))

if rounds%2 == 0 or rounds < 1:
    print(f"{rounds} is a wrong number... if you want the game to be end well you have to choose an odd number!")

# ha a körök száma páratlan, mehetünk tovább
else:

    item_list = ["rock", "paper", "scissors"]
    first_player = input("What is the name of the first player?")
    second_player = input("What is the name of the second player?")
    first_scores = 0
    second_scores = 0

    # szabályok meghatározása előre

def game_result(choice1, choice2):
    
    rules = {
        "rock": "scissors",   # kő legyőzi az ollót
        "scissors": "paper",  # olló legyőzi a papírt
        "paper": "rock"       # papír legyőzi a követ
        }
        
    if choice1 == choice2:
            return "It's a tie!"
       
    elif rules[choice1] == choice2:
       
            return f"{first_player} wins! {choice1} beats {choice2}"
    else:
            return f"{second_player} wins! {choice2} beats {choice1}"

    # kör kiírása és hozzáadása
round_num = 0  # a körök száma itt kezelve lesz

while round_num < rounds:  # amíg el nem érjük a kívánt köröket
        print(f"Round {round_num + 1}")


        # választás bekérése
        choice1 = ""
        choice2 = ""
        while True:  # a választásokat addig kérjük, amíg nem lesz érvényes
            choice1 = input(f"{first_player}, choose rock, paper, or scissors: ").lower()
            choice2 = input(f"{second_player}, choose rock, paper, or scissors: ").lower()

            # ellenőrzés, hogy az "item_list" elemeinek egyikét adták-e meg, különben hiba kiírása
            if choice1 not in item_list or choice2 not in item_list:
                print("Invalid choice! Please choose rock, paper, or scissors!")
            else:
                break

        # eredmény kiírása
        result = game_result(choice1, choice2)
        print(result)

        # pont hozzáadása a nyertesnek
        if "wins!" in result:
            if first_player in result:
                first_scores += 1
            else:
                second_scores += 1
            round_num += 1

    # végső pontszám kiírása
print(f"\nFinal Scores: {first_player}: {first_scores}, {second_player}: {second_scores}")
if first_scores > second_scores:
        print(f"{first_player} wins the game with!")
else:
        print(f"{second_player} wins the game!")

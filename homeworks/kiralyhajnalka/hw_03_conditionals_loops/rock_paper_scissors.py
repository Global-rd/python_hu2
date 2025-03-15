# 2. feladat: while és for loop használata

while True:
    try:
        rounds = input("Hány kört akarnak játszani a játékosok?: ")
        if rounds.isdigit():
            rounds = int(rounds)
            if rounds % 2 == 1 and rounds > 0:
                break
            else:
                print("Hiba: Csak pozitív páratlan számú kört lehet megadni!")
        else:
            print("Hiba: Kérlek, adj meg egy érvényes számot!")
    except ValueError:
        print("Hiba: Kérlek, adj meg egy érvényes számot!")

choices = ["rock", "paper", "scissors"]

player1_score = 0
player2_score = 0

for round_num in range(1, rounds + 1):
    print(f"\n{round_num}. kör:")

while True:  

    while True:
        choice1 = input("Első játékos választ (rock, paper, scissors): ").lower()
        if choice1 in choices:
            break
        else:
            print("Hiba: Csak 'rock', 'paper' vagy 'scissors' választható!")
    
    while True:
        choice2 = input("Második játékos választ (rock, paper, scissors): ").lower()
        if choice2 in choices:
            break
        else:
            print("Hiba: Csak 'rock', 'paper' vagy 'scissors' választható!")
    
    if choice1 == choice2:
        print("Döntetlen!")
        continue
    elif (choice1 == "rock" and choice2 == "scissors") or \
         (choice1 == "scissors" and choice2 == "paper") or \
         (choice1 == "paper" and choice2 == "rock"):
        print("Első játékos nyerte a kört!")
        player1_score += 1
    else:
        print("Második játékos nyerte a kört!")
        player2_score += 1
    break

print("\nJáték vége!")
if player1_score > player2_score:
    print(f"Az első játékos nyert {player1_score} ponttal!")
else:
    print(f"A második játékos nyert {player2_score} ponttal!")

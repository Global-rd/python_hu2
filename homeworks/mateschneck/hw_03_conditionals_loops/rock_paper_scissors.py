def get_valid_rounds():
    while True:
        try:
            rounds = int(input("Hány kört akartok játszani? (páratlan szám): "))
            if rounds % 2 == 1:
                return rounds
            else:
                print("Hiba: páratlan számot adj meg!")
        except ValueError:
            print("Hiba: egész számot adj meg!")

def get_valid_choice(player):
    valid_choices = ["rock", "paper", "scissors"]
    while True:
        choice = input(f"{player}, válassz (rock/paper/scissors): ").lower()
        if choice in valid_choices:
            return choice
        else:
            print("Hiba: Érvénytelen választás! Csak 'rock', 'paper' vagy 'scissors' lehet.")

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return 0
    elif (choice1 == "rock" and choice2 == "scissors") or \
         (choice1 == "scissors" and choice2 == "paper") or \
         (choice1 == "paper" and choice2 == "rock"):
        return 1
    else:
        return 2

def play_game():
    rounds = get_valid_rounds()
    score1 = 0
    score2 = 0

    for _ in range(rounds):
        print("\nÚj kör!")
        choice1 = get_valid_choice("1. játékos")
        choice2 = get_valid_choice("2. játékos")
        winner = determine_winner(choice1, choice2)

        if winner == 1:
            print("1. játékos nyerte ezt a kört!")
            score1 += 1
        elif winner == 2:
            print("2. játékos nyerte ezt a kört!")
            score2 += 1
        else:
            print("Döntetlen!")

    print("\nJáték vége!")
    if score1 > score2:
        print(f"Az 1. játékos nyert {score1} ponttal!")
    else:
        print(f"A 2. játékos nyert {score2} ponttal!")

if __name__ == "__main__":
    play_game()

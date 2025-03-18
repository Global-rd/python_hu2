# Number of rounds
while True:
    try:
        rounds = int(input("Enter the number of rounds (it must be an odd number): "))
        if rounds % 2 == 0:
            print("Failure! Enter an odd number!")
        else:
            break
    except ValueError:
        print("Failure! Enter a valid number!")

player1_score = 0
player2_score = 0

for round in range(1, rounds + 1):
    print(f"\n{round}. round")
    while True:
    # Player 1 choice   
        while True:
            player1_choice = input("Player 1 (rock, paper, scissors): ").lower()
            if player1_choice in ["rock", "paper", "scissors"]:
                break
        else:
            print("Failure: Enter a valid choice (rock, paper, scissors)!")

    # Player 2 choice
        while True:
            player2_choice = input("Player 2 (rock, paper, scissors): ").lower()
            if player2_choice in ["rock", "paper", "scissors"]:
                break
        else:
            print("Failure: Enter a valid choice (rock, paper, scissors)!")

    # Who won?
        if player1_choice == player2_choice:
            print("It's a tie! Try again!")
            continue
        elif (player1_choice == "rock" and player2_choice == "scissors") or \
             (player1_choice == "scissors" and player2_choice == "paper") or \
             (player1_choice == "paper" and player2_choice == "rock"):
            print("Player 1 wins this round!")
            player1_score += 1
        else:
            print("Player 2 wins this round!")
            player2_score += 1
        break   

# Results
print("\nGame over!")
print(f"Results of Player 1: {player1_score}")
print(f"Results of Player 2: {player2_score}")

if player1_score > player2_score:
    print("First player won!")
elif player2_score > player1_score:
    print("Second player won!")
else:
    print("It is a tie!")
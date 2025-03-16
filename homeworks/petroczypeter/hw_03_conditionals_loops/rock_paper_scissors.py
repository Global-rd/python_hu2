# Rock - Paper - Scissors game for 2 players
# 1. Ask for the number of rounds to be played from the user (needs to be odd number to prevent tie)
# 2. Players will need to enter either "rock" or "paper" or "scissors" if user enters incorrect input then ask again
# 3. Track scores, increase the winner's score after each round and declare the final winner

print("Welcome to Rock-Paper-Scissors a.k.a. kő-papír-olló!")

# Ask for the names of the players
player1_name = input("Enter Player 1's name: ").strip().title()
while player1_name == "":
    print("Error: Name cannot be empty. Please enter a valid name.")
    player1_name = input("Enter Player 1's name: ").strip().title()

player2_name = input("Enter Player 2's name: ").strip().title()
while player2_name == "":
    print("Error: Name cannot be empty. Please enter a valid name.")
    player2_name = input("Enter Player 2's name: ").strip().title()

# Ask for the number of rounds, avoid tie, so only accept odd numbers

while True:
    rounds = int(
        input("Enter the number of rounds (must be an odd number): ").strip()
    )  # so I presume the user will enter a number...

    if rounds % 2 == 1:  # Check if the number is odd
        break  # Exit loop when a valud input is given

    print(
        "Error: The number of rounds must be an odd number to avoid ties. Please try again."
    )

# Initialize player scores
player1_score = 0
player2_score = 0

print(f"GAME BEGINS! {player1_name} vs. {player2_name}")

# List of all valid hands
valid_hands = ["rock", "paper", "scissors"]

for round_number in range(1, rounds + 1):
    print(f"Round {round_number} or {rounds}:")

    player1_hand = ""
    player2_hand = ""

    # Get Player1's hand
    while True:
        player1_hand = (
            input(
                f"Dear {player1_name}, pleae enter your hand (type: 'rock' or 'paper' or 'scissors'): "
            )
            .strip()
            .lower()
        )
        if player1_hand in valid_hands:
            break
        print(
            "Error: Invalid hand, please try again (once again... please type either rock or paper or scissors)"
        )

    # Get Player2's hand
    while True:
        player2_hand = (
            input(
                f"Dear {player2_name}, pleae enter your hand (type: 'rock' or 'paper' or 'scissors'): "
            )
            .strip()
            .lower()
        )
        if player2_hand in valid_hands:
            break
        print(
            "Error: Invalid hand, please try again (once again... please type either rock or paper or scissors)"
        )

    # Now let's check who's won the round
    if player1_hand == player2_hand:
        print("Tie!")
    elif (
        (player1_hand == "rock" and player2_hand == "scissors")
        or (player1_hand == "scissors" and player2_hand == "paper")
        or (player1_hand == "paper" and player2_hand == "rock")
    ):
        print(f"{player1_name} won this round!")
        player1_score += 1
    else:
        print(f"{player2_name} won this round!")
        player2_score += 1

# Final results
print("The Final results of the game:")
print(f"{player1_name}: {player1_score} points")
print(f"{player2_name}: {player2_score} points")

# Check if there is a winner or if we need sudden death rounds
while player1_score == player2_score:
    print(
        "It's a tie! According to our tutor 'nem tudnak döntetlent játszani!' is the rule, so now we're Entering SUDDEN DEATH rounds until we have a winner!"
    )

    # Play a sudden death round
    round_number += 1
    print(f"Sudden Death Round! Round {round_number}:")

    # Get Player 1's hand again
    while True:
        player1_hand = (
            input(f"{player1_name}, enter your move (rock, paper, or scissors): ")
            .strip()
            .lower()
        )
        if player1_hand in valid_hands:
            break
        print("Error: Invalid move. Please enter 'rock', 'paper', or 'scissors'.")

    # Get Player 2's hand again
    while True:
        player2_hand = (
            input(f"{player2_name}, enter your move (rock, paper, or scissors): ")
            .strip()
            .lower()
        )
        if player2_hand in valid_hands:
            break
        print("Error: Invalid move. Please enter 'rock', 'paper', or 'scissors'.")

    # Determine the round winner
    if player1_hand == player2_hand:
        print("This round is a tie! We must continue sudden death! 🔄")
    elif (
        (player1_hand == "rock" and player2_hand == "scissors")
        or (player1_hand == "scissors" and player2_hand == "paper")
        or (player1_hand == "paper" and player2_hand == "rock")
    ):
        player1_score += 1
        print(f"{player1_name} wins the game with {player1_score} points!")
        break  # Exit sudden death
    else:
        player2_score += 1
        print(f"{player2_name} wins the game with {player2_score} points!")
        break  # Exit sudden death


if player1_score > player2_score:
    print(f"{player1_name} wins the game! Congratulations! Well fought")
else:
    print(f"{player2_name} wins the game! Congratulations! Well fought")

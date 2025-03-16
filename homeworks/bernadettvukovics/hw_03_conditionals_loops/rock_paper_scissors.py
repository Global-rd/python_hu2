import sys  # If we need exit on error

# Ask for the number of rounds (must be an odd number)
while True:
    try:
        rounds = int(input("Enter the number of rounds (must be an odd number): "))
        if rounds % 2 == 1:
            break
        print("The number of rounds must be odd!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

player1_score = 0
player2_score = 0

# Run the game
for round_num in range(1, rounds + 1):
    print(f"\n--- Round {round_num} ---")

    while True:  # This loop ensures a valid round outcome before moving to the next one
        while True:
            p1_move = input("Player 1, enter your move (rock, paper, scissors): ").strip().lower()
            if p1_move in ["rock", "paper", "scissors"]:
                break
            print("Invalid move! Please enter 'rock', 'paper', or 'scissors'.")

        while True:
            p2_move = input("Player 2, enter your move (rock, paper, scissors): ").strip().lower()
            if p2_move in ["rock", "paper", "scissors"]:
                break
            print("Invalid move! Please enter 'rock', 'paper', or 'scissors'.")

        # Determine the winner of the round
        if p1_move == p2_move:
            print("It's a tie! Play the round again.")
            continue  # Restart the round if it's a tie

        elif (p1_move == "rock" and p2_move == "scissors") or \
             (p1_move == "scissors" and p2_move == "paper") or \
             (p1_move == "paper" and p2_move == "rock"):
            print("Player 1 wins this round!")
            player1_score += 1
        else:
            print("Player 2 wins this round!")
            player2_score += 1

        break  # Exit the inner while loop only when a winner is decided

# Game over, print final results
print("\n--- Game Over ---")

if player1_score > player2_score:
    print(f"Player 1 wins with {player1_score} points!")
else:
    print(f"Player 2 wins with {player2_score} points!")
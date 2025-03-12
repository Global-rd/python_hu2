import time

#Rock, Paper, Scissors

print("Welcome to Rock, Paper, Scissors!")
time.sleep(1)
while True:
    number_of_rounds = int(input("How many rounds would you like to play? Please enter an uneven number!"))
    if number_of_rounds % 2 == 1:
        break
    else:
        print("Incorrect answer, please enter how many rounds would you like to play again! Use an uneven number!")

players = ["Player 1", "Player 2"]
answers = ["rock", "paper", "scissors"]
player_1_score = 0
player_2_score = 0
rounds = 0
while rounds < number_of_rounds:
    player_1_choice = input("Player 1, please choose from rock, paper, scissors: ").strip().lower()
    player_2_choice = input("Player 2, please choose from rock, paper, scissors: ").strip().lower()
    if player_1_choice not in answers or player_2_choice not in answers:
        print("Please choose from rock, paper, scissors.")
        continue
    if player_1_choice == player_2_choice:
        winner = "It's a tie, both players win!"
        player_1_score += 1
        player_2_score += 1
    elif player_1_choice == "rock" and player_2_choice == "scissors":
        winner = (f"{players[0]} wins!")
        player_1_score += 1
    elif player_1_choice == "paper" and player_2_choice == "rock":
        winner = (f"{players[0]} wins!")
        player_1_score += 1
    elif player_1_choice == "scissors" and player_2_choice == "paper":
        winner = (f"{players[0]} wins!")
        player_1_score += 1
    else:
        winner = (f"{players[1]} wins!")
        player_2_score += 1
    rounds += 1
    print(f"Round {rounds}: {winner} {players[0]}: {player_1_score}, {players[1]}: {player_2_score}.")
    time.sleep(1)
if player_1_score > player_2_score:
    print("Player 1 wins!")
elif player_1_score < player_2_score:
    print("Player 2 wins!")
else:
    print("It's a tie!")
time.sleep(1)
print(f"Final score: {players[0]}: {player_1_score} point(s), {players[1]}: {player_2_score} point(s).")
time.sleep(1)
print(f"Player 1 and Player 2 thank you for playing!")

valid_choices = ["rock", "paper", "scissors"]


while True:
 
        rounds = int(input("How many rounds do you want to play? (Enter an odd number): "))
        if rounds % 2 == 1:
            break
        else:
            print("Error! The number of rounds must be odd to prevent a tie!")
   

player1_score = 0
player2_score = 0


current_round = 1
while current_round <= rounds:
    print(current_round)

  
    while True:
        player1_choice = input("Player 1, enter your choice (rock, paper, scissors): ").strip().lower()
        if player1_choice in valid_choices:
            break
        else:
            print("Wrong answer! Only 'rock', 'paper', or 'scissors' are allowed!")

    while True:
        player2_choice = input("Player 2, enter your choice (rock, paper, scissors): ").strip().lower()
        if player2_choice in valid_choices:
            break
        else:
            print("Wrong answer! Only 'rock', 'paper', or 'scissors' are allowed!")

    # result
    if player1_choice == player2_choice:
        print(" It's a tie! This round will be replayed.")
        continue  
    elif (player1_choice == "rock" and player2_choice == "scissors") or \
         (player1_choice == "scissors" and player2_choice == "paper") or \
         (player1_choice == "paper" and player2_choice == "rock"):
        print("Player 1 wins this round!")
        player1_score += 1
    else:
        print("Player 2 wins this round!")
        player2_score += 1

    current_round += 1  # Only increase the round counter if there was no tie


print(" Game Over! ")
if player1_score > player2_score:
    print(f" Player 1 wins the game with a score of {player1_score} - {player2_score}!")
else:
    print(f" Player 2 wins the game with a score of {player2_score} - {player1_score}!")
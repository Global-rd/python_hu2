# homework_03_conditionals_loops, task nr.2 using "while and for loops"

# intro
print(" This is a Scissors - Paper - Rock game ")
print("****************************************")

# inputs
# make sure 1. player name is not empty

player1 = input("Enter the name of player 1 : ")
while not player1:  
    print("Error: Player 1's name cannot be empty.")
    player1 = input("Enter the name of player 1 : ")

# make sure 2. player name is not empty

player2 = input("Enter the name of player 2 : ")
while not player2:  
    print("Error: Player 2's name cannot be empty.")
    player2 = input("Enter the name of player 2 : ")

# number of rounds, make sure its not empty and it is an odd number

while True:  
    rounds_input = input("How many rounds you want to play? Please enter an odd number: ")
    if not rounds_input:
        print("Error: Number of rounds cannot be empty.")
        continue 
    try:
        rounds = int(rounds_input)
        if rounds % 2 != 0:
            break  
        else:
            print("Error: Please enter an odd number.")
    except ValueError:
        print("Error: Invalid input. Please enter a number.")

# setting start points 

player1_points = 0
player2_points = 0
played_rounds = 0
choice_allowed = ["scissors","paper","rock"]

while played_rounds < rounds:
    print(f"\nRound {played_rounds + 1}:")
    while True:
        player1_choice = input(f" {player1}, choose scissors, paper, or rock: ").lower()
        if player1_choice in choice_allowed:
            break
        else:
            print("Error: Invalid choice. Please choose scissors, paper, or rock. ")
    while True:
        player2_choice = input(f" {player2}, choose scissors, paper, or rock: ").lower()
        if player2_choice in choice_allowed:
            break
        else:
            print("Error: Invalid choice. Please choose scissors, paper, or rock. ")

    if player1_choice == player2_choice:  # player1 and player2's choice is identical
        print(f"Draw! Repeat round {played_rounds +1}.")
        continue
    elif (player1_choice == "rock" and player2_choice == "scissors") or (player1_choice == "paper" and player2_choice == "rock") or (player1_choice == "scissors" and player2_choice == "paper"): # player1 wins
        print(f" {player1} wins this round {played_rounds +1}!")
        player1_points += 1; played_rounds += 1     
    else:  # player2 wins
        print(f" {player2} wins this round {played_rounds +1}!") 
        player2_points += 1; played_rounds += 1
    
print("\nGame Over !")

if player1_points > player2_points:
    print(f" {player1} wins with {player1_points} points! {player2} had {player2_points}. ")
else:
    print(f" {player2} wins with {player2_points} points! {player1} had {player1_points}. ")

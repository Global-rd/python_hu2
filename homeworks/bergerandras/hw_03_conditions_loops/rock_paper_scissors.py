rps_rules = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

valid_inputs = ["rock", "paper", "scissors"]

rounds = int(input("Type the number of rounds you want to play: "))

while rounds / 2 == round(rounds / 2) or rounds <= 0:
    print("Invalid number of rounds!")
    rounds = int(input("Please type a number that is odd: "))
current_round = 0
while current_round < rounds:
    player_1 = input("Player 1: ")
    player_2 = input("Player 2: ")
    if player_1.lower() in valid_inputs and player_2.lower() in valid_inputs:
        if player_1.lower() == player_2.lower():
            print("Tie!")
            continue
        elif rps_rules[player_1] == player_2:
            print("Player 1 wins!")
            current_round+=1
        elif rps_rules[player_2] == player_1:
            print("Player 2 wins!")
            current_round+=1
    else:
        print("Invalid input!")

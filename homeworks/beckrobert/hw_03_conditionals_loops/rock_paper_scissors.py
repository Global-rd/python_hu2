target_round = int(input("how many rounds would you like to play? it could be only odd number"))
while target_round%2 == 0:
    print("you gave an even number. it could be only odd number!")
    target_round = int(input("how many rounds would you like to play? it could be only odd number"))

print("it's a classical rock, paper, scissors game, you can only put these inputs when choosing")
round = 0
player_1_score = 0
player_2_score = 0

while round < target_round:

    while True:
        player1_choice = input("player 1's choice: ")
        if player1_choice in ["rock", "paper", "scissors"]:
            break
        print("Invalid choice, please try again")

    while True:
        player2_choice = input("player 2's choice: ")
        if player2_choice in ["rock", "paper", "scissors"]:
            break
        print("Invalid choice, please try again")

    if player1_choice ==  player2_choice:
        print("it's a draw, choose again!")
    
    elif ((player1_choice == "paper" and player2_choice == "rock") or
          (player1_choice == "rock" and player2_choice == "scissors") or
          (player1_choice == "scissors" and player2_choice == "paper")):
        player_1_score +=1
        round+=1
        print("it's one point to, player1")
    else:
        player_2_score +=1
        round+=1
        print("it's one point to, player2") 

print(f"player 1 has {player_1_score} point(s), player 2 has {player_2_score} point(s)")
if player_1_score > player_2_score:
    print("the winner is player 1")
else:
    print("the winner is player 2")




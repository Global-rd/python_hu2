

while True:
    rounds=int(input("How many rounds do you want to play? "))
    if rounds%2==1:
        break
    else:
        print("wrong number!")


counter_1=0  #player 1 wins
counter_2=0  #player 2 wins



while True:
    counter_total=counter_1 + counter_2 
    if counter_total==rounds:
        break

    while True:
        player_1_choice=input("Player 1, please choose: rock, paper or scissors? ").lower()
        if player_1_choice in ["rock", "paper", "scissors"]:
            break
        else:
            print("Player 1, please try again!")

    while True:
        player_2_choice=input("Player 2, please choose: rock, paper or scissors? ").lower()
        if player_2_choice in ["rock", "paper", "scissors"]:
            break
        else:
            print("Player 2, please try again!")


    if player_1_choice==player_2_choice:
        print("it is a draw, do it again!") 
    elif player_1_choice=="paper" and player_2_choice=="rock":
        print("player_1 wins this round")
        counter_1 +=1
    elif player_1_choice=="rock" and player_2_choice=="scissors":
        print("player_1 wins this round")
        counter_1 +=1
    elif player_1_choice=="scissors" and player_2_choice=="paper":
        print("player_1 wins this round")
        counter_1 +=1
    else:
        print ("player_2 wins this round")
        counter_2 +=1

score=[counter_1, counter_2]  

print("end of the game")
print("-----------------------------")
if counter_1>counter_2:
    print("player 1 won the game, with the score of:", score, "")
else:
    print("player 2 won the game  with the score of:", score, "")












#bekérem a körök számát, addig amíg nem páratlan adnak meg
player_1_points = 0
player_2_points = 0
rounds = int(input("Please write down how many rounds you want to play. Be aware that you can give only odd numbers: "))
while rounds % 2 == 0:
    print("Wrong number, please enter an odd number!")
    rounds = int(input("Please write down how many rounds you want to play. Be aware that you can give only odd numbers: "))

#a megadott körök száma szerint fut a kód
for round in range(1, rounds+1):
    #bekérem a az első majd a második játékos válaszát, addig, amíg nem a megfelelőt adják meg
    while True:
        player_1 = input("Player 1 please choose on of these: Rock | Paper | Scissor: ").capitalize()
        if player_1 in  ["Rock", "Paper", "Scissor"]: 
            player_1_answer = player_1    
            break
        else:
            print("Wrong answer. Please enter: Rock | Paper | Scissor")

    while True:
        player_2 = input("Player 2 please choose on of these: Rock | Paper | Scissor: ").capitalize()
        if player_2 in ["Rock", "Paper", "Scissor"]:
            player_2_answer = player_2    
            break
        else:
            print("Wrong answer. Please enter: Rock | Paper | Scissor")

    #megnézem, hogy melyik játékos győzött és pontot ad neki  
    if (player_1_answer == "Rock" and player_2_answer == "Scissor") or (player_1_answer == "Scissor" and player_2_answer == "Paper") or (player_1_answer == "Paper" and player_2_answer == "Rock"):
        player_1_points += 1
    elif (player_2_answer == "Rock" and player_1_answer == "Scissor") or (player_2_answer == "Scissor" and player_1_answer == "Paper") or (player_2_answer == "Paper" and player_1_answer == "Rock"):
        player_2_points += 1    
    while player_1 == player_2:
        print("It's a draw, please choose again")
        player_1 = input("Player 1 please  choose on of these: Rock | Paper | Scissor: ").capitalize()
        if player_1 in  ["Rock", "Paper", "Scissor"]: 
            player_1_answer = player_1    
            player_1_points += 1
        else:
            print("Wrong answer. Please enter: Rock | Paper | Scissor")        
        player_2 = input("Player 2 please choose on of these: Rock | Paper | Scissor: ").capitalize()
        if player_2 in ["Rock", "Paper", "Scissor"]:
            player_2_answer = player_2
            player_2_points += 1 
        else:
            print("Wrong answer. Please enter: Rock | Paper | Scissor")  
            if (player_1_answer == "Rock" and player_2_answer == "Scissor") or (player_1_answer == "Scissor" and player_2_answer == "Paper") or (player_1_answer == "Paper" and player_2_answer == "Rock"):
                player_1_points += 1
            elif (player_2_answer == "Rock" and player_1_answer == "Scissor") or (player_2_answer == "Scissor" and player_1_answer == "Paper") or (player_2_answer == "Paper" and player_1_answer == "Rock"):
                player_2_points += 1       
print("---------------")

#összeadom a pontokat, hogy lássam ki nyert, és azt kiiratom
if player_1_points > player_2_points:
    print(f"Player 1 won the game! The score: {player_1_points}")
else:
    print(f"Player 2 won the game! The score: {player_2_points}")
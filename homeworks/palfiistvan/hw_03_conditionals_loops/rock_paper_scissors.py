answers = ["rock", "paper", "scissors"]
player1_score = 0
player2_score = 0

# input round
while True:
    rounds = int(input("How many rounds do we play?"))
    if rounds %2 != 0 and rounds > 1:
        break
    print("This is not good! The number of circles must be more than 1 and odd.")

print(rounds)

count = 1
while count < rounds + 1:
    while True:
        answer1 = input(f"In {count} round the Player 1's answer: ")
        if answer1 in answers:
            break

    while True:
        answer2 = input(f"In {count} round the Player 2's answer: ")
        if answer2 in answers:
            break
    
    if answer1 == answer2:
        print("Is draw, Restart!")
        continue

    print(f"In {count} round the player 1 answere is: {answer1}, and the player 2 answere is: {answer2}")

    if (answer1 == "paper" and answer2 == "rock") or (answer1 == "scissors" and answer2 == "paper") or (answer1 == "rock" and answer2 == "scissors"):
        player1_score += 1
    elif (answer2 == "paper" and answer1 == "rock") or (answer2 == "scissors" and answer1 == "paper") or (answer2 == "rock" and answer1 == "scissors"):
        player2_score += 1

    count += 1

print("Game over!")
print(f"the points of player 1: {player1_score}")
print(f"the points of player 2: {player2_score}")
print("-------------------------------------------")
if player1_score > player2_score:
    print(f"The winner is player 1 with {player1_score} points")
else:
    print(f"The winner is player 2 with {player2_score} points")
print("Congratulations!")
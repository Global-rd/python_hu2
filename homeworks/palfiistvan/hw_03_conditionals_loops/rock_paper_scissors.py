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
        answer1 = input("Player 1's answer: ")
        if answer1 in answers:
            break

    while True:
        answer2 = input("Player 2's answer: ")
        if answer2 in answers:
            break

    print(f"In {count} round the player 1 answere is: {answer1}, and the player 2 answere is: {answer2}")
    count += 1
print("Game over!")
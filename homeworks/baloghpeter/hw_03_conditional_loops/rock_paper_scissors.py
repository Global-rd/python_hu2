import random

user_name = input("Enter your name: ").title()
while True:
    user_rounds = int(input("How many rounds do you want to play? (Must be an odd number): "))
    if user_rounds % 2 == 1:
        break
    print("Please enter an odd number to ensure a winner.")

user_score = 0
computer_score = 0
rounds_played = 0


while rounds_played < user_rounds:
    print(f"\nRound {rounds_played + 1}:")

    user_choice = input("Choose (rock, paper, or scissors): ").lower()

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie! Please try again.")
        continue  

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win this round!")
        user_score += 1
    else:
        print("You lose this round!")
        computer_score += 1

    rounds_played += 1

print("\nGame Over!")
print(f"{user_name} scored {user_score} points.")
print(f"The computer scored {computer_score} points.")

if user_score > computer_score:
    print(f"Congratulations, {user_name}! You are the overall winner!")
elif user_score < computer_score:
    print("The computer wins the game!")
else:
    print("It's a tie game!")

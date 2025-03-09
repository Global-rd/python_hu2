"""
Feladat: Kő-papír-olló játék

Írj egy python programot ami levezényli a kő-papír-olló játékot két játékos között. 

A program kérje be, hogy hány kört akarnak játszani a játékosok. 

Figyelj oda, hogy olyan számot kell megadnia a felhasználónak ami mellett nem tudnak döntetlent játszani! Ha nem ilyen számot ad meg, írj ki hibaüzenetet és addig kérd be újra a körök számát amíg páratlan számot nem ad meg. 

Ezután a program felváltva kérje be az első és második játékos válaszát, ami kizárólag a következő stringek valamelyik lehet: "rock", "paper", "scissors". Ellenkező esetben kezeld úgy a hibát ahogy a körök számánál. 

Tárold a nyertesek pontjait, és minden kör végén növeld az aktuális játékos pontszámát. A végén printeld ki ki nyert, és hány ponttal.
"""

#Define the number of rounds
def get_valid_rounds():
    rounds = int(input("Please enter the number of rounds you want to play: "))
    while rounds % 2 == 0:
        print("Please enter an odd number of rounds so there can be a clear winner!")
        rounds = int(input("Please enter the number of rounds you want to play: "))
    return rounds

#Define options
def get_valid_choice(player):
    valid_choices = ["rock", "paper", "scissors"]
    while True:
        choice = input(
            f"{player}. player's choice (rock/paper/scissors): ").lower()
        if choice in valid_choices:
            return choice
        else:
            print(
                "Error: Invalid choice. Please choose from 'rock', 'paper' or 'scissors'.")

#Rules of the game
def play_round():
    while True:
        choice1 = get_valid_choice(1)
        choice2 = get_valid_choice(2)
        if choice1 == choice2:
            print("Draw! Let's play this round again.")
            continue
        if (choice1 == "rock" and choice2 == "scissors") or \
           (choice1 == "paper" and choice2 == "rock") or \
           (choice1 == "scissors" and choice2 == "paper"):
            return 1
        else:
            return 2

#The game
rounds = get_valid_rounds()
player1_score = 0
player2_score = 0
for current_round in range(1, rounds + 1):
    print(f"\n{current_round}. round:")
    winner = play_round()
    if winner == 1:
        player1_score += 1
        print("Player 1 won the round!")
    else:
        player2_score += 1
        print("Player 2 won the round!")

#Print the results
print("\nEnd of the game!")
print(f"Player 1 score: {player1_score}")
print(f"Player 2 score: {player2_score}")

#Declare the winner
if player1_score > player2_score:
    print("Player 1 won the game!")
else:
    print("Player 2 won the game!")
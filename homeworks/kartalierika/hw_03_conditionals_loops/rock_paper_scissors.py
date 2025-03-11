print("--------------------------------")
print("Let's play Rock-Paper-Scissors!")
print("--------------------------------")

while True:
    rounds = int(input("How many rounds would you like to play? It should be an odd number: "))
    if rounds % 2 == 1:
        break
    print("The number must be odd.")
   
   
points = {"Player 1": 0, "Player 2": 0}
options = ["rock", "paper", "scissors"]

for round_num in range(rounds):
    print(f"\nRound {round_num + 1}:")
    
    while True:
        p1 = input("Player 1's choice: ")
        while p1 not in options:
            print("Invalid choice! Please choose between rock, paper, or scissors.")
            p1 = input("Player 1's choice: ")
        
        p2 = input("Player 2's choice: ")
        while p2 not in options:
            print("Invalid choice! Please choose between rock, paper, or scissors.")
            p2 = input("Player 2's choice: ")
        
        if p1 != p2:
            break
        print("Draw! Please choose again.")
    
    if (p1, p2) in [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]:
        print("Player 1 wins this round!")
        points["Player 1"] += 1
    else:
        print("Player 2 wins this round!")
        points["Player 2"] += 1

if points["Player 1"] > points["Player 2"]:
    winner = "Player 1"
else:
    winner = "Player 2"

print("--------------------------------")
print(f"\nGame Over! {winner} won with: {points['Player 1']} - {points['Player 2']}")
print("--------------------------------")

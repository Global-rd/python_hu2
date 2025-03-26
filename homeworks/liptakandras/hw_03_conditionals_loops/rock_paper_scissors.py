
# HÁNY KÖRT AKARNAK JÁTSZANI?

rounds_selected_by_players = int(input("How many rounds would you like to play?"))  # biztosan számnak kell lennie


# DÖNTETLEN NEM LEHET

while rounds_selected_by_players % 2 == 0:
    rounds_selected_by_players = int(input("The game cannot be even in the end. Please enter an uneven number!"))  # ez csak szám lehet

print(f"Let's start!")


# JÁTÉKOSOK PONTOKAT KAPNAK MINDEN KÖR UTÁN

player_1_points = 0
player_2_points = 0


# A JÁTÉK A 0. KÖRTŐL INDUL

rounds = 0
    

# JÁTÉK
   
while rounds < rounds_selected_by_players:  # amint egyenlők, már nincs több kör
    
    # JÁTÉKOSOKNAK VÁLASZTANIUK KELL

    print(f"Player 1: {player_1_points} points - Player 2: {player_2_points} points")
    print(f"ROUND {rounds + 1}! Select your weapon!")

    player_1_weapon = input("Player 1, rock, Paper or scissors?").lower()  # lower az összehasonlíthatóság miatt
    while player_1_weapon not in ["rock", "paper", "scissors"]:
        player_1_weapon = input("Player 1, you must choose a valid weapon. Rock, Paper or scissors?").lower()

    player_2_weapon = input("Player 2, Rock, Paper or scissors?").lower()
    while player_2_weapon not in ["rock", "paper", "scissors"]:
        player_2_weapon = input("Player 2, you must choose a valid weapon. Rock, Paper or scissors?").lower()

    # HA NEM VALID FEGYVERT VÁLASZTOTT VALAMELYIK JÁTÉKOS

   # if player_1_weapon not in ["rock", "paper", "scissors"] or player_2_weapon not in ["rock", "paper", "scissors"]:
    #    print(f"Invalid weapon! You both have to choose rock, paper or scissors!")
    
    # HA MINDKÉT JÁTÉKOS VALID FEGYVERT VÁLASZTOTT

    print(f"Player 1 chose {player_1_weapon} and player 2 chose {player_2_weapon}")
    
    # JÁTÉK SZABÁLYOK / JÁTÉK LOGIKA

    if player_1_weapon == player_2_weapon:
        print("Draw. Let's play this round again!") # döntetlen esetén senki nem kap pontot és nem adódik hozzá egy a "rounds"-hoz
        continue  # újra kell kezdeni a kört
    elif player_1_weapon == "rock" and player_2_weapon == "scissors" or player_1_weapon == "paper" and player_2_weapon == "rock" or player_1_weapon == "scissors" and player_2_weapon == "paper":
        print(f"Point for player 1")
        player_1_points += 1
    else:
        print("Point for player 2")
        player_2_points += 1
        
    rounds += 1
    
#  HA A JÁTÉK VÉGET ÉRT:
    
if player_1_points > player_2_points:
    print(f"GAME OVER! Player 1 won by {player_1_points - player_2_points} points.")
else:
    print(f"GAME OVER! Player 2 won by {player_2_points - player_1_points} points.")
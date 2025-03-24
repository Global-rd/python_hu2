
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

    print(f"Select your weapon!")

    player_1_weapon = input("Rock, Paper or scissors?").lower()  # lower az összehasonlíthatóság miatt
    player_2_weapon = input("Rock, Paper or scissors?").lower()

    # HA NEM VALID FEGYVERT VÁLASZTOTT VALAMELYIK JÁTÉKOS

    if player_1_weapon not in ["rock", "paper", "scissors"] or player_2_weapon not in ["rock", "paper", "scissors"]:
        print(f"Invalid weapon! You both have to choose rock, paper or scissors!")

        continue  # az invalid fegyverválasztás esetén újra kell kezdeni a loopot
    
    # HA MINDKÉT JÁTÉKOS VALID FEGYVERT VÁLASZTOTT

    print(f"Player 1 chose {player_1_weapon} and player 2 chose {player_2_weapon}")
    
    # JÁTÉK SZABÁLYOK / JÁTÉK LOGIKA

    if player_1_weapon == player_2_weapon:
        print("Draw. Let's play this round again!") # döntetlen esetén senki nem kap pontot és nem adódik hozzá egy a "rounds"-hoz
        continue  # újra kell kezdeni a kört
    elif player_1_weapon == "rock" and player_2_weapon == "scissors":
        print(f"Point for player 1")
        player_1_points += 1
        rounds += 1
    elif player_1_weapon == "paper" and player_2_weapon == "rock":
        print(f"Point for player 1")
        player_1_points += 1
        rounds += 1
    elif player_1_weapon == "scissors" and player_2_weapon == "paper":
        print("Point for player 1")
        player_1_points += 1
        rounds += 1
    else:  #
        print("Point for player 2")
        player_2_points += 1
        rounds += 1
    
#  HA A JÁTÉK VÉGET ÉRT:
    
if player_1_points > player_2_points:
    print(f"Player 1 won by {player_1_points - player_2_points} points.")
else:
    print(f"Player 2 won by {player_2_points - player_1_points} points.")
import os
import time
import getpass
import pprint

def decide_winner(player_1_choice: str, player_2_choice: str):

    rules = {
        "kő": "olló",  # player_1 nyer
        "olló": "papír",  # player_1 nyer
        "papír": "kő"  # player_1 nyer
    }

    if rules[player_1_choice] == player_2_choice:
        return "player_1"
    else:
        return "player_2"

def clear_console():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:
        os.system('clear')

def get_names_n_round():
    
    game = {}
    
    game["player_1"] = input("Első játékos neve: ").strip().title()
    game["player_2"] = input("Második játékos neve: ").strip().title()

    while True:
        try:
            num_of_rounds = int(input("Körök száma: "))
            if num_of_rounds > 0 and num_of_rounds % 2 == 1:
                game["num_of_rounds"] = num_of_rounds
                break
            else:
                print("Kérlek, páratlan pozitív egész számot adj meg!")
                continue
        except ValueError:
            print("Érvénytelen bevitel! Kérlek, páratlan pozitív egész számot adj meg!")
            continue
    return game    

def show_teaser(game: dict):
    clear_console()
    print(f"Játékos 1: {game["player_1"]}")
    time.sleep(1)
    print(f"Játékos 2: {game["player_2"]}")
    time.sleep(1)
    print(f"Körök száma: {game["num_of_rounds"]}")
    time.sleep(1)
    clear_console()
    print("Induljon a játék!")
    time.sleep(1)    
    clear_console()    
    
    i = 3
    for s in range(0,3):        
        print(i)
        time.sleep(1)
        clear_console()
        i -= 1

def get_choices(game: dict):
    getpass_outstr = "add meg a választásod, majd nyomj ENTER-t: kő (\"k\"), papír (\"p\"), olló (\"o\"): "
    warn_outstr = "Kérlek a \"k\", \"p\", \"o\" betűk közül válassz (Kő: \"k\", papír: \"p\", olló: \"o\"), majd nyomj ENTER-t!"

    choice_dict = {
        "k":"kő",
        "p":"papír",
        "o":"olló"
    }
    
    while True:
        # player_1 választása
        while True:          
            player_1_choice = getpass.getpass(f"{game["player_1"]}, {getpass_outstr}")
            if player_1_choice in ["k","p","o"]:
                break
            else:
                print(warn_outstr)
                continue

        # player_2 választása
        while True:            
            player_2_choice = getpass.getpass(f"{game["player_2"]}, {getpass_outstr}")
            if player_2_choice in ["k","p","o"]:
                break
            else:
                print(warn_outstr)
                continue    

        if player_1_choice == player_2_choice:
            print(f"\nDöntetlen ({choice_dict[player_1_choice]} vs {choice_dict[player_2_choice]})! Játsszátok újra a kört!\n")
            continue
        else:
            break  

    return choice_dict[player_1_choice], choice_dict[player_2_choice]
        
def play(game: dict):  
    
    game["rounds"] = {}
    player_1_pts = 0
    player_2_pts = 0
    
    for round in range(1,game["num_of_rounds"]+1):        
        clear_console()
        print(f"Kör {round}.\n-----------------")

        player_1_choice, player_2_choice = get_choices(game)
        winner = decide_winner(player_1_choice, player_2_choice)   
        
        # elmentjük a változásokat a game dict-be
        game["rounds"][round] = {"player_1_choice":player_1_choice, "player_2_choice":player_2_choice, "winner":winner}

        if winner == "player_1":
            player_1_pts += 1
        else:
            player_2_pts += 1

        # kiírjuk a kör eredményét
        clear_console()
        print(f"{game["player_1"]} : {player_1_choice}")
        print(f"{game["player_2"]} : {player_2_choice}")
        print(f"A kör nyertese {game[winner]}!")
        time.sleep(3)

    game["player_1_pts"] = player_1_pts
    game["player_2_pts"] = player_2_pts

    if player_1_pts > player_2_pts:
        game["winner"] = f"{game["player_1"]} ({player_1_pts}:{player_2_pts})"
    else:
        game["winner"] = f"{game["player_2"]} ({player_2_pts}:{player_1_pts})"

    return game

def show_result(game: dict):
    
    clear_console()
    print(f"A játék nyertese: {game["winner"]} !!!!")
    print("\n\n\n----------------------------------------------")
    pprint.pprint(game)
    print("\n\n\n----------------------------------------------\n")




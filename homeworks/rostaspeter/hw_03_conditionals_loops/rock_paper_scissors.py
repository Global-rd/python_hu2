player1wins = 0
player2wins = 0
game = 0

matches = int(input("Hány kört szeretnétek játszani?  "))
while matches % 2 == 0 or matches < 0:
    print("Csak nullánál nagyobb, páratlan számot adhatsz meg!  ")
    matches = int(input("Hány kört szeretnétek játszani?  "))

while True:
    game += 1
    print(f"\n{game}. meccs kezdődik!")

    player1 = input("Első játékos választása  ")
    while player1 not in ["rock", "paper", "scissors"]:
        print("A választási lehetőségek: rock, paper or scissors!")
        player1 = input("Első játékos választása  ")

    player2 = input("Második játékos választása  ")
    while player2 not in ["rock", "paper", "scissors"]:
        print("A választási lehetőségek: rock, paper or scissors!")
        player2 = input("Második játékos választása  ")

    if player1 == player2:
        print("Döntetlen!")
        game -= 1
        continue

    if (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
        player1wins += 1
        print(f"Első játékos kapja a pontot! Az állás: {player1wins}:{player2wins}")
    else:
        player2wins += 1
        print(f"Második játékos kapja a pontot! Az állás: {player1wins}:{player2wins}")

    if (player1wins > matches / 2) or (game == matches and player1wins > player2wins):
        print("\nElső játékos nyert!")
        break
    elif (player2wins > matches / 2) or (game == matches and player1wins < player2wins):
        print("\nMásodik játékos nyert!")
        break

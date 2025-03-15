
while True:
    try:
        rounds = int(input("Körök száma? (Páratlan számot adj meg!): "))
        if rounds % 2 == 1:
            break
        else:
            print("Páratlan számot adj meg!")
    except ValueError:
        print("Egész számot adj meg!")

player1_score = 0
player2_score = 0

for _ in range(rounds):
    print("\nÚj kör!")
    while True:
        while True:
            player1_choice = input("1. játékos, válassz (kő, papír, olló): ")
            if player1_choice in ["kő", "papír", "olló"]:
                break
            else:
                print("Hiba: Csak 'kő', 'papír' vagy 'olló' lehet a választás!")
    
        while True:
            player2_choice = input("2. játékos, válassz (kő, papír, olló): ")
            if player2_choice in ["kő", "papír", "olló"]:
                break
            else:
                print("Hiba: Csak 'kő', 'papír' vagy 'olló' lehet a választás!")

        if player1_choice == player2_choice:
            print("Döntetlen")
            continue
        elif (player1_choice == "kő" and player2_choice == "olló") or \
         (player1_choice == "olló" and player2_choice == "papír") or \
         (player1_choice == "papír" and player2_choice == "kő"):
            print("Nyert az 1. játékos!")
        player1_score += 1
    else:
        print("Nyert a 2. játékos!")
        player2_score += 1
    break
print("\nVége")
if player1_score > player2_score:
    print(f"1. játékos nyert {player1_score} - {player2_score}-ra!")
else:
    print(f"2. játékos nyert {player2_score} - {player1_score}-ra!")

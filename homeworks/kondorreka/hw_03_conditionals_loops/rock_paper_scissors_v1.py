'''Feladat 2: while és for loop használata
Hozz létre egy rock_paper_scissors.py nevű file-t, és kódold le a következő feladat
megoldását:
Írj egy python programot ami levezényli a kő-papír-olló játékot két játékos között. A
program kérje be, hogy hány kört akarnak játszani a játékosok. Figyelj oda, hogy
olyan számot kell megadnia a felhasználónak ami mellett nem tudnak döntetlent
játszani! Ha nem ilyen számot ad meg, írj ki hibaüzenetet és addig kérd be újra a
körök számát amíg páratlan számot nem ad meg. Ezután a program felváltva kérje
be az első és második játékos válaszát, ami kizárólag a következő stringek
valamelyik lehet: "rock", "paper", "scissors". Ellenkező esetben kezeld úgy a hibát
ahogy a körök számánál. Tárold a nyertesek pontjait, és minden kör végén növeld
az aktuális játékos pontszámát. A végén printeld ki ki nyert, és hány ponttal.'''

 

while True:

    try:

        round = int(input('Hány kört szeretnétek játszani?\n'
                           'Páratlan számot adj meg, hogy ne legyen döntetlen!\n'))

        if round <= 0:
            print(f'Vicces! A körök száma nem lehet negatív vagy 0.')        

        elif round % 2 == 0:
            print('A körök számának páratlannak kell lennie!\n'
                  'Nem tudnám elviselni ha nem derül ki, hogy ki a jobb.\n')

        else:
            print(f'Akkor hajrá, {round} kört fogtok játszani.\n'
                  'Győzzön a jobbik!\n')
            break

    except ValueError:
        print('Légyszi numerikus értéket adj meg!')  

#A játékosok kezdő pontjai      
score1 = 0
score2 = 0

#Elfogadott értékek
accepted = ["rock", "paper", "scissors"]

#Játszott körök száma
played_rounds = 1

while played_rounds <= round:
 
    while True:
        tip1 = input('1. játékos: "rock", "paper", "scissors"? ').strip().lower()

        if tip1 in accepted:
           break
        print("1. játékos helyesen írd be a tippet!")

    while True:
        tip2 = input('2. játékos: "rock", "paper", "scissors"? ')

        if tip2 in accepted:
            break

        print("2. játékos helyesen írd be a tippet!")

    print(f'{tip1} vs. {tip2}')

    if tip1 == tip2:
        print(f'{played_rounds}. kör: Döntetlen!')
        played_rounds += 1

    elif tip1 == "rock" and tip2 == "scissors":
        score1 += 1
        print(f'{played_rounds}. kör: 1. játékos nyert!')
        played_rounds += 1
    
    elif tip1 == "scissors" and tip2 == "paper":
        score1 += 1
        print(f'{played_rounds}. kör: 1. játékos nyert!')
        played_rounds += 1

    elif tip1 == "paper" and tip2 == "rock":
        score1 += 1
        print(f'{played_rounds}. kör: 1. játékos nyert!')
        played_rounds += 1

    else:
        score2 += 1
        print(f'{played_rounds}. kör: 2. játékos nyert!')
        played_rounds += 1

while score1 == score2:
    print("Döntetlen. Egy extra kör követezik!")

    while True:
        tip1 = input('1. játékos: "rock", "paper", "scissors"? ').strip().lower()

        if tip1 in accepted:
           break
        print("1. játékos helyesen írd be a tippet!")

    while True:
        tip2 = input('2. játékos: "rock", "paper", "scissors"? ')

        if tip2 in accepted:
            break

        print("2. játékos helyesen írd be a tippet!")

    print(f'{tip1} vs. {tip2}')

    if tip1 == tip2:
        print(f'{played_rounds}. kör: Döntetlen!')
        played_rounds += 1

    elif tip1 == "rock" and tip2 == "scissors":
        score1 += 1
        print(f'{played_rounds}. kör: 1. játékos nyert!')
        played_rounds += 1
    
    elif tip1 == "scissors" and tip2 == "paper":
        score1 += 1
        print(f'{played_rounds}. kör: 1. játékos nyert!')
        played_rounds += 1

    elif tip1 == "paper" and tip2 == "rock":
        score1 += 1
        print(f'{played_rounds}. kör: 1. játékos nyert!')
        played_rounds += 1

    else:
        score2 += 1
        print(f'{played_rounds}. kör: 2. játékos nyert!')
        played_rounds += 1

if score1 > score2:
    print(f'{score1}:{score2} --> A győztes az 1. játékos!')

else:
    print(f'{score2}:{score1} --> A győztes az 2. játékos!')


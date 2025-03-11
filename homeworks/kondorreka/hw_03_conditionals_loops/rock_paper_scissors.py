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

#Tippek bekérése és ellenőrzése
def tip(player_num):

    accepted = ["rock", "paper", "scissors"] #Elfogadott értékek
    while True:
            tip = input(f'{player_num}. játékos: "rock", "paper", "scissors"? ').strip().lower()

            if tip in accepted:
                break

            else:
                print(f'{player_num}. játékos helyesen add meg az tipped!')
    return(tip)
#-------------------------------------------------------------------
def game(tip1, tip2, played_rounds):
    """
    tippek ellenőrzése, melyik játékos kapja a pontot
    """

    flag = None

    if tip1 == tip2:
        flag = 0
        print(f'{played_rounds}. kör: {tip1} vs. {tip2}, Döntetlen. Ezt nem veszem figyelembe, játszátok újra a kört.')
        

    elif (tip1 == "rock" and tip2 == "scissors") or (tip1 == "scissors" and tip2 == "paper") or (tip1 == "paper" and tip2 == "rock"):
        flag = 1
        print(f'{played_rounds}. kör: {tip1} vs. {tip2}, 1. játékos nyert!')
        
    else:
        flag = 2
        print(f'{played_rounds}. kör: {tip1} vs. {tip2}, 2. játékos nyert!')

    return(flag)

#-------------------------------------------------------------------

while True:

    try:

        rounds = int(input('Hány kört szeretnétek játszani?\n'
                           'Páratlan számot adj meg, hogy ne legyen döntetlen!\n'))

        if rounds <= 0:
            print(f'Vicces! A körök száma nem lehet negatív vagy 0.')        

        elif rounds % 2 == 0:
            print('A körök számának páratlannak kell lennie!\n'
                  'Nem tudnám elviselni ha nem derülne ki, hogy ki a jobb.\n')

        else:
            print(f'Akkor hajrá, {round} kört fogtok játszani.\n'
                  'Győzzön a jobbik!\n')
            break

    except ValueError:
        print('Légyszi numerikus értéket adj meg!')  

#A játékosok kezdő pontjai      
score1 = 0
score2 = 0

#Játszott körök száma
played_rounds = 1

# tip1 = tip(1)
# tip2 = tip(2)

while played_rounds <= rounds:
    tip1 = tip(1)
    tip2 = tip(2)
    flag = game(tip1, tip2, played_rounds)

    if flag == 1:
        score1 += 1
    elif flag == 2:
        score2 += 1
    else:
        played_rounds += -1 #ha döntetlen, akkor ne nőjjön a játszott körök száma
    
    print(f'A jelenlegi állás: {score1} : {score2}')
    print('--------------------------------------------------')

    played_rounds += 1

# while score1 == score2:
#     print("Döntetlen. Egy extra kör követezik!")

#     tip1 = tip(1)
#     tip2 = tip(2)
#     flag = game(tip1, tip2, played_rounds)

#     if flag == 1:
#         score1 += 1
#     elif flag == 2:
#         score2 += 1
        
#     print('--------------------------------------------------')
#     played_rounds += 1

if score1 > score2:
    print(f'A végeredmény: {score1}:{score2} az 1. játékos javára! Gratulálok 1. játékos!!!')

else:
    print(f'A végeredmény: {score2}:{score1} a 2. játékos javára! Gratulálok 2. játékos!!!')


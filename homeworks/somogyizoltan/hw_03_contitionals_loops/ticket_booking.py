"""
Ebben a házi feladatban egy mozi helyfoglaló rendszerének egy egyszerűsített
változatát kell lefejlesztened. A fehasználónak képesnek kell lennie kiválasztani
melyik filmre szeretne helyet (vagy helyeket) foglalni. Egy 5x5-ös mátrixban (list of
lists) látnia kell mely helyek szabadok, és ezekből le kell tudnia foglalni azt a jegy
mennyiséget amennyit szeretne. A feladathoz segítséget nyújtanak a következő
pontok:
● Készíts egy tetszőleges listát a kedvenc filmjeiddel.
● Ezután kérd be a felhasználótól a film nevét amire szeretne jegy(eket) foglalni.
Amennyiben a film nincs a listádban, addig kérdezd a felhasználót amíg egy
olyan filmet nem választ ami szerepel az előre definiált filmek között.
● Készíts egy 2 dimenziós listát (list of lists) amely 5 sort és 5 oszlopot
reprezentál.Állítsd minden értéket 0-ra, ezek fogják a szabad helyeket
jelenteni.
● Használj egy nested for loopot hogy ezt ki is printeld a felhasználónak.
● Kérdezd meg a felhasználót, hogy hány jegyet szeretne vásárolni.
● Ezután minden jegynek a sor és oszlopszámát kérd be tőle. Amennyiben ez
egy valid oszlop és sor szám (nem kisebb vagy nagyobb mint az elérhető
számok, és nem foglalt még a hely), tárold el a foglalást, és frissítsd a
terminálban az üléseket (printeld ki minden iterációban amikor egy foglalás
megtörténik). Kerüljön 1-es a lefoglalt helyre.
● Biztosítsd, hogy nem foglal több jegyet a felhasználó mint amennyit
eredetileg kért.
Ha végzett, printelj ki egy összegzést a lefoglalt jegyekről.
"""

my_films = ["Avatar", "Aranyhaj", "A profi", "Star Wars - Ébredő erő", "King Kong", "Trója", "Valami Amerika", "Tarzan"]

while True:
    film_choise = input("Melyik filmre szeretnél jegyet venni: ")
    if film_choise in my_films:
        break
    else:
        print(f"Ez a film {film_choise} nincs a választható filmek között. Válassz másikat")

chairs = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

print("SOR/SZÉK   1  2  3  4  5")
print("   ")       # Elválasztó sor nyomtatása
for i in range(1, 6):
    row_str = "   "
    for j in range(1, 6):
        row_str += str(chairs[i-1][j-1]) + "  "
    
    print(f"{i}       {row_str}")


print("A fenti táblázatban a 0 az üres helyeket jelenti.")
print("A vászonhoz legközelebb az 1-es sor van.")
print("     ")

numbers_of_ticket = int(input("Add meg, hogy mennyi jegyet szeretnél venni: "))

actual_ticket = 1

# Ha több jegyet vesznek, azt egy listben eltárolom
act_row = [] 
act_col = []
for n in range(0, numbers_of_ticket):
    act_row.append(0)
    act_col.append(0)

while actual_ticket <= numbers_of_ticket:
    while True:
        print(f"Add meg az {actual_ticket} jegy foglalásához a pontos ülőhelyet: ")
        act_row[actual_ticket-1] = int(input("Melyik sorban szeretnél ülni (1-5): "))
        act_col[actual_ticket-1] = int(input("Add meg melyik széken szeretnél ülni (1-5): "))

        if act_row[actual_ticket-1] in range(1,6) and act_col[actual_ticket-1] in range(1, 6): 
            if chairs[act_row[actual_ticket-1]-1][act_col[actual_ticket-1]-1] == 0:
                # Minden rendben van, a szék üres és a megfelelő sor és oszlop száma volt megadva, lefoglalni a helyet és tovább menni
                chairs[act_row[actual_ticket-1]-1][act_col[actual_ticket-1]-1] += 1
                actual_ticket += 1
                break
            else:
                print("Sajnos ez a hely már foglalt! Válassz másikat!")
        else:
            # Sor és szék nem stimmel, hiba és újra bekérni az sort és széket
            print("Rossz számokat adtál meg az előbb! Kérlek add meg újra egy és öt között!")


print(f"A megrendelés az {film_choise} c. filmre kész.")
print(f"Összesen {numbers_of_ticket} darab jegyet rendeltél.")
for n in range(0, numbers_of_ticket):
    print(f"Ezekre a helyekre: {act_row[n]} sorban {act_col[n]} széken")

print("     ")
print("A terem aktuális foglalási táblázata:")
print("SOR/SZÉK   1  2  3  4  5")
print("   ")       # Elválasztó sor nyomtatása
for i in range(1, 6):
    row_str = "   "
    for j in range(1, 6):
        row_str += str(chairs[i-1][j-1]) + "  "
    
    print(f"{i}       {row_str}")
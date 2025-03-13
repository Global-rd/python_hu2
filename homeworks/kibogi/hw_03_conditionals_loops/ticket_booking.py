movies =["Casablanca", "IT", "Taxi", "Alien"] #Készíts egy tetszőleges listát a kedvenc filmjeiddel.

selectedmovie = str()

"""Ezután kérd be a felhasználótól a film nevét amire szeretne jegy(eket) foglalni.
Amennyiben a film nincs a listádban, addig kérdezd a felhasználót amíg egy
olyan filmet nem választ ami szerepel az előre definiált filmek között."""

while selectedmovie not in movies: 
    selectedmovie = input ("Melyik filmre szertél helyet foglalni?")

    if selectedmovie not in movies:
        print ("Ezt a filmet nem játszuk.")

"""Készíts egy 2 dimenziós listát (list of lists) amely 5 sort és 5 oszlopot
reprezentál.Állítsd minden értéket 0-ra, ezek fogják a szabad helyeket
jelenteni."""

seats = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
] 

"""Használj egy nested for loopot hogy ezt ki is printeld a felhasználónak."""

for row in seats:
    for seat in row:
        print (seat, end=" ")
    print()

numberoftickets = int(input("Hány jegyet szeretnél vásárolni? ")) #Kérdezd meg a felhasználót, hogy hány jegyet szeretne vásárolni.

bookings = [] #Változo az összegzésnek

"""Ezután minden jegynek a sor és oszlopszámát kérd be tőle. Amennyiben ez
egy valid oszlop és sor szám (nem kisebb vagy nagyobb mint az elérhető
számok, és nem foglalt még a hely), tárold el a foglalást, és frissítsd a
terminálban az üléseket (printeld ki minden iterációban amikor egy foglalás
megtörténik). Kerüljön 1-es a lefoglalt helyre."""

for i in range(numberoftickets): #Biztosítsd, hogy nem foglal több jegyet a felhasználó mint amennyit eredetileg kért.
    currentticket = i + 1
    
    seatavailable = False

    while seatavailable == False:
        selectedrow = 0
        selectedseat = 0
        while selectedrow == 0:
            selectedrow = int(input(f"Hányadik sorban legyen az {currentticket}. hely? "))

            if selectedrow in range(1,6):
                break
            else:
                selectedrow = 0
                print ("Ez a sor nem létezik. ")

        while selectedseat == 0:
            selectedseat = int(input(f"Hányadik helyet kéred az {selectedrow}. sorban? "))

            if selectedseat in range (1,6):
                break
            else:
                selectedseat = 0
                print ("Ez a hely nem létezik. ")

        if seats[selectedrow-1][selectedseat-1] == 0:
            seatavailable = True
            seats[selectedrow-1][selectedseat-1] = 1

            currentbooking = [selectedrow, selectedseat]
            bookings.append(currentbooking)

            for row in seats:
                for seat in row:
                    print (seat, end=" ")
                print()
            break
        else:
            print("Ez a hely már foglalt. ")


print(f"Köszönjük a foglalásodat. Ezeked a helyeket foglaltad le a {selectedmovie} cimü filmre:") #Ha végzett, printelj ki egy összegzést a lefoglalt jegyekről.
i = 1
for ticket in bookings:
    print (f"{i}. jegy: {ticket[0]}. sor, {ticket[1]}. hely.")
    i += 1
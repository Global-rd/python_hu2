# filmek listája
list_of_movies = ["Star Wars", "Harry Potter", "Lord Of The Rings", "Matrix", "Pirates Of The Caribbean", "Transporter", "Mission Impossible"]

# az 5x5-ös 2 dimenziós lista a szabad helyekről
available_tickets = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]
# meghatározzuk a nem foglalt jegyeket
nonbooked = 0

# bontsuk szét a listák listáját hogy számolható legyen
for inner_list in available_tickets:
    for numbers in inner_list:
        if numbers == 0:
            nonbooked += 1


# meghatározzuk a film változóját, amibe bekérünk
movie = ""

# addig kérdezzük, ameddig a listán szereplő filmek valamelyikét nem választja
while movie not in list_of_movies:
    movie = input("What movie do you want to watch?").title()
    if movie not in list_of_movies:
        print(f"{movie} is not available in the cinema right now, sorry!")

# kiprinteljük, mennyi szabad jegy van a filmre
print(f"We have {nonbooked} available tickets for {movie} now!")

# üres változóban mentjük el a később bekérendő foglalási darabszámot
number_of_tickets = 0

# nested loopban meghatározzuk a feltételeket, hogy a megfelelő számó jegyet lehessen megvásárolni, 0-nál nagyobb számot adjon meg és ne adhasson meg többet, mint amennyi rendelkezésre áll
while number_of_tickets > nonbooked or number_of_tickets <= 0:
    number_of_tickets = int(input("How many tickets do you want to book?"))
    if number_of_tickets > nonbooked:
        print(f"Sorry, but we have only {nonbooked} available tickets for {movie} now!")
    elif number_of_tickets <= 0:
        print("You have to enter a positive number!")
    else:
        for row in available_tickets:     # megfelelő szám esetén kiprinteljük a kód elején meghatározott 2d listát az eredeti (row) formájában
            print(row)
        print(f"Please choose {number_of_tickets} seats from the listed above!")  # a jegyeknek megfelelő számú székek lefoglalása

#-------- ezt követően a chatgpt oldotta meg a feladatot, nem akartam félbehagyni, de innentől nem teljesen világos (ezt a try,except dolgot ha jól tudom, nemis vettük még)---------
booked_seats = 0
# most bekérjük, melyik székeket (melyik oszlop, melyik sor) akarja lefoglalni, ha a megvett jegyeknél többet, hiba kiírása
while booked_seats < number_of_tickets:

    seat = input(f"Please enter the seat number you want to book (row, column): ")

    # Érvényesítjük, hogy a bevitt adat helyes formátumú és a szék szabad-e
    try:
        row, col = map(int, seat.split(','))  # a bemeneti adatokat sorra és oszlopra bontjuk
        row -= 1  # a felhasználó 1-től számolja a sorokat, mi viszont 0-tól
        col -= 1  # a felhasználó 1-től számolja az oszlopokat, mi viszont 0-tól

        # ellenőrizzük, hogy a megadott hely a megfelelő tartományban van-e, és hogy a hely szabad-e
        if 0 <= row < len(available_tickets) and 0 <= col < len(available_tickets[row]) and available_tickets[row][col] == 0:
            # Ha szabad, lefoglaljuk
            available_tickets[row][col] = 1
            booked_seats += 1
            print(f"Seat {seat} has been successfully booked!")
        else:
            print(f"Sorry, seat {seat} is already taken or invalid. Please try again.")

    except ValueError:
        print("Invalid input. Please enter the seat as row,column (e.g., 1,3).")

# A jegyek sikeres foglalása után kiíratjuk az új jegyállapotot
print("\nUpdated seat availability:")
for row in available_tickets:
    print(row)

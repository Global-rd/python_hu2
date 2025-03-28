
#bekérem hogy melyik filmet akarja nézni
movies = ["Lotr", "Terminator", "Predator"]
want_to_see = input(f"These are the available movies {movies}, please choose one: ").capitalize()
while want_to_see not in movies:
    print("Wrong answer, please choose another movie!")
    want_to_see = input(f"These are the available movies {movies}, please choose one: ").capitalize()

#elérhető ülések
print("Available seats represent the '0' the taken seats represent '1'. Here is the list:")
available_seats = [
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
for seats in available_seats:
    print(seats)

#bekérem hány jegyet akar venni, és hogy hova szeretne
ticket_number = int(input("How many tickets do you want to buy?: "))

#bekérem a sor és oszlop számot
for round in range(1, ticket_number + 1):
    row_number = int(input("Please give me the row of the seat: "))
    while (row_number == 0) or (row_number >= 6):
        print("Please give a valid number")
        row_number = int(input("Please give me the row of the seat: "))
    column_number = int(input("Please give me the column of the seat: "))
    while (column_number == 0) or (column_number >= 6):
        print("Please give a valid number")
        column_number = int(input("Please give me the column of the seat: "))
    #elvonok egyet a megadott számból, a felhasználó kénylme érdekében, hogy ne keljen eltolnia 1el a számokat
    row_number = row_number - 1
    column_number = column_number - 1 

    while available_seats[row_number][column_number] == "1":
        print("Please choose another seat, this one is already taken")
        row_number = int(input("Please give me the row of the seat: "))
        column_number = int(input("Please give me the column of the seat: "))
        row_number = row_number - 1
        column_number = column_number - 1
    else:
        available_seats[row_number][column_number] = "1"
        for seats in available_seats:
            print(seats)    

print("You have succesfully booked the seat(s)")
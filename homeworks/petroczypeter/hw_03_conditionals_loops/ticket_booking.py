print("Welcome to our little Cinema!")

# Define available movies
movies = [
    "The Dark Knight",
    "Lock, Stock and Two Smoking Barrels",
    "RocknRolla",
    "The Gentlemen",
]

# Assign a 5x5 room for each movie ( let's presume that there is only one show for each movie
# otherwise I cannot solve this task :D )
rooms = {}

for movie in movies:  # Loop through each movie
    room = []  # Create a 5x5 grid for the movie
    for i in range(5):  # create rows
        row = []
        for j in range(5):  # create columns (these will be the seats)
            row.append(0)  # Fill with zero (so all seats are initially available)
        room.append(row)  # Add the row to the grid
    rooms[movie] = room  # Store the grid in the dictionary

# Ask the user to select a movie
print("The list of the movies that you can chose from:")
for movie in movies:
    print(f"- {movie}")

while True:
    selected_movie = input(
        "Enter the title of the movie you want to book tickets for: "
    ).strip()

    if selected_movie.lower() in [movie.lower() for movie in movies]:
        break  # valid selection

    print(
        "Error: This moview is not available, or you had a typo... please select a movie form the list."
    )
    print("The list of the movies that you can chose from:")
    for movie in movies:
        print(f"- {movie}")

# Find the correct title case version from the list
for movie in movies:
    if selected_movie.lower() == movie.lower():
        selected_movie = movie  # Restore original formatting

print(f"You have selected: {selected_movie}. Great choice!")

print(
    f"Seating for {selected_movie} (0 = means the seat is available, 1 = means the seat is booked:"
)
for row in rooms[selected_movie]:
    print(row)

# Ask the user how many tickets she/he wants
while True:
    tickets = int(
        input(
            "Enter the number of tickets you'd like to buy (number should be between 1-25): "
        ).strip()
    )
    if 1 <= tickets <= 25:
        break
    print("Error: Please enter a valid number of tickets (between 1-25).")

print("Let's choose seat!" if tickets == 1 else "Let's choose your seats!")

booked_seats = []

for ticket in range(tickets):  # looping through each ticket
    while True:
        print(f"Select seat {ticket +1} of {tickets}: ")

        row = int(input("Enter the row number (0-4): ").strip())
        column = int(input("Enter the column number (0-4): ").strip())

        # Validate row & column are within range
        if 0 <= row < 5 and 0 <= column < 5:
            if rooms[selected_movie][row][column] == 0:  # if the seat is available
                rooms[selected_movie][row][column] = 1  # then flag it as booked
                booked_seats.append((row, column))  # append the list
                break  # Exit loop
            else:
                print("This seat is booked. Please choose another one.")
        else:
            print("Invalid seat selection. Choose a row and column between 0-4.")

    # showing the newly booked room
    print("Updated seating in the room")
    for row in rooms[selected_movie]:
        print(row)

# print out the booking summary
print("Booking summary")
print(f"Movie: {selected_movie}")
print(f"Booked {'Seat' if tickets == 1 else 'Seats'}:")

for seat in booked_seats:
    print(f" - Row {seat[0]}, Column {seat[1]}")

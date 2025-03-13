# Favourite movies
films = ["TopGun1", "TopGun2", "LordOfRings1", "LordOfRings2", "Airplane!"]

# choose a movie    
while True:
    selected_film = input("Which film do you want to book tickets for? ").strip()
    if selected_film in films:
        break
    else:
        print("Error: The film you specified is not in the list. Choose another movie!")

# 5x5 matrix with 0s    
seats = [[0 for _ in range(5)] for _ in range(5)]

# Show the matrix   
print("free places (0 = free, 1 = occupied):")
for row in seats:
    print(" ".join(map(str, row)))

# enter the number of tickets
while True:
    try:
        num_tickets = int(input("Enter the number of tickets (1-25): "))
        if 0 < num_tickets <= 25:
            break
        else:
            print("Error, enter a number between 1 and 25!")
    except ValueError:
        print("Error, enter a valid number!")

# booking of tickets
for ticket in range(num_tickets):
    while True:
        try:
            row = int(input(f"Enter {ticket + 1}. ticket's row number (0-4): "))
            col = int(input(f"Enter {ticket + 1}. ticket's column number (0-4): "))
            if 0 <= row < 5 and 0 <= col < 5:
                if seats[row][col] == 0:
                    seats[row][col] = 1
                    break
                else:
                    print("Error: The seat is already taken!")
            else:
                print("Error, enter a number between 0 and 4!")
        except ValueError:
            print("Error, enter a valid number!")

    # Matrix update
    print("updated places (0 = free, 1 = occupied):")
    for row in seats:
        print(" ".join(map(str, row)))

# summary   
print("\nSummary:")
print(f"Movie: {selected_film}")
print(f"Number of tickets: {num_tickets}")
print("reserved seats:")
for i in range(5):
    for j in range(5):
        if seats[i][j] == 1:
            print(f"row: {i}, column: {j}") 
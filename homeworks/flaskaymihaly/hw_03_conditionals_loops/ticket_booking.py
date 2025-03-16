
movie_choices=["shallow", "sonic", "avatar"]
print("Select from the following movies: Shallow, Sonic, Avatar")

while True:
    pick=(input("What movie do you select? ")).lower()
    if pick in movie_choices:
        break
    else:
        print("The movie you selected is not available, please pick another movie from: Shallow, Sonic, Avatar!")


print("-------------------------------")
print(f"available seats for {pick.title()}:")
available_seats = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

#------------------------------------------------------------------------------
while True:
    ticket_amount=int(input("How many tickets would you like to reserve?"))
    if ticket_amount<=25:
        print(f"Thank you for specifying the number of tickets that you reserve ({ticket_amount})")
        break
    else:
        print("Sorry we only have a total of 25 seats available!")
print("------------------------------------------------------------------------")
counter=0
while True:
    if counter==ticket_amount:
        print("We have reserved the above seats for you! ")
        break
    else:
        seat_location=input("which row and which seat number do you prefer? Give us two numbers respectively, divided by a comma: ").split(",")
        seat_location_id=list(map(int, seat_location))   
        
        seat_row = seat_location_id[0]-1
        seat_number = seat_location_id[1]-1

    if 0 <= seat_row <= 4 and 0 <= seat_number <= 4:
        print("We have that seat in our cinema")
        if available_seats[seat_row][seat_number]==0:
            print("and it is available to reserve")
            available_seats[seat_row][seat_number]=1
            counter +=1

        else:
            print("that seat is already taken. Please choose another one.")
    else:
        print("We only have 5 rows with 5 seats in each row. please choose accordingly")
    print("-------------------------------------------------------------------------------------------------")            
    print(available_seats)
    
   
    





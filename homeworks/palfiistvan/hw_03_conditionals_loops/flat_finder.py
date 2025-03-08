# Sarah rent apartment if location is "New York" or "San Fransisco" and the rent < 4000 USD
# if place is "Washington" she should not rent apartment
# if place is "Chicago" and rent > 4000 USD she rent apartment
# else place is anywhere and rent < 3000 USD she rent apartment

place = input("Please enter the place: ")
rent  = int(input("Please enter the rent [USD]: "))

print(rent < 4000)
print(place == "New York" or place == "San Fransisco") 

if place == "Chicago":
    print(f"Sarah will rent the apartment in {place} for {rent}")

elif rent < 3000 and place != "Washington":
    print(f"Sarah will rent the apartment in {place} for {rent}")

elif (rent < 4000) and (place == "New York" or place == "San Fransisco"):
    print(f"Sarah will rent the apartment in {place} for {rent}")

else:
    print(f"Sarah will not rent the apartment in {place} for {rent}")
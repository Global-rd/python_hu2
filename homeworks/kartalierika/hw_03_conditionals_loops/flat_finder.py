while not (city := input("Enter a city: ").strip().title()):
    print("City is not valid. Please enter a city.")

try:
    rental = int(input("Rental price per month (in USD): "))
except ValueError:
    print("Please enter a valid number.")
    exit()


if city in ('New York', 'San Francisco') and rental < 4000:
    print(f"Sarah can move to {city}.")
elif city == 'Washington':
    print(f"Sarah can't move to {city}.")
elif city == 'Chicago':
    print(f"Sarah can move to {city}.")
elif rental <= 3000:
    print(f"Sarah can move to {city}.")
else:
    print(f"Sarah can't move to {city}.")


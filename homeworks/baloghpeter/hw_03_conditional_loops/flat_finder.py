
city = input("Please enter the city: ").strip().title()


if city == "Washington":
    print("I not found a new flat.")
elif city == "Chicago":
    print("I found your dream flat.")
else:
    budget = int(input("Please enter your maximum budget (USD): "))
    if city == "New_York" or city == "Chicago" and budget <= 4000:
        print(f"I found some flats in {city} to {budget} (USD)")
    elif budget > 4000:
        print(f"I not a found flat in {city} to {budget} (USD)")
    elif budget <= 3000:
        print(f"I found some flats in {city} to {budget} (USD)")
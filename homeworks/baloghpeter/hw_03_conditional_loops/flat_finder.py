
city = input("Please enter the city: ").strip().title()


if city == "Washington":
    print("I not found a new flat.")
elif city == "Chicago":
    print("I found your dream flat.")
else:
    budget = int(input("Please enter your maximum budget (USD): "))
    if city in["New_York", "Chicago"] and budget <= 4000:
        print(f"I found some flats in {city} to {budget} (USD)")
    elif budget > 4000:
        print(f"I not found a flat in {city} to {budget} (USD)")
    elif budget <= 3000:
        print(f"I found one flat in {city} to {budget} (USD)")
    else:
        print("Error")
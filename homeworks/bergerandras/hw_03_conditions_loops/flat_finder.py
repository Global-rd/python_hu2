city = input("Type a city: ")

if city.lower() == "chicago":
    print(f"{city} is perfect!")
elif city.lower() == "washington":
    print(f"{city} is not suitable!")
else:
    rent_cost = int(input("Type the rent in USD: "))
    if city.lower() == "new york" or city.lower() == "san fransisco" and rent_cost < 4000:
        print(f"{city} is suitable!")
    elif rent_cost <= 3000:
        print(f"{city} is ideal!")
    else:
        print(f"{city} is too expensive! It is {rent_cost} USD")
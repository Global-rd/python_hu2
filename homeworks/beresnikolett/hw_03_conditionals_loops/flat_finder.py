#Ideal:
#1. Chicago
#Second best:
#2. New York for < 4000 Usd
#3. San Francisco for < 4000 Usd
#No go:
#1. Washington
#If not Chicago, New York, San Francisco or Washington, then:
# =< 3000 Usd

city = input("Where is the flat located? ").capitalize().strip()

if city == "Chicago":
    rent_price = int(input("What is the rent price? "))
    print(f"Yay! You can move in your dream city, {city} for {rent_price:.2f} $ rent/month.")
elif city == "New York" or city == "San Francisco":
    rent_price = int(input("What is the rent price? "))
    if rent_price < 4000:
        print(f"Great choice! {city} is a wonderful city to live in for {rent_price:.2f} $ rent/month.")
    else:
        print(f"Sorry, {city} is not the best choice for you for {rent_price:.2f} $ rent/month, the rent is too high. Continue searching!")
elif city == "Washington":
    print(f"Sorry, the city where the flat is {city} which is not an option for you, continue searching.")
else: 
    rent_price = int(input("What is the rent price? "))
    if rent_price <= 3000:
        print(f"Good news! You can move in {city} for {rent_price:.2f} $ rent/month.")
    else: 
        print(f"Sorry, {city} is not the best choice for you for {rent_price:.2f} $ rent/month, the rent is too high. Continue searching!")

city = input("Where is the flat located? ").capitalize().strip()

while True:
    city = input("Where is the flat located? ").capitalize().strip()
    if city == "Chicago":
        rent_price = int(input("What is the rent price? "))
        print(f"Yay! You can move in your dream city, {city} for {rent_price:.2f} $ rent/month.")
        break
    elif city == "New York" or city == "San Francisco":
        rent_price = int(input("What is the rent price? "))
        if rent_price < 4000:
            print(f"Great choice! {city} is a wonderful city to live in for {rent_price:.2f} $ rent/month.")
            break
        else:
            print(f"Sorry, {city} is not the best choice for you for {rent_price:.2f} $ rent/month, the rent is too high. Continue searching!")
    elif city == "Washington":
        print(f"Sorry, the city where the flat is {city} which is not an option for you, continue searching.")
    else:
        rent_price = int(input("What is the rent price? "))
        if rent_price <= 3000:
            print(f"Good news! You can move in {city} for {rent_price:.2f} $ rent/month.")
            break
        else:
            print(f"Sorry, {city} is not the best choice for you for {rent_price:.2f} $ rent/month, the rent is too high. Continue searching!")

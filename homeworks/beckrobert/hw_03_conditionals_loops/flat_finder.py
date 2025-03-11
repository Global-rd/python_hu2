us_flat_city = input("give me the name of the city: ")
us_flat_price = int(input("give me the price of the flat in USD: "))

if us_flat_city == "chicago":
    print(f"you can rent the flat in {us_flat_city} for a price {us_flat_price}USD, because you love the city")
    
elif us_flat_city == "washington":
    print(f"you cannot rent the flat in {us_flat_city} for a price {us_flat_price}USD, because you hate the city")

elif us_flat_city == ("new york" or "san francisco") and us_flat_price <=4000:
    print(f"you can rent the flat in {us_flat_city} for a price {us_flat_price}USD")

elif us_flat_price <=3000:
    print(f"you cannot rent the flat in {us_flat_city} for a price {us_flat_price}USD")

else: print(f"you cannot rent the flat in {us_flat_city} for a price {us_flat_price}USD")


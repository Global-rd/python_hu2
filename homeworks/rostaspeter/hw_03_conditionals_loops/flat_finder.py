city = input("Add meg a várost!")
price = int(input("Add meg a havi lakbért dollárba!"))

if city in ["New York", "San Francisco"] and price < 4000:
    print(f"Sarah {price} dollárért szívesen beköltözne {city} városába")
elif city == "Washington":
    print(f"Sarah nem költözik {city}ba")
elif city == "Chicago":
    print(f"Sarah elköltözik {city}ba")
elif price < 3000 and (city != "New York" or city != "San Fransisco" or city != "Washington" or city != "Chicago"):
    print(f"Sarah elköltözik {city} városába {price} dolláros albérleti díjjal")
else:
    print(f"Sarah nem költözik {city} városába {price} dollárért havonta")
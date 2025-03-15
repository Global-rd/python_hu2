city = input("Melyik városban van a lakás? ")
rent = int(input("Mennyi a havi lakbér (USD)? "))
if city == "Washington":
    print(f"Sarah utálja Washingtont, nem költözik oda semmi pénzért.")
elif city in ["New York"] and rent < 4000 or city in ["San Francisco"] and rent < 4000:
    print(f"Sarah szívesen beköltözne a {city}-ban található lakásba.")
elif city == "Chicago":
    print(f"Sarah imádja Chicago-t, pénz nem számít, kiveszi a lakást!")
elif rent <= 3000:
    print(f"Sarahnak megfelel a lakás {city}-ban, mert olcsó.")
else:
    print(f"A lakbér túl magas, ({rent} USD), így sarah nem költöik oda.")

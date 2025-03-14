# 1. feladat: Hétköznapi nyelven leírt szöveg konvertálása Python kód-ra
#(if-elif-else,opetátorok)

city = input("Melyik városban szeretne lakni?: ")
rent = int(input("Havi lakbér ára?: "))

city = city.lower()

if city == "Washington":
        print (f"Sarah gyűlöli {city.capitalize()}-t és semmi pénzért nem lakna ott.")

elif city == "Chicago":
        print(f"Sarah annyira imádja {city.capitalize()}-t,hogy bármit megadna azért, hogy ott lakhasson!")

elif city == "new york" or city == "san francisco" and rent < 4000:
        print (f"Sarah nagyon szereti ezt a várost, szívesen venne ki lakást {city.capitalize()}-ban")
else:
        print(f"Sarah nem költözne {city.capitalize()}-ba.")




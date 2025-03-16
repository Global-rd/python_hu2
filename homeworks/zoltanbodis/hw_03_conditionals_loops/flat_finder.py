print("--------------------------------------------------------------------\nA program az előre meghatározott feltételek, valamint az általad megadott\nelhelyezkedés és ár alapján kiszámolja, hogy beköltözhetsz-e a lakásba.\n--------------------------------------------------------------------\n")

city = input("Add meg a várost: ").strip().title()
city_l = city.lower()

while True:
    price = input("Add meg a lakbért: ")
    try:
        if "," in price:
            price = price.replace(",",".")    
        price = float(price)
        break
    except ValueError:
        continue

"""
Nagyon szereti New York-ot és San Fransisco-t, bármelyik városban
kivenne egy lakást, ha az albérlet ára kevesebb mint 4000 USD
havonta.

Gyűlöli Washington-t, és semmi pénzért nem lakna ott

Annyira imádja Chicago-t, hogy még a pénz sem akadály, bármit
megadna azért hogy ott lakhasson

Ha bármilyen más helyről van szó, 3000 USD vagy ez alatti havi lakbér
ellenében költözne oda.
"""    

if city_l == "chicago":
    moving = True
elif city_l == "washington":
    moving = False
elif city_l in ("new york", "san francisco") and price < 4000:
    moving = True
elif price <= 3000:
    moving = True    
else:
    moving = False


if moving:
    str_out = "beköltözhetsz"
else:
    str_out =  str_out = "nem költözhetsz be"    

print(f"\nA kinézett lakásba {str_out} ({city}, {price} USD)\n")
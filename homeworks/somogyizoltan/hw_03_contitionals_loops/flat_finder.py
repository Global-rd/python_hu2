"""
Feladat 1: Hétköznapi nyelven leírt szöveg konvertálása Python kód-ra (if-elif-
else, operátorok)

A feladat célja, hogy elsajátítsd azt a képességet hogy hétköznapi módon
megfogalmazott feladatokat fordítasz le python-ra. Sarah-nak kell segítened
a lakáskeresésben, a következőket tudjuk:

● Nagyon szereti New York-ot és San Fransisco-t, bármelyik városban
kivenne egy lakást, ha az albérlet ára kevesebb mint 4000 USD
havonta.
● Gyűlöli Washington-t, és semmi pénzért nem lakna ott
● Annyira imádja Chicago-t, hogy még a pénz sem akadály, bármit
megadna azért hogy ott lakhasson
● Ha bármilyen más helyről van szó, 3000 USD vagy ez alatti havi lakbér
ellenében költözne oda.

Írj egy programot, amely bekéri a felhasználótól a várost és a lakbér árát.
Ezután a fentiek alapján printeld ki egy f-string használatával hogy az adott
feltételek (város és albérlet ára) mellett be tudna e költözni az adott helyre.
"""

# bekérni a várost és a lakbért, tesztelni nem fogom, feltételezem, hogy a bejövő adatok jók

city = input("Add meg a város nevét: ")
rent_fee = int(input("Add meg a havi lakbért: "))

# logikai tesztek, hogy a szöveges megadás alapján melyik feltétel teljesül
if city in ("New York", "San Francisco"): 
    if rent_fee < 4000:
        final_text = f"Sarah ebbe a városba - {city} - be tudna költözni egy {rent_fee} USD-ért kínált albérletbe"
    else:
        final_text = f"Sarah ebbe a városba - {city} - nem tudna költözni egy {rent_fee} USD-ért kínált albérletbe, mert túl magas az ár" 
elif city == "Washington":
    final_text = f"Sarah ebbe a városba - {city} - semmiképpen sem szeretne költözni még ennyi pénzért {rent_fee} USD sem!"    
elif city == "Chicago":
    final_text = f"Sarah ebbe a városba - {city} - szívesen be tudna költözni ennyi pénzért is {rent_fee} USD"
else:
    if rent_fee <= 3000:
        final_text = f"Sarah ebbe a városba - {city} - be tudna kóltözni egy {rent_fee} USD-ért kínált albérletbe"
    else:
        final_text = f"Sarah ebbe a városba - {city} - nem tudna kóltözni egy {rent_fee} USD-ért kínált albérletbe, mert túl magas az ár"

print(final_text)
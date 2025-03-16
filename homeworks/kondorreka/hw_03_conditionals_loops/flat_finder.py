"""Feladat 1: Hétköznapi nyelven leírt szöveg konvertálása Python kód-ra (if-elif-
else, operátorok)

Hozz létre egy flat_finder.py nevű file-t, és kódold le a következő feladat
megoldását:
A feladat célja, hogy elsajátítsd azt a képességet hogy hétköznapi módon
megfogalmazott feladatokat fordítasz le python-ra. Sarah-nak kell segítened
a lakáskeresésben.
Írj egy programot, amely bekéri a felhasználótól a várost és a lakbér árát.
Ezután a fentiek alapján printeld ki egy f-string használatával hogy az adott
feltételek (város és albérlet ára) mellett be tudna e költözni az adott helyre."""

city = input("Melyik városban van az ingatlanod?").lower()

while True:
    try:
        price = int(input("Milyen áron szeretnéd kiadni? (USD/hó)"))

        if price <= 0:
            print("Te akarsz fizetni, hogy ott laknak? Na fuss neki újra!")
            continue
        
        break

    except ValueError:
        print('Kérlek számmal írd be az összeget.')



#Gyűlöli Washington-t, és semmi pénzért nem lakna ott.
if "washington" in city:
    print(f'Sajnos Sarah számára nem megfelelő ez az ingatlan.')

#Annyira imádja Chicago-t, hogy még a pénz sem akadály, bármit megadna azért hogy ott lakhasson.
elif "chicago" in city:
    city = "chicago" 
    print(f'Sarah, megtaláltam az álomlakásod! Welcome to {city.capitalize()}!')

#Nagyon szereti New York-ot és San Francisco-t, bármelyik városban kivenne egy lakást, 
#ha az albérlet ára kevesebb mint 4000 USD havonta.
elif city in {"new york", "san francisco"} and price < 4000:
    if "new york" in city:
        city = "new york"
    elif "san francisco" in city:
        city = "san francisco"
    print(f'Sarah, ezt a {city.title()}-i lakást érdemes lenne megnézned. Az ára csak {price} USD havonta.')

elif price <= 3000:
    print(f'Hát ez nem a kedvenc lokációd, de olcsó. Csak {price} USD havonta.')

else:
    print(f'Sajnos Sarah, nincs árban és lokációban is megfelelő ingatlanom.')



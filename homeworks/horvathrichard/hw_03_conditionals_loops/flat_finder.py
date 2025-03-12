# Kérjük be az albérlet helyét és díját a felhasználótól (utóbbit integerként, a függvények miatt)

area = input("Which city is the apartment in?")

# Hozzunk létre egy listát a kedvelt városokról
preferred_areas = ["New York", "San Francisco"]

# Logika: ha a település Washington, ne is menjen tovább, mert nem jó, ha viszont Chicago, akkor azért ne menjen tovább, mert a pénz nem számít
if area == "Washington":
    print(f"NO WAY I COULD LIVE IN {area}!!")

elif area == "Chicago":
    print(f"{area} is your favourite city, so the price doesn't matter!")

# ha az előző két település nem teljesült, akkor folytathatjuk a díj bekérésével és a további feltétellel
else:

    cost = int(input("How much the apartment costs?"))

    if area == "Chicago":
        print(f"{area} is your favourite city, so the price {cost}$ doesn't matter for this!")

    elif area in preferred_areas and cost<4000:
        print(f"Seems to be a good deal in {area} for only {cost}$!")

    elif area not in preferred_areas and cost<=3000:
        print(f"{area} can be okay for {cost}$")

    else:
        print(f"{area} for {cost}$ doesn't seem to be a good deal")

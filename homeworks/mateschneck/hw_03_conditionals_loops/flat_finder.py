def flat_finder():
    # ár és város megadása
    city = input("Kérlek, add meg a várost: ")
    rent = float(input("Kérlek, add meg a havi lakbért amit ki tudsz érte fizetni (USD): "))

    # függvény
    if city.lower() == "new york" or city.lower() == "san francisco":
        if rent < 4000:
            result = "beköltözne"
        else:
            result = "nem költözne be"
    elif city.lower() == "washington":
        result = "semmi pénzért nem lakna ott"
    elif city.lower() == "chicago":
        result = "beköltözne, nincs árkorlát"
    else:  # bármelyik másik vátos
        if rent <= 3000:
            result = "beköltözne"
        else:
            result = "nem költözne be"

    
    print(f"Sara {result} a(z) {city} városba a havi {rent} USD albérlettel.")

# flat finder
if __name__ == "__main__":
    flat_finder()
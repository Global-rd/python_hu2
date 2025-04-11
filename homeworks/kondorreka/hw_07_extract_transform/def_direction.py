"""
a. Ha a price_change_percentage_24h értéke nagyobb mint 0, az oszlop
értéke legyen “+”
b. Ha negatív, az oszlop értéke legyen “-“
c. Ha kereken 0, az érték legyen “0”
"""

def direction(x):
    if x > 0:
        return "+"
    elif x < 0:
        return "-"
    elif x == 0:
        return "0"
    else:
        raise ValueError(f"Hibás érték: {x}")
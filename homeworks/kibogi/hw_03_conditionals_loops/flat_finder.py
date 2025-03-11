city = input ("Add meg a város nevét")
cost_usd = input ("Add meg a bérleti díjat")
cost = int(cost_usd)

if city == "New York" or city == "San Francisco":
    if cost < 4000:
        print (f"A lakás {city}-ban található és az ára csak {cost} USD, ezért Sarah ide tudna költözni.")
    else:
        print (f"A lakás {city}-ban található és az ára {cost} USD, ez túl sok, ezért Sarah ide nem tudna költözni.")

elif city == "Washington":
    print (f"A lakás {city}-ban található és az ára {cost} USD, de ide Sarah semmi pénzért nem költözne.")

elif city == "Chicago":
    print (f"A lakás {city}-ban található és az ára {cost} USD, de Sarah annyira szereti ezt a várost, hogy a pénz nem érdekli.")

elif cost <= 3000:
    print (f"A lakás {city}-ban található és az ára {cost} USD. Ez az ár ebben a városban elfogadható, ezért Sarah ide tudna költözni.")

else:
        print(f"A lakás {city}-ban található és az ára {cost} USD. Ez az ár ebben a városban túl drága, ezért Sarah ide nem tudna költözni.")


# Nagyon szereti New York-ot és San Fransisco-t, bármelyik városban kivenne
# egy lakást, ha az albérlet ára kevesebb mint 4000 USD havonta.
# Rule1: if price < 4000
#
# Gyűlöli Washington-t, és semmi pénzért nem lakna ott
# Rule2: never rent
#
# Annyira imádja Chicago-t, hogy még a pénz sem akadály, bármit megadna azért
# hogy ott lakhasson
# Rule 3: Always Rent
#
# Ha bármilyen más helyről van szó, 3000 USD vagy ez alatti havi lakbér
# ellenében költözne oda.
# Rule 4: price <= 3000

city = (
    input("Enter the city's name").strip().title()
)  # no lead/tail space, every letter with Capital
rent = int(
    input("Enter the expected monthly rent in USD: ").strip()
)  # convert input to integer

# Sarah's preference in code - Solution option #1
if city == "Chicago":
    decision = "She will definitely move in, price doesn't matter blingbling"
elif city in ["New York", "San Farnsisco"] and rent < 4000:
    decision = (
        f"She will move to {city} because the rent is affordable ({rent} $ / month)"
    )
elif city == "Washington":
    decision = "She will never move to Washington"
elif rent <= 3000:
    decision = (
        f"She will move to {city} because the rent is affordable ({rent} $ / month)"
    )
else:
    decision = f"She will Not move to {city} because {rent} $ / month is too high"

print(decision)

# Sarah's preference in code - Solution option #2
decision = "No"  # setting decision to a default value,
# so she won't move unless we match one of her options

if city == "Chicago":
    decision = "Yes"
elif city in ["New York", "San Fransisco"] and rent < 4000:
    decision = "Yes"
elif rent <= 3000 and city != "Washington":
    decision = "Yes"

print(
    f"Sarah's decision for {city} (rent {rent} $ / month): {decision}, let's move in!"
    if decision == "Yes"
    else f"Sarah's deicion for {city} (rent {rent} $ / month: {decision}, let's skip this one.)"
)


# INPUTOK

city = str(input("Which city would you like to live in?"))  # str, hogy biztosan string legyen, de ebben nem vagyok biztos

# A rental fee-t csak lentebb, a logika alapján bizonyos esetekben kérem be.

city = city.lower()  # az értékek miatt csupa kisbetű, mert a bekért adatban lehet nagybetű is

# FELTÉTELRENDSZER

if city == "washington":  # Washington kizárása -> így nem kérek be rental fee-t
    print(f"Sarah, you wouldn't move to any apartment in this city.")
elif city == "chicago":  # Chicago-ba bármi áron beköltözne -> így nem kérek be rental fee-t
    print(f"Sarah, you would love to rent the apartment in Chicago.")
elif city == "new york" or city == "san francisco":
    rent = int(input("What is the rental fee of the apartment in USD?"))
    if rent < 4000:
        print(f"Sarah, this apartment matches with your requiremnets.")
    else:
        print(f"Sarah the rental fee is higher than your ideal price.")
else:
    rent = int(input("What is the rental fee of the apartment in USD?"))
    if rent < 3000:
        print(f"Sarah, this apartment matches with your requiremnets.")
    else:
        print(f"Sarah the rental fee is higher than your ideal price.")
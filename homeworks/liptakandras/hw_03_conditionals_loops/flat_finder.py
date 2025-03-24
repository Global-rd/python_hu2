
# INPUTOK

city = str(input("Which city would you like to live in?"))  # str, hogy biztosan string legyen, de ebben nem vagyok biztos
rent = int(input("What is the rental fee you are wondering to pay in USD?"))

city = city.lower()  # az értékek miatt csupa kisbetű, mert a bekért adatban lehet nagybetű is

# FELTÉTELRENDSZER

if city == "washington":  # Washington kizárása
    print(f"Sarah wouldn't move to the city.")
elif city == "chicago":  # Chicago-ba bármi áron beköltözne
    print(f"Sarah would like to rent the apartment.")
elif city == "new york" or city == "san francisco":
    if rent < 4000:
        print(f"Sarah would like to rent the apartment.")
    else:
        print(f"Sarah finds the rent too high.")
else:
    if rent < 3000:
        print(f"Sarah would like to rent the apartment")
    else:
        print(f"Sarah finds the rent too high")

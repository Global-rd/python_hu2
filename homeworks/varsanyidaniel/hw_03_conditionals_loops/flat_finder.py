new_home_location=input("Add meg, hogy hol van a lakás: ")
new_home_price=int(input("Add meg, hogy mennyi a havi bér (USD): "))
if new_home_location == "Chicago":
    print(f"Sarah nagyon szívesen beköltözne a {new_home_location} -i lakásba {new_home_price} USD havi áron.")

elif new_home_location == "Washington":
    print(f"Sarah biztos hogy nem költözne be a {new_home_location} -i lakásba. ({new_home_price} USD-nyi havi bérért sem!)")

elif new_home_location == "New York" or "San Francisco":
    if new_home_price < 4000:
        print(f"Sarah szívesen beköltözne a {new_home_location} -i lakásba {new_home_price} USD havi áron.")
    else:
        print(f"Sajnos Sarah nem költözne be a {new_home_location} -i lakásba {new_home_price} USD havi bérért.")

elif new_home_price < 3000:
    print(f"Sarah beköltözne a {new_home_location} -i lakásba {new_home_price} USD havi áron.")

else:
    print(f"Sajnos Sarah nem költözne be a {new_home_location} -i lakásba {new_home_price} USD havi bérért.")
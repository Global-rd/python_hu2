""" 
Sarah is looking for an apartment to rent. She has a list of cities where she would like to live, and a budget.
She likes New York, San Francisco, and Chicago. She does not like Washington, so she doesn't want to live here.
New York and San Francisco are expensive, but she can afford them if the rent is less than $4000.
She loves Chicago and the price is not a problem for her.
She could live anywhere else if the rent is less than $3000.
"""

city = input("Please enter a city for Sarah: ")
price = int(input("Please enter the monthly rent in US $: "))

if city == "Chicago":
    print(f"Sarah likes this apartment in {city} for {price} US $.")
elif price < 3000 and city != "Washington":
    print(f"Sarah likes it, so she will rent in {city} for {price} US $.")
elif price < 4000 and city in ["New York", "San Francisco"]:
    print(f"Sarah likes this, she will rent in {city} for {price} US $.")
else:
    print(f"Sarah will not rent in {city} for {price} US $. Please try again.")
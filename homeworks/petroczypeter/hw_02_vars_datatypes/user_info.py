# The following dictionary was given
user_info = {
    "name": "Mike",
    "age": 25,
    "favourite_meals": ["pizza", "carbonara", "sushi"],
    "phone_contacts": {
        "Mary": "+36701234567",
        "Tim": "+36207654321",
        "Tim2": "+36304567321",
        "Jim": "+364005000",
    },
}

# 1. Ask the user for 4 programming languages.
# the input string should be converted into a list
languages = input("Enter 4 programming languages (comma-separated, no spaces): ").split(
    ","
)
user_info["skills"] = (
    languages  # this new list should be added to the user_info dictionary as "skills"
)

# 2. Sort favourite_meals alphabetically
user_info["favourite_meals"].sort()

# 3. Print second last item in favourite_meals, and print the full list as well
print("Second last item in favourite_meals:", user_info["favourite_meals"][-2])
print("Favourite meals:", user_info["favourite_meals"])

# 4. Add "spaghetti" to favourite_meals
user_info["favourite_meals"].append("spaghetti")

# 5 duplicate the favourit_meals list's 3rd and 4th elements
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

# 6. Remove duplicates
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))

# 7 Swap favourite_meals list's first and last elements
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = (
    user_info["favourite_meals"][-1],
    user_info["favourite_meals"][0],
)

# 8. add to the "phone_contracts" dictionary a new contact
user_info["phone_contacts"]["Béla"] = "+36201231234"

# 9. Delete Tim because that number is inactive
del user_info["phone_contacts"]["Tim"]

# 10. add a new person to "phone_contacts" with two phone numbers
user_info["phone_contacts"]["Géza"] = ["+36201231235", "+36201231236"]

# Extra challenge 1: print the last three skills in reverse order
print("Last three skills in reverse order:", user_info["skills"][-1:-4:-1])

# Extra challenge 2: Rename Tim2 to Tim
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")

# Print out the entire user_info dictionary
print(user_info)

# User data
user_info = {
    "name": "Mike",
    "age": 25,
    "favourite_meals": [
        "pizza",
        "carbonara",
        "sushi"
    ],
"phone_contacts": {
    "Mary": "+36701234567",
    "Tim": "+36207654321",
    "Tim2": "+36304567321",
    "Jim": "+364005000"
    }
}


# 1) Ask for 4 programming language. Convert string to list. Divide by comma
skills = input("Tell me 4 programming languages you know: ").split(",")
user_info["skills"] = skills
print(user_info["skills"].sort())

# 2) Arrange the favourite meals in ascending order
user_info["favourite_meals"].sort()
print(user_info["favourite_meals"])

# 3) Print the second last favourite meal
print(user_info["favourite_meals"][-2])

# 4) Add spaghetti to the favourite meals
user_info["favourite_meals"].append("spaghetti")
user_info["favourite_meals"].sort()
print(user_info["favourite_meals"])

# 5) Create a new favourite_meals list by adding from current favourite_meals list 3. and 4. item
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
print(user_info["favourite_meals"])

# 6) Delete duplicates from favourite_meals
user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))
print(user_info["favourite_meals"])

# 7) Change the first and the last item of the favourite_meals list
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
print(user_info["favourite_meals"])

# 8) Add a new user to the phone_contacts
user_info["phone_contacts"]["Bob"] = "+36301234567"
print(user_info["phone_contacts"])

# 9) Delete Tim from the phone book
del user_info["phone_contacts"]["Tim"]
print(user_info["phone_contacts"])

# 10) Add a user with 2 phone numbers
user_info["phone_contacts"]["Carol"] = ["+362022222222","+363033333333"]
print(user_info["phone_contacts"])


# Extra 1) Print the skills list last 3 items reverse
reversed_skills = user_info["skills"][-1:-4:-1]
print(user_info["skills"])
print(reversed_skills)

# Extra 2) Rename Tim2 to Tim
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
print(user_info["phone_contacts"])
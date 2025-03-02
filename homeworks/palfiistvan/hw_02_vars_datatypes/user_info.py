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

# 1.
prog_languages = input("Give me 4 program languages separated by a comma: ")
print(prog_languages)
prog_languages_list = prog_languages.split(",")
print(prog_languages_list)
user_info.update({"skills": prog_languages_list})
print(f"1. {user_info}")

# 2.
print(f"2a {user_info["favourite_meals"]}")
user_info["favourite_meals"] = sorted(user_info["favourite_meals"])
print(f"2b {user_info["favourite_meals"]}")

# 3.
print(f"3. {user_info["favourite_meals"][-2]}")

# 4.
user_info["favourite_meals"].append("spaghetti")
print(f"4. {user_info["favourite_meals"]}")

# 5.
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:])
print(f"5. {user_info["favourite_meals"]}")

# 6.
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
print(f"6. {user_info["favourite_meals"]}")

# 7.
temp = user_info["favourite_meals"][0]
user_info["favourite_meals"][0] = user_info["favourite_meals"][-1]
user_info["favourite_meals"][-1] = temp
print(f"7. {user_info["favourite_meals"]}")

# 8.
user_info["phone_contacts"].update({"Jack": "+368099999"})
print(f"8. {user_info["phone_contacts"]}")

# 9.
user_info["phone_contacts"].pop("Tim")
print(f"9. {user_info["phone_contacts"]}")

# 10.
#user_info["phone_contacts"].update({"Adam": "[+368099999, +3690999999]"})
user_info["phone_contacts"].update({"Adam": ["+368099999", "+3690999999"]})
print(f"10. {user_info["phone_contacts"]}")
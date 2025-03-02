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

# 1
programming_languages = input("Írj be 4 programozási nyelvet: ").split(",")
user_info["skills"] = programming_languages
print("--------------------------------------------------------------------------------")
print(user_info["skills"])
print("--------------------------------------------------------------------------------")

# 2
user_info["favourite_meals"].sort()
print(user_info["favourite_meals"])
print("--------------------------------------------------------------------------------")

# 3
print(user_info["favourite_meals"][-2])
print("--------------------------------------------------------------------------------")

# 4
user_info["favourite_meals"].append("spaghetti")
print(user_info["favourite_meals"])
print("--------------------------------------------------------------------------------")

# 5
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
print(user_info["favourite_meals"])
print("--------------------------------------------------------------------------------")

# 6
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
print(user_info["favourite_meals"])
print("--------------------------------------------------------------------------------")

# 7
user_info_last_fav_meal = user_info["favourite_meals"][-1]
user_info["favourite_meals"][-1] = user_info["favourite_meals"][0]
user_info["favourite_meals"][0] = user_info_last_fav_meal
print(user_info["favourite_meals"])
print("--------------------------------------------------------------------------------")

# 8
user_info["phone_contacts"]["Joe"] = "+36305555555"
print(user_info["phone_contacts"])
print("--------------------------------------------------------------------------------")

# 9
del user_info["phone_contacts"]["Tim"]
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
print(user_info["phone_contacts"])
print("--------------------------------------------------------------------------------")

# 10
user_info["phone_contacts"]["Ric"] = ["+36305468793", "+36302347951"]
print(user_info["phone_contacts"])
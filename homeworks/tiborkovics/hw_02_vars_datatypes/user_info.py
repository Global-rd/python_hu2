

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

languages = input("Kerlek adj meg 4 prog nyelvet").split(",")   # 1/1

<<<<<<< Updated upstream
user_info["skills"] = languages # 1/2
print(user_info)

user_info["favourite_meals"].sort()  # 2
print(user_info)

print(user_info["favourite_meals"][-2])  # 3
print(user_info)


user_info["favourite_meals"].append("spaghetti") # 4
print(user_info)

user_info["favourite_meals"].append("favourite_meals"[2:4])  # 5
print(user_info)


user_info["favourite_meals"] = list(set(user_info["favourite_meals"])) # 6
print(user_info)

user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
# 7
print(user_info)

user_info["phone_contacts"]["Tibi"] = "+367002421010" # 8
print(user_info)

del user_info["phone_contacts"][1] # 9
print(user_info)

user_info["phone_contacts"]["Anyu"] = ["+36701455098" , "+36707884956"] # 10
print(user_info)
=======
skills = list[languages] # 1/2

languages = user_info["skills"] # 1/3

user_info["favourite_meals"].sort()  # 2

print(user_info["favourite_meals"][-1])  # 3


user_info["favourite_meals"].append("spaghetti") # 4

user_info["favourite_meals"].append("favourite_meals"[2:4])  # 5


user_info["favourite_meals"] = set(user_info["favourite_meals"])

user_info = list(user_info) # 6

user_info["favourite_meals"][0]. # 7


>>>>>>> Stashed changes




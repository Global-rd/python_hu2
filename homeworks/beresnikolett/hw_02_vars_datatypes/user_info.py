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
        "Jim": "+364005000"},
    }
user_skills = list(input("Provide 4 of your programming languages separated by comma: ").split(", "))
user_info["skills"] = user_skills
user_info["favourite_meals"].sort()
print(user_info["favourite_meals"][-2])
user_info["favourite_meals"].append("spaghetti")
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:])
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
user_info["phone_contacts"]["Mia"] = ["+36301357246"]
user_info["phone_contacts"].pop("Tim")
user_info["phone_contacts"]["Allie"] = ["+36200112233", "+36302244556"]
print(user_info)
print(user_info["skills"][-3:][::-1])
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
print(user_info["phone_contacts"])

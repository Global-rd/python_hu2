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
user_skills = list(set(input("Provide 4 of your programming languages separated by comma: ").split(", ")))
user_info["skills"] = user_skills
user_info["favourite_meals"].sort()
print(user_info["favourite_meals"][-2:-1])
user_info["favourite_meals"].append("spaghetti")
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:])
list(set(user_info["favourite_meals"]))
print(user_info)


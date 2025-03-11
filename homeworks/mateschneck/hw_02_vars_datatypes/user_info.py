# user data
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

# 1. programnyelvek
skills_input = input("Adj meg 4 db programnyelvet kötőjelekkel: ")
user_info["skills"] = skills_input.split(",")

# 2. rendezés
user_info["favourite_meals"].sort()

# 3. utolsó előtti
print("Utolsó előtti kedvenc étel:", user_info["favourite_meals"][-2])

# 4. hozzáadás
user_info["favourite_meals"].append("spaghetti")

# 5. duplikálás
if len(user_info["favourite_meals"]) >= 4:
    user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

# 6. törlés
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))

# 7. csere
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]

# 8. hozzáadás
user_info["phone_contacts"]["John"] = "+36501234567"

# 9. Tim törlés
user_info["phone_contacts"].pop("Tim", None)

# 10. két telefon
user_info["phone_contacts"]["Alex"] = ["+36609876543", "+36709998877"]

# Extra 1
print("Utolsó 3 skill ellentétes sorrendben:", user_info["skills"][-3:][::-1])

# Extra 2
if "Tim2" in user_info["phone_contacts"]:
    user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")

print(user_info)

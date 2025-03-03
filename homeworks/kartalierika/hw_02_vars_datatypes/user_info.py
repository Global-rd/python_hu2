#Felhasználói adatok módosítása

#Felhasználó adatai
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

print("-------------------------")

# 1. Programozási nyelvek bekérése
prog_skills = input("Write 4 programming languages: ").split(",")
user_info["skills"] = prog_skills

#2. Favourite meals ABC
user_info["favourite_meals"].sort()

print("-------------------------")

#3. Fav meals utolsó előtti eleme
print(user_info["favourite_meals"])

print("-------------------------")

print(user_info["favourite_meals"][-2])

#4. Új étel hozzáadása
user_info["favourite_meals"].append("spaghetti")

print("-------------------------")

#5. Harmadik és negyedik elem hozzáadása újra
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
print(user_info["favourite_meals"])

print("-------------------------")

#6. Duplikációk törlése
user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))

#7. Első és utolsó elem csere
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]

#8. Új kontakt hozzáadása
user_info["phone_contacts"]["Gyula"] = "+36303102877"

#9. Tim törlése
user_info["phone_contacts"].pop('Tim')

#10. Két telefonszám
user_info["phone_contacts"]["Béla"] = ["+36306578655", "+36307635644"]

print("-------------------------")

#11. Skills ellentétes sorrendben
print(user_info["skills"][-3:][::-1])

#12. Tim2 átnevezése
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"]["Tim2"]
del user_info["phone_contacts"]["Tim2"]

print("-------------------------")
print(user_info)
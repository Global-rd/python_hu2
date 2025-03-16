#dictionary létrehozása

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

# 1. Kérjünk be 4 programozási nyelvet vesszővel elválasztva, szóköz nélkül.
# Konvertáld a kapott stringet egy listává és adjuk hozzá a dictionary-hez "skills" néven.

languages = input("Adja meg a 4 programozási nyelvet: ")
user_info["skills"] = languages.split(",")
print(user_info)

# 2. Rendezzük a favourite_meals listát ABC sorrendbe
user_info["favourite_meals"].sort()
print(user_info["favourite_meals"])

# 3. Printeld ki a favourite_meals lista utolsó előtti elemét 
print(user_info["favourite_meals"][-2])

# 4. Adj hozzá egy “spaghetti” string-et ugyanehhez a listához. 
user_info["favourite_meals"].append("spaghetti")
print (user_info["favourite_meals"])

# 5. Add hozzá a favourite_meals-hez az aktuális favourit_meals lista 
# harmadik és negyedik elemét (nem az index-ét) újra.
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
print(user_info["favourite_meals"])

# 6. Ezután töröld az így keletkezett duplikátumokat! 
user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))
print(user_info["favourite_meals"])

# 7. Cseréld fel a favourite_meals lista első és utolsó elemét!
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
print(user_info["favourite_meals"])

# 8. A “phone_contacts” dictionary-hez adj hozzá egy új elemet, tetszőleges névvel és telefonszámmal. 
user_info["phone_contacts"]["Petra"] = "+36201112223"
print(user_info["phone_contacts"])

# 9. Tim és Tim2 ugyanazt az embert reprezentálják a “phone_contacts” ban, viszont a "Tim" key mögött lévő telefonszám már nem él. Töröld ki a telefonkönyvből!
user_info["phone_contacts"].pop("Tim")
print(user_info["phone_contacts"])

# 10. Új személy hozzáadása két telefonszámmal
user_info["phone_contacts"]["Peter"] = ["+36201112233", "+36205556677"]
print(user_info["phone_contacts"])

# Extra 1: 
print(user_info["skills"][-3:][::-1])

# Extra 2: 
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
print(user_info["phone_contacts"])












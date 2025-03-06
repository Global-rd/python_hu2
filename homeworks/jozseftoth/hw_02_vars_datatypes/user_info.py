# Kezdő dictionary
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

# Felhasználó adjon meg 4 programozási nyelvet 
languages_input = input("Adj meg 4 programozási nyelvet (vesszővel elválasztva, szóközök nélkül): ")

# string listává konvertálása
languages_list = languages_input.split(',')

# Hozzáadjuk a dictionary-hoz "skills" néven
user_info["skills"] = languages_list

# Ellenőrzés
print("1. Lépés - Skills hozzáadása:")
print(user_info)
print()

# A favourite_meals lista elemei abc szerint növekvő sorrendben
user_info["favourite_meals"].sort()

# Ellenőrzés
print("2. Lépés - favourite_meals rendezése növekvő sorrendbe:")
print(user_info)
print()

# Print-> favourite_meals lista utolsó előtti eleme
print("3. Lépés - favourite_meals utolsó előtti eleme:")
print(user_info["favourite_meals"][-2])
print()

# Egy "spagetti" string a favourite_meals listához
user_info["favourite_meals"].append("spagetti")

# Ellenőrzés
print("4. Lépés - spagetti hozzáadása:")
print(user_info)
print()

# Adjunk hozzá az aktuális favourite_meals lista 3. és 4. elemét (de nem az indexét!)
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

# Ellenőrzés
print("5. Lépés - favourite_meals 3. és 4. elemének hozzáadása:")
print(user_info)
print()

# Töröljük a keletkezett duplikátumokat
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))

# Ellenőrzés
print("6. Lépés - Duplikátumok törlése:")
print(user_info)
print()

# Cseréljük le a favourite_meals lista első és utolsó elemét
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]

# Ellenőzés
print("7. Lépés - favourite_meals első és utolsó elemének cseréje:")
print(user_info)
print()

# Új elem a phone_contacts dictionary-hoz
user_info["phone_contacts"]["Kergemarha"] = "+36332222222"

# Ellenőrzés
print("8. Lépés - Új elem hozzáadása a phone_contacts-hoz:")
print(user_info)
print()

# Töröljük a Tim mögötti telefonszámot
del user_info["phone_contacts"]["Tim"]

# Ellenőrzés
print("9. Lépés - Tim telefonszámának törlése:")
print(user_info)
print()

# A Tim2 -> Tim
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")

# Ellenőrzés
print("10. Lépés - Tim2 -> Tim:")
print(user_info)
print()

# Adjunk hozzá egy új embert két telefonszámmal
user_info["phone_contacts"]["Alice"] = ["+36701112233", "+36704445566"]

# Ellenőrzés
print("11. Lépés - Új név hozzáadása két telefonszámmal:")
print(user_info)
print()

# Print a skills lista utolsó 3 eleme ellentétes sorrendben
print("12. Lépés - Skills lista utolsó 3 eleme ellentétes sorrendben:")
print(user_info["skills"][-3:][::-1])
print()

# Ellenőrzés
print("Végső user_info:")
print(user_info)
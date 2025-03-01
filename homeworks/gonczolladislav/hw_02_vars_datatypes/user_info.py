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

#1. Bekérjük a felhasználótól a programozási nyelveket
nyelvek = input("Kérlek, adj meg 4 programozási nyelvet vesszővel elválasztva: ")

# A stringet listává alakítjuk
nyelvek_lista = nyelvek.split(",")

# Hozzáadjuk a "skills" kulcsot és a listát a dictionary-hez
user_info["skills"] = nyelvek_lista
print("1.feladat:")
print(user_info)

#2. Rendezés abc szerint
user_info["favourite_meals"].sort()
print("2.feladat:")
print(user_info)

#3. Az utolsó előtti elem kiírása
print("3.feladat:")
print(user_info["favourite_meals"][-2])

#4.  "spaghetti" hozzáadása a listához
user_info["favourite_meals"].append("spaghetti")
print("4.feladat:")
print(user_info)

#5. A harmadik és negyedik elem ismételt hozzáadása
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
print("5.feladat:")
print(user_info)

#6. Duplikátumok eltávolítása
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
print("6.feladat:")
print(user_info)

#7. Első és utolsó elem felcserélése
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
print("7.feladat:")
print(user_info)

#8. Új elem hozzáadása a phone_contacts dictionary-hez
user_info["phone_contacts"]["Anna"] = "+361012345678"
print("8.feladat:")
print(user_info)

#9. "Tim" törlése a phone_contacts dictionary-ből
del user_info["phone_contacts"]["Tim"]
print("9.feladat:")
print(user_info)

#10. Új név hozzáadása két telefonszámmal
user_info["phone_contacts"]["Peter"] = ["+36501112233", "+36504445566"]
print("10.feladat:")
print(user_info)

#Extra1: Lekérjük az utolsó 3 elemet a skills-ből és megfordítjuk a sorrendet
utolso_3 = user_info["skills"][-1:-4:-1]
print("Extra 1:", utolso_3)
print(user_info)

#Extra2:  Átnevezzük Tim2-t Tim-re
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
print("Extra 2:")
print(user_info)
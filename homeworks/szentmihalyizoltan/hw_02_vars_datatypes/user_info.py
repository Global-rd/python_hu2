from pprint import pprint

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

#Bekérem a négy nyelvet
planguage = input("Please give the 4 programming language, separetad by coma: ")

#A bekért nyelveket listává alakítom, amit a "skill"-ek közé felveszek 
planguage_list = planguage.split(",")
pprint(planguage_list)
pprint(type(planguage_list))
user_info["skills"] = planguage_list
pprint(user_info)
print("------------------------------------------")

#ABC sorrendbe állítom a kajákat
user_info["favourite_meals"].sort()
pprint(user_info["favourite_meals"])
print("------------------------------------------")

#Kipprintelem a utolsó előtti elemet
pprint(user_info["favourite_meals"][-2])
print("------------------------------------------")

#Hozzáadom a spagettit
user_info["favourite_meals"].append("spagetthi")
pprint(user_info["favourite_meals"])
print("------------------------------------------")

#Hozzáadom a 3. és 4. elemet
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
pprint(user_info["favourite_meals"])
print("------------------------------------------")

#Törlöm a duplikátumokat
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
pprint(user_info["favourite_meals"])
print("------------------------------------------")

#Felcserélem az első és utolsó elemet
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
print("------------------------------------------")

#Hozzáadom az új embert a kontaktokhoz
user_info["phone_contacts"]["Joe"] = "+36304561235"
pprint((user_info["phone_contacts"]))
print("------------------------------------------")

#Kitörlöm Timet
del user_info["phone_contacts"]["Tim"]
pprint((user_info["phone_contacts"]))
print("------------------------------------------")

#Hozzáadom az új embert a két telefonszámmal a kontaktokhoz
user_info["phone_contacts"]["Scarlet"] = ("+363045624235", "+36302432332113")
pprint((user_info["phone_contacts"]))
print("------------------------------------------")

#Kiprintelem a 3 utolsó skill-t fordított sorrendben
print(user_info["skills"][-1:-4:-1])
print("------------------------------------------")

#Kicserélem Tim2-t Tim-re
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
pprint((user_info["phone_contacts"]))
print("------------------------------------------")

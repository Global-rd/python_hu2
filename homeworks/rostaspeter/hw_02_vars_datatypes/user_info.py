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

#1.  bekér 4 nyelvet
user_info["skills"] = input("Írj 4 programozási nyelvet: ").split(",")
pprint(user_info)

#2.  rendezés
user_info["favourite_meals"].sort()
pprint(user_info)

#3.  utolsó előtti elem
print(user_info["favourite_meals"][-2])

#4.  hozzáadás
user_info["favourite_meals"].append("Spaghetti")
pprint(user_info)

#5.  duplikálás
user_info["favourite_meals"].extend(user_info["favourite_meals"][-2:])
pprint(user_info)

#6.  duplikálás törlése
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
pprint(user_info)

#7.  csere
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
pprint(user_info)

#8.  hozzáadás
user_info["phone_contacts"]["Peti"] = "+36301234567"
pprint(user_info)

#9.  törlése
del user_info["phone_contacts"]["Tim"]
pprint(user_info)

#10.  2telefonszám
user_info["phone_contacts"]["Zoli"] = ["+36302345678", "+36303456789"]
pprint(user_info)


#EXTRA 1
print(user_info["skills"][-3:][::-1])

#EXTRA 2
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"]["Tim2"]
del user_info["phone_contacts"]["Tim2"]
print(user_info)
#---DICTIONARY---
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
#----------------

# 1. 4 programozási nyelv beérése
languages = input("Adj meg 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül!")

# az előző input listává konvertálása
skills = languages.split(',')

#hozzáadás a fennti dictionary-hez
user_info["skills"] = skills

#printeljük ki az eredményt
print(user_info)

# 4. Adj hozzá egy “spaghetti” string-et a "favourite_meals" listához.
user_info["favourite_meals"].append("spaghetti")

# 2.Rendezd a favourite_meals lista elemeit abc szerinti növekvő sorrendbe.
user_info["favourite_meals"].sort()

# 3. Printeld ki a favourite_meals lista utolsó előtti elemét
print(user_info["favourite_meals"][-2])

# 5. Add hozzá a favourite_meals-hez az aktuális favourit_meals lista harmadik és negyedik elemét (nem az index-ét) újra.
third_fourth = user_info["favourite_meals"][2:4]  #meghatározzuk a 3. és 4. elemet a listában
user_info["favourite_meals"].extend(third_fourth)  #bővítjük a meglévő listát a két elemmel (nem csupán appendeljük, mert az törli a duplikációt)
print(user_info)

# 6. Ezután töröld az így keletkezett duplikátumokat!
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))  # setté alakítjuk, az törli a duplikációt, majd visszaalakítjuk list-re
print(user_info)

# 7. Cseréld fel a favourite_meals lista első és utolsó elemét!
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0] # innentől egyszerűen az első,utolsó elem = utolsó,első elem
print(user_info)

# 8. A “phone_contacts” dictionary-hez adj hozzá egy új elemet, tetszőleges névvel és telefonszámmal.
user_info["phone_contacts"]["Dave"] = "+364005001"
print(user_info)

# 9. Tim és Tim2 ugyanazt az embert reprezentálják a “phone_contacts”- ban, viszont a "Tim" key mögött lévő telefonszám már nem él. Töröld ki a telefonkönyvből!
del user_info["phone_contacts"]["Tim"]
print(user_info)

# 10. Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2 telefonszáma is van!
user_info["phone_contacts"]["Daniel"] = ["+364005002", "+364005003"]
print(user_info)


# Extra 1: Printeld ki a “skills” lista utolsó 3 elemét ellentétes sorrendben!
print(user_info["skills"][-1:-4:-1])

# Extra 2: Most, hogy Tim-nek már csak 1 telefonszáma van, érdemes lenne átnevezni Tim2-t Tim-re!
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2") # a poppal átrakjuk Tim2 telefonszámát a Tim-hez
print(user_info)

print("-------")
print(type(user_info["phone_contacts"]["Daniel"]))
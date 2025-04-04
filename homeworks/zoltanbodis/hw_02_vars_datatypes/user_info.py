import pprint

user_info = {
    "name": "Mike",
    "age": 25,
    "favourite_meals": ["pizza","carbonara","sushi"],
    "phone_contacts": {
        "Mary": "+36701234567",
        "Tim": "+36207654321",
        "Tim2": "+36304567321",
        "Jim": "+364005000"
        }
    }


"""
1. Kérj be a felhasználótól 4 programozási nyelvet vesszővel elválasztva,
szóközök nélkül. Konvertáld a kapott stringet egy listává, és add hozzá
a fenti dictionary-hez “skills” néven.
"""
skills = input("Adj meg 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül: ").split(",")
user_info["skills"] = skills
print(user_info["skills"])

# pprint.pprint(user_info)

"""
2. Rendezd a favourite_meals lista elemeit abc szerinti növekvő
sorrendbe.
"""
user_info["favourite_meals"].sort()

"""
3. Printeld ki a favourite_meals lista utolsó előtti elemét
"""
print("\n3. Printeld ki a favourite_meals lista utolsó előtti elemét \n------------------------------------------")
print(f"Favourite meals: {", ".join(user_info["favourite_meals"])}")
print(f"Utolsó előtti elem: {user_info["favourite_meals"][-2]}")

"""
4. Adj hozzá egy “spaghetti” string-et ugyanehhez a listához.
"""
user_info["favourite_meals"].append("spaghetti")

print("\n4. Adj hozzá egy “spaghetti” string-et ugyanehhez a listához. \n------------------------------------------")
print(f"Favourite meals: {", ".join(user_info["favourite_meals"])}")

"""
5. Add hozzá a favourite_meals-hez az aktuális favourit_meals lista
harmadik és negyedik elemét (nem az index-ét) újra.
"""
#user_info["favourite_meals"].extend(user_info["favourite_meals"][2], user_info["favourite_meals"][3])
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

print("\n5. Add hozzá a favourite_meals-hez az aktuális favourit_meals lista harmadik és negyedik elemét (nem az index-ét) újra. \n------------------------------------------")
print(f"Favourite meals: {", ".join(user_info["favourite_meals"])}")


"""
6. Ezután töröld az így keletkezett duplikátumokat!
"""
print("\n6. Ezután töröld az így keletkezett duplikátumokat! \n------------------------------------------")
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))

# visszarendezem az abc sorrendet is, mert a set() elrontotta
user_info["favourite_meals"].sort()
print(f"Favourite meals: {", ".join(user_info["favourite_meals"])}")


"""
7. Cseréld fel a favourite_meals lista első és utolsó elemét!
"""
print("\n7. Cseréld fel a favourite_meals lista első és utolsó elemét! \n------------------------------------------")
# egysoros értékcserével meg lehet szépen cserélni
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
print(f"Favourite meals: {", ".join(user_info["favourite_meals"])}")

"""
8. A “phone_contacts” dictionary-hez adj hozzá egy új elemet, tetszőleges névvel és telefonszámmal.
"""
print("\n8. A phone_contacts dictionary-hez adj hozzá egy új elemet, tetszőleges névvel és telefonszámmal. \n------------------------------------------")
user_info["phone_contacts"].update({"Kim":"+36201112222"})
pprint.pprint(user_info["phone_contacts"])

"""
9. Tim és Tim2 ugyanazt az embert reprezentálják a “phone_contacts”-
ban, viszont a "Tim" key mögött lévő telefonszám már nem él. Töröld
ki a telefonkönyvből!
"""
print("\n9. Tim és Tim2 ugyanazt az embert reprezentálják a phone_contacts-\nban, viszont a \"Tim\" key mögött lévő telefonszám már nem él. Töröld ki a telefonkönyvből! \n------------------------------------------")
del user_info["phone_contacts"]["Tim"]
pprint.pprint(user_info["phone_contacts"])

"""
10.Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2
telefonszáma is van!
"""
print("\n10.Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2 telefonszáma is van! \n------------------------------------------")
user_info["phone_contacts"].update({"Pim":["+36201212333","+3630976543"]})
pprint.pprint(user_info["phone_contacts"])

"""
Extra 1: Printeld ki a “skills” lista utolsó 3 elemét ellentétes sorrendben!
"""
print("\nExtra 1: Printeld ki a “skills” lista utolsó 3 elemét ellentétes sorrendben! \n------------------------------------------")
print(f"A skills utolsó három eleme fordított sorrendben: {", ".join(user_info["skills"][-3:][::-1])}")

"""
Extra 2: Most, hogy Tim-nek már csak 1 telefonszáma van, érdemes lenne átnevezni Tim2-t Tim-re!
"""
print("\nExtra 2: Most, hogy Tim-nek már csak 1 telefonszáma van, érdemes lenne átnevezni Tim2-t Tim-re! \n------------------------------------------")
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"]["Tim2"]
del user_info["phone_contacts"]["Tim2"]

pprint.pprint(user_info["phone_contacts"])

print("\n\n")
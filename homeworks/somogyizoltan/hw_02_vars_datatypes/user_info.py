# HW 2, Második feladat


# Alap adatok
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

# Feladatok
"""
1. Kérj be a felhasználótól 4 programozási nyelvet vesszővel elválasztva,
szóközök nélkül. Konvertáld a kapott stringet egy listává, és add hozzá
a fenti dictionary-hez “skills” néven.
"""

# Felhasználói adatbevitel a megadás szerint, amiben levágjuk a felesleges space-eket, és a vessző mentén feldaraboljuk listává
prog_lang = list(input("Adj meg 4 programozási nyelvet vesszővel elválasztva: ").strip().split(','))

# Hozzá adni az így kapott listát az eredeti dictionary-hez
user_info["skills"] = prog_lang

# Próba nyomtatás
print(prog_lang)
print(user_info)

"""
2. Rendezd a favourite_meals lista elemeit abc szerinti növekvő
sorrendbe.
"""
# sort() metódus
user_info["favourite_meals"].sort()

print(user_info["favourite_meals"])

"""
3. Printeld ki a favourite_meals lista utolsó előtti elemét
"""

print(user_info["favourite_meals"][-2])
print(user_info["favourite_meals"]) 

"""
4. Adj hozzá egy “spaghetti” string-et ugyanehhez a listához.
"""

user_info["favourite_meals"].append("spaghetti")
print(user_info["favourite_meals"])                                    

"""
5. Add hozzá a favourite_meals-hez az aktuális favourit_meals lista
harmadik és negyedik elemét (nem az index-ét) újra.
"""

user_info["favourite_meals"].append(user_info["favourite_meals"][2])
user_info["favourite_meals"].append(user_info["favourite_meals"][3])
print(user_info["favourite_meals"])  

"""
6. Ezután töröld az így keletkezett duplikátumokat!
"""

user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
print(user_info["favourite_meals"])  

"""
7. Cseréld fel a favourite_meals lista első és utolsó elemét!
"""

# egy segéd változón keresztül
one_elem = user_info["favourite_meals"][0]
user_info["favourite_meals"][0] = user_info["favourite_meals"][-1]
user_info["favourite_meals"][-1] = one_elem
print(user_info["favourite_meals"])  


"""
8. A “phone_contacts” dictionary-hez adj hozzá egy új elemet,
tetszőleges névvel és telefonszámmal.
"""

user_info["phone_contacts"]["Anne"] = "+36305553475"
print(user_info)  

"""
9. Tim és Tim2 ugyanazt az embert reprezentálják a “phone_contacts”-
ban, viszont a "Tim" key mögött lévő telefonszám már nem él. Töröld
ki a telefonkönyvből!
"""

user_info["phone_contacts"].pop("Tim")
print(user_info)  


"""
10.Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2
telefonszáma is van!
"""

user_info["phone_contacts"]["Gina"] = ("+36206543217", "+36708521479")
print(user_info)  

"""
Extra 1: Printeld ki a “skills” lista utolsó 3 elemét ellentétes sorrendben!
"""

print(user_info["skills"][-1],user_info["skills"][-2],user_info["skills"][-3])

"""
Extra 2: Most, hogy Tim-nek már csak 1 telefonszáma van, érdemes lenne
átnevezni Tim2-t Tim-re!
"""

# egy segéd változón keresztül
one_elem = user_info["phone_contacts"]["Tim2"]
# törölni az eredetit
user_info["phone_contacts"].pop("Tim2")
# hozzáadni a megváltozott névvel a telefonszámot
user_info["phone_contacts"]["Tim"] = one_elem
print(user_info)  



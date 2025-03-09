from pprint import pprint
import re

# Feladat 2: List és dictionary műveletek használata

"""Hozz létre egy user_info.py file-t, és kódold le a következő feladat
megoldását. Nyugodtan használj kommenteket a különböző feladatpontok
előtt, hogy később könnyedén átlásd hogy melyik sor milyen funkciót lát el.
Adott a következő dictionary, amely egy felhasználó adatai tartalmazza
(másold át a kódodba):"""

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

"""1. Kérj be a felhasználótól 4 programozási nyelvet vesszővel elválasztva,
szóközök nélkül. Konvertáld a kapott stringet egy listává, és add hozzá
a fenti dictionary-hez “skills” néven."""

skills = []

for i in range(4):
    language = input('Adj meg egy programozási nyelvet!')
    skills.append(language)

user_info['skills'] = skills
#print(user_info)

#Itt a feladat az lett volna, hogy egy input()-ból kapott string-et szeleteld fel és alakítsd listává.

skills_2 = input('Adj meg 4 programozási nyelvet vesszővel elválasztva: ')
#skills_2 = skills_2.split(',')           #tudom, hogy ez lenne az elvárt megoldás
skills_2 = re.split(r'[;, -]+', skills_2) #de, képtelen vagyok bízni a felhasználóban :-(
user_info['skills_2'] = skills_2

"""Rendezd a favourite_meals lista elemeit abc szerinti növekvő
sorrendbe."""

#user_info["favourite_meals"] = sorted(user_info["favourite_meals"])
#print(user_info["favourite_meals"])

#fyi hogy van egy sort() method is
user_info["favourite_meals"].sort()

print(f'1.1 4 programozási nyelv for ciklussal (skills): {skills}')
print(f'1.2 4 programozási nyelv vesszővel elválasztva (skills_2): {skills_2}')
print(f'1.3 favourite_meals lista elemeit abc szerinti növekvő sorrendbe: {user_info["favourite_meals"]}')
print('1.4 új dictionary skillekkel: ')
pprint(user_info)

# 3. Printeld ki a favourite_meals lista utolsó előtti elemét

print(f'3. favourite_meals lista utolsó előtti eleme: {user_info["favourite_meals"][-2]}')

# 4. Adj hozzá egy “spaghetti” string-et ugyanehhez a listához.

user_info["favourite_meals"].append("spaghetti")
print(f'4. favourite_meals lista “spaghetti”-vel: {user_info["favourite_meals"]}')
                                                                     
# 5. Add hozzá a favourite_meals-hez az aktuális favourit_meals lista harmadik és negyedik elemét (nem az index-ét) újra.

user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
print(f'5. favourite_meals az aktuális favourit_meals lista harmadik és negyedik elemével: {user_info["favourite_meals"]}')

# 6. Ezután töröld az így keletkezett duplikátumokat!

# user_info["favourite_meals"] = user_info["favourite_meals"][0:4]

##Tanultunk egy egész effektív módszerről a set-eknél a duplikátumok törléséhez, az kéne ide.
#ezt próbáltam, de töröltem, mert nem tetszett, hogy megváltozott a sorrend:
#user_info["favourite_meals"] = list(set(user_info["favourite_meals"])) 

##esetleg a dict.fromkeys() használata is szuper
#ez viszont tetszik. Köszi :-)

user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))

print(f'6. duplikátumok nélkül: {user_info["favourite_meals"]}')

# 7. Cseréld fel a favourite_meals lista első és utolsó elemét!

user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
print(f'7. favourite_meals lista első és utolsó eleme cserélve: {user_info["favourite_meals"]}')

# 8. A “phone_contacts” dictionary-hez adj hozzá egy új elemet, tetszőleges névvel és telefonszámmal.

user_info["phone_contacts"].update({'Bob': '+3630123456789'})
print(f'8. “phone_contacts” dictionary új elemmel: ')
pprint(user_info["phone_contacts"])

# 9. Tim és Tim2 ugyanazt az embert reprezentálják a “phone_contacts”-ban, 
# viszont a "Tim" key mögött lévő telefonszám már nem él. Töröld ki a telefonkönyvből!

user_info["phone_contacts"].pop("Tim")


print(f'9. "Tim" key mögött lévő telefonszám törölve:')
pprint(user_info["phone_contacts"])

# 10.Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2 telefonszáma is van!

user_info["phone_contacts"].update({'Max': ['+36301234500', '+361245873']})
print(f'10. új ember akinek 2 telefonszáma is van: ')
pprint(user_info["phone_contacts"])

# Extra 1: Printeld ki a “skills” lista utolsó 3 elemét ellentétes sorrendben!

print(f'Extra1: “skills” lista utolsó 3 eleme ellentétes sorrendben: {user_info["skills"][-3:][::-1]}')

# Extra 2: Most, hogy Tim-nek már csak 1 telefonszáma van, érdemes lenne átnevezni Tim2-t Tim-re!

user_info["phone_contacts"]['Tim'] = user_info["phone_contacts"].pop("Tim2")
print(f'Extra2: Tim2-t Tim-re nevezve: ')
pprint(user_info["phone_contacts"])

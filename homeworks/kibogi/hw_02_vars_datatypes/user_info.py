import pprint

user_info = {
    "name": "Mike",
    "age": 25,
    "favourite_meal": [
        "pizza",
        "carbonara",
        "sushi"
    ],
    "phone_contacts": {
    "Mary": "+36701234567",
    "Tim": "+36207654321",
    "Tim2": "+36304567321",
    "Jim": "+364005000"
    },
    

}


programing_languages = input ("Give me four different programing languages") #Kérj be a felhasználótól 4 programozási nyelvet vesszővel elválasztva,szóközök nélkül.
skills = programing_languages.split(",") #Konvertáld a kapott stringet egy listává
user_info.update({"skills": skills}) #és add hozzá a fenti dictionary-hez “skills” néven.

print (skills)
print (type(skills))

print (list(reversed(skills[-3:]))) #Extra 1: Printeld ki a “skills” lista utolsó 3 elemét ellentétes sorrendben!

pprint.pprint(user_info)

user_info["favourite_meal"].sort() #Rendezd a favourite_meals lista elemeit abc szerinti növekvő sorrendbe.
print(user_info["favourite_meal"])

print (user_info["favourite_meal"][-2]) #Printeld ki a favourite_meals lista utolsó előtti elemét

user_info["favourite_meal"].append("spagetti") #Adj hozzá egy “spaghetti” string-et ugyanehhez a listához.

print (user_info["favourite_meal"])

user_info["favourite_meal"].extend(["sushi", "spagetti"]) #Add hozzá a favourite_meals-hez az aktuális favourit_meals lista harmadik és negyedik elemét (nem az index-ét) újra.

print (user_info["favourite_meal"])

user_info["favourite_meal"] = list(set(list(user_info["favourite_meal"]))) #Ezután töröld az így keletkezett duplikátumokat!

print (user_info["favourite_meal"])

user_info["favourite_meal"][0], user_info["favourite_meal"][-1] =user_info["favourite_meal"][-1], user_info["favourite_meal"][0] #Cseréld fel a favourite_meals lista első és utolsó elemét!

print (user_info["favourite_meal"])

user_info["phone_contacts"].update({"Joe": "+45145454785"}) #A “phone_contacts” dictionary-hez adj hozzá egy új elemet, tetszőleges névvel és telefonszámmal.

user_info["phone_contacts"].pop("Tim") #Tim és Tim2 ugyanazt az embert reprezentálják a “phone_contacts”-ban, viszont a "Tim" key mögött lévő telefonszám már nem él. Töröld ki a telefonkönyvből!

pprint.pprint(user_info)

user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2") #Extra 2: Most, hogy Tim-nek már csak 1 telefonszáma van, érdemes lenne átnevezni Tim2-t Tim-re!

pprint.pprint(user_info)

user_info["phone_contacts"].update({"Kate": ["+45145454785", "+546545"]})

pprint.pprint(user_info)
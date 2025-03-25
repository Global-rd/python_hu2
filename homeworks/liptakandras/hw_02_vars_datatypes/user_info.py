
# plusz printeket azért tettem bele, hogy ellenőrizni tudjam, amiket csináltam

import pprint

# COPY OF TASK DESCRIPTION CODE

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


# 1. 4 PROGRAMOZÁSI NYELV BEKÉRÉSE

print("Please add 4 programming languages you have experience with!")  # instrukció és beviteli mezők a felhasználónak
programming_language_1 = input("1st programming language: ")
programming_language_2 = input("2nd programming language: ")
programming_language_3 = input("3rd programming language: ")
programming_language_4 = input("4th programming language: ")

string_of_programming_languages = f"{programming_language_1},{programming_language_2},{programming_language_3},{programming_language_4}"  # egyesítés egy stringbe, vesszővel elválaszta, szóközök nélkül
print(string_of_programming_languages)

list_of_programming_languages = string_of_programming_languages.split(",")  # string konvertálása listává a vesszők mentén
print(list_of_programming_languages)

user_info["skills"] = list_of_programming_languages
print(user_info)

# 2. FAVORITE MEALS ELEMEK RENDEZÉSE

user_info["favourite_meals"].sort()
print(user_info["favourite_meals"])


# 3. FAVOURITE MEALS LISTA UTOLSÓ ELŐTTI ELEMÉNEK KIPRINTELÉSE

print(user_info["favourite_meals"][-2])  # már az abc sorrendben rendezés szerinti utolsó előttit printelem


# 4. HOZZÁADÁS A LISTÁHOZ

user_info["favourite_meals"].append("spaghetti")


# 5. 3-4 ELEMEK HOZZÁADÁSA ÚJRA A LISTÁHOZ

user_info["favourite_meals"].append

list_elements = user_info["favourite_meals"][2:4]

user_info["favourite_meals"].extend(list_elements)
print(user_info["favourite_meals"])


# 6. DUPLIKÁTUMOK TÖRLÉSE

user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
print(user_info)


# 7. ELEMEK SORRENDJÉNEK FELCSERÉLÉSE

first_element = user_info["favourite_meals"][0]
last_element = user_info["favourite_meals"][-1]

user_info["favourite_meals"][0] = last_element
user_info["favourite_meals"][-1] = first_element

print(user_info)

# 8. ÚJ ELEM HOZZÁADÁSA (PHONE CONTACT)

user_info["phone_contacts"]["Andras"] = "123456789"


# 9. ELEM TÖRLÉSE

del user_info["phone_contacts"]["Tim"]
print(user_info)


# 10. ELEM HOZZÁADÁS KÉT ÉRTÉKKEL

    # Ha listaként adom hozzá

user_info["phone_contacts"]["Lebron"] = ["987654321", "192837465"]

    # Vagy ha külön key-value párokként, mint ahogy Tim volt

print(user_info)
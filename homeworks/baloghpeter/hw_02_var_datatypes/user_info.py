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

print("----------")
prog_languages = input("Adj meg 4 programozási nyelvet: ")
prog_languages_lista = prog_languages.split(",")

user_info["skills"] = prog_languages_lista
print("1.feladat:")
print(user_info)

user_info["favourite_meals"].sort()
print("2.feladat:")
print(user_info)

print("3.feladat:")
print(user_info["favourite_meals"][-2])

user_info["favourite_meals"].append("spaghetti")
print("4.feladat:")
print(user_info)

user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
print("5.feladat:")
print(user_info)

user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
print("6.feladat:")
print(user_info)

user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
print("7.feladat:")
print(user_info)

user_info["phone_contacts"]["Anna"] = "+361012345678"
print("8.feladat:")
print(user_info)

del user_info["phone_contacts"]["Tim"]
print("9.feladat:")
print(user_info)

user_info["phone_contacts"]["Peter"] = ["+36501112233", "+36504445566"]
print("10.feladat:")
print(user_info)
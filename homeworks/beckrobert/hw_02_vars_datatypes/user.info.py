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

code = input("adj meg négy programozási nyelvet vesszővel elválasztva, szóköz nélkül: ")

code_list = code.split(",")  

user_info["skills"] = code_list

user_info["favourite_meals"].sort()

print(user_info["favourite_meals"][-2])

user_info["favourite_meals"].append("spaghetti")

user_info["favourite_meals"].extend(user_info["favourite_meals"][1:3])

user_info["favourite_meals"].pop(4)
user_info["favourite_meals"].pop(4)

user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]

user_info["phone_contacts"]["Fregoli"] = "+36203989682"

del user_info["phone_contacts"]["Tim"]

user_info["phone_contacts"]["Gabe"] = ["+36201112233", "+36704445566"]

print(user_info)
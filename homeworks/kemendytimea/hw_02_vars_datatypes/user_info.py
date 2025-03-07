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
#1:
languages = input("Adj meg 4 programozasi nyelvet, vesszovel elvalasztva: ")
user_info["skills"] = languages.split(",")
#2:
user_info["favourite_meals"].sort()
#3:
print(user_info["favourite_meals"][-2])
#4:
user_info["favourite_meals"].append("spaghetti")
#5:
user_info["favourite_meals"].extend([user_info["favourite_meals"][2], user_info["favourite_meals"][3]])
#6:
user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))
#7:
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
#8:
user_info["phone_contacts"]["Morris"] = "+36123456789"
#9:
del user_info["phone_contacts"]["Tim"]
#10:
user_info["phone_contacts"]["Lilus"] = ["+37123456789", "+38123456789"]
#szorgalmi_1:
print(user_info["skills"][-3:][::-1])
#szorgalmi_2:
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
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
skills_string=input("Give me 4 program languages that you can use separated by commas, without spaces: ").strip()
#C#,JavaScript,C++,Java
Mike_skills=skills_string.split(",")
print(Mike_skills)
user_info["skills"]=Mike_skills
print(user_info)
user_info["favourite_meals"].sort()
print(user_info["favourite_meals"])
print(user_info["favourite_meals"][-2])
user_info["favourite_meals"].append("spaghetti")
print(user_info["favourite_meals"])
user_info["favourite_meals"].append("sushi")
user_info["favourite_meals"].append("spaghetti")
print(user_info["favourite_meals"])
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
user_info["favourite_meals"].sort()
user_info["favourite_meals"][0], user_info["favourite_meals"][-1]=user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
print(user_info["favourite_meals"])

user_info["phone_contacts"]["Katie"] = "+36301234567"
print(user_info["phone_contacts"])
user_info["phone_contacts"]["Tim2"]=" "

user_info["phone_contacts"]["Bela"]= "+36201234567", "+36301236547"
print(user_info["phone_contacts"])


last_three_reversed = user_info["skills"][-3:][::-1]
print(last_three_reversed)
user_info["phone_contacts"]["Tim2"]="Tim"
print(user_info)
del user_info["phone_contacts"]["Tim2"]
print(user_info)








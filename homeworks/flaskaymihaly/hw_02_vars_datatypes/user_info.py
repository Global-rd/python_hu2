from pprint import pprint

user_info={
    "name":"Mike",
    "age":"25",  
    "favourite_meals": ["pizza", "carbonara", "sushi"], 
    "phone_contacts":{"Mary": "06701234567",
                      "Tim": "06207654321",
                      "Tim2": "06304567321",
                      "Jim": "06304005000",},     
   }

#1
computer_languages=input("Please write four different programming languages, separated with a comma: ")
computer_langauge_list=computer_languages.split(",")
user_info["skills"]=computer_langauge_list
print("-----------------------------------------------")
#2
(user_info["favourite_meals"].sort())

#3
print(user_info["favourite_meals"] [-2])

#4 
user_info["favourite_meals"].append("spaghetti")

#5
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

#6
user_info["favourite_meals"]=list(set(user_info["favourite_meals"]))
#print(type(user_info["favourite_meals"]))

# 7 ez nem a legelagánsabb....hogyan lehetne egyszerűbben??
user_info["favourite_meals"][0], user_info["favourite_meals"][-1]=user_info["favourite_meals"][-1], user_info["favourite_meals"][0]

#8
user_info["phone_contacts"].update({"Zexter": "06504005000",})
#user_info["phone_contacts"]["Dexter"]="0650400500"

#9
del user_info["phone_contacts"]["Tim"]

#10
user_info["phone_contacts"]["zsexter"]=["0650400500", "0652400500"]

pprint(user_info)

print("---------------------------------------------")
print("for extra points")
print("---------------------------------------------")

print(user_info["skills"][-1:-4:-1])

user_info["phone_contacts"]["Tim"]=user_info["phone_contacts"].pop("Tim2")

pprint(user_info)

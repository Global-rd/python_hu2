from pprint import pprint
user_info = {

    "name" : "Mike",
    "age" : 25,
    "favourite_meals" : [
        "pizza" ,
        "carbonara" ,
        "sushi"
    ],
    "phone_contacts" : {
        "Mary" : "+36701234567",
        "Tim" : "+36207654321",
        "Tim2" : "+36304567321",
        "Jim" : "+364005000"
    }
}

#1
codenames=input("Adj meg négy darab programozási nevet, vesszővel elválasztva egymástól, viszont szóközök nélkül: ")
user_info["skills"] = codenames.split(",")
#2
user_info["favourite_meals"].sort()
#3
print("A favourite_meals lista utolsó előtti eleme:",user_info["favourite_meals"][-2])
#4
user_info["favourite_meals"].append("spaghetti")
#5
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
#6
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
#7
user_info["favourite_meals"][0],user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1],user_info["favourite_meals"][0]
#8
user_info["phone_contacts"]["Juliet"] = "+367772220"
#9
del(user_info["phone_contacts"]["Tim"])
#10
user_info["phone_contacts"]["Andrew"] = ["+369992221" , "+368883331"]

print("Az eddigi dictionary:")
pprint(user_info)

#e1
print("- - - - - - - - - - - - - - - - -")
print("Extrák:")
reverse_skills = user_info["skills"][-1:-4:-1]
print(reverse_skills)

#e2
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"]["Tim2"]
del user_info["phone_contacts"]["Tim2"]
print(user_info["phone_contacts"])

print("- - - - - - - - - - - - - - - - -")
pprint(user_info)
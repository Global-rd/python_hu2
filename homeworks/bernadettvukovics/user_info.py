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

# 1. Request 4 programming languages, convert them to a list, add them to the dictionary.
skills = input("Please provide 4 programming languages, separated by commas: ")
skills_list = skills.split(",")  # Convert string to list
user_info["skills"] = skills_list
print(f"Programming languages added: {user_info['skills']}")

# 2. Sorting list of favourite_meals ABC
user_info["favourite_meals"].sort()  # Sorting in alphabetical order
print(f"Sorted meals: {user_info['favourite_meals']}")

# 3. Print the penultimate item.
print(f"Penultimate meal: {user_info['favourite_meals'][-2]}")

# 4. Add a spaghetti string to the favourite_meals list
user_info["favourite_meals"].append("spaghetti")
print(f"New meal added: {user_info['favourite_meals']}")

# 5. Add the third and fourth items of the list to favourite_meals again
user_info["favourite_meals"].append(user_info["favourite_meals"][2])
user_info["favourite_meals"].append(user_info["favourite_meals"][3])
print(f"Duplicated meals added: {user_info['favourite_meals']}")

# 6. Delete duplicates!
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))  # Set removes duplicates
print(f"Duplicates removed: {user_info['favourite_meals']}")

# 7. Replace the first and last items in the favourite_meals list
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
print(f"First and last meals swapped: {user_info['favourite_meals']}")

# 8. Add a new item to the dictionary "phone_contacts"
name = input("Enter the name of the new contact: ")
phone = input("Enter the phone number of the new contact: ")
user_info["phone_contacts"][name] = phone
print(f"New contact added: {name} - {phone}")

# 9. Delete "Tim" from "phone_contacts"
del user_info["phone_contacts"]["Tim"]
print("Tim removed from the phone book.")

# 10. Add a new person with 2 phone numbers
name = input("Enter the name of the person with 2 phone numbers: ")
phone1 = input("Enter the first phone number: ")
phone2 = input("Enter the second phone number: ")
user_info["phone_contacts"][name] = [phone1, phone2]
print(f"New contact added: {name} - {phone1}, {phone2}")

# Extra 1: Print the last 3 items in the skills list in reverse order
if len(user_info["skills"]) >= 3:
    print(f"The last three skills in reverse order: {user_info['skills'][-1:-4:-1]}")
else:
    print("Not enough skills in the list.")
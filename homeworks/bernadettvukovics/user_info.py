

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

# 1. Task: Request 4 programming languages, convert them to a list, add them to the dictionary. 
def add_skills():
    skills = input("Please provide 4 programming languages, separated by commas: ")
    skills_list = skills.split(",")  # Convert string to list
    user_info["skills"] = skills_list
    print(f"Programming languages added: {user_info['skills']}")

# 2. Task: Sorting list of favourite_meals ABC
def sort_favourite_meals():
    user_info["favourite_meals"].sort()  # Sorting in alphabetical order
    print(f"Sorted meals: {user_info['favourite_meals']}")

# 3. Task: Print the penultimate item.
def print_second_last_meal():
    print(f"Penultimate meal: {user_info['favourite_meals'][-2]}")

# 4. Task: Add a spaghetti string to the favourite_meals list 
def add_spaghetti():
    user_info["favourite_meals"].append("spaghetti")
    print(f"New meal added: {user_info['favourite_meals']}")

# 5. Task: Add the third and fourth items of the list to favourite_meals again
def add_duplicated_meals():
    user_info["favourite_meals"].append(user_info["favourite_meals"][2])
    user_info["favourite_meals"].append(user_info["favourite_meals"][3])
    print(f"Duplicated meals added: {user_info['favourite_meals']}")

# 6. Task: Delete duplicates!
def delete_duplicates():
    user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))  # Set removes duplicates
    print(f"Duplicates removed: {user_info['favourite_meals']}")

# 7. Task: Replace the first and last items in the favourite_meals list
def swap_first_last_meal():
    user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
    print(f"First and last meals swapped: {user_info['favourite_meals']}")

# 8. Task: Add a new item to the dictionary "phone_contacts"
def add_phone_contact():
    name = input("Enter the name of the new contact: ")
    phone = input("Enter the phone number of the new contact: ")
    user_info["phone_contacts"][name] = phone
    print(f"New contact added: {name} - {phone}")

# 9. Task: Delete "Tim" from "phone_contacts"
def delete_tim():
    del user_info["phone_contacts"]["Tim"]
    print("Tim removed from the phone book.")

# 10. Task: Add a new person with 2 phone numbers
def add_two_phone_numbers():
    name = input("Enter the name of the person with 2 phone numbers: ")
    phone1 = input("Enter the first phone number: ")
    phone2 = input("Enter the second phone number: ")
    user_info["phone_contacts"][name] = [phone1, phone2]
    print(f"New contact added: {name} - {phone1}, {phone2}")

# Extra 1: Print the last 3 items in the skills list in reverse order
def print_last_three_skills():
    if len(user_info["skills"]) >= 3:
        print(f"The last three skills in reverse order: {user_info['skills'][-1:-4:-1]}")
    else:
        print("Not enough skills in the list.")

# Testing

add_skills()
sort_favourite_meals()
print_second_last_meal()
add_spaghetti()
add_duplicated_meals()
delete_duplicates()
swap_first_last_meal()
add_phone_contact()
delete_tim()

add_two_phone_numbers()

print_last_three_skills()
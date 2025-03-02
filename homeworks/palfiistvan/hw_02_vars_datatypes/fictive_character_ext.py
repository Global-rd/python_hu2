# Sajnos nem működik, nem tudom hogyan kell lecserélni a teljes stringet.

name = input("What is your name? ").strip().capitalize()
age = int(input("How old are you? "))
age_in_days = age * 365
experience = int(input("years of experience? "))
profi = input("Do you want to become a professional Python developer? (yes/no)")
if profi == "yes":
    profi.replace("yes", "wants")
if profi == "no":
    profi.replace("no", "does not want")

# print(name)
# print(age)
# print(age_in_days)
# print(experience)
# print(profi)

my_character = f"My character is {age_in_days} days old. His/her name is {name} and he/she has {experience} years experience. He/she {profi} to be a Python developer!"
print(my_character)
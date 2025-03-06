# Sajnos nem működik, nem tudom hogyan kell lecserélni a teljes stringet.

name = input("What is your name? ").strip().capitalize()
age = int(input("How old are you? "))
age_in_days = age * 365
experience = int(input("years of experience? "))
dev_motivation = input("Do you want to become a professional Python developer? (yes/no)")
dev_intention = "wants" if dev_motivation == "yes" else "does not want"

# print(name)
# print(age)
# print(age_in_days)
# print(experience)
# print(dev_motivation)

my_character = f"My character is {age_in_days} days old. His/her name is {name} and he/she has {experience} years experience. He/she {dev_intention} to be a Python developer!"
print(my_character)
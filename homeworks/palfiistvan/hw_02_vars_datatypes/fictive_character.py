name = input("What is your name? ").strip().capitalize()
age = int(input("How old are you? "))
age_in_days = age * 365
experience = int(input("years of experience? "))

# print(name)
# print(age)
# print(age_in_days)
# print(experience)

my_character = f"My character is {age_in_days} days old. His/her name is {name} and he/she has {experience} years experience."
print(my_character)
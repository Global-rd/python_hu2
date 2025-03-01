#name input field with capital first letters and spaces removed
name = input("What is your full name: " ).strip().title()

#age input field, data type defined as integer
age = int(input("How old are you: "  ))

#gender input field
gender = input("What is your gender? (female/male: "  ).lower().strip()

#age in days calculation
ageindays = age * 365

#Python experience input field, data type defined as integer
exp = int(input("How many years of Python programming experience do you have: "  ))

#Python goals input field
goal = input("Do you want to be a professional Python developer? (yes/no): "  ).lower().strip()

#Ternary operator for the goal
goal_var = "wants" if goal == "yes" else "does not want"

#Ternary operator for gender
gender_var = "He" if gender == "male" else "She"

#Ternary operator for gender 2
gender_var2 = "he" if gender == "male" else "she"

#Ternary operator for gender 3
gender_var3 = "His" if gender == "male" else "Her"

#Summary of the character
print("----------------")
print(f"My character is {ageindays} days old. {gender_var3} name is {name} and {gender_var2} has {exp} years experience. {gender_var} {goal_var} to be a Python developer!")

#check data types
print("----------------")
print(type(name))
print(type(age))
print(type(exp))
print(type(goal))
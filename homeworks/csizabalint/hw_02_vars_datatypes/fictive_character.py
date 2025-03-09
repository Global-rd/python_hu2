#   Homework 2

# 1) create inputs: name, age, python experience
# 2) name should be written with capital letter and there shouldn't be space before or after
# 3) convert age to the appropriate data type and store it in a new variable, it should show how old is the character in days
# 4) print all the variables in f-string
# 5) final result should look like this: "My character is <age_in_days> old. His/her name is <name> and he/she has <python_exp_in_years> years experience."

first_name = input("What is your first name?: ").strip().capitalize()
last_name = input("What is your last name?: ").strip().capitalize()
age = int(input("How old are you? "))
experience = int(input("How many years of python experience do you have? "))
age_in_days = age * 365

print(f"My character is {age_in_days} days old. His/her name is {first_name} {last_name} and he/she has {experience} years of python experience.")


# 6) create an input: do you want your character to be pro python programmer?
# 7) add the answer to the final f-string

goal = "wants" if input("Do you want to be a pro python programmer? ").strip() == "yes" else "does not want"

print(f"My character is {age_in_days} days old. His/her name is {first_name} {last_name} and he/she has {experience} years of python experience. He/She {goal} to be a python programmer")

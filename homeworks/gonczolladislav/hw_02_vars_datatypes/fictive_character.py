# declare variables and call inputs
user_first_name = input("Type your first name : ").strip().capitalize()
user_last_name = input("Type your last name : ").strip().capitalize()
user_age = int(input("How old are you?(type years): "))
user_age_in_days = user_age * 365
user_python_experience = int(input("Please type your Python experience in years : "))
wants_to_be_python_dev = input("Please name your intention to became a professional Python developer. Answer with yes or no. :").strip().lower()

user_intention = "wants" if wants_to_be_python_dev == "yes" else "does not want"

# f-strings
user_introduction_1 = f"My character is {user_age} years old. I have one useless information about this : Age in days is : {user_age_in_days}. :-)))"
user_introduction_2 = f"His/her name is {user_first_name} {user_last_name} and he/she has {user_python_experience} years experience with Python programming."
user_introduction_3 = f"He/she {user_intention} to be a Python developer !"

print(user_introduction_1,user_introduction_2,user_introduction_3)










# declare variables and call inputs
user_first_name = input("Type your first name : ")
user_first_name = user_first_name.strip()
user_first_name = user_first_name.capitalize()

user_last_name = input("Type your last name : ")
user_last_name = user_last_name.strip()
user_last_name = user_last_name.capitalize()

user_age = int(input("How old are you?(type years): "))
user_age_in_days = user_age * 365

user_python_experience = int(input("Please type your Python experience in years : "))

user_intention_to_became_a_prof_python_developer = input("Please name your intention to became a professional Python developer. Answer with yes or no. :")
user_intention_to_became_a_prof_python_developer = user_intention_to_became_a_prof_python_developer.strip()
user_intention_to_became_a_prof_python_developer = user_intention_to_became_a_prof_python_developer.lower()

# save answer to boolean variable
if user_intention_to_became_a_prof_python_developer == "yes": 
    user_intention_boolean = True 
elif user_intention_to_became_a_prof_python_developer == "no":
    user_intention_boolean = False 
else:user_intention_boolean = None

# f-strings
user_introduction_1 = f"My character is {user_age} years old. I have one useless information about this : Age in days is : {user_age_in_days}. :-)))"
user_introduction_2 = f"His/her name is {user_first_name} {user_last_name} and he/she has {user_python_experience} years experience with Python programming."

if user_intention_boolean == True: 
    user_intention = "wants"
    user_introduction_3 = f"He/she {user_intention} to be a Python developer !"
elif user_intention_boolean == False: 
    user_intention = "does not want"
    user_introduction_3 = f"He/she {user_intention} to be a Python developer !"
else: 
    user_introduction_3 = "We dont know the user's intention to be a Python developer."   

print(user_introduction_1,user_introduction_2,user_introduction_3)










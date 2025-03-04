name = input("Give me your full name") #katalin ipacs
age = input("Give me your age in numbers") #45
Python_experience = input("How long have you been working with Python? Answer in years (number)") #1
age_in_days = int(age)*365.25
capitalized_name = (name.title())
introduction = f"My character is {age_in_days} old. Her name is {capitalized_name} and she has {Python_experience} year of experience."

print(introduction)

wish = input("Would you like to be a Python Grand Master? (yes/no)").strip().lower()
is_Python_Grand_Master = True if wish =="yes" else False
print(is_Python_Grand_Master)

introduction=f"My character is {age_in_days} old. Her name is {capitalized_name} and she has {Python_experience}"\
f"She would like to become a Python Developer and that is {is_Python_Grand_Master}."
print(introduction)
